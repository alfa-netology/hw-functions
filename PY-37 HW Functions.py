import os

documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
  ]

directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
  }

def clear():
  """ очищает консоль """
  os.system('cls||clear')

def show_commands():
  """ выводит список всех доступных комманд """

  clear()
  commands = [
    'p – выводит имя человека по номеру документа',
    's - выводит номер полки на которой хранится документ по его номеру',
    'l - выводит список всех документов в формате passport "2207 876234" "Василий Гупкин" ',
    'a - добавление нового документа в каталог и перечень полок',
    'd - удаление записи из базы по номеру документа',
    'm - перемещение документа на новую полку',
    'as - добавление новой полки',
    'h - выводит список всех доступных команд',
    'x - закончить работу с программой'
  ]
  
  print("Cписок всех доступных комманд: \n")
  for command in commands: 
    print(command)
  print()

def show_people():
  """ выводит сведения о человеке по номеру документа """

  clear()
  print("Поиск имени по номеру документа.\n")
  document_number = input("введите номер: ")

  for item in documents:
    if item["number"] == document_number: 
      result = f"{item['name']} - {item['type']} {document_number}"      
      break      
    else:
      result = "в базе нет документа с таким номером"
  return result

def show_shelf():
  """ выводит номер полки, на которой хранится документ по его номеру """

  clear()
  print("Поиск полки, на которой хранится документ.\n")
  document_number = input("введите номер документа: ")

  for shelf, values in directories.items():
    if document_number in values:    
      result = f"{document_number} хранится на полке {shelf}"
      break
    else:
      result = "в базе нет документа с таким номером"
  return result

def show_documents_list():
  """ выводит список всех документов в базе """

  clear()
  print("Cписок всех хранящихся в базе документов:\n")
  if len(documents) == 0:
    print("В настоящий момент база не содержит ни одной записи\n")
  else:
    for id, item in enumerate(documents):
      print(id + 1, '. {type} "{number}" "{name}"'.format(**item), sep='')
    print()

def add_record():
  """ 
  добавление новой записи в базу 
  с указанием номера и типа документа, имени владельца и номера полки
  """

  clear()
  print("Добавление новой записи\n")

  while True:
    number = input("номер документа: ")
    document_type = input("тип документа: ") 
    name = input("имя владельца: ")
    shelf = input("номер полки: ") 

    if '' not in {number, document_type, name, shelf}:
      if shelf in directories:
        directories[shelf].append(number)
        document = dict(type = document_type, number = number, name = name)
        documents.append(document) 
        print()
        print(f"запись - {documents[-1:]} \nдобавлена в базу на полку #{shelf} - {directories[shelf]}\n")        
        break
      else:
        print(f'\nВы пытаетесь добавить документ на несуществующую полку {shelf}, давайте попробуем еще раз')      
    else:
      print('\nВведны неполные данные, давайте попробуем еще раз')

def delete_record():
  """ удаление записи из базы по номеру документа """

  clear()
  print("Удаление записи из базы по номеру документа.\n")
  document_number = input("введите номер: ")

  if delete_record_from_directories(document_number):
    delete_record_from_documents(document_number)
  else:
    print(f'Документ #{document_number} отсутствует в базе. Удаление невозможно.\n')
  
def delete_record_from_directories(document_number):
  """ удаляет документ с полки """

  for shelf, values in directories.items():
    flag = 0    
    if document_number in values:            
      values.remove(document_number)
      print(f'\nдокумент #{document_number} удален с полки {shelf}')      
      flag = 1
      break
  if flag == 1: return True
  else: return False

def delete_record_from_documents(document_number):
  """ удаление записи из каталога """
  for id, item in enumerate(documents):
    if document_number == item['number']:
      print(f"запись {item} удалена из базы\n")
      del documents[id]

def change_shelf():
  """ перемещение документа на другую полку """

  clear()
  print("Перемещение документа на другую полку\n")

  while True:    
    document_number = input("номер документа: ")
    shelf_old = check_document(document_number)

    if shelf_old == False:
      print(f'\nДокумента с #{document_number} нет в базе. Перемещение невозможно\n')
      break

    elif shelf_old != False:
      shelf_new = input("номер полки для перещения: ")
      if '' not in {document_number, shelf_new}: 
        if shelf_new != shelf_old:
          if shelf_new in directories:
            directories[shelf_new].append(document_number)
            directories[shelf_old].remove(document_number)
            print(f'\nДокумент #{document_number} перемещен с полки {shelf_old} на полку {shelf_new}\n')
            show_shelf_list()
            break
          else:
            print(f'\nПолки {shelf_new} не существует. Перемещение невозможно\n')
            break
        else:
          print(f'\nДокумент #{document_number} уже находится на полке {shelf_old}\n')
          break                
      else:
        print('\nВведны неполные данные, давайте попробуем еще раз')          

def add_shelf():
  """ создание новой полки """

  clear()
  print("Создание новой полки\n")

  while True:
    shelf = input("номер полки: ") 

    if '' not in {shelf}:
      if shelf not in directories:
        directories[shelf] = []
        show_shelf_list()
        break
      else:
        print(f'\nПолка {shelf} уже существует\n') 
        break     
    else:
      print('\nВведны неполные данные, давайте попробуем еще раз')

def check_document(document_number):
  """ проверка наличия документа на полке """

  for shelf, values in directories.items():
    flag = 0
    if document_number in values:
      flag = 1
      break

  if flag == 1:
    return shelf
  else: return False   

def show_shelf_list():
  """ выводит список полок и документов на них """
  for shelf, values in directories.items():
    print(shelf, values)
  print()

clear()
print("Делопроизводство версия 0.1")
print("введите 'h' что бы получить список всех доступных команд\n")

while True:
  command = input('введите команду: ')

  if command in ['h', 'p', 's', 'l', 'a', 'd', 'm', 'as', 'x']:

    if command == 'h': show_commands()
    
    elif command == 'p': print(show_people(), '\n')
    elif command == 's': print(show_shelf(), '\n')
    elif command == 'l': show_documents_list()
    elif command == 'a': add_record()
    elif command == 'd': delete_record()
    elif command == 'm': change_shelf()
    elif command == 'as': add_shelf()

    elif command == 'x': break

  else:
    clear()
    print('введена несуществующая команда')
    print("введите 'h' что бы получить список всех доступных команд\n")
