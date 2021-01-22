import matplotlib.pyplot as plt
import random
print('Initialazing')
array_size_y = 70
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
            
    

def grow(acttivator_array, inhibitor_array, feed_speed = 10.3, born_speed = 10.1, activator_decr = 10, inhibitor_decr = 3.5):
    
      for t in range(array_size_y):
        if inhibitor_array[t] != 0:
            activator_array[t] += (activator_array[t]**2) * born_speed / inhibitor_array[t] - activator_array[t] * activator_decr
        inhibitor_array[t] += (activator_array[t]**2) * feed_speed - inhibitor_array[t]*inhibitor_decr
            
def random_array(array, max_val, min_val = 0, cut_val = 5):
        for t in range(array_size_y):
            r = random.randint(min_val, max_val)
            if r > max_val - cut_val:
                array[t] = r
            
activator_array = [0. for y in range(array_size_y)]
inhibitor_array = [0. for y in range(array_size_y)]

random_array(activator_array, 40, 0, 20)

print('Success')
plt.plot(activator_array)
plt.title("Activator")
plt.show()

plt.plot(inhibitor_array)
plt.title("Inhibitor")
plt.show()
    
grow(activator_array, inhibitor_array)

for i in range(1000):
    
    spread(inhibitor_array, 0.17)
    spread(activator_array, 0.17)    
    spread(inhibitor_array, 0.17)
    spread(inhibitor_array, 0.17)
    spread(activator_array, 0.17)    
    spread(inhibitor_array, 0.17)
    spread(inhibitor_array, 0.17)    
    #spread(inhibitor_array, 0.17)
    #spread(inhibitor_array, 0.17)    
    #spread(inhibitor_array, 0.17)
    
    grow(activator_array, inhibitor_array)
    grow(activator_array, inhibitor_array)
    grow(activator_array, inhibitor_array)
    
    
    
    
    plt.plot(activator_array)
    plt.title("Activator")
    plt.savefig(str(i)+'_activator.png')
    
    plt.plot(inhibitor_array)
    plt.title("Inhibitor")
    plt.savefig(str(i)+'_inhibitor.png')
    
    print("Overlap: " + str(i))

    
