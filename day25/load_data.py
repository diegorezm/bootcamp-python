import pandas as pd

base = {}

data = pd.read_csv("./50_states.csv")
states = data["state"]
x = data["x"]
y = data["y"]

for state, x_cor, y_cor in zip(states, x,y):
    base[state] = (x_cor, y_cor)


