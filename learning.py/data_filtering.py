
from matplotlib import pyplot as plt
import pandas as pd

# Specify the correct file path for the CSV file
read = pd.read_csv("learning.py/product_excel.csv")
df = pd.DataFrame(read)

# Print the DataFrame (optional)
print(df)

# Define a list of data with dollar values
data_list = ['$69.99', '$88.99', '$96.99', '$97.99', '$99.99', '$101.99', '$102.99', '$103.99', '$107.99', '$121.99', '$130.99', '$148.99', '$172.99', '$233.99', '$251.99', '$320.99', '$399.99', '$489.99', '$537.99', '$587.99', '$603.99']

# Convert the dollar values to numeric values
numeric_price = pd.to_numeric([price.replace('$', '') for price in data_list])
print(numeric_price)

# Filter the DataFrame based on numeric prices
filtered_data = df[(numeric_price > 60) & (numeric_price < 100)]
print(filtered_data)

# for making like bar diagram or histogram 

mark_range = [0,50,100,150,200,250,300,350,400,450,500,550,600,650,700]
plt.title("Price for sample")
plt.hist(mark_range,numeric_price)
plt.show()