FROM python:latest

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY . /app

EXPOSE 8080
CMD [ "python", "server.py" ]
