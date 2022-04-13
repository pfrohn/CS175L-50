'''
Name: Patrick Frohn
CS-175L
Eckert
4/6/22
'''




import matplotlib.pyplot as plt
import numpy as np



def main():
    rent,gas,food,clothing,car_payment,misc = file()
    
    

    listy = [rent,gas,food,clothing,car_payment,misc]
    labels = []






    labels.append(rent[0])
    rent.remove(rent[0])
    labels.append(gas[0])
    gas.remove(gas[0])
    labels.append(food[0])
    food.remove(food[0])
    labels.append(clothing[0])
    clothing.remove(clothing[0])
    labels.append(car_payment[0])
    car_payment.remove(car_payment[0])
    labels.append(misc[0])
    misc.remove(misc[0])


    numbers = []

    numbers.append(rent[0])
    listy.remove(listy[0])
    numbers.append(gas[0])
    listy.remove(listy[0])
    numbers.append(food[0])
    listy.remove(listy[0])
    numbers.append(clothing[0])
    listy.remove(listy[0])
    numbers.append(car_payment[0])
    listy.remove(listy[0])
    numbers.append(misc[0])
    listy.remove(listy[0])
    
    fig, ax = plt.subplots()
    ax.pie(numbers, labels = labels)
    ax.set_title('Grocery Store')
    plt.show()
   
    
    
    
    
    
    






def file():
    expenses = open('expenses.txt','r')
    rent = expenses.readline()
    rent = rent.strip('\n',)
    rent = rent.split('\t')
    gas = expenses.readline()
    gas = gas.strip('\n')
    gas = gas.split('\t')
    food = expenses.readline()
    food = food.strip('\n')
    food = food.split('\t')
    clothing = expenses.readline()
    clothing = clothing.strip('\n')
    clothing = clothing.split('\t')
    car_payment = expenses.readline()
    car_payment = car_payment.strip('\n')
    car_payment = car_payment.split('\t')
    misc = expenses.readline()
    misc = misc.strip('\n')
    misc = misc.split('\t')
    
    return rent,gas,food,clothing,car_payment,misc
    
    
if __name__ == '__main__':
    main()
