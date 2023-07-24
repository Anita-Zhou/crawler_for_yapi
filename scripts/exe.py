import add_default
import os
import json

def process_files(source_folder, target_folder):
    for i in range(3, 6):
        folder_name = str(i)
        print("folder name: " + str(folder_name))
        source_subfolder = os.path.join(source_folder, folder_name)
        target_subfolder = os.path.join(target_folder, folder_name)
        os.makedirs(target_subfolder, exist_ok=True)
        
        for file_name in os.listdir(source_subfolder):
            source_file = os.path.join(source_subfolder, file_name)
            target_file = os.path.join(target_subfolder, file_name)
            
        
            # Read JSON string from input file
            with open(source_file, 'r') as file:
                json_string = file.read()

            print("source_file name: " + str(source_file))
            # Parse JSON string into a JSON object
            json_object = json.loads(json_string)

            # Modify the JSON object as desired
            # Only output the object when the property "value" exist
            if "value" in json_object["properties"].keys():
                print("value in json_object.keys() ")
                val_obj = json_object["properties"]["value"]
                add_default.set_default("root", "value", val_obj)

                # Convert the JSON object back to a JSON string
                updated_json_string = json.dumps(json_object, indent=2, ensure_ascii=False)

                # Write the JSON string to the output file
                with open(target_file, 'w') as file:
                    file.write(updated_json_string)

# Example usage
source_folder = './texts'
target_folder = './updated_texts'

process_files(source_folder, target_folder)
