import re

with open("./assets/potential-contacts.txt") as f:
    text = f.read()
with open("./assets/existing-contacts.txt") as f:
    existing = f.read()

pattern_phone = r'(?:(?:\+1-)?\(?\d{3}\)?\s?-?\.?)?\d{3}-?\.?\d{4}(?:x\d{1,6})?'
pattern_email = r'\S+@\S+\.(?:com|org|net|biz|info|edu)'

phone_numbers = re.findall(pattern_phone, text)
emails = re.findall(pattern_email, text)


with open("phone-numbers.txt", "w") as fp:
    formatted_phone_numbers = []
    no_duplicate_phone_numbers = []
    sorted_phone_numbers = []

    for number in phone_numbers:
        if len(number) < 9:
            number = "206-" + number

    for number in phone_numbers:
        number_string = ""
        has_ext = False
        has_parenthesis = False
        for index, char in enumerate(number):
            if char == ".":
                number_string += "-"
                continue
            if char == "(":
                has_parenthesis = True
                continue
            if char == ")":
                number_string += "-"
                continue
            if char == "+":
                has_ext = True
                number_string += char
                continue
            if has_ext is True and index == 6:
                if char.isdigit():
                    number_string += f"-{char}"
                    continue
            if has_ext is False:
                if has_parenthesis is False and index == 3:
                    if char.isdigit():
                        number_string += f"-{char}"
                        continue
                if has_parenthesis is False and index == 6:
                    if char.isdigit():
                        number_string += f"-{char}"
                        continue
            number_string += char
        formatted_phone_numbers.append(number_string)

    while formatted_phone_numbers:
        number = formatted_phone_numbers.pop()
        if number not in no_duplicate_phone_numbers and number not in existing:
            no_duplicate_phone_numbers.append(number)

    sorted_phone_numbers = sorted(no_duplicate_phone_numbers)

    for number in sorted_phone_numbers:
        if number == sorted_phone_numbers[-1]:
            fp.write(number)
            continue
        fp.write(f"{number}\n")


with open("emails.txt", "w") as fe:
    no_duplicates_emails = []

    while emails:
        email = emails.pop()
        if email not in no_duplicates_emails and email not in existing:
            no_duplicates_emails.append(email)

    sorted_emails = sorted(no_duplicates_emails)
    for email in sorted_emails:
        if email == sorted_emails[-1]:
            fe.write(email)
            continue
        fe.write(f"{email}\n")