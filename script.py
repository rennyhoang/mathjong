import os
import shutil
import csv

currDir = '/home/renny/dl/mahjong-dataset/'
imgDir = '/home/renny/dl/mahjong-dataset/images/'
filename = 'data.csv'
fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

for row in rows[583:]:
    print(row)
    imageName = row[0]
    dirName = row[1]
    shutil.move(imgDir + imageName, currDir + dirName)
