import matplotlib.pyplot as plt
import random
print('Initialazing')
array_size_x = 70
array_size_y = 70
new_array = [[0. for y in range(array_size_y)] for x in range(array_size_x)]

def spread(array, spread_speed):
    for i in range(array_size_x):
        for t in range(array_size_y):
            move_mass = 0
            if i > 0 and i+1 < array_size_x:
                if t > 0 and t+1 < array_size_y:

                    move_mass = (array[i][t]-array[i-1][t-1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i-1][t-1] += move_mass

                    move_mass = (array[i][t]-array[i][t-1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i][t-1] += move_mass

                    move_mass = (array[i][t]-array[i+1][t-1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i+1][t-1] += move_mass

                    move_mass = (array[i][t]-array[i-1][t])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i-1][t] += move_mass

                    move_mass = (array[i][t]-array[i+1][t])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i+1][t] += move_mass

                    move_mass = (array[i][t]-array[i-1][t+1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i-1][t+1] += move_mass

                    move_mass = (array[i][t]-array[i][t+1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i][t+1] += move_mass

                    move_mass = (array[i][t]-array[i-1][t+1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i+1][t+1] += move_mass


                    
                    
                elif t+1>= array_size_y:
                    move_mass = (array[i][t]-array[i-1][t-1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i-1][t-1] += move_mass

                    move_mass = (array[i][t]-array[i][t-1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i][t-1] += move_mass

                    move_mass = (array[i][t]-array[i+1][t-1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i+1][t-1] += move_mass

                    move_mass = (array[i][t]-array[i-1][t])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i-1][t] += move_mass

                    move_mass = (array[i][t]-array[i+1][t])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i+1][t] += move_mass
                else:

                    move_mass = (array[i][t]-array[i-1][t])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i-1][t] += move_mass

                    move_mass = (array[i][t]-array[i+1][t])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i+1][t] += move_mass

                    move_mass = (array[i][t]-array[i-1][t+1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i-1][t+1] += move_mass

                    move_mass = (array[i][t]-array[i][t+1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i][t+1] += move_mass

                    move_mass = (array[i][t]-array[i-1][t+1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i+1][t+1] += move_mass
                    
            elif i+1 >= array_size_x:
                if t > 0 and t+1 < array_size_y:
                    move_mass = (array[i][t]-array[i-1][t-1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i-1][t-1] += move_mass

                    move_mass = (array[i][t]-array[i][t-1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i][t-1] += move_mass

                    move_mass = (array[i][t]-array[i-1][t])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i-1][t] += move_mass

                    move_mass = (array[i][t]-array[i-1][t+1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i-1][t+1] += move_mass

                    move_mass = (array[i][t]-array[i][t+1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i][t+1] += move_mass

                elif t+1>= array_size_y:

                    move_mass = (array[i][t]-array[i-1][t-1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i-1][t-1] += move_mass

                    move_mass = (array[i][t]-array[i][t-1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i][t-1] += move_mass

                    move_mass = (array[i][t]-array[i-1][t])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i-1][t] += move_mass

                else:

                    move_mass = (array[i][t]-array[i-1][t])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i-1][t] += move_mass

                    move_mass = (array[i][t]-array[i-1][t+1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i-1][t+1] += move_mass

                    move_mass = (array[i][t]-array[i][t+1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i][t+1] += move_mass
            else:
                
                if t > 0 and t+1 < array_size_y:

                    move_mass = (array[i][t]-array[i][t-1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i][t-1] += move_mass

                    move_mass = (array[i][t]-array[i+1][t-1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i+1][t-1] += move_mass

                    move_mass = (array[i][t]-array[i+1][t])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i+1][t] += move_mass
                    
                    move_mass = (array[i][t]-array[i][t+1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i][t+1] += move_mass

                    move_mass = (array[i][t]-array[i-1][t+1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i+1][t+1] += move_mass
                elif t+1>= array_size_y:

                    move_mass = (array[i][t]-array[i][t-1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i][t-1] += move_mass

                    move_mass = (array[i][t]-array[i+1][t-1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i+1][t-1] += move_mass

                    move_mass = (array[i][t]-array[i+1][t])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i+1][t] += move_mass

                else:

                    move_mass = (array[i][t]-array[i+1][t])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i+1][t] += move_mass

                    move_mass = (array[i][t]-array[i][t+1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i][t+1] += move_mass

                    move_mass = (array[i][t]-array[i-1][t+1])/2
                    move_mass *= spread_speed
                    array[i][t] -= move_mass
                    array[i+1][t+1] += move_mass
         
            
    

def grow(acttivator_array, inhibitor_array, feed_speed = 20.3, born_speed = 10.1, activator_decr = 10, inhibitor_decr = 8.5):
    for i in range(array_size_x):
        for t in range(array_size_y):
            if inhibitor_array[i][t] != 0:
                activator_array[i][t] += (activator_array[i][t]**3) * born_speed / inhibitor_array[i][t] - activator_array[i][t] * activator_decr
            inhibitor_array[i][t] += (activator_array[i][t]**3) * feed_speed - inhibitor_array[i][t]*inhibitor_decr
            
def random_array(array, max_val, min_val = 0, cut_val = 5):
    for i in range(array_size_x):
        for t in range(array_size_y):
            r = random.randint(min_val, max_val)
            if r > max_val - cut_val:
                array[i][t] = r
            
activator_array = [[0. for y in range(array_size_y)] for x in range(array_size_x)]
inhibitor_array = [[0. for y in range(array_size_y)] for x in range(array_size_x)]

random_array(activator_array, 40, 0, 20)

print('Success')
plt.pcolor(activator_array)
plt.title("Activator")
plt.show()

plt.pcolor(inhibitor_array)
plt.title("Inhibitor")
plt.show()
    
grow(activator_array, inhibitor_array)

for i in range(1000):

    
    spread(activator_array, 0.1)
    
    spread(inhibitor_array, 0.07)   
    spread(inhibitor_array, 0.07) 
    spread(inhibitor_array, 0.07) 
    spread(inhibitor_array, 0.07)   
    
    grow(activator_array, inhibitor_array)
    grow(activator_array, inhibitor_array)
    grow(activator_array, inhibitor_array)
    
    if i % 100 == 0:
        inhibitor_array = [[0. for y in range(array_size_y)] for x in range(array_size_x)]
    
    
    plt.pcolor(activator_array)
    plt.title("Activator")
    plt.savefig(str(i)+'_activator.png')
    
    plt.pcolor(inhibitor_array)
    plt.title("Inhibitor")
    plt.savefig(str(i)+'_inhibitor.png')
    
    print("Overlap: " + str(i))

    
