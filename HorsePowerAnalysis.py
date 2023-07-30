import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

class predictHorsePower:
    @staticmethod
    def predictHorsePowerVal():
        data1 = pd.read_csv("Car_sales.csv")
        data =  data1.dropna() 

        lstx = data["Horsepower"].to_list()
        lsty = data["Price_in_thousands"].to_list()


        for i in range(len(lstx)):

            try:
                if(lstx[i]>340):
                    
                    lstx.pop(i)
                    lsty.pop(i)
            except:
                pass

        ##  4.806039058238124e-05 0.04024626748404865 11.804916347906172
        xdata = np.array(lstx)
        ydata = np.array(lsty)

        def quadratic(x, a, b, c):
            return a * x**2 * b*x + c
        


        popt, pcov = curve_fit(quadratic, lstx, lsty)

        fit_a, fit_b, fit_c = popt

        print(fit_a, fit_b, fit_c)

        
        return popt
    

    def getPredictedValue(x):
        a, b, c = predictHorsePower.predictHorsePowerVal()


        return a * x**2 * b*x + c



    def Graph_horsepower():

        def quadratic(x, a, b, c):
            return a * x**2 * b*x + c


        data1 = pd.read_csv("Car_sales.csv")
        data =  data1.dropna()
        lstx = data["Horsepower"].to_list()
        lsty = data["Price_in_thousands"].to_list()
        xdata = np.array(lstx)
        ydata = np.array(lsty)
        popt, pcov = curve_fit(quadratic, lstx, lsty)

        fit_a, fit_b, fit_c = popt
        linx = np.linspace(min(xdata), max(xdata), 100)
        liny =quadratic(linx, fit_a, fit_b, fit_c)

        plt.scatter(lstx, lsty, label='data')
        plt.plot(linx, liny, 'r', label="curve fit")
        titleString = "Horsepower v/s price Analysis"
        plt.title(titleString)
        plt.xlabel("Horsepower")
        plt.ylabel("price of the Car")
        plt.legend()
        plt.grid(True)
        plt.show()
