import tkinter as tk
import customtkinter as ctk


class MainMenuFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.header_name = "PlotMenu header"
   

        # self.header = ctk.CTkLabel(self, text=self.header_name)
        # self.header.grid(row=0, column=0, padx=10, pady=10)

        self.grid(pady=300)

        self.MakePlotButton = ctk.CTkButton(master=self,
                                               text="Make Plot",
                                               command=self.hide)
        
        self.MakePlotButton.grid(row=0, column=0, padx=10, pady=10)


        self.CalculateButton = ctk.CTkButton(master=self,
                                               text="Calculate",
                                               command=self.calculate)
        
        self.CalculateButton.grid(row=1, column=0, padx=10, pady=10)



        self.ExitButton = ctk.CTkButton(master=self,
                                        text='Exit',
                                        command=self.quit)
        self.ExitButton.grid(row=2, column=0, padx=10, pady=10)
 

        
        

    def show(self):
        self.grid(expand=True, fill="both")
    
    def hide(self):
        self.grid_forget()
    
    def calculate(self):
        # TODO: implement calculation and display result in textbox
        self.textbox.delete("1.0", "end")  # clear previous content
        self.textbox.insert("1.0", "Calculation result")
