# Containerization with Docker
![image](https://github.com/user-attachments/assets/7a571e73-76f3-4efe-a4dd-644c0c856011)

## set up docker01 - Ubuntu 20.04 cloud server
IP Address: 10.0.5.12 (change web01 address to 10.0.5.20) \
Default Gateway: 10.0.5.2 \
DNS: 10.0.5.5 \
![image](https://github.com/user-attachments/assets/e8491101-e466-4046-be31-eb397ee2f159)

### changing hostname. it is different on Ubuntu Cloud
- in `/etc/cloud/cloud.cfg`:
```
preserve_hostname: true
hostname: docker01-charlotte (add this line under)
fqdn: docker01-charlotte.charlotte.local (add this line under)
```
- change hostname for 127.0.1.1 in `/etc/hosts` file

![image](https://github.com/user-attachments/assets/c921d829-5bc4-4048-a4fb-de42b1f413a7)

- finally, `sudo hostnamectl hostname docker01-charlotte`
- update DNS records on mgmt01 (remember to change web01 record too)

## docker installation
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04

update and install prerequisite packages, this will let apt use packages over HTTPS
```
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```
add the GPG key
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
add docker repo to APT sources
```
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
```
validate installation is from docker repo. Notice that docker-ce is not installed, 
but the candidate for installation is from the Docker repository for Ubuntu 20.04 (focal).
```
apt-cache policy docker-ce | head
```
![image](https://github.com/user-attachments/assets/bb0207b1-5010-4d36-9fdd-028ec450cc5e)

install docker
```
sudo apt install docker-ce
```

check status
```
sudo systemctl status docker
```

### executing the docker command without sudo:
add user to the docker group, apply the new group membership, and logout/log back in
```
sudo usermod -aG docker charlotte
su - charlotte
```

## using docker
### downloading images
search for images availabe on Docker Hub
```
docker search <image-name>
```
download from Dockuer Hub
```
docker pull <image-name>
```
see installed images
```
docker images
```


## docker-compose
- https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04
> "Docker Compose is a tool that allows you to run multi-container application environments based on definitions set in a YAML file."

download the 1.29.2 release and save the executable file at /usr/local/bin/docker-compose
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
make docker-compose executable:
```
sudo chmod +x /usr/local/bin/docker-compose
```
verify installation
```
docker-compose --version
```

The following command pulls down an Arch Linux based docker image, invokes it in a container, and runs /bin/echo "HELLO SYS265 SNOWY DAYS '' before deleting the container.
```
docker run --rm archlinux:latest /bin/echo "HELLO SYS265 SNOWY DAYS"
```


___

## docker run command syntax (example)
- e.g. The following command will pull down the image, application and dependencies associated with a simple python web application. `docker run -d -P training/webapp python app.py`
- `docker`: CLI for interacting with docker
- `run`: create and start a new container
- `-d` (or `--detach`): the container runs in the background.
  - useful for non-interactive services, like webservers and databases  
- `-P` (or `--publich-all`): automatically publishes all exposed ports of the container to random host ports.
  - This allows external access to the services running in the container without having to specify port mappings manually.
- `training/webapp`: the docker image from which the container is created
  -  In this case, an image named `webapp` that is located in the `training` repository 
- `python`: command that will be executed inside the container once it starts
- `app.py`: argument passed to the python command
  - the Python script `app.py` should be executed by the Python interpreter when the container starts. 
 

- `docker run httpd` will automatically set up an apache web server in the container

### to stop docker process
```
docker stop <container ID>
```

## dockerized WordPress
https://github.com/docker/awesome-compose/tree/master/wordpress-mysql

- create a directory `docker-wp`
- create compose.yml
>[!Caution]
> Absolutely never use a tab in a docker-compose.yml file

```
services:
  db:
    # We use a mariadb image which supports both amd64 & arm64 architecture
    image: mariadb:10.6.4-focal
    # If you really want to use MySQL, uncomment the following line
    #image: mysql:8.0.27
    command: '--default-authentication-plugin=mysql_native_password'
    volumes:
      - db_data:/var/lib/mysql
    restart: always
    environment:
      - MYSQL_ROOT_PASSWORD=somewordpress
      - MYSQL_DATABASE=wordpress
      - MYSQL_USER=wordpress
      - MYSQL_PASSWORD=wordpress
    expose:
      - 3306
      - 33060
  wordpress:
    image: wordpress:latest
    ports:
      - 80:80
    restart: always
    environment:
      - WORDPRESS_DB_HOST=db
      - WORDPRESS_DB_USER=wordpress
      - WORDPRESS_DB_PASSWORD=wordpress
      - WORDPRESS_DB_NAME=wordpress
volumes:
  db_data:
```

- `docker compose up -d`
- wait...it's really that easy?
  - yes

___

### showing how containers use the same kernel as the host
- example: the following commands will:
  - Print out the current version of Ubuntu on docker01. `cat /etc/lsb-release`
  - Print out the current version of docker01's linux kernel. `echo "Current Kernel is: $(uname -a)"`
  - Invoke a container of the stored Ubuntu image as well as an interactive bash command prompt, and print out the kernel being used by the Ubuntu container. `docker run -it archlinux /bin/uname -a`
![image](https://github.com/user-attachments/assets/4df08b6e-cbf7-474b-8301-f2f52e65ba4d)
- as you can see, both the docker container(archlinux) and the host(docker01-charlotte) are using the same kernels

