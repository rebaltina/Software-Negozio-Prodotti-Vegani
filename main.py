import datetime
import json

def main():
  action = choose_an_input()


  if action == "aggiungi":

    add_new_product("inventory.json")
    

  elif action == "elenca":

    inventory = read_file ("inventory.json")
    product_list = [key for key in inventory.keys()]

    print(f"i prodotti disponibili in magazzino sono i seguenti:{product_list}")

  elif action == "vendita":  

    today = datetime.datetime.now()
    date = today.strftime("%m/%d/%Y, %H:%M:%S")
    sales = add_new_sale("inventory.json", "vendite.json", date)



  elif action == "profitti":

    calculate_profits("vendite.json", "inventory.json")

  else:

    print("bye bye") #only remaining command is "chiudi"

if __name__ == '__main__':
    main()

 
