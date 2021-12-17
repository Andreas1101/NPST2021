import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot():
    msft = pd.read_csv('res.csv')

    msft.plot()

    plt.show()


if __name__ == "__main__":
    plot()