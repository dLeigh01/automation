import re

with open("./assets/potential-contacts.txt") as f:
    text = f.read()

pattern_phone = r'(?:(?:\+1-)?\(?\d{3}\)?\s?-?)?\d{3}-?\d{4}(?:x\d{1,6})?'
pattern_email = r'\S+@\S+\.(?:com|org|net|biz|info|edu)'

phone_numbers = re.findall(pattern_phone, text)
emails = re.findall(pattern_email, text)

with open("emails.txt", "w") as fe:
    no_duplicates_emails = []
    while emails:
        email = emails.pop()
        if email not in no_duplicates_emails:
            no_duplicates_emails.append(email)

    sorted_emails = sorted(no_duplicates_emails)
    for email in sorted_emails:
        if email == sorted_emails[-1]:
            fe.write(email)
            continue
        fe.write(f"{email}\n")