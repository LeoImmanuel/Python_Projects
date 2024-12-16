import re

def extract_data_from_file(file_path):
    with open(file_path,'r') as file:
        content = file.read()

        numbers_pattern = r'\b(\d+)\b|\b\d{3,}.*\d{3,}\b'
        get_all_matched_numbers = re.findall(numbers_pattern, content)

        email_pattern = r'https?://\S+'
        get_email_links = re.findall(email_pattern, content)

    return get_all_matched_numbers, get_email_links

file_path = r'G:\OneDrive\Desktop\sample.txt'
output_file_path = r'G:\OneDrive\Desktop\extracted_data.txt'

numbers, urls = extract_data_from_file(file_path)

with open(output_file_path,'w') as output_file:
    output_file.write("\nNumbers extracted\n")
    for number in numbers:
        output_file.write(f"{number} \n")

    output_file.write("\nLinks extracted: \n")
    for url in urls:
        output_file.write(f"{url} \n")