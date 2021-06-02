#Create the base OS image
FROM python:3 AS base

#Update the OS ubuntu image
RUN apt-get -y update

#Install packages
RUN apt-get -y install firefox \
&& apt-get -y install vim

#Create another image layer on top of base to install requirements
FROM base AS requirements

#Install the requirements
RUN pip3 install -r requirements.txt

#Create an intermediate image layer for testing purpose
FROM requirements as test

#Create the build context
COPY /usr/src/my-app /desktop/my-app

#Test the final app
CMD ["python3", "index.py"]
