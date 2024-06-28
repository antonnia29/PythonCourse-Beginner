# Antonnia Abdul - AN24020013912

#Pseudocode to show the cafe inventory and stock prices

""" Steps:
1. Create a dictionary for stock items
2. Create a dictionary of price list per item
3. Calculate for the overall cost per item (quauntity)
4. Calculate overall inventory cost
5. Display all to user

"""

menu = ["Soup", "Rice", "Chicken", "Cous-Cous", "Fish"]

stock = {
"Soup" : 50,
"Rice" : 126,
"Chicken": 389,
"Cous-Cous" : 648,
"Fish" : 988
}



price = {
"Soup" : 1.69,
"Rice" : 6.99,
"Chicken": 14.98,
"Cous-Cous" : 8.98,
"Fish" : 19.50
}



print("\n------------------- Cafe Inventory & Stock Prices  -------------------- \n")

item_value = 0

# inventory calculation

for item in menu:
    item_value += (stock[item]) * (price[item])
    chicken = stock["Chicken"] * price["Chicken"]
    cous_cous = stock["Cous-Cous"]* price["Cous-Cous"]
    fish = stock["Fish"]* price["Fish"]
    rice = stock["Rice"]* price["Rice"]
    soup = stock["Soup"]* price["Soup"]


# Display to user

print(f"List of all stock invertory and quantity...\n{stock}")

print("\n----------------------------------------------------------------------- \n")

print(f"Total stock value for all items = £ {int(item_value)}")

print("\n------------------------------------------------------------------------ \n")

print(f"Total value of Chicken is: £{(int(chicken))}")
print(f"Total value of Cous-Cous is: £{(int(cous_cous))}")
print(f"Total value of Fish is: £{(int(fish))}")
print(f"Total value of Rice is: £{(int(rice))}")
print(f"Total value of Soup is: £{(int(soup))}")


print("\n--------------------------  End of Inventory   ------------------------ \n")



