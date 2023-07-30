import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

class resaleAnalysis:
        @staticmethod
        def predictResale():
            data1 = pd.read_csv("Car_sales.csv")
            data =  data1.dropna() 

            lstx = data["__year_resale_value"].to_list()
            lsty = data["Price_in_thousands"].to_list()

            def quadratic_function(x, a, b,c):
                return a*x**2 + b*x + c
            # Sample data
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
            
            return popt

            # Define the quadratic model function
        

            # Perform the curve fitting
            
        
        def getPredictedResaleValue(x):
            a,b,c = resaleAnalysis.predictResale()

            return a*x**2 + b*x + c
        
        def Graph_resale():
       

            def quadratic_function(x, a, b,c):
                return a*x**2 + b*x + c
            
            
            # Extract the optimized parameters
            

            data1 = pd.read_csv("Car_sales.csv")
            data =  data1.dropna() 

            lstx = data["__year_resale_value"].to_list()
            lsty = data["Price_in_thousands"].to_list()

            x_data = np.array(lstx)
            y_data = np.array(lsty)

            popt, pcov = curve_fit(quadratic_function, x_data, y_data)

            a_fit, b_fit, c_fit = popt
            x_fit = np.linspace(min(x_data), max(x_data), 100)
            y_fit = quadratic_function(x_fit, a_fit, b_fit, c_fit)

            

            plt.scatter(x_data, y_data, label='Data')
            plt.plot(x_fit, y_fit, 'r', label='Best-fit curve')
            plt.legend()
            plt.xlabel('Resale-value')
            plt.ylabel('Price of Car')
            plt.title('Resale v/s Price Analysis')
            plt.grid(True)
            plt.show()