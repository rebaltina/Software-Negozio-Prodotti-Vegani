def choose_an_input():
    '''
    helping user to choose a valid input
    '''
  action = input(f"Inserisci un comando ")

  help_menu = {"aggiungi": "aggiungi un prodotto al magazzino", 
  "elenca": "elenca i prodotto in magazzino",
  "vendita": "registra una vendita effettuata",
  "profitti": "mostra i profitti totali",
  "aiuto" : "mostra i possibili comandi",
  "chiudi": "esci dal programma" }

  if action not in help_menu.keys():
    print(f'Comando non valido. I comandi disponibili sono i seguenti: {help_menu.items()}')
  else:

    print(f"Ora {help_menu[action]}")

    return action

def create_file (filename, data):
    '''
    :param filename: name of the file you want to create 
    :param data: dictionary of data to write in the file
    '''
  with open(filename, 'w+') as file:
        json.dump(data, file, indent=3, ensure_ascii=False)
        print(f"file {filename} has been created")

def read_file (filename):
    '''
    :param filename: name of the file you want to read 
    '''
  with open(filename, 'r') as in_file:
      data = json.load(in_file)

  return data

def update_file (filename, new_data):
    '''
    :param filename: name of the file you want to create or update
    :param new_data: dictionary of data to write in the file
    '''
  try:
    with open(filename, 'r+') as in_file:
      data = json.load(in_file)
      in_file.seek(0)
      data.update(new_data)
      json.dump(data, in_file, indent=3, ensure_ascii=False)

      print(f"file {filename} has been updated with new record")

    return data
         
  except FileNotFoundError:

    print("file not found")

    return {}

def insert_data_in_database(filename, data):
    '''
    :param filename: name of the file you want to create or update
    :param new_data: dictionary of data to write in the file
    ''' 
  new_data = update_file(filename, data)
  if new_data == {}:
    create_file(filename, data)


def add_new_product(filename):
    '''
    :param filename: inventory filename
    '''
  inventory = {}
  product = input("Nome del prodotto: ")

  quantity = 0
  while quantity == 0:
    try:
      quantity = int(input("quantità: "))
    except:
      print("il numero inserito non è un numero!")


  if product in inventory.keys():
    inventory[product]["quantità"]+=quantity
  else:
    cost = 0
    price = 0
    while cost == 0:
      try:
        cost = float(input("Prezzo di acquisto: "))
      except:
        print("l'input inserito non è un numero!")
    while price == 0:
      try:
        price = float(input("Prezzo di vendita: "))
      except:
        print("l'input inserito non è un numero!")

    inventory[product] = {"quantità": quantity, "prezzo di vendita": price , "prezzo di acquisto" : cost}

    insert_data_in_database(filename, inventory)


def add_new_sale(inventory_filename, date): 

    '''
    :param inventory_filename: overwritten or created (if it does not exist) file name for storing sales
    :param date: date of the sales, previously obtained
    '''

  sales = {}

  inventory = read_file (inventory_filename)

  product = input("Nome del prodotto: ")
  assert(product in inventory.keys()), "il prodotto inserito non si trova in magazzino: per aggiungere un nuovo prodotto inserire il comando 'aggiungi'"
    
  quantity = int(input("quantità: "))
  total_sale = inventory[product]["prezzo di vendita"]* quantity
  sales[date] = {"products": [{}], "total_sales" : 0.0}    
  sales[date]["products"][0][product] = {"quantità": quantity, "total_spent": total_sale}
  sales[date]["total_sales"] += total_sale

  new_sale = input("Aggiungere un altro prodotto ?(si/no): ")
  
  if new_sale == "no":

    return sales

  elif new_sale == "si":

    product = input("Nome del prodotto: ")
    assert(product in inventory.keys()), "il prodotto inserito non si trova in magazzino: per aggiungere un nuovo prodotto inserire il comando 'aggiungi'"
    
    quantity = int(input("quantità: "))
    sales[date]["products"][0][product] = {"quantità": quantity, "total_spent": total_sale}
    sales[date]["total_sales"] += total_sale

  return sales

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


  print(f"Il profitto lordo attuale è di {gross_income}$")
  print(f"Il profitto netto attuale è di {gross_income-total_costs}$")

  return
