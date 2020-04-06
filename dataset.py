# This file reads the CSV file and imports all of the
# files into one structure, ready to be used in a
# SK-learn classifier.

import pandas as pd
from pandas import read_csv, DataFrame
from sklearn.model_selection import train_test_split

names = ["filename", "composer", "genre_id"]

csv_data = read_csv(
    "metadata.csv",
    names = names,
    sep=",")

data = []

for filename, composer, genre_id in zip(csv_data.filename, csv_data.composer, csv_data.genre_id):
    new_filename = "cleanCsv/" + composer + "/" + filename[:-4]+".csv" # the filename
    data.append([new_filename, genre_id]) # the genre

    #print(new_filename)
    songSample = read_csv(new_filename)
    #songSample.drop([1,2], axis=1)

# Split the data
#x_train, x_test, y_train, y_test = train_test_split(
#   data_x, data_y, test_size = 0.3
#)

