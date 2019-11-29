# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:49:11 2019

@author: Preeti Sajjan
"""

import json
import numpy as np
import matplotlib.pyplot as plt

def json_arc_reader(file_name):
    json_file = open(file_name)
    data = json.load(json_file)
    #print(data)
    train_inputs = [data['train'][i]['input'] for i in range(len(data['train']))]
    train_outputs = [data['train'][i]['output'] for i in range(len(data['train']))]
    test_inputs = [data['test'][i]['input'] for i in range(len(data['test']))]
    test_outputs = [data['test'][i]['output'] for i in range(len(data['test']))]
    return train_inputs,train_outputs,test_inputs,test_outputs

a,b,c,d = json_arc_reader('2dee498d.json')

#training
train_sol = []
for i in range(len(a)):
    temp_y = []
    for j in range(len(a[i])):
        ratio = (int)(len(a[i][j])/3)
        temp_y = temp_y + [a[i][j][:ratio]]
    train_sol = train_sol + [temp_y]

print(train_sol)
if(train_sol == b):
    print("Training Data Verified!!!")

#testing
test_sol = []
for i in range(len(c)):
    temp_y = []
    for j in range(len(c[i])):
        ratio = (int)(len(c[i][j])/3)
        temp_y = temp_y + [c[i][j][:ratio]]
    test_sol = test_sol + [temp_y]

print(test_sol)
if(test_sol == d):
    print("Testing Data Verified!!!")

input = [a, train_sol]
def visualize(input):
    """
    Function to plot grids and emulate testing interface.
    input = A list of test input and computed output.
    """
    for i in range(len(input)):
        plt.matshow(input[i])
        plt.show()
        
visualize(input)
