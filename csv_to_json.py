import json

def format_json_key(str):
    '''Format json keys for headers'''
    return str.lower().replace(' ', '_')

def main():
    # Define csv file name. The generated json file will be the same name .json
    csv_filename = 'test.csv'
    json_filaname = csv_filename.split('.')[0] + '.json'

    # Read from csv file
    with open(csv_filename, 'r') as f:
        data = f.readlines()

    # Create json keys from csv headers
    keys = [format_json_key(word.strip('\n')) for word in data[0].split(",")]

    json_data = []

    # Loop through each csv row
    for row in data[1:]:
        # For each value in a row, assign key value pairs
        json_data.extend([
            {
                keys[index]: value.strip('\n') for index, value in enumerate(row.split(','))
            } 
        ])

    # Write to json file 
    with open(json_filaname, 'w') as f:
        json.dump(json_data, f, indent=4)
    
    print(f"\n\"{json_filaname}\" created successfully.\n")

if __name__ == "__main__":
    main()
