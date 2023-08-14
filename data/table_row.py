import re


class TableRow:

    def __init__(self, website, popularity, front_end, back_end, database, notes):
        self.__website = re.sub(r'[0-9]|[\[\]]', '', website)
        self.__popularity = int(re.sub(r'[^\w\s]', '', popularity.split(" ")[0]))
        self.__front_end = re.sub(r'[0-9]|[\[\]]', '', front_end)
        self.__back_end = re.sub(r'[0-9]|[\[\]]', '', back_end)
        self.__database = re.sub(r'[0-9]|[\[\]]', '', database)
        self.__notes = re.sub(r'[0-9]|[\[\]]', '', notes)

    def get_website(self):
        return self.__website

    def get_popularity(self):
        return self.__popularity

    def get_front_end(self):
        return self.__front_end

    def get_back_end(self):
        return self.__back_end

    def get_database(self):
        return self.__database

    def get_notes(self):
        return self.__notes
