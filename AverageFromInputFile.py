'''
Pat Frohn
CS175L
Eckert
Average From Input File
3/9/22
'''


def main():
    counter = 1
    total = 0
    numbers = open('numbers.txt','r')
    for num in numbers:
        num1 = float(num)
        total+=num1
        print('I read in',counter,'number(s), current number is:'f'{num1:>8} Total is:',f'{total:<8}')
        counter = counter + 1
    counter = counter - 1
    average = total / counter
    print('Average:',average)


if __name__ == '__main__':
    main()
        
