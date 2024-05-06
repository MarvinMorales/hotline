import json
import os


class Load_Copies(object):
    def __init__(self):
        self.data = self.load_copies()

    def load_copies(self):
        joined_path = os.path.join(os.getcwd(), "app", "data", "data_copies.json")
        with open(joined_path, "r") as file:
            return json.load(file)
