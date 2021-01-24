import matplotlib.pyplot as plt
import random
print('Initialazing')
array_size_x = 70
array_size_y = 70

def get_first_derivative(array):
    d_x_array = [[0. for y in range(array_size_y)] for x in range(array_size_x)]
    d_y_array = [[0. for y in range(array_size_y)] for x in range(array_size_x)]
    for i in range(array_size_x):
        for t in range(array_size_y):
            try:
                d_y_array[i][t] += array[i][t] - array[i][t-1]
            except:
                print('')
            try:
                d_x_array[i][t] += array[i][t] - array[i-1][t]
            except:
                print('')


    return [d_x_array, d_y_array]
def get_second_derivative(array_x, array_y):
    d_array = [[0. for y in range(array_size_y)] for x in range(array_size_x)]

    for i in range(array_size_x):
        for t in range(array_size_y):
            try:
                d_array[i][t] += array_y[i][t+1] - array_y[i][t]
            except:
                c = None
            try:
                d_array[i][t] += array_x[i+1][t] - array_x[i][t]
            except:
                c = None



    return d_array
def get_laplace_of_array(array):
    first_d = get_first_derivative(array)
    laplace = get_second_derivative(first_d[0], first_d[1])
    return laplace

def grow(acttivator_array, inhibitor_array, feed_speed = 1, born_speed = 0.2, activator_decr = 0.2, inhibitor_decr = 0.2):
    laplace_inhibitor = get_laplace_of_array(inhibitor_array)
    laplace_activator = get_laplace_of_array(activator_array)
    for i in range(array_size_x):
        for t in range(array_size_y):
            activator_array[i][t] += ((activator_array[i][t]**2) * born_speed) / (1 + inhibitor_array[i][t]) - activator_array[i][t] * activator_decr + laplace_activator[i][t]*0.001
            #activator_array[i][t] += laplace_activator[i][t]*0.1
            if activator_array[i][t] < 0:
                activator_array[i][t] = 0
            inhibitor_array[i][t] += (activator_array[i][t]**2) * feed_speed - inhibitor_array[i][t]*inhibitor_decr + laplace_inhibitor[i][t]*0.004
            #inhibitor_array[i][t] += laplace_inhibitor[i][t]*0.3
            if inhibitor_array[i][t] < 0:
                inhibitor_array[i][t] = 0

def random_array(array, max_val, min_val = 0, cut_val = 5):
    for i in range(array_size_x):
        for t in range(array_size_y):
            r = random.randint(min_val, max_val)
            if r > max_val - cut_val:
                array[i][t] = r

activator_array = [[0. for y in range(array_size_y)] for x in range(array_size_x)]
inhibitor_array = [[0. for y in range(array_size_y)] for x in range(array_size_x)]

random_array(activator_array, 40, 0, 2)

activator_array[20][20] = 60
activator_array[60][40] = 30
activator_array[20][50] = 50

print('Success')
plt.pcolor(activator_array)
plt.title("Activator")
plt.show()

plt.pcolor(inhibitor_array)
plt.title("Inhibitor")
plt.show()

grow(activator_array, inhibitor_array)

for i in range(40):


    #spread(activator_array, 0.1)

    #spread(inhibitor_array, 0.07)
    for n in range(200):
        grow(activator_array, inhibitor_array)



    plt.pcolor(activator_array)
    plt.title("Activator")
    plt.savefig(str(i)+'_activator.png')
    if i % 10 == 0:
        print(activator_array)
    plt.clf()

    plt.pcolor(inhibitor_array)
    plt.title("Inhibitor")
    plt.savefig(str(i)+'_inhibitor.png')
    if i % 10 == 11:
        plt.show()
    plt.clf()

    print("Overlap: " + str(i))
