import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk

from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("MEDAL")
        self.geometry(f"{1200}x{800}")
        self.resizable(True, True)

        # configure grid layout (3 columns)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # create middle column with main menu buttons
        self.main_menu_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_menu_frame.grid(row=0, column=1)#, pady=30, sticky="nsew")
        self.main_menu_frame.grid_columnconfigure(0, weight=2)
        self.main_menu_frame = ctk.CTkLabel(self.main_menu_frame, text="Main menu",
                                                  font=ctk.CTkFont(size=20, weight="bold"))

        self.create_plot_button = ctk.CTkButton(self.main_menu_frame,
                                                text="Create Plot",
                                                command=self.create_plot_event)
        self.create_plot_button.grid(row=0,
                                     column=0,
                                     pady=(10, 20),
                                     sticky="ew")
        
        self.calculate_button = ctk.CTkButton(self.main_menu_frame,
                                              text="Calculate",
                                              command=self.calculate)
        self.calculate_button.grid(row=1,
                                   column=0,
                                   pady=(10, 20),
                                   sticky="ew")

        self.exit_button = ctk.CTkButton(self.main_menu_frame,
                                         text="Exit",
                                         command=self.quit)
        self.exit_button.grid(row=2,
                              column=0,
                              pady=(10, 20),
                              sticky="nsew")


        # create plot menu
        self.plot_menu_frame = ctk.CTkFrame(self)
        self.plot_menu_frame.grid(row=0, column=1)#, pady=30, sticky="nsew")
        self.plot_menu_frame.grid_columnconfigure(0, weight=2)

        self.plot_create_plot_button = ctk.CTkButton(self.plot_menu_frame,
                                                     text="One Variable",
                                                     command=self.create_plot)
        self.plot_create_plot_button.grid(row=0,
                                          column=0,
                                          pady=(10,20),
                                          sticky="ew")

        self.plot_exit_button = ctk.CTkButton(self.plot_menu_frame,
                                         text="Exit",
                                         command=self.quit)
        self.plot_exit_button.grid(row=1,
                              column=0,
                              pady=(10, 20),
                              sticky="ew")
        

        self.plot_back_button = ctk.CTkButton(self.plot_menu_frame,
                                              text="Back",
                                              command=self.back_event)
        self.plot_back_button.grid(row=2,
                              column=0,
                              pady=(10, 20),
                              sticky="nsew")
        
        self.plot_menu_frame.grid_forget()



    
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
        
        self.save_button = ctk.CTkButton(self.plot_frame,
                                         text="Save Plot",
                                         command=self.save_plot)
        
        self.save_button.grid(row=3,
                              column=3,
                              pady=(10, 20),
                              sticky="nsew")


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

if __name__ == "__main__":
    app = App()
    app.mainloop()
