buying_price=float(input("enter your buying price"))
selling_price=float(input("enter your selling price"))
if selling_price>buying_price:
    profit=selling_price-buying_price
    print("you are in profit")
    print("profit=",profit)
else:
    loss=buying_price-selling_price
    print("you are in loss")
    print("loss=",loss)