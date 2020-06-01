import pandas as pd
dict = {
    "country":["Brazil","Russia","India","China","south Africa"],
    "Capital":["Brasilia","Moscow","New Delhi","Beijing","Pretoria"],
    "Area":[8.516,17.10,3.286,9.579,1.221],
    "Population":[200.4,143.5,1252,1357,52.98]
}

brics = pd.DataFrame(dict)
brics.index = ["BR","RU","IN","CH","SA"]
print(brics)