import re


def extract_phone(input):
    phone_regex = re.compile(r'\(?\d{2}\)?\s?\d{4,5}-?\d{4}')
    match = phone_regex.search(input)

    if not match:
        return None

    return match.group()


def extract_all_phones(input):
    phone_regex = re.compile(r'\(?\d{2}\)?\s?\d{4,5}-?\d{4}')
    return phone_regex.findall(input)


def is_valid_phone(input):
    phone_regex = re.compile(r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$')
    match = phone_regex.search(input)

    if not match:
        return False

    return True


def is_valid_phone(input):
    phone_regex = re.compile(r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$')
    match = phone_regex.fullmatch(input)

    if not match:
        return False

    return True


if __name__ == '__main__':
    print(extract_all_phones(
        'That\'s my phone number 81 99811-3680 or my phone number 81 123-2180'))
    print(extract_phone('That\'s not my phone number 81 123-2180'))
    print(is_valid_phone('818113680'))
