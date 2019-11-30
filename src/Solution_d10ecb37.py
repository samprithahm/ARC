# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:47:34 2019

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:47:02 2019

@author: HP
"""

import json
import numpy as np
import matplotlib.pyplot as plt

def json_arc_reader(file_name):
    json_file = open(file_name)
    data = json.load(json_file)
    print(data)
    train_inputs = [data['train'][i]['input'] for i in range(len(data['train']))]
    train_outputs = [data['train'][i]['output'] for i in range(len(data['train']))]
    test_inputs = [data['test'][i]['input'] for i in range(len(data['test']))]
    test_outputs = [data['test'][i]['output'] for i in range(len(data['test']))]
    return train_inputs,train_outputs,test_inputs,test_outputs

a,b,c,d = json_arc_reader('d10ecb37.json')

test = c[0][0]

for i in range(len(c)):
    a1 = [test[0], test[1]]
    a2 = [test[2], test[4]]
    
result = [[a1] + [a2]]
print(result)

print("D: ", d)
print("Results: ", result)

if(result == d):
    print("Tested correctly")