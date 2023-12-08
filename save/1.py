import csv
import contacts

def save_numbers_to_contacts(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        numbers_list = list(reader)

    for numbers in numbers_list:
        for number in numbers:
            contacts.add(phone=number)

# مثال استفاده:
file_path = 'numbers.txt'  # مسیر فایل .txt
save_numbers_to_contacts(file_path)