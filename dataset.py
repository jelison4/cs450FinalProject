# This file reads the CSV file and imports all of the
# files into one structure, ready to be used in a
# SK-learn classifier.

import pandas as pd
from pandas import read_csv, DataFrame
from sklearn.model_selection import train_test_split

names = ["filename", "composer", "genre_id"]

csv_data = read_csv(
    'metadata.csv',
    names = names,
    sep=",")

data = []

for filename, composer, genre_id in zip(csv_data.filename, csv_data.composer, csv_data.genre_id):
    data.append(
        ["csvData/" + composer + "/" + filename[:-4]+".csv", # the filename
        genre_id]) # the genre

filenames = pd.DataFrame(data, columns = ["filename", "genre_id"])
data_y = filenames.drop(["filename"], axis=1)

filenames = filenames.drop(["genre_id"], axis=1)

data_x = pd.DataFrame()

for index, row in filenames.iterrows():
    songfilename = row["filename"]
    print(songfilename)
    #songSample = read_csv(songfilename, skiprows = 30, nrows = 50)
    #songSample.drop([1,2], axis=1)

# Split the data
#x_train, x_test, y_train, y_test = train_test_split(
#    data_x, data_y, test_size = 0.3
#)
