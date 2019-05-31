import pickle, os


class PickleDb(object):
    def __init__(self, content, db_path):
        self.content = content
        self.db_path = db_path

    def save(self):
        pickle.dump(self.content, open(self.db_path, 'wb'))

    def select(self):
        return pickle.load(open(self.db_path, 'rb'))

