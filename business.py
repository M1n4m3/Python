products = {}
income = 0

while True:
    print("\n1. Add Product  2. Sell Product  3. Show Income  4. Exit")
    choice = input("Choose option: ")

    if choice == '1':
        name = input("Product name: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        products[name] = {'price': price, 'stock': stock}
    elif choice == '2':
        name = input("Product to sell: ")
        qty = int(input("Quantity: "))
        if name in products and products[name]['stock'] >= qty:
            total = qty * products[name]['price']
            products[name]['stock'] -= qty
            income += total
            print(f"Sold {qty} x {name} for ${total:.2f}")
        else:
            print("Not enough stock or product not found.")
    elif choice == '3':
        print(f"Total income: ${income:.2f}")
    elif choice == '4':
        break
    else:
        print("Invalid option.")
