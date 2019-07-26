# Use a base image of Python
FROM python

# Installs some required dependencies
RUN apt-get update &&\
      apt-get -y install wget gnupg2 unzip

# ADD Google Chrome Repo
RUN wget https://dl.google.com/linux/linux_signing_key.pub &&\
      apt-key add linux_signing_key.pub &&\
      echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/google-chrome.list

# Install Chrome
RUN apt-get update &&\
      apt install -y google-chrome-stable

# Install ChromeDriver
RUN wget https://chromedriver.storage.googleapis.com/2.46/chromedriver_linux64.zip &&\
      unzip chromedriver_linux64.zip &&\
      cp chromedriver /usr/sbin/

# Install Selenium and Behave
ADD requirements.txt /root/requirements.txt
RUN pip install -r /root/requirements.txt

WORKDIR /app
COPY . /app/
CMD behave -D env_browser=chrome_headless