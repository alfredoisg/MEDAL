import customtkinter as ctk

class MainMenuFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.parent = parent
        
        self.label = ctk.CTkLabel(self, text="Main menu")
        self.label.pack(pady=10)
        
        self.plot_button = ctk.CTkButton(self, text="Create Plot", command=self.on_plot_button)
        self.plot_button.pack(pady=10)
        
        self.calculate_button = ctk.CTkButton(self, text="Calculate", command=self.on_calculate_button)
        self.calculate_button.pack(pady=10)
        
        self.exit_button = ctk.CTkButton(self, text="Exit", command=self.quit)
        self.exit_button.pack(pady=10)
        
    def on_plot_button(self):
        self.parent.go_to_frame("example")
        
    def on_calculate_button(self):
        # TODO: implement calculation and display result in textbox
        pass


    def show(self):
        self.pack(expand=True, fill="both")
        
    def hide(self):
        self.pack_forget()

class MainMenuFrame2(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.parent = parent
        
        self.label = ctk.CTkLabel(self, text="Main menu")
        self.label.grid(row=0, column=0, pady=10)
        
        self.plot_button = ctk.CTkButton(self, text="Create Plot", command=self.on_plot_button)
        self.plot_button.grid(row=1, column=0, pady=10)
        
        self.calculate_button = ctk.CTkButton(self, text="Calculate", command=self.on_calculate_button)
        self.calculate_button.grid(row=2, column=0, pady=10)
        
        self.exit_button = ctk.CTkButton(self, text="Exit", command=self.quit)
        self.exit_button.grid(row=3, column=0, pady=10)
        
    def on_plot_button(self):
        self.parent.go_to_frame("example")
        
    def on_calculate_button(self):
        # TODO: implement calculation and display result in textbox
        pass
        
    def show(self):
        self.grid(row=0, column=1, sticky="nsew")
        
    def hide(self):
        self.grid_forget()

class ExampleFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        
        self.label = ctk.CTkLabel(self, text="Example frame")
        self.label.pack(pady=10)
        
        self.back_button = ctk.CTkButton(self, text="Back", command=self.on_back_button)
        self.back_button.pack(pady=10)
        
    def on_back_button(self):
        self.parent.go_to_frame("main_menu")

    def show(self):
        self.pack(expand=True, fill="both")
        
    def hide(self):
        self.pack_forget()
