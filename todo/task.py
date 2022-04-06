from json import JSONEncoder


class Task:
    def __init__(self, id, content="", done=False):
        self.id = id
        self.content = content
        self.done = done

    def __eq__(self, other):
        return self.id == other.id

    @staticmethod
    def from_json(json_dct):
        return Task(json_dct["id"], json_dct["content"], json_dct["done"])


class TaskEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
