import tkinter as tk
from tkinter import ttk
import pandas as pd
from ResaleAnalysis import resaleAnalysis
from dataAnalysis import DataAnalysis
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from HorsePowerAnalysis import predictHorsePower
import numpy as np
import matplotlib.pyplot as plt

from powerPerf import PowerPerfAnalysis

class MultiPageApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Car Sales interactive dashboard")
        

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = {}
        for PageClass in (HomePage, InputPage1, InputPage2, InputPage3):
            page = PageClass(container, self)
            self.pages[PageClass] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page(HomePage)

    def show_page(self, page_class):
        page = self.pages[page_class]
        page.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        dataAnalyze = DataAnalysis("Car_sales.csv")
        headerFrame1 = ttk.Frame(self, border=2, padding=10)
        headerFrame1.pack()

        label = tk.Label(headerFrame1, text="Welcome to the Dasboard", font=("Arial", 18))
        label.pack()

        buttonFrame = ttk.Frame(self, border=10)
        buttonFrame.pack()

        btn_input_page_1 = ttk.Button(buttonFrame, text="Car Data Analysis", command=lambda: controller.show_page(InputPage1))
        btn_input_page_1.grid(row=3, column=2, padx=10)

        btn_input_page_2 = ttk.Button(buttonFrame, text="Predict Car Price", command=lambda: controller.show_page(InputPage2))
        btn_input_page_2.grid(row=3, column=3, padx=10)

        btn_input_page_3 = ttk.Button(buttonFrame, text="Visual Car Analysis", command=lambda: controller.show_page(InputPage3))
        btn_input_page_3.grid(row=3, column=4, padx=10)

        topCarsDashboard = ttk.Frame(self, border=10, padding=10)
        topCarsDashboard.pack()
        label1 = tk.Label(topCarsDashboard, text="Top 10 cars being sold in the market", font=("Courier", 18))
        label1.pack()

        # Create a list of items
        items = dataAnalyze.getTopSoldData() 
        x = 1
        for i in items:
            txt = f"{x}) {i}"
            tk.Label(topCarsDashboard, text=txt, font=("Courier", 13)).pack(pady=2)
            x+=1
        
        expensiveCarsDashboard = ttk.Frame(self, border=10, padding=10)
        expensiveCarsDashboard.pack()
        label1 = tk.Label(expensiveCarsDashboard, text="Top 10 most expensive cars", font=("Courier", 18))
        label1.pack()

        # Create a list of items
        items = dataAnalyze.getTopExpensiveData()
        x = 1
        for i in items:
            txt = f"{x}) {i}"
            tk.Label(expensiveCarsDashboard, text=txt, font=("Courier", 13)).pack(pady=2)
            x+=1
        




