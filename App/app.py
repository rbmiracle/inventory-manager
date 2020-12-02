from tkinter import *
from fileview import FileView


root = Tk(className=' CSC 130 Group Project- Inventory System')
root.geometry("1024x768")
frmMain = Frame(root, bd=1, relief=GROOVE)

OPTIONS = ["Inventory Number", "Manufacturer", "Price", "Count"]


# Clears the text box and displays what is in text
def setTextInput(text):
    clearTextBox()
    main_text.insert("1.0", text)


# Clears the text box
def clearTextBox():
    main_text.delete("1.0", "end")


# Appends what is in text to what is currently in the text box
def appendTextInput(text):
    main_text.insert(END, (text + "\n"))


# Clears the text box and then reads in the help file and displays it
def displayHelp():
    clearTextBox()
    file = open("help.txt")
    line = file.read()
    file.close()
    setTextInput(line)


def displayProduct(prod_id):
    product = "Product Details:\n"+FV.print_product(id_selection=prod_id)
    appendTextInput(product)


def updateProduct(prod_id):
    is_found, prod_index = FV.product_id_in_inventory(prod_id)
    if is_found:
        update_window = Toplevel(root)
        update_window.title("Update Product")
        update_window.geometry("400x350+512+512")
        label_update = Label(update_window, text="Enter new information for %s" % FV.get_item_attribute(prod_index, 0))
        label_update.pack(pady=10)

        frame_display = Frame(update_window, bd=1, relief=GROOVE)
        id_string = StringVar(value=FV.get_item_attribute(prod_index, 0))
        man_string = StringVar(value=FV.get_item_attribute(prod_index, 1))
        name_string = StringVar(value=FV.get_item_attribute(prod_index, 2))
        cost_string = StringVar(value=FV.get_item_attribute(prod_index, 3))
        price_string = StringVar(value=FV.get_item_attribute(prod_index, 4))
        quantity_string = StringVar(value=FV.get_item_attribute(prod_index, 5))
        sku_string = StringVar(value=FV.get_item_attribute(prod_index, 6))
        # Input for ID
        label_id = Label(frame_display, text="ItemID: ")
        entry_id = Entry(frame_display, textvariable=id_string)
        # Input for Manufacturer
        label_man = Label(frame_display, text="Manufacturer: ")
        entry_man = Entry(frame_display, textvariable=man_string)
        # Input for Name
        label_name = Label(frame_display, text="Name: ")
        entry_name = Entry(frame_display, textvariable=name_string)
        # Input for Cost
        label_cost = Label(frame_display, text="Cost: ")
        entry_cost = Entry(frame_display, textvariable=cost_string)
        # Input for Price
        label_price = Label(frame_display, text="Price: ")
        entry_price = Entry(frame_display, textvariable=price_string)
        # Input for Quantity
        label_quantity = Label(frame_display, text="Quantity: ")
        entry_quantity = Entry(frame_display, textvariable=quantity_string)
        # Input for SKU
        label_sku = Label(frame_display, text="SKU: ")
        entry_sku = Entry(frame_display, textvariable=sku_string)

        button_display = Button(frame_display, text="Update Product", command=lambda: [submitUpdate(
            prod_id, id_string.get(), man_string.get(), name_string.get(), cost_string.get(), price_string.get(),
            quantity_string.get(), sku_string.get()), update_window.destroy()])
        # Adding all the GUI to grid
        label_id.grid(row=0, column=0)
        entry_id.grid(row=0, column=1)
        label_man.grid(row=1, column=0)
        entry_man.grid(row=1, column=1)
        label_name.grid(row=2, column=0)
        entry_name.grid(row=2, column=1)
        label_cost.grid(row=3, column=0)
        entry_cost.grid(row=3, column=1)
        label_price.grid(row=4, column=0)
        entry_price.grid(row=4, column=1)
        label_quantity.grid(row=5, column=0)
        entry_quantity.grid(row=5, column=1)
        label_sku.grid(row=6, column=0)
        entry_sku.grid(row=6, column=1)
        button_display.grid(row=7, columnspan=2, pady=10)

        frame_display.pack()
    else:
        appendTextInput(prod_id + " does not exist.")


