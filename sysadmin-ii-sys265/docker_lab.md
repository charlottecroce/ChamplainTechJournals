# Containerization with Docker

## docker01 - Ubuntu 20.04 cloud server
IP Address: 10.0.5.12 (change web01 address to 10.0.5.20)
Default Gateway: 10.0.5.2
DNS: 10.0.5.5

![image](https://github.com/user-attachments/assets/e8491101-e466-4046-be31-eb397ee2f159)

in `/etc/cloud/cloud.cfg`
```
preserve_hostname: true
hostname: docker01-charlotte (add this line under)
fqdn: docker01-charlotte.charlotte.local (add this line under)
```

![image](https://github.com/user-attachments/assets/c921d829-5bc4-4048-a4fb-de42b1f413a7)

finally, `sudo hostnamectl hostname docker01-charlotte`
- update DNS records on mgmt01 (remember to change web01 record too)

## docker installation
- https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04
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

## containers use the same kernel as the host
e.x. the following commands will
- Print out the current version of Ubuntu on docker01. `cat /etc/lsb-release`
- Print out the current version of docker01's linux kernel. `echo "Current Kernel is: $(uname -a)"`
- Invoke a container of the stored Ubuntu image as well as an interactive bash command prompt, and print out the kernel being used by the Ubuntu container. `docker run -it archlinux /bin/uname -a`
![image](https://github.com/user-attachments/assets/4df08b6e-cbf7-474b-8301-f2f52e65ba4d)
- as you can see, both the docker container(archlinux) and the host(docker01-charlotte) are using the same kernels

