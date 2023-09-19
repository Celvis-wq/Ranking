# ranking.py
# Celvis

# Import
import csv
from urllib import request

# Create a variable called employees
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

# Parse the data
reader = csv.DictReader(data.splitlines())

# Print the data
for row in reader:
    print('-' * 20)
    print("Rank:", row['Rank'])
    print("Boy Name:", row['Boy Name'])
    print("Girl Name:", row['Girl Name'])

response.close() # end