'''
Pat Frohn
CS175L
Eckert
Average From Input File with Exception
'''



def main():
    try:
        total = 0.0
        numbers = open('numbers.txt','r')
    except IOError:
        print('File not found!')
    average(numbers)

def average(numbers):
    average = 0
    counter = 1
    total = 0
    try:
        for num in numbers:
            counter = counter + 1
            num1 = float(num)
            total = total + num1
        counter = counter - 1
        average = total / counter
        print('Average:',f'{average:.2f}')
    except ValueError:
        print('Error: Unknown Value!')
        
        




if __name__ == '__main__':
    main()

