DATA_FILE = "data.txt"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return file.readlines()
    except:
        return []

def save_data(data):
    with open(DATA_FILE, "w") as file:
        file.writelines(data)
