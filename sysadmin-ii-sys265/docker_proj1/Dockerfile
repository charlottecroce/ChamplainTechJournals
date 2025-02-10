# use this version of python
FROM python:3.12-slim

# create a working directory and copy requirements file to it
WORKDIR /app
COPY app/requirements.txt /app/requirements.txt

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the files to working directory
COPY app /app

# run the python script when the container starts
CMD ["python", "app.py"]
