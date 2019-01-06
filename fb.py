for i in range(1, 1000):
    output = ''
    if not i % 3:
        output += 'Fizz'
    if not i % 5:
        output += 'Buzz'
    if output:
        output += '!'
        print(output)
    else:
        print(i)