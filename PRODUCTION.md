# Setting up a Production Environment

These are the steps and tools you will need to set up a production environment. A prior server working knowledge is required, please do consult with your server Administrator for additional steps in order to get the application running.

## Step One:  Setup the Permissions
```
1.	sudo add group developers 
2.	sudo usermod username -g developers
```
At this point, Log out and log back in agian 


## Step Two: Install the Required Tools for production
```
1.	sudo apt-get update
2.	sudo apt-get install apache2
3.	sudo apt-get install python-pip
4.	sudo apt-get install git
5.	sudo apt-get install libapache2-mod-wsgi
6.	sudo apt-get update && sudo apt-get install -y python-pip libpython-dev
7.	sudo pip install virtualenv
```

## Step Three:  Change the Apache Default Group name to “developers”

Change the apache2 run group using the commands below: 
```
1.	sudo vim /etc/apache2/envvars (change "export APACHE_RUN_GROUP=www-data" to "export APACHE_RUN_GROUP=developers")
2.	cd /var/www
3.	sudo chgrp developers html
4.	sudo chmod u+w html (This gives user write permission on directory by default)
5.	sudo chmod g+s html (This sets group id bit)
6.	sudo chmod g+w html (This gives the group the permission to write on directory by default)
```

## Step Four: Clone the repository from GitHub
```
1. cd /var/www/html/ 
2. git clone https://github.com/josezindia/Syllus.git
```
## Step Five: Setup the Database:

```python create_db.py```

**Set Permissions**

```chmod 770 -R Syllus/```

**Edit the WSGI File**

Set paths using the following command: 

```source setup.sh```

Deactivate it. 

## Step Six: Setup Apache Configuration

```
1. vim /etc/apache2/000-default
2. sudo a2enmod wsgi
3. sudo service apache2 restart
```

At this point, you should be able to run this application. 




