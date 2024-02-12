import os
from prettytable import PrettyTable
from menu import MENU,resources, coins

class CoffeMachine:
  money: float
  menu: dict[str, dict[str, float]]
  resources:  dict[str, float]
  operations: list[str]

  def __init__(self) -> None:
    self.money = 0
    self.menu = MENU
    self.resources = resources
    self.operations = ["report", "espresso","latte","cappuccino", "exit"]

  def display_resources(self) -> PrettyTable:
    prettyTable = PrettyTable()
    prettyTable.field_names = ["Resources" ,"Quantity"]
    for item, value in self.resources.items():
      prettyTable.add_row([item, value])
    prettyTable.add_row(["Money", self.money])
    return prettyTable

  def handle_money(self, product:dict[str, float]) -> bool:
    wallet: dict[str, float] = {}
    print("Please provide the money")
    for item in coins:
      dollar = int(input(f"How many {item}: "))
      wallet[item] = dollar
    for wallet_money, i in zip(wallet, coins):
      wallet[wallet_money] *= coins[i]
    total = sum(wallet.values())
    cost = product["cost"]
    if total > cost:
      print(f"Here is {total - cost} in change")
      return True
    elif total < cost:
      print("Not enough money.")
      return False
    return True
  
  def handle_resources(self, product:dict[str, float]) -> bool:
    ingredients = product["ingredients"]
    for product_ingredients, resource in zip(ingredients, self.resources):
      if ingredients[product_ingredients] >  self.resources[resource]:
        print(f"Not enough {product_ingredients}.")
        return False
      else:
        resources[resource] -= ingredients[product_ingredients]
    return True

  def start(self) -> None:
    while True:
      user_operation = input("What would you like to do? (exit,report, espresso, latte,cappuccino) ")
      while user_operation not in self.operations:
          user_operation = input("Please provide a valid operation! (exit,report, espresso, latte,cappuccino) ")
      match user_operation:
        case "report":
          table = self.display_resources()
          print(table)
        case "espresso":
            espresso = MENU["espresso"]
            handle_money = self.handle_money(espresso)
            if  not handle_money:
              print("You got an error during the payment process. Finishing program.")
              break
            handle_resources = self.handle_resources(espresso)
            if not handle_resources:
              break
            self.money += espresso["cost"]
        case "latte":
            latte = MENU["latte"]
            handle_money = self.handle_money(latte)
            if  not handle_money:
              print("You got an error during the payment process. Finishing program.")
              break
            handle_resources = self.handle_resources(latte)
            if not handle_resources:
              break
            self.money += latte["cost"]
            
        case "cappuccino":
            cappuccino = MENU["cappuccino"]
            handle_money = self.handle_money(cappuccino)
            if  not handle_money:
              print("You got an error during the payment process. Finishing program.")
              break
            handle_resources = self.handle_resources(cappuccino)
            if not handle_resources:
              break
            self.money += cappuccino["cost"]
        case "exit":
            break
          
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    coffeMachine = CoffeMachine() 
    coffeMachine.start()