# This file reads the CSV file and imports all of the
# files into one structure, ready to be used in a
# SK-learn classifier.

from mido import MidiFile
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
        [MidiFile("data/" + composer + "/" + filename), # the filename
        genre_id]) # the genre

data_x = data[0]
data_y = data[1]

# Split the data
x_train, x_test, y_train, y_test = train_test_split(
    data_x, data_y, test_size = 0.3
)

