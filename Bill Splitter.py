# This Project will allow the user to input and split the bill between a party
# The Key features include splitting an equal amount after tax and tip
# Having the ability to split the bill by item

# This block just gathers the basic information regarding the bill
print("Please input party size: ")
partySize = int(input())

print("Please input sales tax: ")
salesTax = float(input())
salesTax = (salesTax / 100)

print("Please input tip percentage (Do not input percentage sign): ")
tipPercentage = float(input())
tipPercentage = (tipPercentage / 100)

print("Would you like to split evenly by check amount or item?")
print("Please input 'By check' or 'By item'")
splitChoice = input().casefold()


# Will complete based on splitting by the check
if splitChoice == "by check": 
    print("Please input subtotal: ")
    subTotal = float(input())
    taxAmount = round(subTotal * salesTax, 2)
    tipAmount = round((subTotal + taxAmount) * tipPercentage, 2)
    totalPrice =  round(subTotal + taxAmount + tipAmount, 2)
    sharedAmount = round(totalPrice / partySize, 2)

    print(f"Subtotal: ${subTotal}")
    print(f"Taxes: ${taxAmount}")
    print(f"Tip: ${tipAmount}")
    print("------------------------")
    print(f"Total: ${totalPrice}")
    print(f"Price per person: ${sharedAmount}")
#  Will check based on total spent per person
elif splitChoice == "by item": 
    counter = 1

    while counter <= partySize: 
        print(f"How did did person {counter} spend? ")
        itemAmount = float(input("$"))
        taxAmount = round(itemAmount * salesTax, 2)
        tipAmount = round((itemAmount + taxAmount) * tipPercentage, 2)
        totalPrice = round(itemAmount + taxAmount + tipAmount, 2)

        print(f"Person {counter} owes: ${totalPrice}")

        counter += 1
else:
    print("Invalid choice. Please select 'by check' or 'by item'")