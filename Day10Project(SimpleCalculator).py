#Definindo funções de algebra
def add(n1, n2):
    return n1 + n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0 :
        print('Cant divide by 0')
        return n1
        
    return n1 / n2

def sub(n1, n2):
    return n1 - n2
#Definindo dicionário de operações
operations = { '+' : add ,
             '-' : sub,
             '*' : mult,
             '/' : div }
#Iniciando programa
n1 = float(input("What's our first number? "))
print('+\n-\n*\n/\n')

while True:
    op = input('Pick a operation: ')
#Verificando se a opreação é válida    
    if op not in operations:
        print('Invalid operation.')
        continue
    
    n2 = float(input("What's your second number? "))
    
    result = operations[op](n1,n2)
    
    print(result)
    n1 = result
#Verificando continuidade ou interrupção de uso do programa    
    while True:
        continue_with_result = input('Do you want continue operating with last result?[y/n] ').lower()
        if continue_with_result  in ['y', 'n']:
            break
        print('Choose y, or, n.')
    if continue_with_result == 'n' :
        print("Thank you for use the calculator program")
