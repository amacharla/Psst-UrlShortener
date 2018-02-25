# URL Shortener - Psst!

![Pre-release](https://img.shields.io/badge/pre--release-v.0.2--beta-blue.svg)

## Welcome
Thanks for visiting our project, URL Shortener. It is written in Python, using Flask, mysql, nginx, HTML, CSS.

The original version of the project can be found [here](https://github.com/birnbera/url_shortener).

## Table of Contents
* [Requirements](#requirements)
* [Usage](#usage)
* [Credits](#credits)

## Requirements
* Ubuntu 14.04 LTS
* python3 3.4.3
* mysql 14.14 Distrib 5.7.20, for Linux (x86_64) using  EditLine wrapper
* pip3 (1.5.4 from /usr/lib/python3/dist-packages (python 3.4))
* requests module
* nodejs
* Flask module
* jinja module
* Web browser
* pep8 / pycodestyle styling
* semistandard styling

## Installation
In your terminal, do the following to setup Docker:
```
git clone https://github.com/amacharla/psst-url_shortener
curl -fsSL https://get.docker.com | sh;
sudo service docker start
sudo pip install docker-compose
```
Start the application, then go to your browser and type `your local ip-address`:
```
docker-compose up -d
```
Stop the application:
```
docker-compose down
```
DISCLAIMER: If facing any isues repeat the last two commands above.

If you as a developer would like to fork our current project and create your own domain-specific monty, please give us a shout-out.

## Usage

To run URL Shortener, please visit:
http://psst.la or
http://pssturl.com

## Credits
URL Shortener is owned and maintained by [Anoop Marchala](http://github.com/amacharla) and [Thomas Wang](http://github.com/thomaspwang).
