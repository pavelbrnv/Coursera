class Client:
    name = ''
    balance = 0


clients = dict()


def get_client(client_name):
    return clients.get(client_name, None)


def get_or_create_client(client_name):
    client = clients.get(client_name, 0)
    if client == 0:
        client = Client()
        client.name = client_name
        clients[client_name] = client
    return client


def deposit_to(client_name, value):
    client = get_or_create_client(client_name)
    client.balance += value


def withdraw_from(client_name, value):
    client = get_or_create_client(client_name)
    client.balance -= value


def get_balance(client_name):
    client = get_client(client_name)
    if client is not None:
        print(client.balance)
    else:
        print('ERROR')


def transfer_between(source_name, destination_name, value):
    withdraw_from(source_name, value)
    deposit_to(destination_name, value)


def income(value_percents):
    for client in clients.values():
        if client.balance > 0:
            client.balance += int(client.balance * value_percents / 100)


def main():
    inFile = open('input.txt', 'r', encoding='utf8')
    for operation in map(lambda l: l.split(), inFile):
        operation_name = operation[0]
        if operation_name == 'DEPOSIT':
            deposit_to(operation[1], int(operation[2]))
        elif operation_name == 'WITHDRAW':
            withdraw_from(operation[1], int(operation[2]))
        elif operation_name == 'BALANCE':
            get_balance(operation[1])
        elif operation_name == 'TRANSFER':
            transfer_between(operation[1], operation[2], int(operation[3]))
        elif operation_name == 'INCOME':
            income(int(operation[1]))
    inFile.close()


main()
