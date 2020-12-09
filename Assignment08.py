# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# <Lauren Parker>,<12.6.20>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
str_file_name = "products.txt"
list_of_products = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Lauren Parker>,<12.6.20>,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to the Product class
    def __init__(self, product_name:str, product_price:float):
        """Set name and price of a new object"""
        # Attributes
        try:
            self.__product_name = str(product_name)
            self.__product_price = float(product_price)
        except Exception as e:
            raise Exception("Error setting initial values:\n" +str(e))

    # Properties
    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value:str):
        if str(value).isnumeric():
            self.__product_name = value
        else:
            raise Exception("Error: Please do not use numbers when entering names!")

    # Product price
    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value:float):
        if str(value).isnumeric():
            self.__product_price = float(value)
        else:
            raise Exception("Error: Please only use numbers for price!")

    # Methods
    def to_string(self):
        """alias of __str__(), converts product data to string """
        return self.__str__()

    def __str__(self):
        """Converts product data to string"""
        return self.product_name + "," + str(self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Lauren Parker>,<12.6.20>,Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name: str, list_of_product_objects: list):
        """Write data to a file from a list

        :param file_name: (string) name of file
        :param list_of_product_objects: (list) of product objects
        :return: (bool) with status of success
        """
        success_status = False
        try:
            file = open(file_name, "w")
            for product in list_of_product_objects:
                file.write(product.__str__() + "\n")
            file.close()
            success_status = True
            print("Your file has been saved!")
        except Exception as e:
            print("There was an error!")
            print(e, e.__doc__, type(e), sep="\n")
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):
        """Reads data from a file into a list of product rows

        :param file_name: (string) with name of file
        :return: (list) of product rows
        """
        list_of_product_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                row = Product(data[0], data[1])
                list_of_product_rows.append(row)
            file.close()
        except Exception as e:
            print("There was an error!")
            print(e,e.__doc__, type(e), sep="\n")
        return list_of_product_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Performs input and output tasks"""

    @staticmethod
    def print_menu_items():
        """Display a menu of choices to the user

        :return: nothing"""
        print("""
        ************************
        Please choose and option:
        ************************
                                                                                            
        1) Show current data                                                                         
        2) Add data to list                                                                          
        3) Save your data to a file                                                                  
        4) Exit                                                                                      
        """)
        print()  # Blank line for appearance

    @staticmethod
    def input_menu_choice():
        """Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Blank line for appearance
        return choice

    @staticmethod
    def print_current_list_items(list_of_rows: list):
        """Print the current items in the list

        :param list_of_rows: (list) of rows of data
        """
        print("Your current items are as follows:")
        for row in list_of_rows:
            print(row.product_name + "," + str(row.product_price))
        print("----------------------------")
        print()  # Blank line for appearance

    def input_product_data():
        """Gets product and price from user
        """
        try:
            name = str(input("Please enter a product: ").strip())
            price = float(input("Please enter the estimated price of the item: ").strip())
            print()
            p = Product(product_name=name, product_price=price)
        except Exception as e:
            print(e)
        return p

    # Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
try:
    list_of_products = FileProcessor.read_data_from_file(str_file_name)

    while True:
        IO.print_menu_items()
        str_choice = IO.input_menu_choice()
        if str_choice.strip() == '1':
            IO.print_current_list_items(list_of_products)
            continue
        elif str_choice.strip() == '2':
            list_of_products.append(IO.input_product_data())
            continue
        elif str_choice.strip() == "3":
            FileProcessor.save_data_to_file(str_file_name, list_of_products)
            continue
        elif str_choice.strip() == "4":
            print("See ya later, alligator!")
            break
except Exception as e:
    print("There was an error!")
    print(e, e.__doc__, type(e), sep = "\n")


# Main Body of Script  ---------------------------------------------------- #


