def btoo(num):
    octal_digit = 0
    i = 0
    count = 1
    octal_array = [0] * 32
    pos = 0
    while num != 0:
        digit = num % 10
        octal_digit += digit * pow(2, i)
        i += 1
        octal_array[pos] = octal_digit
        num = num // 10
        if count % 3 == 0:
            octal_digit = 0
            i = 0
            pos += 1

        count += 1

    for j in range(pos, -1, -1):

        print(octal_array[j], end='')











