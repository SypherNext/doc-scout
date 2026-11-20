import csv

# A field with an embedded double quote
data = 'model,description\ngpt-4,"Model with 8"" context"\n'
# The correct CSV writes "" to escape a quote

reader = csv.DictReader(data.splitlines())
for row in reader:
    print(row)
    # {'model': 'gpt-4', 'description': 'Model with 8" context'}
