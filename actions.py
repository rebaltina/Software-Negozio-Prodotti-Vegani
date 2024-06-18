def choose_an_input():

  action = input(f"Inserisci un comando ")

  
  help_menu = {"aggiungi": "aggiungi un prodotto al magazzino",
  "elenca": "elenca i prodotto in magazzino",
  "vendita": "registra una vendita effettuata",
  "profitti": "mostra i profitti totali",
  "aiuto" : "I comandi disponibili sono i seguenti: aggiungi: aggiungi un prodotto al magazzino elenca: elenca i prodotto in magazzino vendita: registra una vendita effettuata profitti: mostra i profitti totali aiuto: mostra i possibili comandi chiudi: esci dal programma",
   "chiudi": "Esci dal programma"}

  while action != "chiudi":

    if action == "aggiungi":
      add_new_product("inventory.json")
    elif action == "elenca":
      list_products("inventory.json")
    elif action == "vendita":
      add_new_sale("inventory.json", "vendite.json")
    elif action == "profitti":
      calculate_profits("vendite.json", "inventory.json")
    elif (action not in help_menu.keys()) | (action == "aiuto"):
      print(f'Comando non valido. I comandi disponibili sono i seguenti: {help_menu.items()}')

    action = input(f"Inserisci un comando ")

  if action == "chiudi":

      print("Bye bye") #only remaining command is "chiudi"

      return

def add_new_product(filename):
    '''
    :param filename: inventory filename
    '''
    inventory = read_file(filename)
    product = input("Nome del prodotto: ")

    quantity = 0

    while quantity <= 0:
      try:
        quantity = int(input("quantità: "))
        if quantity < 0:
          raise ValueError("il numero inserito non è un numero intero positivo!")
      except ValueError:
        print("l'input inserito non è un numero intero!")     

    if product in inventory.keys():
      
      print(f"prodotto {product} già presente in inventory: aggiornamento quantità di {product} in corso..")

      inventory[product]["quantità"]+=quantity
      
      
    else:

      cost = 0
      price = 0

      while cost <= 0:
        try:
          cost = float(input("Prezzo di acquisto: "))
          if cost < 0:
            raise ValueError("il numero inserito non è un numero positivo!")
        except ValueError:
          print("il numero inserito non è un numero intero!")

      while price <= 0:
        try:
          price = float(input("Prezzo di vendita: "))
          if price < 0:
            raise ValueError("il numero inserito non è un numero positivo!")
        except ValueError:
          print("il numero inserito non è un numero valido! Ex. prezzo valido: 3.5")

      inventory[product] = {"quantità": quantity, "prezzo di vendita": price , "prezzo di acquisto" : cost}

    insert_data_in_database(filename, inventory)

def list_products(filename):

    inventory = read_file (filename)

    print(f"i prodotti disponibili, in magazzino sono i seguenti:")
    for key in inventory.keys():
      
      print(f'{inventory[key]["quantità"]} di {key} al prezzo di  {inventory[key]["prezzo di acquisto"]} euro')


