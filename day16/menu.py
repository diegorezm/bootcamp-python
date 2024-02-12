MENU: dict[str, dict[str, float]] = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources: dict[str, float] = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins: dict[str,float] = {
  "pennies": 0.01,
  "dimes": 0.1,
  "nickeles": 0.5,
  "quarters": 0.25
}