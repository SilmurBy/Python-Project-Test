class Table:
    __table_tuple: tuple

    def __init__(self, outer_tuple):
        self.__table_tuple = outer_tuple

    def get_table(self):
        return self.__table_tuple
