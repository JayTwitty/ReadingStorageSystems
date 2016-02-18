from database_classes import StorageSystem, StorageSystemException

storage_reader = StorageSystem()

system = True
while system:
    username = input("What is your username? ")
    password = input("What is your password? ")
    print(storage_reader.get_by_username_pw(username, password))
    if storage_reader.get_by_username_pw(username, password) != None:
        continue
    else:
        system = False
