import csv

f = open("records_Cleaned.csv")
data = csv.reader(f,delimiter=',')
cnt = 0
for line in data:
    if cnt is 1:
        print(line)
        print("Length = " + str(len(line)))
    cnt = cnt + 1
