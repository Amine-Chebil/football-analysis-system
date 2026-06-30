import json

def convert_key_1_to_int(json_file):
    def convert_keys(obj):
        if isinstance(obj, dict):
            new_dict = {}
            for key, value in obj.items():
                new_key = int(key) if key == '1' else key
                new_dict[new_key] = convert_keys(value)
            return new_dict
        elif isinstance(obj, list):
            return [convert_keys(item) for item in obj]
        else:
            return obj

    with open(json_file, 'r') as file:
        data = json.load(file)

    converted_data = convert_keys(data)

    with open(json_file, 'w') as file:
        json.dump(converted_data, file, indent=4)

# Example usage
convert_key_1_to_int('C:/Users/conta/Desktop/football_analysis/stubs/ball_bboxes.json')
