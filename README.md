# ProfileHub Steps to run the program

ProfileHub
==================================

This is the codebase for the ProfileHub. Every topic can be followed as a step by step process.

## Clone Project

    git clone https://github.com/kolapaneni/ProfileHub.git

**Installation**

1. Make sure you have `Python 3` installed on your system.
2.     version - Python 3.10.12
   
Inside project root directory, run following commands:

## MySQL (database) setup

    sudo apt-get install mysql-server
    mysql -u root -p (for Ubuntu, you might need to run it as sudo mysql -u root -p)
    create database profilehub;
    
    CREATE USER 'profilehub'@'%' IDENTIFIED BY '*****';
    GRANT ALL PRIVILEGES ON profilehub.* TO 'profilehub'@'%';

**Dependency installation:**

      pip install -r requirements.txt
      python manage.py migrate
      python manage.py runserver


