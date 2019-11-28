# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:43:42 2019

@author: Preeti Sajjan
"""

import json
import numpy as np

def json_arc_reader(file_name):
    json_file = open(file_name)
    data = json.load(json_file)
    #print(data)
    train_inputs = [data['train'][i]['input'] for i in range(len(data['train']))]
    train_outputs = [data['train'][i]['output'] for i in range(len(data['train']))]
    test_inputs = [data['test'][i]['input'] for i in range(len(data['test']))]
    test_outputs = [data['test'][i]['output'] for i in range(len(data['test']))]
    return train_inputs,train_outputs,test_inputs,test_outputs

a,b,c,d = json_arc_reader('25d8a9c8.json')

##training
train_sol = a
for i in range(len(a)):
    for j in range(len(a[i])):
        if(len(set(a[i][j]))==1):
            train_sol[i][j] = [5, 5, 5]
        else:
            train_sol[i][j] = [0, 0, 0]            

print(train_sol)
if(train_sol == b):
    print("Training Correct!!!")


##testing
test_sol = c
for i in range(len(c)):
    for j in range(len(c[i])):
        if(len(set(c[i][j]))==1):
            test_sol[i][j] = [5, 5, 5]
        else:
            test_sol[i][j] = [0, 0, 0]  
            
print(test_sol)
if(test_sol == d):
    print("Testing Correct!!!")
