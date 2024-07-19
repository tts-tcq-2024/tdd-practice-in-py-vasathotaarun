import re
def add(number_string):
    numbers = re.findall(r'\d+', number_string)
    number_list = []
    for number in numbers:
        if int(number) < 1000:
            number_list.append(int(number))
    return sum(number_list)
