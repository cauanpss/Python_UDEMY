MENU = {
    "espresso": {
        "ingredients":{
            "water":50,
            "coffe":18,
        },
    "cost":1.5
    },

    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffe":24,
        },
    "cost":2.5
    },

    "capuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffe":24,
        },
    "cost":3.0,
    }
}

storage = {
    "water":500,
    "coffe":200,
    "milk":400,
}

for nome_bebida in MENU:
    print(f"Bebida: {nome_bebida}")
    for ingrediente in MENU[nome_bebida]:
        print(f"  - {ingrediente}: {MENU[nome_bebida][ingrediente]}")


# MENU([key][key][key])
# ingredientes = MENU["capuccino"]["ingredients"]
# for item, quantidade in ingredientes.items():
#     print(f'{item}: {quantidade}')

# def getPrice(drink_name):
#     return f"The {drink_name} cost is ${MENU[drink_name]["cost"]}"
# print(getPrice("latte"))
    
