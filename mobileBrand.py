import csv
import pandas as pd 
import plotly.figure_factory as ff 

df = pd.read_csv("data.csv")

graph = ff.create_distplot([df["Mobile Brand"].tolist()], ["Mobile Brand"], show_hist = True)
graph.show()