from database_classes import StorageSystem, StorageSystemException

storage_reader = StorageSystem()

while True:
    username = input("What is your username? ")
    password = input("What is your password? ")
    try:
        print(storage_reader.get_by_username_pw(username, password))
    except StorageSystemException:
        print(storage.)