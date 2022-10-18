#credit by Muhamad Fahraz Firdaus


#input product name to variable
product_name = input("input the product name : ")
#input amount of items
amount_items = int (input("how many items do you buy product: "))
#input product price to variable
price_product = int(input("input the price of product : "))
#total cost product
totalcost_product = amount_items * price_product
# set 10% variable
persen = int (input("input profit persentage of product : "))
#calculate the persentage from the product price
sale_price = int (price_product + price_product*persen/100)
#profit per sale
profitPerSale = int (sale_price - price_product)
#input amount of selling
amount_selling = int (input ("input total Selling your  product : "))
# total total selling
total_selling = int (sale_price * amount_selling)
#calculate the profit
total_profit = int (total_selling - totalcost_product)

print("\n product name : " + str(product_name) )
print ("amount of items : " + str(amount_items))
print("cost per items : " + str(price_product))
print("total purchase product : " + str (totalcost_product))
print("percentage of profit take : " + str(persen)+"%" )
print("profit per sale : " + str(profitPerSale)) 
print("cost per sale : " + str(sale_price))
print("amount of selling : " + str (amount_selling))
print("total selling : " + str (total_selling))
print("total profit : " + str (total_profit))