def add_new_sale(inventory_filename, sales_filename):

    '''
    :param inventory_filename: overwritten or created (if it does not exist) file name for storing sales
    :param date: date of the sales, previously obtained
    '''
    today = datetime.datetime.now()
    date = today.strftime("%m/%d/%Y, %H:%M:%S")

    sales = {}

    inventory = read_file (inventory_filename)

    product = input("Nome del prodotto: ")
    #assert(product in inventory.keys()), "il prodotto inserito non si trova in magazzino: per aggiungere un nuovo prodotto inserire il comando 'aggiungi'"

    if product not in inventory.keys():

      print(f"{product} non si trova in magazzino: per aggiungere un nuovo prodotto inserire il comando 'aggiungi' e ripetere l'intera vendita")

      choose_an_input()

    quantity = 0

    while quantity <= 0:
      try:
        quantity = int(input("quantità: "))
        if quantity < 0:
          raise ValueError("il numero inserito non è un numero intero positivo!")
      except ValueError:
        print("il numero inserito non è un numero intero positivo!")

    while quantity > inventory[product]["quantità"]:

      print(f'Attualmente la quantità di {product} disponibile in magazzino è di {inventory[product]["quantità"]}: \n inserisci una quantità inferiore')
      quantity = int(input("quantità: "))

    inventory[product]["quantità"] -= quantity

    total_spent = inventory[product]["prezzo di vendita"] * quantity
    sales[date] = {"products": [{}], "total_sales" : 0.0}
    sales[date]["products"][0][product] = {"quantità": quantity, "total_spent": total_spent}
    sales[date]["total_sales"] += total_spent

    new_sale = input("Aggiungere un altro prodotto ?(si/no): ")

    if new_sale == "no":

      insert_data_in_database(sales_filename, sales)
      insert_data_in_database(inventory_filename, inventory)

      print("vendita registrata!")

      return 

    elif new_sale == "si":

      product = input("Nome del prodotto: ")
      #assert(product in inventory.keys()), "il prodotto inserito non si trova in magazzino: per aggiungere un nuovo prodotto inserire il comando 'aggiungi'"
      if product not in inventory.keys():
        print(f"{product} non si trova in magazzino: per aggiungere un nuovo prodotto inserire il comando 'aggiungi' e ripetere l'intera vendita")

        choose_an_input()


      quantity = int(input("quantità: "))
      while quantity <= 0:
        try:
          quantity = int(input("quantità: "))
          if quantity < 0:
            raise ValueError("il numero inserito non è un numero intero positivo!")
        except ValueError:
          print("il numero inserito non è un numero intero positivo!") 

      inventory[product]["quantità"] -= quantity
      total_spent = inventory[product]["prezzo di vendita"] * quantity
      sales[date]["products"][0][product] = {"quantità": quantity, "total_spent": total_spent}
      sales[date]["total_sales"] += total_spent

    
    insert_data_in_database(sales_filename, sales)
    insert_data_in_database(inventory_filename, inventory)

    print("vendita registrata!")

    return 

def calculate_gross_income (sales):
    '''
    :param sales: dictionary containing sales (as by source json file)
    '''
    gross_income = 0
    sold_products = []
    for date in sales.keys():
      gross_income += sales[date]["total_sales"]
      sold_products.append(sales[date]["products"])
    return gross_income, sold_products

def extract_sold_products(sold_products):
    '''
    :param sold_products: list of nested dictionaries where keys are product names and values are dictionary for quantities and expenses
    '''
    sold_quantity_product = {}

    for index in range(len(sold_products)):
      sale = sold_products[index]
      for index_b in range(len(sale)):
        for key in (sale[index_b].keys()):
          if key in sold_quantity_product.keys():
            sold_quantity_product[key] += sale[index_b][key]['quantità']
          else:
            sold_quantity_product[key] = sale[index_b][key]['quantità']
    return sold_quantity_product

def calculate_total_costs(sold_quantity_product, inventory):
    '''
    :param sold_quantity_product: dictionary containing products as keys and product quantities as value
    :param inventory: dictionary loaded from inventory json file
    '''
    total_costs = 0
    for product in sold_quantity_product.keys():
      unit_cost_product = inventory[product]['prezzo di acquisto']
      total_cost_product = sold_quantity_product[product] * unit_cost_product
      total_costs += total_cost_product

      return total_costs

def calculate_profits(sales_filename, inventory_filename):
    '''
    :param sales_filename: sales json file name
    :param sales_filename: inventory json file name
    '''
    vendite = read_file(sales_filename)
    inventory = read_file(inventory_filename)

    gross_income, sold_products = calculate_gross_income (vendite)
    sold_quantity_product = extract_sold_products(sold_products)
    total_costs = calculate_total_costs(sold_quantity_product, inventory)


    print(f"Il profitto lordo attuale è di {gross_income} euro")
    print(f"Il profitto netto attuale è di {gross_income-total_costs}")

    return
