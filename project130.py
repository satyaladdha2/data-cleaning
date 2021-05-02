import pandas as pd 
import csv 

df = pd.read_csv("oneerrorsolved.csv")

del df["Luminosity (Lo)"]

df.to_csv('final.csv')