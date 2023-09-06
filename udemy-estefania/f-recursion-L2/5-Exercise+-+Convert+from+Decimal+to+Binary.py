def convert_to_binary(decimal_num):
    if decimal_num == 0:
        return '0'
    else:
        return (convert_to_binary(decimal_num // 2) + str(decimal_num % 2)).lstrip("0")


print(convert_to_binary(5))