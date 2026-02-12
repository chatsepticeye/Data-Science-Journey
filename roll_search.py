import csv
def searchroll():
    r=input("Enter rollnumber to search: ")
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            if row[1] == r:
                
                print("Found record:", row)
                break
searchroll()

