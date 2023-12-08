import openpyxl
from droidutils import sms

def read_numbers_from_txt(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [line.strip() for line in file if line.strip()]
            return numbers
    except FileNotFoundError:
        print('فایل مورد نظر یافت نشد.')
        return []

def save_numbers_to_contacts(numbers):
    for number in numbers:
        sms.add_contact(number)

        print(f"شماره {number} به مخاطبین افزوده شد.")

# آدرس فایل متنی شامل شماره‌ها
file_path = 'numbers.txt'

# خواندن شماره‌ها از فایل متنی
numbers = read_numbers_from_txt(file_path)

# ذخیره شماره‌ها در مخاطبین گوشی موبایل
save_numbers_to_contacts(numbers)
