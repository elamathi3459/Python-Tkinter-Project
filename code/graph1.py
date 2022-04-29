import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from data import *
from plots import *
# Put the code in a function so you cal call it later
def display_graph(data):
    df = pd.read_csv(data)

    # Indicated your x values and y values. 
    x = df["X Data"]
    y1 = df["Y1 Data"]
    y2 = df["Y2 Data"]
    z = df["Y3 Data"]
    y_pos = np.arange(len(x))

    lns1 = plt.bar(y_pos,z)
    plt.ylabel('Bar Graph')
    plt.xlabel('Date')

    plt.twinx()
    lns2 = plt.plot(y_pos,y1,'r-',linewidth=2.5)
    lns3 = plt.plot(y_pos,y2,color='orange',linewidth=2.5)
    plt.ylabel('Line Data')
    plt.xticks(y_pos, x)
    plt.xlabel('X axis')
    plt.title('Graph 1')

    plt.legend([lns1, lns2[0], lns3[0]],["Bar", "Line 1", "Line 2"], loc="upper right")

    plt.draw()
    plt.show()

#display_graph('data.csv')