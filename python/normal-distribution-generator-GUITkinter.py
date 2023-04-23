import tkinter as tk
import numpy as np

class NormalDistributionGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Normal Distribution Generator")
        self.master.geometry('600x400')
        self.master.resizable(False, False)
        self.master.configure(background='black')
        
        
        self.n_label = tk.Label(master, text="Number of values", bg='black', fg='gray', font=('Arial', 20, 'bold'))
        self.n_label.pack(expand=True)
        
        self.n_entry = tk.Entry(master, bg='gray', justify='center', font=('Arial', 15, 'bold'), width=10)
        self.n_entry.pack(expand=True)
        
        self.generate_button = tk.Button(master, text="Generate", fg='black', bg='gray', font=('Arial', 15), command=self.generate)
        self.generate_button.pack(expand=True)
        
        self.result_label = tk.Label(master, text="", bg='black', fg='white', font=('Arial', 15, 'bold'))
        self.result_label.pack(expand=True)
    
    def generate(self):
        n = int(self.n_entry.get())
        
        x_values = np.random.normal(0, 1, n)
        x_values = np.round(x_values, 2)
        result = " ".join(str(x) for x in x_values)
        result = "[" + result + "]"
        self.result_label.config(text=result)

root = tk.Tk()
app = NormalDistributionGenerator(root)
root.mainloop()
