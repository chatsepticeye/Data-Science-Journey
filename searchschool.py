import csv
def searchroll():
    s = input("Enter School Name to search: ")
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            if row[4] == s:
                
                print("Found record:", row)
                
searchroll()

