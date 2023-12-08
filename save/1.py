import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

def save_contacts_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = file.readlines()

        for number in numbers:
            number = number.strip()  # حذف فاصله‌ها و کاراکترهای خالی از شماره
            parsed_number = phonenumbers.parse(number, "IR")  # تجزیه و تحلیل شماره
            if phonenumbers.is_valid_number(parsed_number):  # بررسی صحت شماره
                formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
                carrier_name = carrier.name_for_number(parsed_number, "en")
                location = geocoder.description_for_number(parsed_number, "fa")
                # ذخیره شماره در مخاطبین یا انجام عملیات دیگر
                print("شماره: ", formatted_number)
                print("اپراتور: ", carrier_name)
                print("مکان: ", location)
                print("-------------------------------")
            else:
                print("شماره نامعتبر: ", number)


file_path = "input.txt"  # مسیر فایل .txt حاوی شماره‌ها
save_contacts_from_file(file_path)
