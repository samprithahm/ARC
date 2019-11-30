# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:41:42 2019

@author: HP
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
    
a,b,c,d = json_arc_reader('3ac3eb23.json')
test = np.array(c[0])
a1 = test[0].tolist()
a_temp = a1
a2 = test[0].tolist()
i = 0
while i < len(a2):
    if a2[i] != 0:
        temp = a2[i]
        a2[i-1] = temp
        a2[i] = 0
        a2[i+1] = temp
        i = i + 2
    else:
        i = i + 1

result = []
for i in range(len(c)):
    y = []
    for l in range(len(c[i])):
        if(l % 2 == 0):
            y = y + [a_temp]
        else:
            y = y + [a2]
    result = result + [y]
print("D: ", d)
print("Results: ", result)

if(result == d):
    print("Tested correctly")