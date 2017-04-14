

numbers = []
stage1 = True

while stage1:

    number = input("Enter a number and after space: '2' for bin or '10' for dec calculation: ")

    numbers = number.split()                                                                    # wprowadzenie dwóch elementów do listy bez znaków typu spacja

    if len(numbers) != 2:                                                                       # sprawdzenie czy użytkownik podał dwa elementy
        print("Please enter two elements")

    elif len(numbers) == 2:                                                                     #jeśli tak

        first_element  = numbers[0]
        second_element = numbers[1]

        if first_element.isdigit() and second_element.isdigit():                                #sprawdzenie czy elementy są liczbami
            if second_element == "2":                                                           #dla przypadku, gdy użytkownik wpisał, że wpisał liczbę binarną,
                for i in first_element:                                                         #sprawdzamy czy podana liczba zawiera inne cyfry niż 0 i 1
                    if i != 0 and i != 1:
                        break
                print("This is not a binary number!")
            elif second_element == "10":                                                        #przypadek, gdzie użytkownik wprowadził liczbę decimal
                stage1 = False                                                                  #wyjście z pętli

            else:
                print("There is no \"" +second_element+"\" calculation format. Put '2' or '10' as a second element.\n") #Gdy użytkownik wpisze inny second_element niż 2 lub 10

        else:
            print("First or second element is not a number.")                                   #gdy użytkownik wprowadzi literę lub słowo zamiast liczby w pierwszy lub drugi element

    numbers = []

def binary_to_decimal(first_element):                                                           #zdefiniowanie funkcji konwertującej liczbę binarną do dziesiętnej
    decimal=0
    for i in range(len(first_element)):
        power=len(first_element)-(i+1)
        decimal += int(first_element[i])*(2**power)
    return decimal

def decimal_to_binary(first_element):                                                           #zdefiniowanie funkcji konwertującej liczbę dziesiętną na binarną
    dec = int(first_element)
    binNum = 0
    power = 0
    while dec > 0:
        binNum += 10 ** power * (dec % 2)
        dec //= 2
        power += 1
    return binNum 


if second_element == "2":                                                                       #odpalenie funkcji i drukowanie wyniku
    binary_to_decimal(first_element)
    print(str(binary_to_decimal(first_element)) + " " + "2")

elif second_element == "10":
    decimal_to_binary(first_element)
    print(str(decimal_to_binary(first_element)) + " " + "10")










#