def submitUpdate(id_selection, new_id, new_manufacturer, new_name, new_cost, new_price,
                 new_quantity_in_stock, new_sku):
    to_print = "Updated Product: \n" + FV.update_product(id_selection, new_id, new_manufacturer, new_name,
                                                          new_cost, new_price, new_quantity_in_stock, new_sku)
    appendTextInput(to_print)


def submitProduct(product_manufacturer="Default", product_name="Default",
                  product_cost=-1.00, product_price=-1.00, quantity_in_stock=-1, product_sku="000000000"):
    new_item = "Product Added:\n" + FV.add_product(product_manufacturer, product_name, product_cost, product_price,
                                                    quantity_in_stock, product_sku)
    appendTextInput(new_item)


def addProduct():
    add_window = Toplevel(root)
    add_window.title("Add a New Product")
    add_window.geometry("400x320+512+512")
    label_add = Label(add_window, text="Enter information to add item to inventory")
    label_add.pack(pady=10)

    frame_display = Frame(add_window, bd=1, relief=GROOVE)
    man_string = StringVar()
    name_string = StringVar()
    cost_string = StringVar()
    price_string = StringVar()
    quantity_string = StringVar()
    sku_string = StringVar()
    # Input for Manufacturer
    label_man = Label(frame_display, text="Manufacturer: ")
    entry_man = Entry(frame_display, textvariable=man_string)
    # Input for Name
    label_name = Label(frame_display, text="Name: ")
    entry_name = Entry(frame_display, textvariable=name_string)
    # Input for Cost
    label_cost = Label(frame_display, text="Cost: ")
    entry_cost = Entry(frame_display, textvariable=cost_string)
    # Input for Price
    label_price = Label(frame_display, text="Price: ")
    entry_price = Entry(frame_display, textvariable=price_string)
    # Input for Quantity
    label_quantity = Label(frame_display, text="Quantity: ")
    entry_quantity = Entry(frame_display, textvariable=quantity_string)
    # Input for SKU
    label_sku = Label(frame_display, text="SKU: ")
    entry_sku = Entry(frame_display, textvariable=sku_string)

    button_display = Button(frame_display, text="Add Product",
                            command=lambda: [submitProduct(man_string.get(), name_string.get(), cost_string.get(),
                                                           price_string.get(), quantity_string.get(), sku_string.get()),
                                             add_window.destroy()])
    # Adding all the GUI to grid
    label_man.grid(row=0, column=0)
    entry_man.grid(row=0, column=1)
    label_name.grid(row=1, column=0)
    entry_name.grid(row=1, column=1)
    label_cost.grid(row=2, column=0)
    entry_cost.grid(row=2, column=1)
    label_price.grid(row=3, column=0)
    entry_price.grid(row=3, column=1)
    label_quantity.grid(row=4, column=0)
    entry_quantity.grid(row=4, column=1)
    label_sku.grid(row=5, column=0)
    entry_sku.grid(row=5, column=1)
    button_display.grid(row=6, columnspan=2, pady=10)

    frame_display.pack()


def deleteProduct(prod_id):
    to_print = "Product Removed:\n" + FV.remove_product(prod_id)
    appendTextInput(to_print)


def displayInventory():
    inventory = "Inventory:\n" + FV.print_file()
    setTextInput(inventory)
    print(inventory)


