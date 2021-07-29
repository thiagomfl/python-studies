def age_group(age):
    if 0 <= age < 18:
        return 'Under age'
    elif age in range(18, 65):
        return 'Adult'
    elif age in range(65, 100):
        return 'Elderly'
    elif age >= 100:
        return 'Centenary'
    else:
        return 'Invalid age'
    

if __name__ == '__main__':
    for age in (17, 35, 0, 87, 111, -2):
        print(f'{age}: {age_group(age)}')
