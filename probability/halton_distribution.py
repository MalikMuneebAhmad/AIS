def halton_distribution(i, b):
    f = 1
    r = 0
    while i > 0:
        f = f/b
        r = r + f * (i % 2)
        i = i/b


def dec_to_bin(x):
    return int(bin(x)[2:])


a = bin(9)

# Convert a number to any specific base


def decimal_to_bases(num, base,i):
    if num > (base-1):
        i += 1
        decimal_to_bases(num // base,base, i)
        print('index ' + str(i))
    return print(num % base)


decimal_to_bases(13,2,0)

