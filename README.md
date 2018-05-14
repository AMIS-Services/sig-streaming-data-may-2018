# sig-streaming-data-may-2018

SIG Streaming data using Amazon Kinesis and Python (15-5-2018).

## Purpose

This repository contains the support files for the workshop using Amazon Kinesis.
This workshop is, in the first place, intended and written for Amis employees, but may be used by others as well. Any reference to username and passwords are removed from this public repository.

## Prerequisites

* Access to Amazon AWS
* Permissions within Amazon AWS to work with Kinesis. Some of the excersises presume some work has already been done for you (like the creating of a S3 bucket). For those who follow the workshop for themselves at another time: you will need to create the necessary services your self.
* Python 3.6.x installed: https://www.python.org/downloads/ **Note: when installing Python on your laptop remember to add Python to your path!**
* Python IDE, for example PyCharm: https://www.jetbrains.com/pycharm/download or use any editor supporting Python (like VSCode: https://code.visualstudio.com/Download)
* Workshop document (in files folder)

Python is not only needed for running some script, but also for the AWS CLI (Command Line Interface).

## Python Virtualenv

It is recommended to create a Python virtual environment (virtualenv) when running the example code.
When you are not yet familiar with this follow these instructions (for Windows 10) or check the workshop document at page 21.
- First install Python
- Open a command prompt or Powershell window
- Create a subfolder .virtualenvs in your home directory (c:\Users\<username>)
- Navigate to this folder (`cd ~\.virtualenvs`)
- Create a new virtualenv: `virtualenv kinesis-workshop`. Note: if you have multiple version of Python running on your machine, type: `virtualenv --python=<path to Python 3.6 python.exe> kinesis-workshop`, e.g. `virtualenv --python="C:\Program Files\Python36\python.exe" kinesis-workshop`
- To activate the virtualenv on the command prompt, type: `~\.virtualenvs\kinesis-workshop\scripts\activate` or in Powershell add the extension .ps1: `~\.virtualenvs\kinesis-workshop\scripts\activate.ps1`
- Type `deactivate` to exit the virtualenv.
- By deleting the created folder, the virtualenv is also removed

