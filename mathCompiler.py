# python calculator

import os
# import re to use regex
import re

# menu for the user
def menu(option):
    # showing the desired option
    if(option == '1'):
        print("Digite a string: ")
        userInput = input()
        if not checkFormula(userInput):
            main()
        else:
            checkSign(userInput)
            main()
    elif(option == '2'):
        exit()
    elif(option != '1' or option != '2'):
        print("Opção inválida.")
        main()

# checking the sign for the operation
def checkSign(userInput):
    for i in userInput:
        if(i == '+'):
            print(sumFunction(userInput))
        elif(i == '-'):
            print(subtractFunction(userInput))
        elif(i == '*'):
            print(multiplyFuction(userInput))
        elif(i == '/'):
            print(divideFunction(userInput))
        elif(i == '|'):
            print(expoFunction(userInput))
        elif(i == '&'):
            print(squareFunction(userInput))

# checking if there is a number in the strign
def checkNumber(userInput):
    numbers = [int(n) for n in re.findall(r'\d+', userInput)]
    return numbers

def checkFormula(userInput):
    open_sign = ['(']
    close_sign = [')']
    forbidden_char = ['{', '}', '[', ']']
    expression = []
    if(userInput[-1] == '('):
        print("Parênteses não foram fechados da maneira correta!")
        return False
    else:
        for item in userInput:
            for char in forbidden_char:
                if(char in item):
                    print("Use apenas parênteses! :)")
                    return False
            if item in open_sign:
                expression.append(item)
            elif item in close_sign:
                position = close_sign.index(item)
                if((len(expression) > 0) and (open_sign[position] == expression[len(expression)-1])):
                    expression.pop()
                else:
                    print("Parênteses não foram fechados da maneira correta!") 
                    return False
        if len(expression) == 0:
            return True

def sumFunction(userInput):
    result = checkNumber(userInput)
    totalSum = 0
    for i in result:
        totalSum = totalSum + i
    return totalSum

def subtractFunction(userInput):
    result = checkNumber(userInput)
    totalSub = [result[i]-result[i+1] for i in range(len(result)-1)]
    return totalSub[-1]

def multiplyFuction(userInput):
    result = checkNumber(userInput)
    totalMult = 1
    for i in result:
        totalMult = totalMult * i
    return totalMult

def divideFunction(userInput):
    result = checkNumber(userInput)
    totalDiv = [result[i]/result[i+1] for i in range(len(result)-1)]
    return int(totalDiv[-1])

def expoFunction(userInput):
    result = checkNumber(userInput)
    totalExp = [result[i]**result[i+1] for i in range(len(result)-1)]
    return totalExp[-1]

def squareFunction(userInput):
    result = checkNumber(userInput)
    for i in result:
        totalSquare = i ** 0.5
    return int(totalSquare)

# MAIN
def main():
    print("\n1 - Calculadora \n2 - Sair \n")
    print("Selecione a opção desejada: ")
    option = input()
    os.system('cls')
    menu(option)

main()

