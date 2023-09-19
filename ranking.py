# ranking.py
# Celvis

# Import
import csv
from urllib import request

# List of employees
employees = {
    "John": "Manager",
    "Alice": "Engineer",
    "Bob": "Designer",
    "Eve": "Sales"
}

# Print employee information
for name, role in employees.items():
    print(name)
    print(role)
    print('-' * 20)

# Request URL
url = "https://raw.githubusercontent.com/aruljohn/popular-baby-names/master/2004/girl_boy_names_2004.csv"
response = request.urlopen(url)
data = response.read().decode('utf-8')

# Parse data
reader = csv.DictReader(data.splitlines())

# Print
# Rank Counter
rankCounter = 0
for row in reader:
    rankCounter += 1
    print('-' * 20)
    print("Rank:", row['Rank'])
    print("Girl Name:", row['Girl Name'])
    print("Boy Name:", row['Boy Name'])
    
    if rankCounter >= 5:
        break # end

response.close()