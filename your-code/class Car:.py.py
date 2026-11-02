class Car:
    def __init__(self,color):
        self.color = 0
        self.position = 0 # initialize position as an attribute

    def move(self): 
        self.position += 1
        return self.position 

bmw = Car("red") 

position = bmw.move
Color = bmw.color # access the color attribute

      
       
class Car:
    def __init__(self, color):
        self.color = color
        self.position = 0

    def move(self):
        self.position += 1
        return self.position

bmw = Car("Red") 
position = bmw.move() 
Color = bmw.color() 

print(dir(str)) # methods and attributes of the string class 

weights = [0.2, 0.3, 0.4]
kanto_list = [65, 46, 57]

yield_apple = sum(w*x for w, x in zip(weights, kanto_list) ) 

some_data = {"Ohio": 2346, "Texas": 4567, "Arizona": 8234}

import pandas as pd
import numpy as np 


new_series = pd.Series(some_data)
print(new_series.values)

list(some_data.keys()) == list(new_series.keys()) 

sdata = {"Ohio": 3500, "Texas": 4000, "Oregon": 5000}
states = ["Ohio", "Texas", "Oregano", "California", "Arizona"] 

my_series = pd.Series(data = sdata, index = states) 

print(my_series.values)
print(my_series.index)

print(my_series.isna())
print(my_series.isna())
my_series.fillna(0, inplace = True) 

# create dioctionary with columns and data
dict_states = {"state": ["Oregano", "Utah", "New_Mexico", "Nebraska"],
               "year": [1990, 1998, 2000, 2020],
               "something_else":[456, "ssdd", 0.23, np.nan]} 

df = pd.DataFrame(dict_states) 

df.head() # first 5 rows 

