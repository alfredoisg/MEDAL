import tkinter as tk
import customtkinter as ctk




class OneVariableMenuFrame(ctk.CTkFrame):
    def __init__(self, header_name="OneVariableMenuFrame"):
        super().__init__()

        self.header_name = header_name
   

        self.header = ctk.CTkLabel(self, text=self.header_name)
        self.header.grid(row=0, column=0, padx=10, pady=10)



