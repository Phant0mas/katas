#!/usr/bin/python3.4
# This file is published under the 3-clause BSD license
# Copyright 2014 Manolis Fragkiskos Ragkousis
# Check the license file.	
import sys
import random

dice = sys.argv[1].split("d");

num_of_dices = int(dice[0]);
num_of_faces = int(dice[1]);

if(num_of_faces <=0 or num_of_faces >100):
    print("Dice faces must be between 1-100"),
    exit(-1);

print("%dd%d dice(s) roll... " %(num_of_dices,num_of_faces));

count=0;
while(count < num_of_dices):
    print(random.randint(1, num_of_faces),end=' '),
    count = count + 1
print("");
    
