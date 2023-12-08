from phonebook import Phonebook

def save_contacts_from_file(file_path):
    pb = Phonebook()

    with open(file_path, 'r') as file:
        numbers = file.read().splitlines()

    for number in numbers:
        pb.add_contact(number)

    pb.save()

    print("شماره‌ها با موفقیت در مخاطبین ذخیره شدند.")

file_path = "numbers.txt"

save_contacts_from_file(file_path)
