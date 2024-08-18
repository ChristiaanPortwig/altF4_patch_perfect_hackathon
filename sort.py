import csv

# Define the input and output file paths
input_file = 'testingfinal.csv'
output_file = 'output.csv'

# Read the data from the CSV file
with open(input_file, mode='r', newline='') as file:
    reader = csv.reader(file)
    # Read all rows into a list
    data = list(reader)

# Sort the data by the first element (first column) as a number in ascending order
sorted_data = sorted(data, key=lambda row: float(row[0]))

# Write the sorted data to a new CSV file
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sorted_data)

print(f"CSV file sorted by the first column and saved to '{output_file}'")
