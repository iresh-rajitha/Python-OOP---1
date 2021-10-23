class Invoice:

    def __init__(self, part_id, description, quantity_of_item, price_per_item):
        self.__part_id = part_id
        self.__description = description
        self.__quantity_of_item = quantity_of_item
        self.__price_per_item = price_per_item

    def get_part_id(self):
        return self.__part_id

    def get_description(self):
        return self.__description

    def get_quantity_of_item(self):
        return self.__quantity_of_item

    def get_price_per_item(self):
        return self.__price_per_item

    def set_part_id(self, part_id):
        self.__part_id = part_id

    def set_description(self, description):
        self.__description = description

    def set_quantity_of_item(self, quantity_of_item):
        self.__quantity_of_item = quantity_of_item

    def set_price_per_item(self, price_per_item):
        self.__price_per_item = price_per_item;

    def get_invoice_price(self):
        if self.__quantity_of_item < 0:
            self.__quantity_of_item = 0
        if self.__price_per_item < 0:
            self.__price_per_item = 0

        return self.__quantity_of_item * self.__price_per_item
