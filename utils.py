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

