import csv
col = ["Salary", "45000", "31000", "40000"]
file = open("sample.csv")
c = 0
for row in csv.reader(file):
    c += 1
    print(row)

file.close()
