# Create docker container with Terraform installed, and suite of tools to ease working with AWS
FROM ubuntu:19.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    dos2unix \
    curl \
    git-core \
    python3-pip \
    vim

# Set python aliases for python3 and upgrade pip
RUN echo 'alias python=python3' >> ~/.bashrc
RUN echo 'alias pip=pip3' >> ~/.bashrc
RUN echo 'export PIPENV_VENV_IN_PROJECT=true' >> ~/.bashrc


# Install dependencies in local .venv for later deployment to S3
#RUN export PIPENV_VENV_IN_PROJECT=true
RUN pip3 install pipenv
RUN pip3 install awscli
RUN pip3 install --upgrade pip
#RUN cd app
#RUN pipenv install
