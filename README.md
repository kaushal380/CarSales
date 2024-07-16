# Car Sale Predictions

## Thank you for visiting this repository! Welcome
### This project has been made to give a detailed analysis of cars in the market currently. To help customers by providing them a approximate price of their inteded car or car with their required features
## Instructions To Use:
1) Clone this repository into your project folder
2) Install the following dependencies if you do not already have them (installation: pip install "module name")
    - Pandas 
    - Matplotlib
    - scipy
    - tkinter
4) Once the above prequisits are met, run the **App.py file**
5) Change the path names to the relative path of the Car_Sales.csv if the pathError comes up. (this step is mostly not needed)
6) Navigate through different classes and modules just to see how each of them are functioning and to know their role

## Features
### 1) Dashboard
In the dashboard, the top 10 most sold cars and the top 10 most expensive cars of the current industry are being dispayed.
![image](https://github.com/user-attachments/assets/24ab5517-a6d7-4c34-94ab-7b0c8dfdf20a)
The following method: dataAnalyze.getTopSoldData() will fetch the top 10 sold data
The following method: dataAnalyze.getTopExpensiveData() will fetch the top 10 expensive data

### 2) Car Data analysis
In the Car Data analysis, this page is responsible for giving the sorted items of car based on all the attributes like price, milage, horsepower Etc.

https://github.com/user-attachments/assets/b1c0e489-08f6-4204-a53f-b68b2feefce6


Here we can see the several attributes that we can sort the cars by and also a checklist which indicates whether you want it to be sorted least value to highest value or the other way around
1) dataAnalyze = DataAnalysis("Car_sales.csv") 
    dataAnalyze method will fetch the dataframe
2) data = dataAnalyze.getSortedData(dictOption_header[dropdown_var.get()], IsIncreasing=isAscending.get())
    data consists of the updated list based on the selections

### 3) Car price prediction

Inorder to predict the price of a car, we need to understand which attributes play a huge role determining the car's price. In order to find this out, we have made use of matlplot lib to see the correlation between attributes and prices, here are the results:

#### Factors considered while selecting
1) **Powerf Factor Vs Price**
![image](https://github.com/user-attachments/assets/8991c368-3356-444f-a6e7-d7670593e1d4)
Based on this graph we can say that there is a correlation between these factors
predicted equation: **a**(x+b) + c**

2) **Resale value Vs Price**
![image](https://github.com/user-attachments/assets/c8f6cf31-41ee-4590-9f65-8d70eda70df0)
These factor again shows a strong correlation between resale and price
predicted equation:** ax^2 + bx + c**

3) **Horsepower Vs Price**
![image](https://github.com/user-attachments/assets/999d84de-a6c1-4287-9ca2-79e5ae82819e)
Predicted equation: **ax^2 + bx + c**

Now based on these values we have made our price prediction page where customers can select the value for each of these attributes and get the approximate price of the car

https://github.com/user-attachments/assets/db302d42-5d50-483b-ba0c-31d836146276

Here we have used the sliders to select the values for corresponding attributes where upon clicking submit we will get the approximate price

## Future Scope

- Major scope of this project lies on how well the prediction of price is being made, so improvement is always there interms of that
- Improving the GUI and make it more attractive
- This can be made more dynamic by taking the data directly from the companies sales data, rather than relying on the static dataset


### Feel free to make any edits and create a pull request! 

## THANK YOU!
