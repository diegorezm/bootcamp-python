import os
from menu import MENU,resources, money

def handle_money(product:dict[str, float]):
  wallet: dict[str, float] = {}
  print("Please provide the money")
  for item in money:
     dollar = int(input(f"How many {item}: "))
     wallet[item] = dollar
  for wallet_money, i in zip(wallet, money):
     wallet[wallet_money] *= money[i]
  total = sum(wallet.values())
  cost = product["cost"]
  if total > cost:
     print(f"Here is {total - cost} in change")
     return True
  elif total < cost:
     print("Not enough money.")
     return False
  return True

def handle_resources(product:dict[str, float]):
  ingredients = product["ingredients"]
  for product_ingredients, resource in zip(ingredients, resources):
    if ingredients[product_ingredients] >  resources[resource]:
       print(f"Not enough {product_ingredients}.")
       return
    else:
      resources[resource] -= ingredients[product_ingredients]
  
def coffe_machine():
  operations = ["report", "espresso","latte","cappuccino", "exit"]
  machine_money = 0
  while True:
    user_operation = input("What would you like to do? (exit,report, espresso, latte,cappuccino) ")
    while user_operation not in operations:
        user_operation = input("Please provide a valid operation! (exit,report, espresso, latte,cappuccino) ")
    match user_operation:
      case "report":
        for item, value in resources.items():
           print(f"{item}: {value}")
        print(f"money: {machine_money}")
      case "espresso":
          espresso = MENU["espresso"]
          handle_money(espresso)
          if  not handle_money:
             print("You got an error during the payment process. Finishing program.")
             exit(1)
          machine_money += espresso["cost"]
          handle_resources(espresso)
      case "latte":
          latte = MENU["latte"]
          handle_money(latte)
          if  not handle_money:
             print("You got an error during the payment process. Finishing program.")
             exit(1)
          machine_money += latte["cost"]
          handle_resources(latte)
      case "cappuccino":
          cappuccino = MENU["cappuccino"]
          handle_money(cappuccino)
          if  not handle_money:
             print("You got an error during the payment process. Finishing program.")
             exit(1)
          machine_money += cappuccino["cost"]
          handle_resources(cappuccino)
      case "exit":
          exit(0)
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    coffe_machine()