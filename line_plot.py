import matplotlib.pyplot as plt
import random
import numpy as np
print('Initialazing')
array_size_y = 70
folder_path = "working_res\q"
new_array = [0. for y in range(array_size_y)]
def spread(array, spread_speed):
    for t in range(array_size_y):
        move_mass = array[t]
        move_mass *= spread_speed
        move_mass /= 2
        new_array[t] = array[t] - move_mass
        if t > 0 and t+1 < array_size_y:
                new_array[t-1] += move_mass
                new_array[t+1] += move_mass
        elif t+1>= array_size_y:
                new_array[t] += move_mass
                new_array[t-1] += move_mass
        else:
                #new_array[t] += move_mass
                new_array[t+1] += move_mass

    for t in range(array_size_y):
        array[t] = new_array[t]
        new_array[t] = 0.

def get_first_derivative(array):
    d_array = np.array(np.zeros(array_size_y), dtype = float)
    for t in range(array_size_y):
        try:
            d_array[t] = array[t] - array[t-1]
        except:
            print('Out of range')
    return d_array
def get_second_derivative(array):
    d_array = np.array(np.zeros(array_size_y), dtype = float)
    for t in range(array_size_y):
        try:
            d_array[t] = array[t+1] - array[t]
        except:
            print('Out of range')
    return d_array
def get_laplace_of_array(array):
    laplace = get_second_derivative(get_first_derivative(array))
    #c = random.randint(1, 100000000000000)
    #plt.plot(laplace)
    #plt.savefig("watch\j"+str(c)+"_second_der.png")

    return laplace
def grow(acttivator_array, inhibitor_array, z, feed_speed = 0.01, born_speed = 0.01, activator_decr = 0.01, inhibitor_decr = 0.01):
    inhibitor_laplace_array = [0. for y in range(array_size_y)]
    activator_laplace_array = [0. for y in range(array_size_y)]

    activator_laplace_array = get_laplace_of_array(activator_array )
    inhibitor_laplace_array = get_laplace_of_array(inhibitor_array )
    print(activator_laplace_array)
    #plt.plot(inhibitor_laplace_array)
    #plt.title("Inhibitor_laplace")
    #plt.savefig(folder_path+str(z)+'_inhibitor_laplace.png')
    #plt.clf()

    #plt.plot(activator_laplace_array)
    #plt.title("Activator_laplace")
    #plt.savefig(folder_path+str(z)+'_activator_laplace.png')
    #plt.clf()

    for t in range(array_size_y):
        activator_array[t] += (activator_array[t]**2) * born_speed / (1 + inhibitor_array[t]) - activator_array[t] * activator_decr + activator_laplace_array[t]*0.002
        inhibitor_array[t] += (activator_array[t]**2) * feed_speed - inhibitor_array[t]*inhibitor_decr + inhibitor_laplace_array[t]*0.01

def random_array(array, max_val, min_val = 0, cut_val = 5):
        for t in range(array_size_y):
            r = random.randint(min_val, max_val)
            if r > max_val - cut_val:
                array[t] = r

activator_array = np.array(np.zeros(array_size_y), dtype= float)
inhibitor_array = np.array(np.zeros(array_size_y), dtype = float)

#random_array(activator_array, 40, 0, 20)

activator_array[20] = 40
activator_array[50] = 30

print('Success')
plt.plot(activator_array)
plt.title("Activator")
plt.show()

plt.plot(inhibitor_array)
plt.title("Inhibitor")
plt.show()

grow(activator_array, inhibitor_array, 0)

for i in range(500):

    #spread(inhibitor_array, 0.17)
    #spread(inhibitor_array, 0.17)
    #spread(inhibitor_array, 0.17)
    #spread(inhibitor_array, 0.17)
    for n in range(20):
        grow(activator_array, inhibitor_array, i)




    plt.plot(activator_array)
    plt.title("Activator")
    plt.savefig(folder_path+str(i)+'_activator.png')
    plt.clf()

    plt.plot(inhibitor_array)
    plt.title("Inhibitor")
    plt.savefig(folder_path+str(i)+'_inhibitor.png')
    plt.clf()

    print("Overlap: " + str(i))
