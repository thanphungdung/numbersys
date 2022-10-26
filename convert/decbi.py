def btod(binary):
    x = binary[::-1]
    ans = 0
    for i in range(len(x)):
        ans += (int(x[i])*(2**i))
    return ans

def dtob(dec):
    final = ''
    dec = int(dec)
    while dec >=1:
        x = int(dec % 2)
        dec = int(dec / 2)
        final += str(x)
        if dec == 1:
            final += '1'
            break
    ans = final[::-1]
    return ans

def main():
    purpose = input('binary to decimal or decimal to binary:')
    if purpose == 'binary':
        bi = input('enter binary num:')
        print(btod(bi))

    elif purpose == 'decimal':
        deci= input('enter decimal num:')
        print(dtob(deci))

    return''

while True:
    print(main())







