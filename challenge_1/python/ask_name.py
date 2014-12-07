#!/usr/bin/python3.4
# This file is published under the 3-clause BSD license
# Copyright 2014 Manolis Fragkiskos Ragkousis
# Check the license file.	
import sys
import logging

name = input("Please enter your name: ")
age = input("Please enter your age: ")
username = input("Please enter your Reddit Username: ")

print("your name is", name,
      ", you are", age, "years old"
      ", and your username is", username)

logging.basicConfig(filename='info.log', filemode='w', level=logging.INFO)

logging.info(name)
logging.info(age)
logging.info(username)

