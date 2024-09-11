import math
import csv

input_data = []

with open('litValue1.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')

    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            input_data.append([float(row[0]), float(row[1]), float(row[2]), float(row[3])])

n = 0
x = 0
y = 0
x2 = 0 #x^2
y2 = 0 #y^2
xy = 0

for i in input_data:
    
    n +=1
    x += n
    y += i[2]
    x2 += n*n
    y2 += i[2]*i[2]
    xy += i[2]*n

r_value = (((n*xy) - (x*y))/math.sqrt(((n*x2) - x*x)*((n*y2) - y*y)))