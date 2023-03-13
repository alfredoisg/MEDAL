import tkinter as tk
import customtkinter as ctk

from tkinter import filedialog
import matplotlib.pyplot as plt

from frames import MainMenuFrame, ExampleFramegit 
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # configure window
        self.geometry("800x600")

        # create left column with textbox
        self.left_frame = ctk.CTkFrame(self)
        self.left_frame.pack(side='left', fill="both", expand=True)
        
        self.textbox = ctk.CTkTextbox(self.left_frame, width=20)
        self.textbox.pack(padx=(20, 10), pady=(20, 20), fill="both", expand=True)
        

        # create right column with plot display
        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.pack(side='right', fill="both", expand=True)
        
        self.plot_frame = ctk.CTkFrame(self.right_frame)
        self.plot_frame.pack(padx=(10, 20), pady=(20, 20), fill="both", expand=True)
        
        self.save_button = ctk.CTkButton(self.right_frame, text="Save Plot", command=self.save_plot)
        self.save_button.pack(pady=(10, 20))

        
        # create frames
        self.main_menu_frame = MainMenuFrame(self)
        # self.main_menu_frame.grid(row=0, column=1)
        self.example_frame = ExampleFrame(self)
        # self.example_frame.grid(row=0, column=1)
        
        # set the initial frame
        self.current_frame = self.main_menu_frame
        self.current_frame.pack(side='right', fill='both', expand=True)
        self.current_frame.show()



        
    def go_to_frame(self, frame_name):
        if frame_name == "main_menu":
            new_frame = self.main_menu_frame
        elif frame_name == "example":
            new_frame = self.example_frame
        else:
            raise ValueError(f"Invalid frame name: {frame_name}")
            
        self.current_frame.hide()
        self.current_frame = new_frame
        self.current_frame.show()
    
    def save_plot(self):
        # Open a Windows window to save the plot
        filename = filedialog.asksaveasfilename(defaultextension=".png")
        plt.savefig(filename)
        tk.messagebox.showinfo("Save Plot", "Plot saved successfully!")
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
