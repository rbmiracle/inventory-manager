from csvhandler import CSVHandler
from product import Product
from arraybag import ArrayBag
from tkinter import *


class FileView(object):

    # Constructor
    def __init__(self):
        """jump table for commands, initialize file_contents dictionary, run get_file() method"""
        # instantiate handler, including name of CSV file to use
        filename = "InventoryData.csv"
        self.handler = CSVHandler(filename)

        # initial sort of CSV file by product ID
        self.handler.sort_by_product_id()

        # define user methods
        self.methods = {}
        self.methods["1"] = self.print_file
        self.methods["2"] = self.print_product
        self.methods["3"] = self.add_product
        self.methods["4"] = self.remove_product
        self.methods["5"] = self.update_product
        self.methods["Q"] = self.quit

        # unprinted method for testing - printInventory
        self.methods["p"] = self.printInventory

        # define headers, fill inventory from CSV file
        self.headers, self.inventory = self.handler.read_file()

    # main operations
    def run(self):
        """prompt user for action they want to take, direct flow of traffic"""
        # prompt user for method to call
        while True:
            print("------------------------")
            print("1: Print Inventory")
            print("2: Print Single Product")
            print("3. Add a Product")
            print("4. Remove a Product")
            print("5. Update a Product")
            print("Q. Quit Program")
            selection = input("Choose an action (#): ").upper()
            method_chosen = self.methods.get(selection, None)

            # call necessary method
            if method_chosen is None:
                print("Unrecognized action chosen")
            else:
                method_chosen()
                if self.handler is None:
                    break

    # exit program
    def quit(self):
        exit()

    # initialize (or re-initialize) printable table with headers
    def initialize_table(self):
        self.table_data = [self.headers]

    # append a single line of product data to the printable table
    def append_to_table(self, product_data):
        self.table_data.append(product_data)

    # format a string with two decimals for $$ data
    def format_two_decimals(self, string_input):
        """return a formatted XX.XX string"""
        input_string = "{input:.2f}"
        formatted_string = input_string.format(input=string_input)

        return formatted_string

    # build up a product string for adding to printable table
    def build_product_string(self, id, manufacturer, product, cost, price, stock, sku):
        format_string = "{productID} \t {productManufacturer} \t {productName} \t " \
                        "{productCost:.2f} \t {productPrice:.2f} \t {stockQty} \t {SKU}"
        product_string = format_string.format(productID=id,
                                              productManufacturer=manufacturer,
                                              productName=product,
                                              productCost=cost,
                                              productPrice=price,
                                              stockQty=stock,
                                              SKU=sku)
        return product_string

    # access contents of CSV file
    def get_file(self):
        """use CSVHandler class to get contents of file, store in file_contents dictionary"""
        self.handler.sort_by_product_id()
        self.headers, self.inventory = self.handler.read_file()

    # print contents of inventory (ArrayBag) object
    def printInventory(self):
        inventory = ""
        for item in self.inventory:
            inventory += item
        return inventory

    # returns specific attributes of inventory item
    # Amber - Need this to get info for update display
    def get_item_attribute(self, prod_index, attribute):
        product = self.inventory.items.__getitem__(prod_index)
        if attribute == 0:
            return product.item_id
        if attribute == 1:
            return product.item_manufacturer
        if attribute == 2:
            return product.item_name
        if attribute == 3:
            return self.format_two_decimals(product.item_cost)
        if attribute == 4:
            return self.format_two_decimals(product.item_price)
        if attribute == 5:
            return product.quantity_in_stock
        if attribute == 6:
            return product.item_sku

    # test to see if a product is present in inventory, checking by product_id
    def product_id_in_inventory(self, product_id):
        """Returns boolean of whether product is present in inventory,
        as well as that product's index within the ArrayBag object"""
        # refresh inventory from CSV file
        self.get_file()

        # initialize product_in_inventory variable to False, product_id_list to empty list, bag_index to 0
        product_in_inventory = False
        product_id_list = []
        bag_index = 0

        # iterate over products present in inventory, building up list of product_id values
        for product in self.inventory:
            product_id_list.append(product.item_id)

        # if specified product_id is in product_id_list, set boolean to True and bag_index to relevant index
        if product_id in product_id_list:
            bag_index = product_id_list.index(product_id)
            product_in_inventory = True

        return product_in_inventory, bag_index

    # print contents of entire file
    def print_file(self):
        # Implemented
        """refresh the file using get_file() method, iterate over file_contents to print"""
        # get (refresh) file contents, re-initialize data table
        self.get_file()
        self.initialize_table()
        print()
        print("Inventory:")

        # iterate over products in inventory
        # sort data elements into a printable table line list
        # append data to table for printing
        for product in self.inventory:
            table_line = [product.item_id,
                          product.item_manufacturer,
                          product.item_name,
                          self.format_two_decimals(product.item_cost),
                          self.format_two_decimals(product.item_price),
                          product.quantity_in_stock,
                          product.item_sku]
            self.table_data.append(table_line)

        # iterate over table data, printing in formatted rows
        to_return = ""
        for row in self.table_data:
            print("{:^12} {:^12} {:^15} {:^12} {:^14} {:^18} {:^12}".format(*row))
            to_return += "{:^12} {:^12} {:^15} {:^12} {:^14} {:^18} {:^12}".format(*row) +"\n"
        return to_return

    # print a single line from file
    def print_line(self, product_id):
        #Implemented
        """prints a single line from file based on passed-in product_id"""
        self.get_file()
        self.initialize_table()

        # if the id_selection is valid, pull the contents at that bag index to a Product
        # compile a printable table line
        # append that table line to the re-initialized table and print
        product_id_in_inventory, bag_index = self.product_id_in_inventory(product_id)
        if product_id_in_inventory:
            product = self.inventory.items.__getitem__(bag_index)
            table_line = [product.item_id,
                          product.item_manufacturer,
                          product.item_name,
                          self.format_two_decimals(product.item_cost),
                          self.format_two_decimals(product.item_price),
                          product.quantity_in_stock,
                          product.item_sku]
            self.table_data.append(table_line)
            to_return = ""
            for row in self.table_data:
                print("{:^12} {:^12} {:^15} {:^12} {:^14} {:^18} {:^12}".format(*row))
                to_return +="{:^12} {:^12} {:^15} {:^12} {:^14} {:^18} {:^12}".format(*row)

            return to_return
        else:
            print("No product with selected ID.")
        print()
        return ("No product with selected ID.")

    # get product ID for printing single product, pass along to _print_line()
    def print_product(self, id_selection=-1):
        #Implemented
        """prompt user for product ID, access file_contents at that key if it is in file, pass id to print_line()"""
        # re-initialize table and get (refresh) file contents
        # self.initialize_table()
        # self.get_file()
        # print()

        # get user input for which product ID to view
        # id_selection = input("Which product (ID) would you like to view? ")
        # print()

        # if id_selection is valid, print its details
        product_id_in_inventory, bag_index = self.product_id_in_inventory(id_selection)
        if product_id_in_inventory:
            print("Product Details:")
            return (self.print_line(id_selection))
        else:
            return( ">>> NO PRODUCT WITH SELECTED ID <<<")
            # self.print_file()
            # print(">>> NO PRODUCT WITH SELECTED ID <<<")
        print()

    # add a Product to the file
    def add_product(self,product_manufacturer="Default", product_name="Default",
                     product_cost=-1.00, product_price=-1.00, quantity_in_stock=-1,product_sku="000000000"):
        # Implemented
        """prompt user for product data, create Product, send that Product to CSVHandler for adding"""
        # re-initialize table and get (refresh/sort) file contents
        self.get_file()
        self.initialize_table()
        print()

        # get last Product ID in file, increment to create next Product ID
        product_id = 0
        for product in self.inventory:
            product_id = int(product.item_id)
        product_id += 1

        # print new ID to terminal, prompt user for product data entry
        print("New Product ID: ", product_id)
        # product_manufacturer = input("Product Manufacturer: ")
        # product_name = input("Product Name: ")
        # product_cost = input("Product Cost: ")
        # product_price = input("Product Price: ")
        # quantity_in_stock = input("Quantity in Stock: ")
        # product_sku = str(input("Product SKU: "))

        # create a new Product from input data, add that new Product to inventory bag
        product_to_add = Product(product_id, product_manufacturer, product_name, product_cost, product_price,
                                 quantity_in_stock, product_sku)
        self.inventory.add(product_to_add)

        # push updated inventory to CSVHandler
        self.handler.update_file_from_inventory(self.headers, self.inventory)

        # print verification
        print()
        print("Product Added:")
        self.print_line(str(product_id))
        return(self.print_line(str(product_id)))

    # remove a Product from CSV file based on Product ID or name
    def remove_product(self, id_selection):
        """get (refresh) file, get user input for product ID to remove, send that product to CSVHandler for removal"""
        # refresh CSV file, set handler
        self.get_file()
        print()

        # initialize product_id_in_inventory to False to open the while loop
        product_id_in_inventory = False

        # use while loop to get a product ID that is in inventory
        while not product_id_in_inventory:
            # id_selection = input("Which product (ID) would you like to remove? ")
            product_id_in_inventory, bag_index = self.product_id_in_inventory(id_selection)
            # print("Selected ID not in Inventory.")
            print()
            
        # Added Code on 12/8/2020 - Amber
        if not product_id_in_inventory:
            return ("Item not in Inventory")

        # print verification of selected product_id
        print()
        print("Product Removed:")
        self.print_line(id_selection)
        to_return = self.print_line(id_selection)
        # remove product at bag_index from inventory, push updated inventory to CSVHandler
        self.inventory.remove(self.inventory.items.__getitem__(bag_index))
        self.handler.update_file_from_inventory(self.headers, self.inventory)
        return to_return
        


    def update_product(self, id_selection, new_id, new_manufacturer, new_name, new_cost, new_price,
                        new_quantity_in_stock, new_sku):
        """get (refresh) file, get user input for product ID to update,
        get new updated details, send both to CSVHandler for updating"""
        # refresh CSV file, set handler
        self.get_file()
        print()

        # initialize product_id_in_inventory to False to open the while loop
        # product_id_in_inventory = False

        # use while loop to get a product ID that is in file_contents keys
        # while not product_id_in_inventory:
            # id_selection = input("Which product (ID) would you like to update? ")
            # product_id_in_inventory, bag_index = self.product_id_in_inventory(id_selection)
            # print("Selected ID not in Inventory.")
            # print()
        if(self.product_id_in_inventory(id_selection)):
        # get COPY of selected product from inventory
        # NOTE: ONLY FOR SEEING PRE-UPDATE PRODUCT INFO
        # DO NOT PASS THIS PRODUCT FOR REMOVAL FROM INVENTORY
            product_id_in_inventory, bag_index = self.product_id_in_inventory(id_selection)
            product = self.inventory.items.__getitem__(bag_index)
            print()
            print("Product to Update:")
            self.print_line(product.item_id)
            print()

            # prompt user for product data entry (new values for product info)
            # new_id = input("Product ID: {} >> ".format(product.item_id))
            # new_manufacturer = input("Product Manufacturer: {} >> ".format(product.item_manufacturer))
            # new_name = input("Product Name: {} >> ".format(product.item_name))
            # new_cost = input("Product Cost: {} >> ".format(product.item_cost))
            # new_price = input("Product Price: {} >> ".format(product.item_price))
            # new_quantity_in_stock = input("Quantity in Stock: {} >> ".format(product.quantity_in_stock))
            # new_sku = str(input("Product SKU: {} >> ".format(product.item_sku)))
            updated_product = Product(new_id, new_manufacturer, new_name, new_cost, new_price,
                                     new_quantity_in_stock, new_sku)

            # remove product at selected bag_index from inventory
            self.inventory.remove(self.inventory.items.__getitem__(bag_index))

            # add updated product to inventory
            self.inventory.add(updated_product)

            # update/sort CSV File
            self.handler.update_file_from_inventory(self.headers, self.inventory)

            # print verification
            print()
            print("Updated Product: ")
            self.print_line(updated_product.item_id)
            print()
            return str(self.print_line(updated_product.item_id))
        else:
            return ("Item not in Inventory")


# run main
if __name__ == "__main__":
    FileView().run()
