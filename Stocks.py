COMMISSION_RATE = float (input("What is the commission rate? "))
NUM_SHARES = int (input("How many shares do you have? "))
PURCHASE_PRICE = int (input("What is the purchase price? "))
SELLING_PRICE = float (input("What is the selling price? "))


amountPaidForStock = NUM_SHARES * PURCHASE_PRICE
purchaseCommission = amountPaidForStock * COMMISSION_RATE
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = NUM_SHARES * SELLING_PRICE
sellingCommission = COMMISSION_RATE * stockSoldFor
totalRecieved = stockSoldFor - sellingCommission
profitOrLoss = totalRecieved - totalPaid

print("Amount paid for stock was $" + str(amountPaidForStock))
print("Commission paid on the purchase is $" + str(purchaseCommission))
print("Amount the stock sold for is $" + str(stockSoldFor))
print("Commission paid on the sale is $" + str(sellingCommission))
print("Profit or Loss is $" + str(profitOrLoss))

