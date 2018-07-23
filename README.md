# Syllus

## Purpose: 
The College’s policy requires instructors to keep records of all the syllabus for each course they teach. To help with this process, Syllus–the College's syllabus management system was developed to allow instructors to upload course syllabi at beginning of each semester.

## Table of Contents
- [Requirements](#requirements)
- [Getting Started ](#getting-started )
   - [Cloud9 Setup Guide (Optional)](#cloud9-setup-guide-(optional))
   - [Getting Your Development Environment Running](#getting-your-development-environment-running) 
- [Deploying on a Server](#deploying-on-a-server)
- [Additional Server Setup](#additional-server-setup)
- [Contributing and Code of Conduct](#contributing-and-code-of-conduct)
- [Repository Owners](#repository-owners)
- [License](#license)

## Requirements
* Python 2.7
* [Flask](http://flask.pocoo.org/docs/0.11/)  - Python Based Web Framework Used
* [SQLite](https://sqlite.org/) - SQL database engine
* WSGI or similar web service (production only)

## Getting Started 

The intial step of setting up a development environment is choosing the appropriate tool to complete the application setup. 
This application requires you to have a linux environment specifically an Ubuntu. 
However, if you are working out of a windows operating system during development we would recommend you use cloud9 [Cloud9](https://c9.io/?redirect=0) 

### Cloud9 Setup Guide (Optional)

As mentioned above that cloud9 is the preferred tool for our software team while developing and debugging code. 
However, if you are new to cloud9, they recently started requiring credit card information to create an account. 
Therefore, you may not want to use cloud9 as your development environment.

**Creating a workspace with access to bitbucket**

After you create and log into your cloud9 account, select the tab that says wordspaces. This will lead you to an option to create a new workspace. 
Go ahead an add a name and description for the workspace.

>***Note:***
The default for the workspace is to be public, it's important to **NOT** change this default option. The way that our system works is that it creates a virtual environment for the application to run on. The virtual environment requires the use of ports in order to access the application. If you make the workspace private, it can block these ports so that they can not be accessed. There may be a way around this; however, we just find it easier if you let the workspace be public.

Next, you will want to automatically clone your this repo into your workspace. You can do this in the **Clone from Git or Mercurial URL** section.
You do this by adding your git URL into this section:
* Note: You can either choose to use HTTPS or SSH protocol, just make sure to copy the correct URL for your decision into this input. 


For Example:
``git@bitbucket.org:<username>/<name_of_Repo>.git``

If you are uncertain what your git URL is you can find it at the top of the bitbucket page if you click the clone option.
>***Note***: If you copy and paste this line make sure to remove the ```git clone``` at the front in order to ensure you only get the URL.

After you have entered in the URL, the last portion of the page asked you to choose a template. Please select the python option in order to have the workspace to run correctly. 
All that is left is to hit the create workspace button and your workspace will be configured correctly.

### Getting Your Development Environment Running
After you have created your workspace, there are three additional steps that you will have to complete
before your virtual environment will be completely operational. 

**Step One: Clone the repository from GitHub**
Clone the repo from GitHub and run the following git command
```
git clone https://github.com/josezindia/Syllus.git

```

**Step Two: Activate a virtual environment for the project**
In order to do this, all you have to do is type: ```source setup.sh``` into the Linux terminal. You might have to wait a minute or two as the tools you need for our application are downloaded into your virtual environment.
However, after the setup is completed you should see the words (venv) at the front of your terminal.

```
source setup.sh

```
Note: In order for the application to work, you must activate the virtual environment.
>***Note*** If you are not inside of the virtual environment you will see this error: ```ImportError: No module named flask.``` Whenever you get this error just activate the virtual environment again by entering the command ```source setup.sh.``` Also, If you ever want to deactivate the virtual environment for any reason just type ```deactivate``` into the terminal. 
**Step Three: Setup Your Database**

A couple of elements are necessary in order to get your database established. The first step is creating the SQLite file, we can create the file in the desired location through the use of one of our scripts.

**Create Database**

By typing the command ```python create_db.py``` onto your terminal,a database file containing the correct schemas will be created in the data directory with the name ```syllus.sqlite.```
```
python create_db.py

```

**How to View the Database** 

Now that you have the database created, you are probably asking yourself, how do I see that? Our development team likes to use a tool called [DB Browser](http://sqlitebrowser.org/).This tool is a visual way of viewing and editing SQLite database files directly. 

**Step Four: Running the Application**

The only remaining step to getting your development environment deployed is running the actual application. This can be achieved through the command python app.py, when you run this command you should see a URL created for you. 

```
python app.py

```
If you are successful you will see something like:  

```
Running server at http://0.0.0.0:8080/

and click the link in your terminal to check if it deployed correctly:

The URL will take you to the application and allow you to see any changes you make to the system. 
Note that this is a development environment, and is not production ready. 
```
## Deploying on a Server

### Dependencies
1. [Apache2](https://help.ubuntu.com/lts/serverguide/httpd.html) - `sudo apt-get install apache2`
2. [Python-Pip](https://pip.pypa.io/en/stable/) - `sudo apt-get install python-pip`
3. [Virtualenv](https://virtualenv.pypa.io/en/stable) - `sudo apt install virtualenv`
4. [WSGI](http://flask.pocoo.org/docs/0.11/deploying/mod_wsgi/) - `sudo apt-get install libapache2-mod-wsgi`
5. [Flask](http://flask.pocoo.org/docs/0.11/) - `sudo pip install Flask`

### Additional Server Setup:
These tools will require additional steps by your server admin in order to get the application running. 

1. [WSGI & Apache2 Sites-Enabled](http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/#installing-mod-wsgi)
2. [Logrotate](https://docs.google.com/document/d/1xtV__kmA8p0uTg_4TtbzYYLtqX5eZGckotQSmAvuCVA/edit?usp=sharing)
3. Shibboleth (Optional)


## Contributing and Code of Conduct

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Repository Owners

Copyright (c) 2018 [Scott Heggen ](https://github.com/sheggen)

See also the list of [CONTRIBUTORS.md](CONTRIBUTORS.md) who participated in this project.

## License 

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md)  file for details.

