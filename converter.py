import os
from pandas import read_csv, DataFrame

names = ["filename", "composer", "genre_id"]

csv_data = read_csv(
    'metadata.csv',
    names = names,
    sep=",")

for filename, composer, genre_id in zip(csv_data.filename, csv_data.composer, csv_data.genre_id):
    command = "Midicsv.exe data/" + composer + "/" + filename + " csvData/" + composer + "/" + filename[:-4] + ".csv"
    #print(command)
    os.system(command)