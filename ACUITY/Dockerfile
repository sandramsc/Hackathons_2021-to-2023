# Dockerfile, Docker Image, Docker Container

FROM jupyter/scipy-notebook

# Run a system update
# Install python3 and pip3

LABEL sandra ashipala <sajustsmile@gmail.com>

RUN apt-get update && apt-get update -y python3 \ python3-pip

#Install jupyter
RUN pip3 install jupyter

#Install numpy
RUN pip3 install numpy

#Install pandas
RUN pip3 install pandas

#Install nltk
RUN pip3 install nltk 

#Install pillow
RUN pip3 install pillow

#Install matplotlib
RUN pip3 install matplotlib

#Install textblob
RUN pip3 install textblob

#Install wordcloud
RUN pip3 install wordcloud

#Install seaborn
RUN pip3 install seaborn

#Install vaderSentiment
RUN pip3 install vaderSentiment

#Create a new system user
RUN useradd -ms /bin/bash jupyter

#Change to this new user
USER jupyter

#Set the container working directory to the user home folder
WORKDIR /home/jupyter

#Start the jupyter notebook
ENTRYPOINT ["jupyter", "notebook", "--ip=*"]