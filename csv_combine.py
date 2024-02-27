import csv
import os

directory_path_to_combine=os.environ.get("DIRECTORY_PATH_TO_COMBINE")
combined_output_file=os.environ.get("COMBINED_OUTPUT_FILE")
if directory_path_to_combine is None or combined_output_file is None:
    print("Error: DIRECTORY_PATH_TO_COMBINE | COMBINED_OUTPUT_FILE |  environment variables are not set.")
    exit(1)

# List of CSV files to combine
# csv_files = ['file1.csv', 'file2.csv', 'file3.csv']
csv_files = os.listdir(directory_path_to_combine)


# Function to combine CSV files
def combine_csv_files(input_files, combined_output_file):
    with open(combined_output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        # Write the header from the first file
        with open(f'{directory_path_to_combine}/{input_files[0]}', 'r', newline='') as infile:
            reader = csv.reader(infile)
            header = next(reader)
            writer.writerow(header)
        # Write the data from all files
        for file in input_files:
            with open(f'{directory_path_to_combine}/{file}', 'r', newline='') as infile:
                reader = csv.reader(infile)
                # Skip the header in additional files
                if file != f'{directory_path_to_combine}/{input_files[0]}':
                    next(reader)
                for row in reader:
                    writer.writerow(row)

# Combine the CSV files
combine_csv_files(csv_files, combined_output_file)

print(f"Combined {len(csv_files)} CSV files into {combined_output_file}.")