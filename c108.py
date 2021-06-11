import csv
import pandas
import plotly.figure_factory as ff
df = pandas.read_csv('data.csv')
fig = ff.create_distplot([df['Weight(Pounds)'].tolist()],['Weight'],show_hist = True)
fig.show()