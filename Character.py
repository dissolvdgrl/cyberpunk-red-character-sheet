class Character:
    def __init__(self):
        self.__handle = ""
        self.__role = ""
        self.__role_ability = ""
        self.__photo = ""

    def get_handle(self):
        return self.__handle

    def set_handle(self, handle):
        self.__handle = handle

    def get_role(self):
        return self.__role

    def set_role(self, role):
        self.__role = role