from sqlite3 import connect 
conn = connect(':memory:')
df = pd.read_sql("SELECT column1, column2 FROM sample_data, conn)
df.to_sql("test_data", conn)  

# shape of df
data_shape = df.shape
print(f"Shape of the dataframe:{data_shape}") 

column_names = df.columns
print(f"The column names are: {column_names}") 

data_types = df.dtypes
print(f"Data types: \n{data_types}")
print(f"Data types:\n{data_types}") 

data_info = df.info() 
df.tail() 

df.sort_values(by = "year", ascending = False)
df.sort_values(by =["year", "region"], ascending = False) 
df.sort_values(by = ["year", region], ascending = False) 

df.sort_values(by = "year", ascending = False)[["year", "region"]] 

subset_columns = list(df.columns)[1:4] # creating a list of column names to create a subset of columns 

df[subset_columns] 

df.sample()
df.sample(frac =0.2)

                  
                 
        
import pymongo
from pymongo import MongoClient 


np.array([[1,2,5], [2,5,6]])

weights = [w1, w2, w3]

yield = sum(w*x for w,x in zip)

np.array([1,4,3])*np.array([-1,5,2,7]) 

random_numbers = np.random.random(5)
random_numbers.size 

def numpy_info(arr):    
    print(arr.dim, arr.shape) 

matrix = np.random.random((3,4)) 

matrix = np.random.randint(2, size =(3,4,6)) 

range = np.arange(0, 100) 

np.linspace(0, 100, 51)

np.round(5.36789, 1)

np.round(np.linspace(0, 100, 50), 2)

a = np.array(a) 

b = a.tolist() 

a = np.random.randint(2, size =(1,2,3)) 

np.zeroes((2,5,10))
np.ones(2,5,10) 

np.eye(5,5, dtype = int) 

np.eye(5,5, dtype = "str") 
np.eye(5,5, dtype = "object") 

average_rate = np.mean(exchange_rates) 

dates[np.argmax(exchange_rate)]

np.sum(exchange_rates) 

np.transpose(matrix)

matrix.T 

array_2d = np.reshape(array_1d, (3, 2)) 

conda install pandas 

[i for i in dir(series) if "_" not in i] 

data = [1, 2,3, 4]
series = pd.Series(data)

type(series)
len(series) 

series.index
series.values

series[3] 

list(some_data.keys())==list(some_data.index()) 

df.head() # check first rows
data_shape = df.shape 

df.columns
df.dtypes 

df.info() 

len(df)

df.sort_values(by = ["region", "year"], ascending = False) 

subset_columns = list(df.columns)[1:4] 

df.sample(frac = 0.02) 

missing_values = pd.isnull(df) 

missing_counts = missing_values.sum() 

df[["Department", "Age"]].groupby("Department").mean()
df["Department", "Age"].groupby("Department").count() 

df[["Department", "Age"]].groupby(by = ["Department", "EducationField"]).agg({"HourlyRate": "mean", "Age": "mean" })

df[["Department", "Age"]].groupby(by = ["Department", "EducationField"]).agg({"HourlyRate": "mean", "Age": "mean"}) 

df[["Department", "Age"]].groupby(by = ["Department", "EducationField"]).agg({"HourlyRate": "mean", "Age": "mean"}) 

df[["Department", "Age"]].groupby("Department").agg("mean") 

target_columns = ["Education_Field", "HourlyRate", "Department", "StandardHours", "Age"] 
columns_to_colapse = ["Department", "EducationField"]
aggregations = ["mean", "max", "min"] 

df[target_columns].groupby(by=columns_to_colapse).agg(aggregations) 

df.head() 

# calculating mean age by Department 

df.pivot_table(values = "Age", index = "Department", aggfunc = "mean") 

df.pivot_table(values = "Age", index = "Department", aggfunc = "max") 

df.pivot_table(values = "Age", index = "Department", aggfunc = "median") 

df.pivot_table(values = "MonthlyIncome", index = ["Department", "EducationField"], aggfunc = "mean") 

pd.crosstab(df["Department"], df["EducationField"]) 

df.pivot_table(values = "Age", index = ["Department", "EducationField"],  aggfunc = "mean") 

pd.crosstab(df["Department"], df["EducationField"], df["MonthlyIncome"], aggfunc= "mean") 

first_df = df.sample(frac = 0.1)
second_df = df.sample(frac = 0.1)

dislay(first_df.head()) ; display(second_df.head()) 

pd.concat([first_df, second_df], axis = 0, keys = ["Table 1", "Table 2"]) # axis = 0, it stacks them on top of each other, keys parameter specifies a hierarchial (multiindex ) structure, have 2 

pd.concat([first_df, second_df], axis = 1, keys = ["left", "right"] 

pd.merge(df1, df2, how = "left") 

%matplotlib inline

%config Inlinebackend.figure_format = "retina"

sns.set_context("poster") 
sns.set(rc = {"figure.figsize":(12., 6.)}) 

sns.set_style("whitegrid") 

%matplotlib inline

%config Inlinebackend.figure_format = "retina" 

import seaborn as sns
import matplotlib.pyplot as plt 

sns.set_context("poster")
sns.set(rc={"figure.figsize":(12., 6.)}) 
sns.set_style("whitegrid") 

penguin.sample(frac= 0.1)

penguins.groupby(by= "species").agg("count") 

sns.countplot(x = penguins.species) 
sns.countplot(x=penguins["species"], palette = "magma")

# group penguins dataframe by "species" column and count the occurence of each species 

flights.head() 

flights.sample() 

flights.groupby(by = ["year", "passengers"]).agg({"passengers": "mean"}).round() # groups all rows belonging to the same year



          
               
            

    flights[["passengers", "month", "age"]].groupby("month").agg({"passengers": "mean"}).round() 
    flights[["passengers", "month", "age"]].groupby("month").agg({"passengers" : "sum"}) 
    sns.barplot(x = "year", y = "passengers", data = flights, ci = None, palette = "magma", estimator = sum) 

    dir(object) 

    from skiimage import io 

    photo = io.imread("") 

    numpy_info(photo) 

    photo.shape[0]
    photo.shape[1]
    photo.shape[2] 

    print(f"First dimension is {photo.shape[0]}, second dimension is {photo.shape[1]}, third dimension is photo.shape[3]") 

    photo[0][0] # color grading 

    reversed_pic = io.imshow(photo[::-1])

    io.imread("") 
    numpy_info(photo) 
    from skiimage import io 

    reversed_pic = io.imshow(photo[::-1]) 

cathedral = io.imshow(photo[200:500, 400:800]) 
io.imshow(photo[:, :, 2]) 

brightness_high = np.where(photo > 100, 200, 0) 
io.imshow(brightness_high) 

brightness_high = np.where(photo > 100, 255, 0) 
io.imshow(brightness_high) 

brightness_low = np.where(photo < 70, 50, 30)
io.imshow(brightness_low) 

from skiimage import io 

photo = io.imread()
numpy_info(photo) 

object(dir) 

reversed_pic = io.imshow(photo[::-1]) 
photo[0]
photo[1]
photo[2] 

cathedral = io.imshow(photo[200:500, 400:800]) 
photo[0][0][1] 

high_brightness = np.where(photo > 200, 250, 0)
io.imshow(high_brightness) 

photo[0][0][0] # red-227
photo[0][0][1] # green-228 

# create a sample 2D array 

 
import numpy as np
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]]) 