class InputPage1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Car Data Analysis", font=("Arial", 18))
        label.pack(pady=10)

        dataAnalyze = DataAnalysis("Car_sales.csv")
        
        # self.input_1 = tk.Entry(self)
        # self.input_1.pack()

        # self.input_2 = tk.Entry(self)
        # self.input_2.pack()

        # btn_submit = tk.Button(self, text="Submit", command=self.submit)
        # btn_submit.pack()
        # Variable to hold the selected option

        def save_option(*args):
            selected_option = dropdown_var.get()
            # Replace this print statement with your saving logic
            print("Selected option:", selected_option)
            # print("corresponding header: ", dictOption_header[selected_option])
            # print("Ascending: ", isAscending)
            # tree.update()
        
        def on_checkbox_change():
            if isAscending.get():
                print("Checkbox is checked")
            else:
                print("Checkbox is unchecked")
        

        def applyFeatures():
            print("corresponding header: ", dictOption_header[dropdown_var.get()])
            print("Ascending: ", isAscending.get())

            data = dataAnalyze.getSortedData(dictOption_header[dropdown_var.get()], IsIncreasing=isAscending.get())
            # print(data)

            tree.delete(*tree.get_children())
            # df = data
            for i, row in data.iterrows():
                item_id = tree.insert('', 'end', values=(row["Manufacturer"], row["Model"], row["Price_in_thousands"]))
                data_mapping[item_id] = row


            
        
        dropdown_var = tk.StringVar()
        isAscending = tk.BooleanVar()
        label1 = tk.Label(self, text="Sort the Car data by", font=("Arial", 12))
        label1.pack(pady=5)
        # Create the dropdown menu
        dropdown = ttk.Combobox(self, textvariable=dropdown_var, state="readonly")
        dropdown.pack(padx=10, pady=5)

        
        


        # Create the checkbox
        checkbox = tk.Checkbutton(self, text="check this if you want it in ascending", variable=isAscending, command=on_checkbox_change)
        checkbox.pack(padx=10, pady=2)

        # Add options to the dropdown menu
        btn_ApplyFeatures = tk.Button(self, text="apply filters", command=applyFeatures)
        btn_ApplyFeatures.pack()

        options = ["Price", "Fuel Effieciency", "Resale value", "HorsePower", "power perf factor", "Highest sales"]
        dictOption_header = {"Price": "Price_in_thousands", "Fuel Effieciency": "Fuel_efficiency", "Resale value": "__year_resale_value", "HorsePower": "Horsepower", "power perf factor":"Power_perf_factor", "Highest sales": "Sales_in_thousands"}
        dropdown['values'] = options

        # Set a default value (optional)
        dropdown.set(options[0])

        # Call the save_option function whenever the dropdown value changes
        dropdown_var.trace("w", save_option)


        self.output_label = tk.Label(self, text="", font=("Arial", 14))
        self.output_label.pack(pady=10)

        btn_returnDashbord = tk.Button(self, text="Return", command=lambda: controller.show_page(HomePage))
        btn_returnDashbord.pack()

        def on_item_click(event):
            item_id = tree.focus()  # Get the item ID of the clicked item
            if item_id:  # Ensure that an item is selected
                item_values = tree.item(item_id, 'values')
                if item_id in data_mapping:  # Check if the item ID is in the data mapping
                    corresponding_data = data_mapping[item_id]
                    show_selected_data(item_values, corresponding_data)

        def show_selected_data(item_values, corresponding_data):
            carName = item_values[0]
            carModel = item_values[1]
            print(type(carName))
            print(type(carModel))
            # print(item_values[0], item_values[1])
            print(type(corresponding_data))
            info_label.config(text=f"More details about: {carName} {carModel}\n{corresponding_data}")



        # Create Treeview widget
        tree = ttk.Treeview(self, columns=("Manufacturer", "Model", "Price"), show="headings")
        tree.heading("Manufacturer", text="Manufacturer")
        tree.heading("Model", text="Model")
        tree.heading("Price", text="Price")

        # Set column widths
        tree.column("Manufacturer", width=100)
        tree.column("Model", width=100)
        tree.column("Price", width=100)

        tree.pack(pady=10)
        df = pd.read_csv("Car_sales.csv")
        # Insert data into the Treeview, displaying only the selected columns
        data_mapping = {}  # Dictionary to store the mapping between item ID and corresponding data
        for i, row in df.iterrows():
            item_id = tree.insert('', 'end', values=(row["Manufacturer"], row["Model"], row["Price_in_thousands"]))
            data_mapping[item_id] = row

        # Bind the callback function to the item click event
        tree.bind("<ButtonRelease-1>", on_item_click)

        # Create a label frame to display the selected data fields
        info_frame = ttk.LabelFrame(self, text="Selected Information", padding=10)
        info_frame.pack(padx=10, pady=10)

        # Create a label to display the selected data
        info_label = ttk.Label(info_frame, text="", font=("Arial", 12))
        info_label.pack(pady=5)

    def submit(self):
        value1 = self.input_1.get()
        value2 = self.input_2.get()
        self.output_label.config(text=f"You entered: {value1} and {value2}")

