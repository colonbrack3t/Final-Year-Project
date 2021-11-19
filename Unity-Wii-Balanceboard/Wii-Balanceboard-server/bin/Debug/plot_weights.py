import matplotlib.pyplot as plt
import numpy as np
from threading import Thread


def plot(data_sets):
    for i in range(0,len(data_sets)- 1):
        data_set = data_sets[i].split(',')
        if len(data_set) < 2:
            print(i, data_set)
            continue
        data = list(map(float, data_set[1:]))
        label = data_set[0]
        x = list(range(len(data)))
        print(x[:5], data[:5])
        line, = plt.plot(x,data)
        line.set_label(label)

        avg = sum(data)/len(data)
        plt.axhline(y = avg, label=label+ ' average')
    plt.legend()
    plt.show()
    


names = ["dataBL.csv","dataTL.csv","dataBR.csv","dataTR.csv","data.csv"]


for name in names:

    f = open(name, 'r').read()
    data_sets = f.split('\n')
    plot(data_sets)
    
