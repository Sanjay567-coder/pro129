import csv 
import pandas as pd

dataset1=[]
dataset2=[]

with open("drawf_star.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset1.append(row)
        dataset1 = dataset1[dataset1['name'].notna()]
        dataset1 = dataset1[dataset1['Distance'].notna()]
        dataset1 = dataset1[dataset1['Mass'].notna()]
        dataset1 = dataset1[dataset1['Radius'].notna()]

with open("bright_stars.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset2.append(row)
        dataset2 = dataset2[dataset2['Star_name'].notna()]
        dataset2 = dataset2[dataset2['Distance'].notna()]
        dataset2 = dataset2[dataset2['Mass'].notna()]
        dataset2 = dataset2[dataset2['Radius'].notna()]
        dataset2 = dataset2[dataset2['Luminosity'].notna()]

headers1=dataset1[0]
star_data1=dataset1[1:]
headers2=dataset2[0]
star_data2=dataset2[1:]
headers=headers1+headers2
star_data=[]

for i in star_data1:
    star_data.append(i)
for a in star_data2:
    star_data.append(a)
with open("final3.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)
