from datetime import datetime
from store import Client, Seller, Purchase

def main():
    client = Client('Maria Lima', 44)
    seller = Seller('Pedro Garrido', 36, 6305)

    purchase1 = Purchase(client, datetime.now(), 512)
    purchase2 = Purchase(client, datetime.now(2018, 6, 4), 256)

    client.register_purchase(purchase1)
    client.register_purchase(purchase2)
    print(f'Client: {client}', '(adult)' if client.is_adult() else '')
    print(f'Seller: {seller}')

    total_value = client.total_purchases()
    qty_purchases = len(client.purchases)
    print(f'Total: {total_value} in {qty_purchases} purchases.')
    print(f'Last purchase: {client.get_last_purchase_date()}')


if __name__ == '__main__':
    main()
