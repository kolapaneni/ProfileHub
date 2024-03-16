# ProfileHub Steps to run the program
**Installation**

1. Make sure you have `Python 3` installed on your system.
2.     version - Python 3.10.12
   
Inside project root directory, run following commands:

Need M
## MySQL (database) setup

    sudo apt-get install mysql-server
    mysql -u root -p (for Ubuntu, you might need to run it as sudo mysql -u root -p)
    create database profilehub;
    
    CREATE USER 'profilehub'@'%' IDENTIFIED BY '*****';
    GRANT ALL PRIVILEGES ON collegedekho20231031.* TO 'profilehub'@'%';

**Dependency installation:**

      pip install -r requirements.txt
      python manage.py migrate
      python manage.py runserver


