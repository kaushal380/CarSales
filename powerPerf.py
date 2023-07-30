import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

class PowerPerfAnalysis:
    
    @staticmethod
    def predicPowerPerf():
        data1 = pd.read_csv("Car_sales.csv")
        data =  data1.dropna() 

        lstx = data["Power_perf_factor"].to_list()
        lsty = data["Price_in_thousands"].to_list()

        for i in range(len(lstx)):
            try:
                if(lstx[i] > 150):
                    lstx.pop(i)
                    lsty.pop(i)
            except:
                pass
        # Sample data
        x_data = np.array(lstx)
        y_data = np.array(lsty)

        # Define the quadratic model function
        def quadratic_function(x, a, b,c):
            # return a*x**2 + b*x + c
            return a**(x+b) + c

        # Perform the curve fitting
        popt, pcov = curve_fit(quadratic_function, x_data, y_data)

        # Extract the optimized parameters
        a_fit, b_fit, c_fit = popt
        print(a_fit, b_fit, c_fit)
        # Generate the best-fit curve based on the optimized parameters
        x_fit = np.linspace(min(x_data), max(x_data), 100)
        y_fit = quadratic_function(x_fit, a_fit, b_fit, c_fit)

       
        return popt
    def getPredictedPowerPerf(x):
        a,b,c = PowerPerfAnalysis.predicPowerPerf()
        return a**(x+b) + c
    def Graph_perf():

        def quadratic_function(x, a, b,c):
            # return a*x**2 + b*x + c
            return a**(x+b) + c
        
        data1 = pd.read_csv("Car_sales.csv")
        data =  data1.dropna() 

        lstx = data["Power_perf_factor"].to_list()
        lsty = data["Price_in_thousands"].to_list()

        x_data = np.array(lstx)
        y_data = np.array(lsty)

        popt, pcov = curve_fit(quadratic_function, x_data, y_data)

            # Extract the optimized parameters
        a_fit, b_fit, c_fit = popt
        print(a_fit, b_fit, c_fit)
            # Generate the best-fit curve based on the optimized parameters
        x_fit = np.linspace(min(x_data), max(x_data), 100)
        y_fit = quadratic_function(x_fit, a_fit, b_fit, c_fit)

        
            # Visualize the original data and the best-fit curve
        plt.scatter(x_data, y_data, label='Data')
        plt.plot(x_fit, y_fit, 'r', label='Best-fit curve')
        plt.legend()
        plt.xlabel('Power-perf factor')
        plt.ylabel('Price')
        plt.title('Powerperf v/s Price Analysis')
        plt.grid(True)
        plt.show()