import pandas as pd

file_path="C:\\Users\\raman\\OneDrive\\Data Engineer Portfolio\\Github\\Social Media Data\\Social Media Data.xlsx"
data = pd.read_excel(file_path)

print(data.head()) #prints the data

print(data.isnull().sum()) #gets the total number of null values from True and False

#lets check the dates fall in first quarter range only and remove all the dates which are outside this range
data["Date"]=pd.to_datetime(data["Date"]) #this converts the column to datetime if not already

data_filtered=data[data["Date"].dt.month<=3]

print(data_filtered)

print(data.describe())