class InputPage2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Predict Car Prices", font=("Arial", 18))
        label.pack(pady=10)
        
        dataPath = "Car_sales.csv"

        data = DataAnalysis(dataPath)
        # self.input_3 = tk.Entry(self)
        # self.input_3.pack()

        # self.input_4 = tk.Entry(self)
        # self.input_4.pack()

        # btn_submit = tk.Button(self, text="Submit", command=self.submit)
        # btn_submit.pack()

        self.output_label = tk.Label(self, text="", font=("Arial", 14))
        self.output_label.pack(pady=10)

        btn_returnDashbord = tk.Button(self, text="Return", command=lambda: controller.show_page(HomePage))
        btn_returnDashbord.pack()

        def GetPrice():
            horsePwer = (float(selected_value1.get()))
            resale = (float(selected_value2.get()))
            powerPerf = (float(selected_value3.get()))
            # print(horsePwer)
            # print(resale)
            # print(powerPerf)
            finalPrice1 = data.getPredictedCost(horsePwer,resale,powerPerf)
            val="$ ",(round(finalPrice1,2) * 1000)
            finalPrice.set(val)
            print(finalPrice.get())
            # print(float(selected_value.get()) + 1)



        # Create a function to handle slider value changes
        def on_slider_change(value):
            selected_value.set((value))  # Update the label with the selected value

        # Create a label to display the selected value from the slider
        

        selected_value = tk.StringVar()
        selected_value.set(0)

        ttk.Label(self, text="Fuel Efficiency ", font=("Courier", 14)).pack(pady=4)

        selected_label = ttk.Label(self, textvariable=selected_value)
        selected_label.pack(pady=10)

        # Create a Scale widget (slider) with a specific range and a step of 1
        # Replace the from_ and to parameters with your desired range
        slider = ttk.Scale(self, from_=15, to=45, orient=tk.HORIZONTAL, command=on_slider_change, length=200)
        slider.pack(fill=tk.X, padx=20, pady=5)

        # Create a function to handle slider value changes


        def on_slider_change1(value):
            selected_value1.set((value))  # Update the label with the selected value

        # Create a label to display the selected value from the slider
        
        selected_value1 = tk.StringVar()
        selected_value1.set(0)

        ttk.Label(self, text="Horsepower ", font=("Courier", 14)).pack(pady=4)
        selected_label1 = ttk.Label(self, textvariable=selected_value1)
        selected_label1.pack(pady=10)

        # Create a Scale widget (slider) with a specific range and a step of 1
        # Replace the from_ and to parameters with your desired range
        
        slider = ttk.Scale(self, from_=55, to=450, orient=tk.HORIZONTAL, command=on_slider_change1, length=200)
        slider.pack(fill=tk.X, padx=20, pady=5)        # Create a function to handle slider value changes




        def on_slider_change2(value):
            selected_value2.set((value))  # Update the label with the selected value

        # Create a label to display the selected value from the slider
        
        selected_value2 = tk.StringVar()
        selected_value2.set(0)

        ttk.Label(self, text="Resale Value ", font=("Courier", 14)).pack(pady=4)
        selected_label2 = ttk.Label(self, textvariable= selected_value2)
        selected_label2.pack(pady=10)

        # Create a Scale widget (slider) with a specific range and a step of 1
        # Replace the from_ and to parameters with your desired range
        slider = ttk.Scale(self, from_=5.160, to=67.550, orient=tk.HORIZONTAL, command=on_slider_change2, length=200)
        slider.pack(fill=tk.X, padx=20, pady=5)        # Create a function to handle slider value changes



        def on_slider_change3(value):
            selected_value3.set((value))  # Update the label with the selected value

        # Create a label to display the selected value from the slider
        
        selected_value3 = tk.StringVar()
        selected_value3.set(0)

        ttk.Label(self, text="Power perf Factor ", font=("Courier", 14)).pack(pady=4)
        selected_label3 = ttk.Label(self, textvariable=selected_value3)
        selected_label3.pack(pady=10)

        # Create a Scale widget (slider) with a specific range and a step of 1
        # Replace the from_ and to parameters with your desired range
        slider = ttk.Scale(self, from_=23.276272, to=188.144323, orient=tk.HORIZONTAL, command=on_slider_change3, length=200)
        slider.pack(fill=tk.X, padx=20, pady=5)

        btn_submit = tk.Button(self, text="Get Price", command=GetPrice)
        btn_submit.pack()

        finalPrice = tk.StringVar()
        finalPrice.set(0)
        ttk.Label(self, text="Approximate Price ", font=("Courier", 14)).pack(pady=4)
        selected_label4 = ttk.Label(self, textvariable=finalPrice)
        selected_label4.pack(pady=10)



# def create_graph(selected_option,self):
#        # Clear the existing graph, if any   

#     # Generate some example data for the graph
#     x = np.linspace(45, 90, 10)
#     if selected_option == "Power/Price":    
#         y = np.sin(x)
#     elif selected_option == "Resale-value/Price":
    
#         y = np.cos(x)
#     elif selected_option == "Power perf/Price":
        
#         y = np.sin(x) + np.cos(x)
#     else:
#         y = x

#     # Create the plot
#     plt.plot(x, y)
#     plt.xlabel('X-axis')
#     plt.ylabel('Y-axis')
#     plt.title(f"Graph for {selected_option}")

    #plt.show()

    # fig =plt.Figure(figsize=(5, 5),dpi=100)
    
    # a=fig.add_subplot(211)
    # a.plot(x,y)
    # canvas = FigureCanvasTkAgg(fig, master=self)
    # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # # Update the canvas with the new plot
    # canvas.draw()
    
    # canvas._tkcanvas.pack()
#    canvas.get_tk_widget.pack()




class InputPage3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        options = ["Power/Price", "Resale-value/Price", "Power perf/Price"]

        def on_option_selected( ):
            selected_value = selected_option.get()
            if selected_value == options[0]:
                predictHorsePower.Graph_horsepower()
            elif selected_value == options[1]:
                resaleAnalysis.Graph_resale()
            else:
                PowerPerfAnalysis.Graph_perf()

            
            selected_option.trace_add('write', on_option_selected)
        label = tk.Label(self, text="Visual Car Analysis", font=("Arial", 18))
        label.pack(pady=5)
        dataPath = "Car_sales.csv"       
        self.output_label = tk.Label(self, text="", font=("Arial", 14))
        self.output_label.pack(pady=1)
        btn_returnDashbord = tk.Button(self, text="Return", command=lambda: controller.show_page(HomePage))
        btn_returnDashbord.pack(side=tk.TOP,pady=10)
        
        selected_option = tk.StringVar( )
        selected_option.set("Power/Price")

        option_menu = tk.OptionMenu(self, selected_option,  *options) 
        option_menu.pack(pady=5)      
        show = tk.Button(self, text='Show', command=on_option_selected) 
        show.pack(pady=60)
        
       

        
       



if __name__ == "__main__":
    app = MultiPageApp()
    app.mainloop()
