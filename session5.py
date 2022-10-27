import enum
from itertools import product
import os, platform, colorama
from tkinter import Menu
from colorama import Fore


#create list product
products = []

#main page
def main ():
    print("------------------------------------------------------")
    print("--------- session 5 - Muhamad Fahraz Firdaus ---------")
    print("-----------------point of sale App--------------------")

    print('MENU :')
    print("""
    1.Add product
    2.Purchase product
    3.product information
    4. Exit App""")

    chooseNavigation = input("Enter Number : ")
    if chooseNavigation == "1" :
       addProduct()
    elif chooseNavigation == "2" :
       purchaseProduct()
    elif chooseNavigation == "3":
        information()
    elif chooseNavigation == "4" :
        print("thanks for using this app")
    else :
        print("invalid input")

#add product
def addProduct():
    while (True):
        print("------------------------------------------------------")
        print("-------------------- Add Product ---------------------")
        print("------------------------------------------------------")
        #create list product
        product= {}
        product['name'] = input('input product name : ')
        product['price'] = int(input('input product price : '))
        product['stock'] = int (input('input product stock : '))
        product['percent'] =int(input('input profit percentage taken : '))

        product['margin'] = int(product['price'])*int(product['percent'])/100
        product['selling_price'] = int(product['price']) + int(product['margin'])


        # add product to products variable
        products.append(product)
    
        #break looping
        itsBreak = input('anything else to add (Y for yes, N for no) ? : ')
        if (itsBreak == 'N'):
            clearDisplay()
            print('-'*50)
            # print(f"{'Product': > 10} {'Price': > 10} {'Stock'}")
            print(f'{" No".ljust(6)}{"Product".ljust(19)} {"Price".ljust(17)} Stock')
            print('-'*50)

            for i,product in enumerate(products):
                i +=1
                print(f" {str(i).ljust(6)}{str(product['name'].ljust(19))}{(str(product['selling_price']).ljust(18))}{product['stock']}")
            print('-'*50)
            print("\n")
            exit()

def showProduct ():
    clearDisplay()
    print('-'*50)
    # print(f"{'Product': > 10} {'Price': > 10} {'Stock'}")
    print(f'{" No".ljust(6)}{"Product".ljust(19)} {"Price".ljust(17)} Stock')
    print('-'*50)

    for i,product in enumerate(products):
        i +=1
        print(f" {str(i).ljust(6)}{str(product['name'].ljust(19))}{(str(product['selling_price']).ljust(18))}{product['stock']}")
    print('-'*50)
    print("\n")

def purchaseProduct():
    print("------------------------------------------------------")
    print("-------------------- purchase App --------------------")
    print("------------------------------------------------------")

    global product
    showProduct()
    choose = input("choose the number : ")
    amount = int(input("purchase amount : "))

    for i, product in enumerate(products):
        if int(choose)-1 == i:
            product["item_sold"] = amount
            total_payment = product['selling_price'] * amount 
            product['income'] = product['item_sold'] * product['selling_price']
            product['stock'] -= amount
            
            clearDisplay()
            print("------------------------------------------------------")
            print("---------------- Receipt of purchase -----------------")
            print("------------------------------------------------------")
            print(f"Product Name  : {product['name']}")
            print(f"Selling Price : {product['selling_price']}")
            print(f"Quantity      : {amount}")
            print(f"Total payment : {total_payment}")
            print("-"*40) 

            exit()

def exit ():
    exit = input("\n enter m for back to menu : ")
    if (exit == "m"):
        main()

def clearDisplay():
    if platform.system() == "Linux":
        os.system('clear')
    if platform.system() == "Windows":
        os.system('cls')

def information():
    global product
    clearDisplay()
    print("------------------------------------------------------")
    print("-------------- information of product ----------------")
    print("------------------------------------------------------")
    print("\n")
    print('='*50)
    print(f'{" No".ljust(6)}{"Product".ljust(5)} {"COGS".ljust(7)}{"profit percent".ljust(5)}{"selling price".ljust(10)} Stock')
    print('='*50)

    for i,product in enumerate(products):
        i +=1
        print(f" {str(i).ljust(6)}{str(product['name'].ljust(5))}{(str(product['price']).ljust(7))}{(str(product['percent']) + '%'.ljust(5))}{(str(product['selling_price']).ljust(10))}{product['stock']}")
    print('-'*50)
    print("\n" * 4)
        
    exit()

if __name__ == "__main__":
    main()  