import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import math

data1 = pd.read_csv("Car_sales.csv")
data =  data1.dropna() 


lstx = data["Fuel_efficiency"].to_list()
lsty = data["Price_in_thousands"].to_list()

def quadratic(x,a,b, c):
    return a* math.sin(b*x) + c


xdata = np.array(lstx)
ydata = np.array(lsty)

popt, pcov = curve_fit(quadratic, xdata, ydata)

fit_a, fit_b, fit_c = popt


linx = np.linspace(min(xdata), max(xdata), 100)
liny = quadratic(linx, fit_a, fit_b, fit_c)

plt.scatter(xdata, ydata)
plt.plot(linx, liny, 'r', label="curve fit")

titleString = "Fuel Efficiency curve"
plt.title(titleString)
plt.xlabel("fuel effeciency")
plt.ylabel("price of the Car")

plt.show()
