import pandas as pd

# data = pd.read_csv("./weather_data.csv")
#
# days: list[str] = data["day"].tolist()
# temps: list[int] = data["temp"].tolist()
# conditions: list[str] = data["condition"].tolist()
# print(data[data["temp"] == data["temp"].max()])

data = pd.read_csv("./nyc_squirrel.csv")
black_fur = len(data[data["Primary Fur Color"] == "Black"])
red_fur = len(data[data["Primary Fur Color"] == "Cinnamon"])
grey_fur = len(data[data["Primary Fur Color"] == "Grey"])

content = {
        "fur": ["Black", "Red", "Grey"],
        "size": [black_fur, red_fur, grey_fur]
}
df  = pd.DataFrame(content)
df.to_csv("./fur_contents.csv")
