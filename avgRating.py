import csv
import pandas as pd 
import plotly.figure_factory as ff 

df = pd.read_csv("data.csv")

graph = ff.create_distplot([df["Avg Rating"].tolist()], ["Average Rating"], show_hist = True)
graph.show()