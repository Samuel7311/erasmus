import json

def merge_json_files(input_files, output_file):
    # Initialize an empty list to store combined data
    combined_data = []

    # Load data from each input JSON file and append it to combined_data
    for input_file in input_files:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            combined_data.extend(data)

    # Write the combined data to the output JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, ensure_ascii=False, indent=4)

# Example usage
input_files = [
    'daswerk/erasmus/spiders/oDaswerk.json',
    'flex/flex/spiders/oFlex.json',
    'flucc/flucc/spiders/oFlucc.json',
    'goabase/goabase/spiders/oGoabase.json',
    'goodnight/goodnight/spiders/oGoodnight.json'
]

output_file = 'combined_data.json'
merge_json_files(input_files, output_file)