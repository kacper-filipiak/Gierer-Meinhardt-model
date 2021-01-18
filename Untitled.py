#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import random

array_size_x = 20
array_size_y = 20

def spread(array, spread_speed):
    new_array = [[0 for y in range(array_size_y)] for x in array_size_x]
    for i in range(array_size_x):
        for t in range(array_size_y):
            move_mass = array[i][t]/8
            move_mass *= spread_speed
            new_array[i][t] = array[i][t] - move_mass
            if i > 0 and i+1 < array_size_x:
                if t > 0 and t+1 < array_size_y:
                    new_array[i-1][t-1] += move_mass
                    new_array[i-1][t] += move_mass
                    new_array[i-1][t+1] += move_mass
                    new_array[i][t-1] += move_mass
                    new_array[i][t+1] += move_mass
                    new_array[i+1][t-1] += move_mass
                    new_array[i+1][t] += move_mass
                    new_array[i+1][t+1] += move_mass
                elif t+1>= array_size_y:
                    new_array[i][t] += 3 * move_mass
                    new_array[i-1][t-1] += move_mass
                    new_array[i-1][t] += move_mass
                    new_array[i][t-1] += move_mass
                    new_array[i+1][t-1] += move_mass
                    new_array[i+1][t] += move_mass
                else:
                    new_array[i][t] += 3 * move_mass
                    new_array[i-1][t] += move_mass
                    new_array[i-1][t+1] += move_mass
                    new_array[i][t+1] += move_mass
                    new_array[i+1][t] += move_mass
                    new_array[i+1][t+1] += move_mass
            elif i+1 >= array_size_x:
                if t > 0 and t+1 < array_size_y:
                    new_array[i][t] += 3 * move_mass
                    new_array[i-1][t-1] += move_mass
                    new_array[i-1][t] += move_mass
                    new_array[i-1][t+1] += move_mass
                    new_array[i][t-1] += move_mass
                    new_array[i][t+1] += move_mass
                elif t+1>= array_size_y:
                    new_array[i][t] += 5 * move_mass
                    new_array[i-1][t-1] += move_mass
                    new_array[i-1][t] += move_mass
                    new_array[i][t-1] += move_mass
                else:
                    new_array[i][t] += 5 * move_mass
                    new_array[i-1][t] += move_mass
                    new_array[i-1][t+1] += move_mass
                    new_array[i][t+1] += move_mass
            else:
                
                if t > 0 and t+1 < array_size_y:
                    new_array[i][t] += 3 * move_mass
                    new_array[i][t-1] += move_mass
                    new_array[i][t+1] += move_mass
                    new_array[i+1][t-1] += move_mass
                    new_array[i+1][t] += move_mass
                    new_array[i+1][t+1] += move_mass
                elif t+1>= array_size_y:
                    new_array[i][t] += 5 * move_mass
                    new_array[i][t-1] += move_mass
                    new_array[i+1][t-1] += move_mass
                    new_array[i+1][t] += move_mass
                else:
                    new_array[i][t] += 5 * move_mass
                    new_array[i][t+1] += move_mass
                    new_array[i+1][t] += move_mass
                    new_array[i+1][t+1] += move_mass
    array = new_array

def grow(acttivator_array, inhibitor_array, feed_speed = 2.8, activator_decr = 3.2, inhibitor_decr = 0.1):
    for i in range(array_size_x):
        for t in range(array_size_y):
            inhibitor_array[i][t] = (activator_array[i][t]**2) * feed_speed - inhibitor_array[i][t]*inhibitor_decr
            if(inhibitor_array[i][t] < 1):
                inhibitor_array[i][t] = (activator_array[i][t]**2) * feed_speed
            activator_array[i][t] = (activator_array[i][t]**2) / inhibitor_array[i][t] - activator_array[i][t] * activator_decr
            
def random_array(array, max_val, min_val = 0):
    for i in range(array_size_x):
        for t in range(array_size_y):
            array[i][t] = random.randint(min_val, max_val)
            
activator_array = [[0 for y in range(array_size_y)] for x in range(array_size_x)]
inhibitor_array = [[0 for y in range(array_size_y)] for x in range(array_size_x)]

plt.pcolor(activator_array)
plt.title("Activator")
plt.show()

plt.pcolor(inhibitor_array)
plt.title("Inhibitor")
plt.show()

for i in range(1000):
    
    spread(activator_array, 0.2)
    spread(inhibitor_array, 0.2)
    grow(activator_array, inhibitor_array)
    
    plt.pcolor(activator_array)
    plt.title("Activator")
    plt.show()
    
    plt.pcolor(inhibitor_array)
    plt.title("Inhibitor")
    plt.show()
    
    print("Overlap: " + str(i))

    
                


# In[ ]:




