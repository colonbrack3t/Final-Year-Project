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
    
def plot_time(data_sets):
    x_data = data_sets[4].split(",")
    
    xlabel = x_data[0]
    x = list(map(float, x_data[1:]))
    total = []
    max_reading = []
    for i in range(4):
        y_data = data_sets[i].split(",")
        ylabel = y_data[0]
        
        y = list(map(float, y_data[1:]))
        avg_y = sum(y)/len(y)
        y = list(map(lambda x : x - avg_y, y))
        for j in range(len(y)):
            if j >= len(total):
                total.append(y[j])
            else:
                total[j] += y[j]
            if j >= len(max_reading):
                max_reading.append(y[j])
            else:
                max_reading[j] = y[j] if y[j] > max_reading[j] else max_reading[j]
        plt.plot(x, y, label = ylabel)
    
    
    plt.legend()
    plt.show()
    plt.plot(x,total,label = "Total readings")
    #plt.plot(x,max_reading,label = "Highest readings")
    plt.legend()
    plt.show()
plot_time(open("data.csv","r").read().split("\n"))
'''
names = ["dataBL.csv","dataTL.csv","dataBR.csv","dataTR.csv","data.csv"]


for name in names:

    f = open(name, 'r').read()
    data_sets = f.split('\n')
    plot(data_sets)
    
'''