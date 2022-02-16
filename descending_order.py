def descending_order(num):
    number = str(num)
    sorted_numbers = sorted(number)
    number = "".join(sorted_numbers)
    number = number[::-1]
    print(number)
    return int(number)
    

descending_order(123456789)