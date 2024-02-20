import csv
import os

# List of CSV files to combine
directory_path = 'to_combine_csv'
csv_files = os.listdir(directory_path)

# csv_files = ['file1.csv', 'file2.csv', 'file3.csv']

# Output combined CSV file
output_file = 'combined_csv/combined_20240219_1816.csv'

# Function to combine CSV files
def combine_csv_files(input_files, output_file):
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        # Write the header from the first file
        with open(f'{directory_path}/{input_files[0]}', 'r', newline='') as infile:
            reader = csv.reader(infile)
            header = next(reader)
            writer.writerow(header)
        # Write the data from all files
        for file in input_files:
            with open(f'{directory_path}/{file}', 'r', newline='') as infile:
                reader = csv.reader(infile)
                # Skip the header in additional files
                if file != f'{directory_path}/{input_files[0]}':
                    next(reader)
                for row in reader:
                    writer.writerow(row)

# Combine the CSV files
combine_csv_files(csv_files, output_file)

print(f"Combined {len(csv_files)} CSV files into {output_file}.")