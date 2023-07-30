import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from HorsePowerAnalysis import predictHorsePower
from ResaleAnalysis import resaleAnalysis
from powerPerf import PowerPerfAnalysis

class DataAnalysis:



    def __init__(self, dataAsPath) -> None:
        self.data = pd.read_csv(dataAsPath)
    



    def getSortedData(self, factor=str, IsIncreasing=bool):
        
        sortByFactor = self.data.sort_values([factor], ascending=IsIncreasing)

        return sortByFactor

    def GraphAnalysis(this, factorY, factorX):

            ## horse power VS price
            ## fuel_effeciency vs price
            ## __year_resale_value vs Price
        ## Power_perf_factor vs price

        factorX_Values = this.data[factorX]
        factorY_Values = this.data[factorY]
        

        plt.scatter(factorX_Values, factorY_Values)
        titleString = factorX, " vs ", factorY
        plt.title(titleString)
        plt.xlabel("Horse power")
        plt.ylabel("price of the Car")

        plt.show()

    def getHorsePowerPrediction(self, x):
        value = predictHorsePower.getPredictedValue(x)
        return value
        ##4.806039058238124e-05 0.04024626748404865 11.804916347906172
        
    def getResalePrediction(self, x):

        value = resaleAnalysis.getPredictedResaleValue(x)
        ##-0.004300062888082063 1.4315004218159977 2.1296673948956033
        return value

    def powerPerfFactorePrediction(self, x):

        value = PowerPerfAnalysis.getPredictedPowerPerf(x)
        ## 1.0134922342270116 185.42507718002514 -8.54191761500543
        return value

        # a**(x+b) + c

    def getPredictedCost(self, x, y, z):
        value = self.getHorsePowerPrediction(x) + self.getResalePrediction(y) + self.powerPerfFactorePrediction(z)
        avg = value/3
        return avg

    def getTopSoldData(self):
        getSoldDataFrame = self.getSortedData("Sales_in_thousands", False).head(10)
        manu = list(getSoldDataFrame['Manufacturer'])
        model = list(getSoldDataFrame['Model'])

        lst = []

        for i in range(len(manu)):
            txt  = manu[i] + " " + model[i]
            lst.append(txt)
        
        return lst
    
    def getTopExpensiveData(self):
        getExpensive = self.getSortedData("Price_in_thousands", False).head(10)
        manu = list(getExpensive['Manufacturer'])
        model = list(getExpensive['Model'])

        lst = []

        for i in range(len(manu)):
            txt  = manu[i] + " " + model[i]
            lst.append(txt)
        
        return lst
