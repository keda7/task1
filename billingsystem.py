import tkinter as tk
from tkinter import ttk
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.invoices = []
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        
        tk.Label(self, text="Invoice System", font=('Helvetica', 18, 'bold'), bg="#ffffff").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Create Invoice",
                  command=lambda: master.switch_frame(CreateInvoicePage)).pack(pady=10)
        tk.Button(self, text="View Invoices",
                  command=lambda: master.switch_frame(ViewInvoicesPage)).pack(pady=10)


class CreateInvoicePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Create Invoice", font=('Helvetica', 18, 'bold')).pack(side="top", fill="x", pady=10)
        self.customer_name = tk.StringVar()
        self.customer_address = tk.StringVar()
        self.product_name = tk.StringVar()
        self.price = tk.StringVar()
        tk.Label(self, text="Customer Name").pack()
        tk.Entry(self, textvariable=self.customer_name).pack()
        tk.Label(self, text="Customer Address").pack()
        tk.Entry(self, textvariable=self.customer_address).pack()
        tk.Label(self, text="Product Name").pack()
        tk.Entry(self, textvariable=self.product_name).pack()
        tk.Label(self, text="Price").pack()
        tk.Entry(self, textvariable=self.price).pack()
        tk.Button(self, text="Add Product",
                  command=self.add_product).pack()
        list_frame = tk.Frame(self)
        list_frame.pack(padx=10, pady=10)
        self.product_list = tk.Text(list_frame, width=40, height=20)
        self.product_list.pack(side=tk.LEFT)
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.product_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.product_list.yview)
        tk.Button(self, text="Create Invoice",
                  command=lambda: self.create_invoice(master)).pack()

    def add_product(self):
        customer_name = self.customer_name.get()
        customer_address = self.customer_address.get()
        product_name = self.product_name.get()
        price = self.price.get()
        self.product_list.insert(tk.END, "Customer Name: " + customer_name + "\n")
        self.product_list.insert(tk.END, "Customer Address: " + customer_address + "\n")
        self.product_list.insert(tk.END, product_name + " - " + price + "\n\n")
        self.customer_name.set("")
        self.customer_address.set("")
        self.product_name.set("")
        self.price.set("")

    def create_invoice(self, master):
        invoice = self.product_list.get("1.0", tk.END)
        master.invoices.append(invoice)
        master.switch_frame(StartPage)

class ViewInvoicesPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="View Invoices", font=('Helvetica', 18, 'bold')).pack(side="top", fill="x", pady=10)
        self.invoice_list_frame = tk.Frame(self)
        self.invoice_list_frame.pack(padx=10, pady=10)
        self.invoice_list = tk.Text(self.invoice_list_frame, width=40, height=20)
        self.invoice_list.pack(side=tk.LEFT)
        scrollbar = tk.Scrollbar(self.invoice_list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.invoice_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.invoice_list.yview)
        for invoice in master.invoices:
            self.invoice_list.insert(tk.END, invoice + "\n\n")
        tk.Button(self, text="Back",
                  command=lambda: master.switch_frame(StartPage)).pack(pady=10)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
