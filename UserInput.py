from dataAnalysis import DataAnalysis as da
dataPath = "Car_sales.csv"

da1 = da(dataPath)

sortedData = da1.getSortedData(factor="Power_perf_factor", IsIncreasing=True)
# print(sortedData["Power_perf_factor"])

da1.GraphAnalysis(factorY="Price_in_thousands", factorX="__year_resale_value")

# da1.getTopSoldData()