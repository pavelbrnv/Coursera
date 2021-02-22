class Customer:
    name = ''
    products = None


customers = dict()

inFile = open('input.txt', 'r', encoding='utf8')
for line in map(lambda l: l.split(), inFile):
    customer_name = line[0]
    product_name = line[1]
    product_quantity = int(line[2])

    customer = customers.get(customer_name, 0)
    if customer == 0:
        customer = Customer()
        customer.name = customer_name
        customer.products = dict()
        customers[customer_name] = customer

    total_product_quantity = customer.products.get(product_name, 0)
    customer.products[product_name] = total_product_quantity + product_quantity
inFile.close()

for customer in sorted(customers.values(), key=lambda c: c.name):
    print(customer.name + ':')
    for product in sorted(customer.products.items(), key=lambda i: i[0]):
        print(product[0], product[1])
