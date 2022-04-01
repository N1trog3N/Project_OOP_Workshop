class Device:

    def __init__(self, type, brand, description):
        self._type = type
        self._brand = brand
        self._description = description

    def __str__(self):
        return f"Device: {self._type}, Brand: {self._brand}, Description: {self._description}"


class Phone(Device):

    def __init__(self, type, brand, os, description):
        super(Phone, self).__init__(type, brand, description)
        self._os = os

    def __str__(self):
        return f"{self._type}\n{super().__str__()}, OS: {self._os}"


class Notebook(Device):

    def __init__(self, type, brand, os, dateofmanufacturing, description):
        super(Notebook, self).__init__(type, brand, description)
        self._dateOfManufacturing = dateofmanufacturing
        self._os = os

    def __str__(self):
        return f"{self._type}\n{super().__str__()}, OS: {self._os}, Date of manufacturing: {self._dateOfManufacturing}"


class TV(Device):

    def __init__(self, type, brand, diagonal, description):
        super(TV, self).__init__(type, brand, description)
        self._diagonal = diagonal

    def __str__(self):
        return f"{self._type}\n{super().__str__()}, Diagonal: {self._diagonal}"
