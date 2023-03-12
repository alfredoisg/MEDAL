import tkinter as tk
import customtkinter as ctk

from one_variable_menu import OneVariableMenuFrame



class PlotMenuFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.header_name = "PlotMenu header"
   

        # self.header = ctk.CTkLabel(self, text=self.header_name)
        # self.header.grid(row=0, column=0, padx=10, pady=10)


        self.OneVariableButton = ctk.CTkButton(master=self,
                                               text="One Variable",
                                               command=self.hide)
        
        self.OneVariableButton.grid(row=0, column=0, padx=10, pady=10)


        self.TwoVariableButton = ctk.CTkButton(master=self,
                                               text="Two Variables",
                                               command=self.hide)
        
        self.TwoVariableButton.grid(row=1, column=0, padx=10, pady=10)

        self.BackButton = ctk.CTkButton(master=self,
                                               text="Back",
                                               command=self.hide)
        
        self.BackButton.grid(row=3, column=0, padx=10, pady=10)

        self.ExitButton = ctk.CTkButton(master=self,
                                        text='Exit',
                                        command=self.quit)
        self.ExitButton.grid(row=4, column=0, padx=10, pady=10)
 

        
        

    def show(self):
        self.grid(expand=True, fill="both")
    
    def hide(self):
        self.grid_forget()
