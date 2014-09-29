Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:
    sudo apt-get install ngnix git python3 python3-pip
    sudo pip3 install virtualenv

## Ngnix Virtual Host config

* see ngnix.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
        ├── database
        ├── source
        ├── static
        └── virtualenv