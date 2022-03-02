'''
Pat Frohn
CS-175L
Eckert
Calculate Average and Grades with Functions
2/28/22
'''

def main():
    score = int(input('Enter score 1: '))
    ltr = determine_grade(score)
    score2 = int(input('Enter score 2: '))
    ltr2 = determine_grade(score2)
    score3 = int(input('Enter score 3: '))
    ltr3 = determine_grade(score3)
    score4 = int(input('Enter score 4: '))
    ltr4 = determine_grade(score4)
    score5 = int(input('Enter score 5: '))
    ltr5 = determine_grade(score5)
    

    avg = calc_average(score,score2,score3,score4,score5)
    avgltr = determine_grade(avg)
    
    print('Score     Numeric Grade  Letter Grade')
    print('-------------------------------------')

    
    print('Score 1:', f'{score:>10}', f'{ltr:>10}')
    print('Score 2:', f'{score2:>10}', f'{ltr2:>10}')
    print('Score 3:', f'{score3:>10}', f'{ltr3:>10}')
    print('Score 4:', f'{score4:>10}', f'{ltr4:>10}')
    print('Score 5:', f'{score5:>10}', f'{ltr5:>10}')

    
    print('The average was ',avg, f'{ltr5:>8}')

    repeat()
    


def calc_average(s1,s2,s3,s4,s5):

    average = (s1 + s2 + s3 + s4 + s5) / 5

    return average


def determine_grade(grade):
    if grade>= 90:
        letter = 'A'
    elif grade >= 80 and grade <= 89:
        letter = 'B'
    elif grade >= 70 and grade <= 79:
        letter = 'C'
    elif grade >= 60 and grade <= 69:
        letter = 'D'
    else:
        letter = 'F'

    return letter


def repeat():
    answer = input('Enter \'yes\' if you would like to do another calculation: ')
    if answer == 'yes' or answer == 'Yes':
        main()
    else:
        print('Goodbye!')


main()

