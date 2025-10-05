import tkinter.messagebox
import customtkinter as ctk
import tkinter
from tkinter import ttk
import database

class app(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Bank Management System")
        self.geometry("1350x725")
        self.resizable(0, 0)
        self.grid_columnconfigure(index = 0,weight = 1)
        ctk.set_default_color_theme("green")

        self.selected_account = None
        self.selected_data = []

        self.home_page()

        style = ttk.Style()
        self.tk.call('source', 'forest-dark.tcl')
        style.theme_use('forest-dark')
        style.configure('Treeview', font = ('', 18), rowheight = 50 )
        style.configure("Treeview.Heading", font=(None, 20, 'bold'))

    def home_page(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        label = ctk.CTkLabel(self, text = "VNIT BANK", font = ("Comic Sans MS", 180, 'bold'))
        label.grid(row = 0, column = 0, sticky = 'news', pady = 100)

        btn1 = ctk.CTkButton(self, text = "LOGIN PAGE", font = ("", 40, "bold"), width = 350, command = self.employee_login_page)
        btn1.place(x = 500, y = 450)
       

    def employee_login_page(self):
        self.clear_frame()

        frame = ctk.CTkFrame(self, fg_color = 'transparent')
        frame.grid(row = 1, column = 0, pady = (130, 50))

        frame1 = ctk.CTkFrame(frame, fg_color = 'transparent')
        frame1.grid(row = 0, column = 0)

        frame2 = ctk.CTkFrame(frame, fg_color = 'transparent')
        frame2.grid(row = 0, column = 1)

        ctk.CTkLabel(frame1, text = "EMPLOYEE USER ID", font = ("", 30, 'bold'), justify = 'left', anchor="w", width = 300).grid(row = 0, column = 0, pady = 20, padx = 20)
        ctk.CTkLabel(frame1, text = "PASSWORD", font = ("", 30, 'bold'), justify = 'left', anchor="w", width = 300).grid(row = 1, column = 0, pady = 20, padx = 20)

        self.entryLogin = ctk.CTkEntry(frame2, placeholder_text="Employee Id", font = ("", 30), width = 350)
        self.entryLogin.grid(row = 0, column = 0, pady = 20, padx = 20)

        self.entryPw = ctk.CTkEntry(frame2, placeholder_text="Password", font = ("", 30), width = 350)
        self.entryPw.grid(row = 1, column = 0, pady = 20, padx = 20)

        button = ctk.CTkButton(self, text = "LOGIN", width = 300, font = ("", 30, 'bold'), command = self.emp_login)
        button.grid(row = 2, column = 0)


    def emp_login(self):
        checked = False
        if self.entryPw.get() == "" or self.entryLogin.get() == "":
            checked = True
            tkinter.messagebox.showerror('ERROR', 'ALL FIELDS REQUIRED')
        if self.entryPw.get() != "vnit" and not checked:
            tkinter.messagebox.showerror('ERROR', 'INVALID USER ID PASSWORD COMBINATION!')
        if self.entryLogin.get() != "vnitbank" and not checked:
            tkinter.messagebox.showerror('ERROR', 'INVALID USER ID PASSWORD COMBINATION!')
        if self.entryPw.get() == "vnit" and self.entryLogin.get() == "vnitbank" and not checked:
            self.emp_option_page()
            
    
    def emp_option_page(self):
        self.clear_frame()

        button1 = ctk.CTkButton(self, text = "MANAGE ACCOUNTS", width = 430, font = ("", 35, 'bold'), command=self.main)
        button1.grid(row = 1, column = 0, pady = (150, 0))

        button2 = ctk.CTkButton(self, text = "MAKE A TRANSACTION", width = 430, font = ("", 35, 'bold'), command=self.transaction)
        button2.grid(row = 2, column = 0, pady = 50)

        button2 = ctk.CTkButton(self, text = "BACK", width = 430, font = ("", 35, 'bold'), command=self.employee_login_page, fg_color = "red", hover_color = "#8c0d0d")
        button2.grid(row = 3, column = 0)


    def transaction(self):
        self.clear_frame()

        button1 = ctk.CTkButton(self, text = "WITHDRAW MONEY", width = 400, font = ("", 35, 'bold'), command=self.withdraw_money)
        button1.grid(row = 1, column = 0, pady = (175, 0))

        button2 = ctk.CTkButton(self, text = "DEPOSIT MONEY", width = 400, font = ("", 35, 'bold'), command=self.deposit_money)
        button2.grid(row = 2, column = 0, pady = 30)

        button2 = ctk.CTkButton(self, text = "BACK", width = 400, font = ("", 35, 'bold'), command=self.emp_option_page, fg_color = "red", hover_color = "#8c0d0d")
        button2.grid(row = 3, column = 0)
    
    def withdraw_money(self):
        self.clear_frame()
        frame = ctk.CTkFrame(self, fg_color = 'transparent')
        frame.grid(row = 1, column = 0, pady = (130, 50))

        frame1 = ctk.CTkFrame(frame, fg_color = 'transparent')
        frame1.grid(row = 0, column = 0)

        frame2 = ctk.CTkFrame(frame, fg_color = 'transparent')
        frame2.grid(row = 0, column = 1)

        ctk.CTkLabel(frame1, text = "ACCOUNT NUMBER : ", font = ("", 30, 'bold'), justify = 'left', anchor="w", width = 320).grid(row = 0, column = 0, pady = 20, padx = 20)
        ctk.CTkLabel(frame1, text = "AMOUNT : ", font = ("", 30, 'bold'), justify = 'left', anchor="w", width = 320).grid(row = 1, column = 0, pady = 20, padx = 20)

        self.acc_no = ctk.CTkEntry(frame2, placeholder_text="Account No", font = ("", 30), width = 350)
        self.acc_no.grid(row = 0, column = 0, pady = 20, padx = 20)

        self.amount = ctk.CTkEntry(frame2, placeholder_text="Amount", font = ("", 30), width = 350)
        self.amount.grid(row = 1, column = 0, pady = 20, padx = 20)

        button_frame = ctk.CTkFrame(self, fg_color = "transparent")
        button_frame.grid(row = 2, column = 0, padx = 10, pady = 10)

        button = ctk.CTkButton(button_frame, text = "WITHDRAW", width = 300, font = ("", 30, 'bold'), command = self.withdraw)
        button.grid(row = 0, column = 0, padx = 15)

        back_button = ctk.CTkButton(button_frame, text = "BACK", width = 300, font = ("", 30, 'bold'), command = self.transaction, fg_color = "red", hover_color = "#8c0d0d")
        back_button.grid(row = 0, column = 1, padx = 15)
    
    def withdraw(self):
        acc_no = self.acc_no.get()

        if database.acc_no_exists(acc_no):
            balance = int(database.get_balance(acc_no))
            amount = int(self.amount.get())
            if amount > 9999:
                tkinter.messagebox.showerror("WITHDRAWAL FAILED", 'MAXIMUM WITHDRAWAL LIMIT EXCEEDED!')
            elif amount <= balance:
                balance -= amount
                database.update_balance(acc_no, str(balance))
                tkinter.messagebox.showinfo("Message", "TRANSACTION SUCCESSFUL!")
            else:
                tkinter.messagebox.showerror("WITHDRAWAL FAILED", 'INSUFFICIENT BALANCE!')
        else:
            tkinter.messagebox.showerror("WITHDRAWAL FAILED", 'INVALID ACCOUNT NUMBER!')

        self.amount.delete(0, 'end')
        self.acc_no.delete(0, 'end')

    def deposit(self):
        acc_no = self.acc_no.get()
        if database.acc_no_exists(acc_no):
            balance = int(database.get_balance(acc_no))
            amount = int(self.amount.get())
            balance += amount
            database.update_balance(acc_no, str(balance))
            tkinter.messagebox.showinfo("Message", "TRANSACTION SUCCESSFUL!")
        else:
            tkinter.messagebox.showerror("DEPOSIT FAILED", 'INVALID ACCOUNT NUMBER!')
        self.amount.delete(0, 'end')
        self.acc_no.delete(0, 'end')
    
    def deposit_money(self):
        self.clear_frame()

        frame = ctk.CTkFrame(self, fg_color = 'transparent')
        frame.grid(row = 1, column = 0, pady = (130, 50))

        frame1 = ctk.CTkFrame(frame, fg_color = 'transparent')
        frame1.grid(row = 0, column = 0)

        frame2 = ctk.CTkFrame(frame, fg_color = 'transparent')
        frame2.grid(row = 0, column = 1)

        ctk.CTkLabel(frame1, text = "ACCOUNT NUMBER : ", font = ("", 30, 'bold'), justify = 'left', anchor="w", width = 320).grid(row = 0, column = 0, pady = 20, padx = 20)
        ctk.CTkLabel(frame1, text = "AMOUNT : ", font = ("", 30, 'bold'), justify = 'left', anchor="w", width = 320).grid(row = 1, column = 0, pady = 20, padx = 20)

        self.acc_no = ctk.CTkEntry(frame2, placeholder_text="Account No", font = ("", 30), width = 350)
        self.acc_no.grid(row = 0, column = 0, pady = 20, padx = 20)

        self.amount = ctk.CTkEntry(frame2, placeholder_text="Amount", font = ("", 30), width = 350)
        self.amount.grid(row = 1, column = 0, pady = 20, padx = 20)

        button_frame = ctk.CTkFrame(self, fg_color = "transparent")
        button_frame.grid(row = 2, column = 0, padx = 10, pady = 10)

        button = ctk.CTkButton(button_frame, text = "DEPOSIT", width = 300, font = ("", 30, 'bold'), command = self.deposit)
        button.grid(row = 0, column = 0, padx = 15)

        back_button = ctk.CTkButton(button_frame, text = "BACK", width = 300, font = ("", 30, 'bold'), command = self.transaction, fg_color = "red", hover_color = "#8c0d0d")
        back_button.grid(row = 0, column = 1, padx = 15)

    def fill_data(self):
        values = database.fetch_data()
        for value in values:
            self.tree.insert(parent='', index = 'end', value = value)

    def main(self):
        self.clear_frame()

        frame = ctk.CTkFrame(self)
        frame.grid(row = 1, column = 0, padx = 2, pady = 20, sticky = 'n')

        self.tree = ttk.Treeview(frame, height=10)
        self.tree.grid(row = 0, column = 0)

        self.tree['columns'] = ("id", "name", "account_type", "balance")

        self.tree.heading('id', text = "Account Number")
        self.tree.column("id", anchor = 'center', width=400)

        self.tree.heading('name', text = "Name")
        self.tree.column("name", anchor = 'center', width=400)

        self.tree.heading('account_type', text = "Account Type")
        self.tree.column("account_type", anchor = 'center', width=400)

        self.tree.heading('balance', text = "Balance")
        self.tree.column("balance", anchor = 'center', width=400)

        self.tree.config(show = "headings")

        self.tree.bind('<ButtonRelease-1>', self.selectItem)

        self.fill_data()

        button_frame = ctk.CTkFrame(self, fg_color = "transparent")
        button_frame.grid(row = 2, columnspan = 2, padx = 10, pady = 10)
        
        self.add_btn = ctk.CTkButton(button_frame, text = "ADD", font = ("", 25, "bold"), width = 150, command = self.add_page)
        self.add_btn.grid(row = 0, column = 0, padx = 15, pady = 20)

        self.update_btn = ctk.CTkButton(button_frame, text = "UPDATE DETAILS", font = ("", 25, "bold"), width = 240, command = self.update_page, state='disabled')
        self.update_btn.grid(row = 0, column = 1, padx = 15, pady = 20)

        self.delete_btn = ctk.CTkButton(button_frame, text = "DELETE", font = ("", 25, "bold"), width = 150, state='disabled', command = self.delete)
        self.delete_btn.grid(row = 0, column = 2, padx = 15, pady = 20)

        self.show_details_btn = ctk.CTkButton(button_frame, text = "SHOW DETAILS", font = ("", 25, "bold"), state='disabled', width = 180, command = self.show_details)
        self.show_details_btn.grid(row = 0, column = 3, padx = 15, pady = 20)

        back_btn = ctk.CTkButton(button_frame, text = "BACK", font = ("", 25, "bold"), width = 150, command = self.emp_option_page, fg_color = "red", hover_color = "#8c0d0d")
        back_btn.grid(row = 0, column = 4, padx = 15, pady = 20)

    def selectItem(self, a):
        list = self.tree.item(self.tree.focus())["values"]
        if list: 
            self.selected_account = self.tree.item(self.tree.focus())["values"][0]
            self.selected_data = database.specific_data(self.selected_account)
            self.delete_btn.configure(state = 'normal')
            self.update_btn.configure(state = 'normal')
            self.show_details_btn.configure(state = 'normal')
        else:
            self.delete_btn.configure(state = 'disabled')
            self.update_btn.configure(state = 'disabled')
            self.show_details_btn.configure(state = 'disabled')
    
    def add(self):
        acc_no = self.entryId.get()
        if database.acc_no_exists(acc_no):
            tkinter.messagebox.showerror("ERROR", "ACCOUNT ALREADY EXISTS!")
        else:
            if self.entryId.get() == '' or self.entryName.get() == '' or  self.entryDoB.get() == '' or  self.entryContact.get() == '' or  self.entryBalance.get() == '':
                tkinter.messagebox.showerror("ERROR", "ALL FIELDS ARE REQUIRED!")
            else:
                database.insert(self.entryId.get(), self.entryName.get(), self.gender.get(), self.entryDoB.get(), self.entryContact.get(), self.accountType.get(), self.entryBalance.get())
                tkinter.messagebox.showinfo("Message", "NEW ACCOUNT ADDED SUCCESSFULLY!")
                self.add_page()
    
    def update(self):
        database.update(self.selected_account, self.entryName.get(), self.gender.get(), self.entryDoB.get(), self.entryContact.get(), self.accountType.get())
        tkinter.messagebox.showinfo("Message", "DETAILS UPDATED SUCCESSFULLY!")

    def delete(self):
        database.delete(self.selected_account)
        self.main()
        tkinter.messagebox.showinfo("Message", "ACCOUNT DELETED SUCCESSFULLY!")
    
    def update_page(self):
        self.clear_frame()

        frame = ctk.CTkFrame(self, fg_color = 'transparent')
        frame.grid(row = 1, column = 0, pady = 30)

        list = ["ACCOUNT NUMBER : ", "NAME : ","GENDER : ", "DATE OF BIRTH : ", "CONTACT NO : ","ACCOUNT TYPE : "]

        frame1 = ctk.CTkFrame(frame, fg_color = 'transparent')
        frame1.grid(row = 0, column = 0)

        frame2 = ctk.CTkFrame(frame, fg_color = 'transparent')
        frame2.grid(row = 0, column = 1)

        for i in range(len(list)):
            ctk.CTkLabel(frame1, text = list[i], font = ("", 20, 'bold'), justify = 'left', anchor="w", width = 250).grid(row = i, column = 0, pady = 20, padx = 20)

        self.entryId = ctk.CTkLabel(frame2, text = self.selected_account, font = ("", 25, 'bold'), width = 200)
        self.entryId.grid(row = 0, column = 0, pady = 20, padx = 20)

        self.entryName = ctk.CTkEntry(frame2, font = ("", 15), width = 200)
        self.entryName.grid(row = 1, column = 0, pady = 20, padx = 20)
        self.entryName.insert(0, self.selected_data[0])

        self.gender = ctk.CTkOptionMenu(frame2, values=["MALE", "FEMALE", "OTHER"], font = ("", 15), width = 200)
        self.gender.grid(row = 2, column = 0, pady = 20, padx = 20)
        self.gender.set(self.selected_data[1])

        self.entryDoB = ctk.CTkEntry(frame2, font = ("", 15), width = 200)
        self.entryDoB.grid(row = 3, column = 0, pady = 20, padx = 20)
        self.entryDoB.insert(0, self.selected_data[2])

        self.entryContact = ctk.CTkEntry(frame2, font = ("", 15), width = 200)
        self.entryContact.grid(row = 4, column = 0, pady = 20, padx = 20)
        self.entryContact.insert(0, self.selected_data[3])

        self.accountType = ctk.CTkOptionMenu(frame2, values=["SAVINGS", "CURRENT"], font = ("", 15), width = 200)
        self.accountType.grid(row = 5, column = 0, pady = 20, padx = 20)
        self.accountType.set(self.selected_data[4])

        button_frame = ctk.CTkFrame(frame, fg_color = "transparent")
        button_frame.grid(row = 1, columnspan = 2, padx = 10, pady = 10)

        update_btn = ctk.CTkButton(button_frame, text = "UPDATE", font = ("", 25, "bold"), width = 150, command = self.update)
        update_btn.grid(row = 0, column = 0, padx = 15, pady = 20)

        back_btn = ctk.CTkButton(button_frame, text = "BACK", font = ("", 25, "bold"), width = 150, command = self.main, fg_color = "red", hover_color = "#8c0d0d")
        back_btn.grid(row = 0, column = 1, padx = 15, pady = 20)

    def add_page(self):
        self.clear_frame()

        frame = ctk.CTkFrame(self, fg_color = 'transparent')
        frame.grid(row = 1, column = 0, pady = 30)

        list = ["ACCOUNT NUMBER : ", "NAME : ","GENDER : ", "DATE OF BIRTH : ", "CONTACT NO : ", "ACCOUNT TYPE : ", "CURRENT BALANCE : "]

        frame1 = ctk.CTkFrame(frame, fg_color = 'transparent')
        frame1.grid(row = 0, column = 0)

        frame2 = ctk.CTkFrame(frame, fg_color = 'transparent')
        frame2.grid(row = 0, column = 1)

        for i in range(len(list)):
            ctk.CTkLabel(frame1, text = list[i], font = ("", 20, 'bold'), justify = 'left', anchor="w", width = 250).grid(row = i, column = 0, pady = 20, padx = 20)

        self.entryId = ctk.CTkEntry(frame2, placeholder_text="Enter ACCOUNT NUMBER", font = ("", 15), width = 200)
        self.entryId.grid(row = 0, column = 0, pady = 20, padx = 20)

        self.entryName = ctk.CTkEntry(frame2, placeholder_text="Enter NAME", font = ("", 15), width = 200)
        self.entryName.grid(row = 1, column = 0, pady = 20, padx = 20)

        self.gender = ctk.CTkOptionMenu(frame2, values=["MALE", "FEMALE", "OTHER"], font = ("", 15), width = 200)
        self.gender.grid(row = 2, column = 0, pady = 20, padx = 20)
        self.gender.set("MALE")

        self.entryDoB = ctk.CTkEntry(frame2, placeholder_text="DD-MM-YYYY", font = ("", 15), width = 200)
        self.entryDoB.grid(row = 3, column = 0, pady = 20, padx = 20)

        self.entryContact = ctk.CTkEntry(frame2, placeholder_text="Enter CONTACT", font = ("", 15), width = 200)
        self.entryContact.grid(row = 4, column = 0, pady = 20, padx = 20)

        self.entryBalance = ctk.CTkEntry(frame2, placeholder_text="Enter BALANCE", font = ("", 15), width = 200)
        self.entryBalance.grid(row = 6, column = 0, pady = 20, padx = 20)

        self.accountType = ctk.CTkOptionMenu(frame2, values=["SAVINGS", "CURRENT"], font = ("", 15), width = 200)
        self.accountType.grid(row = 5, column = 0, pady = 20, padx = 20)
        self.accountType.set("SAVINGS")

        button_frame = ctk.CTkFrame(frame, fg_color = "transparent")
        button_frame.grid(row = 1, columnspan = 2, padx = 10, pady = 10)

        add_btn = ctk.CTkButton(button_frame, text = "ADD", font = ("", 25, "bold"), width = 150, command = self.add)
        add_btn.grid(row = 0, column = 0, padx = 15, pady = 20)

        back_btn = ctk.CTkButton(button_frame, text = "BACK", font = ("", 25, "bold"), width = 150, command = self.main, fg_color = "red", hover_color = "#8c0d0d")
        back_btn.grid(row = 0, column = 1, padx = 15, pady = 20)
    
    def show_details(self):
        self.clear_frame()

        frame = ctk.CTkFrame(self, fg_color = 'transparent')
        frame.grid(row = 1, column = 0, pady = 30)

        list = ["ACCOUNT NUMBER : ", "NAME : ","GENDER : ", "DATE OF BIRTH : ", "CONTACT NO : ", "ACCOUNT TYPE : ", "CURRENT BALANCE : "]

        frame1 = ctk.CTkFrame(frame, fg_color = 'transparent')
        frame1.grid(row = 0, column = 0)

        frame2 = ctk.CTkFrame(frame, fg_color = 'transparent')
        frame2.grid(row = 0, column = 1)

        for i in range(len(list)):
            ctk.CTkLabel(frame1, text = list[i], font = ("", 20, 'bold'), justify = 'left', anchor="w", width = 250).grid(row = i, column = 0, pady = 20, padx = 20)
        
        data = database.get_all_data(self.selected_account)

        for i in range(len(data)):
            ctk.CTkLabel(frame2, text = data[i], font = ("", 20, 'bold'), justify = 'left', anchor="center", width = 250).grid(row = i, column = 0, pady = 20, padx = 20)
        
        back_btn = ctk.CTkButton(frame, text = "BACK", font = ("", 25, "bold"), width = 150, command = self.main, fg_color = "red", hover_color = "#8c0d0d")
        back_btn.grid(row = 1, columnspan = 2, padx = 15, pady = 20)

    
    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

        label_frame = ctk.CTkFrame(self, border_width = 5)
        label_frame.grid(row = 0, columnspan = 2, sticky = "ew")

        ctk.CTkLabel(label_frame, text = "VNIT BANK", font = ("Comic Sans MS", 60)).pack(pady = 15)


if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("green")
    root = app()
    root.mainloop()
