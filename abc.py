import pandas
import plotly.express as px
import csv
df = pandas.read_csv('data.csv')
height = df['Height(Inches)'].tolist()
sum = 0
for i in height:
    sum = sum+i
length = len(height)
mean = sum/length
print(mean)