# Handles the product editor window
def open_prod_window():
    prod_window = Toplevel(root)
    prod_window.title("Product Edit")
    prod_window.geometry("512x512+300+512")
    frame_product = Frame(prod_window)
    frame_product.columnconfigure(0, minsize=100)

    entry_string = StringVar()
    frame_display = Frame(frame_product, bd=1, relief=GROOVE)
    label_display = Label(frame_display, text="Enter product ID to Display")
    entry_display = Entry(frame_display, textvariable=entry_string)
    button_display = Button(frame_display, text="Display Product", command=lambda: displayProduct(entry_string.get()))
    label_display.grid(row=0, column=0, pady=10, padx=10)
    entry_display.grid(row=1, column=0, pady=10)
    button_display.grid(row=2, column=0, pady=10)
    frame_display.columnconfigure(0, minsize=250)
    frame_display.rowconfigure(0, minsize=60)
    frame_display.rowconfigure(1, minsize=60)
    frame_display.rowconfigure(2, minsize=60)
    frame_display.grid(row=0, column=0)

    update_string = StringVar()
    frame_update = Frame(frame_product, bd=1, relief=GROOVE)
    label_update = Label(frame_update, text="Enter product ID to Update")
    entry_update = Entry(frame_update, textvariable=update_string)
    button_update = Button(frame_update, text="Update Product", command=lambda: updateProduct(update_string.get()))
    label_update.grid(row=0, column=0, pady=10, padx=10)
    entry_update.grid(row=1, column=0, pady=10)
    button_update.grid(row=2, column=0, pady=10)
    frame_update.columnconfigure(0, minsize=250)
    frame_update.rowconfigure(0, minsize=60)
    frame_update.rowconfigure(1, minsize=60)
    frame_update.rowconfigure(2, minsize=60)
    frame_update.grid(row=0, column=1)

    frame_add = Frame(frame_product, bd=1, relief=GROOVE)
    label_add = Label(frame_add, text="Open Window to Add")
    button_add = Button(frame_add, text="Add New Product", command=lambda: addProduct())
    label_add.grid(row=0, column=0)
    button_add.grid(row=1, column=0)
    frame_add.columnconfigure(0, minsize=250)
    frame_add.rowconfigure(0, minsize=92)
    frame_add.rowconfigure(1, minsize=92)
    frame_add.grid(row=1, column=0)

    delete_string = StringVar()
    frame_delete = Frame(frame_product, bd=1, relief=GROOVE)
    label_delete = Label(frame_delete, text="Enter product ID to Delete")
    entry_delete = Entry(frame_delete, textvariable=delete_string)
    button_delete = Button(frame_delete, text="Delete Product", command=lambda: deleteProduct(delete_string.get()))
    label_delete.grid(row=0, column=0, pady=10, padx=10)
    entry_delete.grid(row=1, column=0, pady=10)
    button_delete.grid(row=2, column=0, pady=10)
    frame_delete.columnconfigure(0, minsize=250)
    frame_delete.rowconfigure(0, minsize=60)
    frame_delete.rowconfigure(1, minsize=60)
    frame_delete.rowconfigure(2, minsize=60)
    frame_delete.grid(row=1, column=1)

    frame_product.pack(expand=True)

    prod_bottom_frame = Frame(prod_window)
    prod_my_quit = Button(prod_bottom_frame, text="Close Window", command=prod_window.destroy)
    prod_my_quit.pack(side=RIGHT)
    prod_bottom_frame.pack(side=BOTTOM, fill=X, padx=10, pady=10)


# Below this is where the GUI is built
# Title of the program at the top
main_label = Label(frmMain, text="Inventory Management System", font=('Arial', 24, 'bold'))
main_label.grid(row=0, columnspan=2, pady=10)

# Text box that displays all the information
main_text = Text(frmMain, font=('Courier', 12), width=105, height=30, relief="sunken", bg="white")
main_text.grid(row=1, columnspan=2)
displayHelp()

# Inventory button
button_inv = Button(frmMain, text="Inventory", command=lambda: displayInventory())
button_inv.grid(row=2, sticky=W, pady=10, padx=10)

# Product button
button_prod = Button(frmMain, text="Product", command=lambda: open_prod_window())
button_prod.grid(row=2, column=1, sticky=W, pady=10, padx=10)

frmMain.grid_columnconfigure(1, weight=1)
frmMain.pack(fill=Y, padx=5, pady=10)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Frame that holds the bottom 3 buttons
bottom_frame = Frame(root)
clear = Button(bottom_frame, text="Clear", command=lambda: clearTextBox())
my_help = Button(bottom_frame, text="Help", command=lambda: displayHelp())
my_quit = Button(bottom_frame, text="QUIT", command=root.destroy)
my_quit.pack(side=RIGHT)
my_help.pack(side=RIGHT, padx=10)
clear.pack(side=RIGHT)

bottom_frame.pack(side=BOTTOM, fill=X, padx=10, pady=10)

# This runs the actual App
FV = FileView()
root.mainloop()
