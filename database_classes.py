class StorageSystemException(Exception):
    pass

class StorageSystem:

    def __init__(self, file_contents=[]):
        if not file_contents:
            file_contents = self.read_file()
            self.clean_file = [line.split(",") for line in file_contents]
        self.cleaned_data = self.clean_file

    def read_file(self):
        with open("database_storage") as infile:
            data = infile.readlines()
        return data

    def get_by_username_pw(self, name, pw):
        results = []
        # results = [line for line in self.cleaned_data if line[0].lower() == name.lower() and line[1].lower() == pw.lower()]
        for line in self.cleaned_data:
            if line[0].lower() == name.lower() and line[1].lower() == pw.lower():
                results.append(line)
                return results
            elif line[0].lower() == name.lower() and line[1].lower() != pw.lower():
                print("Your password is incorrect. Please try again")
                break
            else:
                print("Your username and password was not found. Please try again")

    def add_to_file(self):
        with open("database_storage", "a") as outfile:
            outfile.write("yo lol")


