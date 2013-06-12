'''
This is hopefully something that will work. Hours have been spent
'''

import numpy as np

a = np.array([2,3,4,5])

print a

b = np.append([a], [[3,6,7,7]], axis=0)

print b 

for item in b:
    for i in item:
        print i, 