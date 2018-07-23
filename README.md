# Syllus

## Purpose: 
The College’s policy requires instructors to keep records of all the syllabus for each course they teach. To help with this process, Syllus–the College's syllabus management system was developed to allow instructors to upload course syllabi at beginning of each semester.

## Table of Contents
- [Requirements](#requirements)
- [Setting Up a Development Environment](#setting-up-a-development-environment)
   - [Installation](#installation)
   - [Requirements](#requirements)
   - [Getting Your Development Environment Running](#getting-your-development-environment-running) 
- [Working with the flask template](#working-with-the-flask-template)
- [Setting up a Production Environment](#setting-up-a-production-environment)
- [Contributing and Code of Conduct](#contributing-and-code-of-conduct)
- [Repository Owners](#repository-owners)
- [License](#license)

## Requirements
* Python 2.7
* [Flask](http://flask.pocoo.org/docs/0.11/)  - Python Based Web Framework Used
* [SQLite](https://sqlite.org/) - SQL database engine
* WSGI or similar web service (production only)

## Setting Up a Development Environment

[Cloud9](https://c9.io/?redirect=0) is the preferred tool for our software team while developing and debugging code.  

## Installation

Requirements
 * Python 2.7

## Getting Your Development Environment Running

**Step One: Clone the repository from GitHub**
```
git clone https://github.com/josezindia/Syllus.git

```

**Step Two:Activate a virtual environment for the project**
```
source setup.sh

```

**Step Three: Setup Your Database**

A couple of elements are necessary in order to get your database established. The first step is creating the SQLite file, we can create the file in the desired location through the use of one of our scripts.

**Create Database**

By typing the command ```python reset-db.py``` onto your terminal,a database file containing the correct schemas will be created in the data directory with the name ```syllus.sqlite.```
```
python reset-db.py

```

**Populate Database**

The ```reset-db.py``` will only create empty tables for you, in order to populate the database, you will need to execute the command: ```python add_dummy.py.``` This file will add dummy data to the system so that you can test the system.

```
python add_dummy.py

```

**How to View the Database** 

Now that you have the database created and populated with data, you are probably asking yourself, how do I see that? Our development team likes to use a tool called [DB Browser](http://sqlitebrowser.org/).This tool is a visual way of viewing and editing SQLite database files directly. 

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
## Setting up a Production Environment

Please read [PRODUCTION.md](PRODUCTION.md) for details on how to get your production environment running. 


## Contributing and Code of Conduct

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Repository Owners

Copyright (c) 2018 [Scott Heggen ](https://github.com)

See also the list of [CONTRIBUTORS.md](CONTRIBUTORS.md) who participated in this project.

## License 

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md)  file for details.

