
from Invoice import Invoice

if __name__ == '__main__':
    i1 = Invoice(1, "Cement", 3, 100)
    print("Invoice 1 amount : " + str(i1.get_invoice_price())) # 300

    i2 = Invoice(1, "Bricks", -5, 100)
    print("Invoice 2 amount : " + str(i2.get_invoice_price()))  # amount should be 0  because quantity is negative

    i3 = Invoice(1, "Bolts and Nuts", 8, -100)
    print("Invoice 3 amount : " + str(i3.get_invoice_price())) # amount should be 0  because price per item is negative

