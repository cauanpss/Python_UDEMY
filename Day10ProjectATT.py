#Definir funções
def get_float_input(prompt):
    while True:
        try:
            return(float(input(prompt)))
        except ValueError:
            print('Invalid input, pick a number')
            continue

def add(n1, n2):
    return n1 + n2

def div(n1, n2):
    if n2 == 0:
        print('0 is a invalid number for divider.')
        return n1
    return n1 / n2

def mult(n1, n2):
    return n1 * n2

def sub(n1, n2):
    return n1 - n2

#Definir dicionário de operadores
operators = {
            '+' : add,
            '-' : sub,
            '*' : mult,
            '/' : div
            }

#Definir entradas/saídas:
n1 = get_float_input("What's your first number?")

print('+\n-\n*\n/'
)
while True:    
    op = input('Pick an operator: ')
    if op not in operators:
        print(f'Invalid input, please choose between {','.join(operators.keys())}')
        continue
    n2 = get_float_input("What's your second number? ")
    result = operators[op](n1, n2)
    n1 = result
    print(result)
#Verificar se o usuário quer continuar
    while True:
        continue_with_result = input('Do you want continue with the last result? [y/n]').lower()
        if continue_with_result in ('y','n'):
            break
        print("Pick an valid answer [y/n]")
    if continue_with_result == 'y':
        continue
    if continue_with_result == 'n':
        print("Thank you for use the calculator program!")
        break