import pandas as pd
import data
import Constants


key = input("Insira uma chave openIA: ")
Constants.Constants.key = key

df = data.read_data_set()
data.shape_data_set(df)





