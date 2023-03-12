import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk

from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



from plot_menu import PlotMenuFrame
from main_menu import MainMenuFrame

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):

    
    def create_plot(self):
        # clear any existing plot
        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        # create new plot
        fig, ax = plt.subplots()
        x = [1, 2, 3, 4, 5]
        y = [10, 8, 6, 4, 2]
        ax.plot(x, y)

        # display plot in the GUI
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

        # add save button
        save_button = ctk.CTkButton(master=self.plot_frame, text="Save Plot", command=self.save_plot)
        save_button.pack(side="bottom", pady=10)

    def create_plot_event(self):
        self.main_menu_frame.grid_forget()  # remove plot frame
        self.plot_menu_frame.grid(row=0, column=1, sticky="ns")


    def back_event(self):
        self.plot_menu_frame.grid_forget()  # remove plot frame
        self.main_menu_frame.grid(row = 0, column = 1, sticky="ns")

    def calculate(self):
        # TODO: implement calculation and display result in textbox
        self.textbox.delete("1.0", "end")  # clear previous content
        self.textbox.insert("1.0", "Calculation result")

    def save_plot(self):
        # Open a Windows window to save the plot
        filename = filedialog.asksaveasfilename(defaultextension=".png")
        plt.savefig(filename)
        tk.messagebox.showinfo("Save Plot", "Plot saved successfully!")

    def __init__(self):
        super().__init__()

        # configure window
        self.title("MEDAL")
        self.geometry(f"{800}x{600}")
        self.resizable(True, True)

        # configure grid layout (3 columns)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)

    
        
        # create plot menu

        self.plotMenuFrame = PlotMenuFrame(self)
        self.plotMenuFrame.grid(row=0, column=1)

        # create middle column with main menu buttons
       
        self.mainMenuFrame = MainMenuFrame(self)
        self.mainMenuFrame.grid(row=0, column=1)


    
        # create left column with textbox
        self.textbox = ctk.CTkTextbox(self, width=20)

        self.textbox.grid(row=0,
                          column=0,
                          padx=(20, 10),
                          pady=(20, 20),
                          sticky="nsew")

        # create right column with plot display and save button
        self.plot_frame = ctk.CTkFrame(self)
        self.plot_frame.grid(row=0,
                             column=2,
                            #  padx=(10, 20),
                             pady=(20, 20),
                             sticky="nsew")



if __name__ == "__main__":
    app = App()
    app.mainloop()
