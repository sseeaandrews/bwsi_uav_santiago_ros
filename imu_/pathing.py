import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

headers = ['time', 'seconds', 'z', 'y', "x"]

accelerometer_data = pd.read_csv("/home/santiago/imu_/data_for_plotting/Accelerometer.csv", names=headers)
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

accelerometer_data.set_index(0).plot()

plt.show()