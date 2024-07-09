import csv
import re

def process_row(row):
    if len(row) >= 19:
        # Concatenate values from columns 18 and 19
        new_value = row[17] + row[18]

        # Update the value in column 19
        row[18] = new_value

    return row

def process_log(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter=' ')
        writer = csv.writer(outfile, delimiter=' ')

        for row in reader:
            # Join fields that are enclosed within double quotes
            joined_row = ' '.join(row)
            quoted_fields = re.findall(r'"([^"]*)"', joined_row)
            
            for quoted_field in quoted_fields:
                joined_row = joined_row.replace(f'"{quoted_field}"', quoted_field.replace(' ', '___'))

            # Split the row using the space delimiter
            processed_row = process_row(joined_row.split(' '))

            # Replace the delimiter within quoted fields
            processed_row = [field.replace('___', ' ') if '___' in field else field for field in processed_row]

            # Write the updated row to the output file
            writer.writerow(processed_row)

    print("Log file manipulation completed.")

# Example usage
process_log('outputwebtxwonoise.log', 'your_output_file.log')
