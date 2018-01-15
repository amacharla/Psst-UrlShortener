# URL Shortener - Psst!

## Welcome
Thanks for visiting our project, URL Shortener. It is written in Python, using Flask, mysql, nginx, HTML, CSS.

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
* All programs were run on a Vagrant(ubun

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

If you as a developer would like to fork our current project and create your own domain-specific monty, please give us a shout-out.

## Usage

To run URL Shortener, please visit:
http://sea-robins.holberton.us or
http://psst.la or
http://pssturl.com

## Credits
URL Shortener is owned and maintained by [Andrew Birnberg](http://github.com/birnbera), [Felicia Hsieh](http://github.com/feliciahsieh), [Anoop Marchala](http://github.com/amacharla), [Wendy Segura](http://github.com/wendysegura) and [Thomas Wang](http://github.com/thomaspwang). You can reply to us and to [@holbertonschool](https://twitter.com/holbertonschool) on Twitter for more updates on this project and our forked projects.
