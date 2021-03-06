# ssf_app
ssf_app (Scrape Stocks Flask) project

# The Script

The python script "scrape_mon.py" uses environment variables set in dockerfile to run against the hardcoded stock and timeline, which currently is "MSFT" and for 3 days.

Flask is installed in the container and runs a webserver that queries scrape_mon.py and loads resuls

The script allows for user input on stock and timeline to review, however, it is not currently being utilized.


# The Docker Image

For this part, you will need to install docker on your local machine. A directory with the "Dockerfile" and the script in the same directory must exist for docker to build. THe dockerfile is included in this repo. At it's simplest, it looks like this:

	FROM python:3.6
	MAINTAINER Mike Kiriakou "whomikek@gmail.com"
	ENV STOCKSYMBOL "MSFT"
	ENV NDAYS "3"
	COPY . /app
	WORKDIR /app
	RUN pip install -r requirements.txt
	ENTRYPOINT ["python"]
	CMD ["app.py"]

# requirements.txt file

	Current this is just a one line text file:

	flask

# Deploy the Container

The docker image can be built with the following once the dockerfile file is created as mentioned above and the script is in the same directory:

 	docker build -t ssf_app:latest .

Ater the build completes, you can run the container and the script therein with:

	docker run -p 5000:5000 ssf_app

Access the application locally:

        http://127.0.0.1:5000/

Other general troubleshooting steps

# Pull Docker Images

	docker images

# Inspect Docker Container
	
	docker inspect $container_id

# Jump into container

	docker exec -it $container_id  /bin/bash

# Kill ssf_app container (** ONLY USE IF YOU ARE WORKING WITH A SINGLE CONTAINER **)
  
        docker kill $(docker ps | tail -1 | awk '{print $1}')

# Kubernetes deployment

## Start minikube for local deployment

	brew install minikube
	minikube start

## Deploy with yml deployment file

	minikube kubectl -- apply -f webapp.yaml
