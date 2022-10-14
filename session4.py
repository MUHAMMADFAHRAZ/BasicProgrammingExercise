#credit by Muhamad Fahraz Firdaus


#input product name to variable
product_name = [""]
product_name[0] = input("input the first product name : ")
product_name[1] = input("input the second product name : ")
product_name[2] = input("input the third product name : ")
#input amount of items
amount_items = []
amount_items[0] = int (input("how many items do you buy first product: "))
amount_items[1] = int (input("how many items do you buy second product: "))
amount_items[2] = int (input("how many items do you buy third product: "))
#input product price to variable
price_product = []
price_product[0] = int(input("input the price of first product : "))
price_product[1] = int(input("input the price of second product : "))
price_product[2] = int(input("input the price of third product : "))
#total cost product
totalcost_product = []
totalcost_product[0] = amount_items[0] * price_product[0]
totalcost_product[1] = amount_items[1] * price_product[1]
totalcost_product[2] = amount_items[2] * price_product[2]
# set 10% variable
persen = []
persen[0] = int (input("input profit persentage of first product : "))
persen[1] = int (input("input profit persentage of first product : "))
persen[2] = int (input("input profit persentage of first product : "))
#calculate the persentage from the product price
sale_price = []
sale_price[0] = price_product[0] + price_product[0]*persen[0]/100
sale_price[1] = price_product[1] + price_product[1]*persen[1]/100
sale_price[2] = price_product[2] + price_product[2]*persen[2]/100
#profit per sale
profitPerSale =[]
profitPerSale[0] = sale_price[0] - price_product[0]
profitPerSale[1] = sale_price[1] - price_product[1]
profitPerSale[2] = sale_price[2] - price_product[2]
#input amount of selling
amount_selling = []
amount_selling[0] = int (input ("input total Selling your first product : "))
amount_selling[1] = int (input ("input total Selling your second product : "))
amount_selling[2] = int (input ("input total Selling your third product : "))
# total total selling
total_selling = []
total_selling[0] = sale_price[0] * amount_selling[0]
total_selling[1] = sale_price[1] * amount_selling[1]
total_selling[2] = sale_price[2] * amount_selling[2]
#calculate the profit
total_profitperitems =[]
total_profitperitems = total_selling[0] - totalcost_product[0]
total_profitperitems = total_selling[1] - totalcost_product[1]
total_profitperitems = total_selling[2] - totalcost_product[2]
#final total profit
FinalTotal_profit = total_profitperitems[0] + total_profitperitems[1] + total_profitperitems[2]

print("\n product name : " + str(product_name) + "\n amount of items : " + str(amount_items) +
"\n cost per items : " + str(price_product) + "\n total purchase product : " + str(totalcost_product) +
"\n percentage of profit take : " + str(persen)+"%" + "\n profit per sale : " + str(profitPerSale) +
"\n cost per sale : " + str(sale_price) + "\n amount of selling : " + str (amount_selling) + 
"\n total selling : " + str (total_selling) + "total profit per item : " + str (total_profitperitems) +
"\n total profit : " + str (FinalTotal_profit))