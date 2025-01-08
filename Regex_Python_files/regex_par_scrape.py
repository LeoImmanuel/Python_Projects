import re
import json

def extract_data(content, output_file_path):
    store_data = {}
    name_pattern = r'The\s(\w+\s\w+)'
    region_pattern = r'native to\s(.*?)[.|,]'
    weight_pattern = r'\s(\d{3}\.\d+|\d,\d{3})\s'
    sc_name_patterns = r'is\s\*{1}(.*?)\*{1}.'

    name = re.search(name_pattern, content)
    if name: 
        store_data["name"] = name.group(1)

    region = re.search(region_pattern, content)
    if region:
        store_data["Region"] = region.group(1)

    weight = re.search(weight_pattern, content)
    if weight:
        store_data["Weight"] = float(weight.group(1).replace(',',''))

    sc_name = re.search(sc_name_patterns, content)
    if sc_name:
        store_data["Scientific_Name"] = sc_name.group(1)

    with open(output_file_path, 'a') as output_file:
        output_file.write(json.dumps(store_data, indent=4) + "\n")

        
# Get name, region, weight and scientific name
paragraph1 = """The African Elephant, a herbivore native to Sub-Saharan Africa, weighs approximately 6,000 kilograms. \
This magnificent creature is primarily found in grasslands and savannahs. The elephant’s lifespan is around 60-70 years, \
and it can drink up to 200 liters of water daily. Its scientific name is *Loxodonta africana*."""

paragraph2 = """The Bengal Tiger, a carnivorous predator, is native to India and nearby countries. \
It weighs roughly 200.123 kilograms and is known for its striking orange coat with black stripes. \
This tiger primarily inhabits dense forests and mangroves. With a lifespan of 10-15 years, it is one of the most iconic big cats. \
Its scientific name is *Panthera tigris tigris*."""

output_file_path = r'G:\OneDrive\Desktop\Python_Projetcs\Beginner_Projects\animals.json'

extract_data(paragraph1, output_file_path)
extract_data(paragraph2, output_file_path)