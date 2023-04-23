import tkinter as tk
import math
import numpy as np

class App:
    def __init__(self, master):
        self.master = master
        
        # set the title of GUI window
        self.master.title('Activation Fonctions')
        
        # set the configuration of GUI window
        self.master.geometry('600x400')
        self.master.resizable(False, False)
        
        # set the background colour of GUI window
        self.master.configure(background='black')
        

        self.label = tk.Label(self.master, text='Enter a number', bg='black', fg='gray', font=('Arial', 20, 'bold'))
        self.label.pack(expand=True)
        
        self.entry = tk.Entry(self.master, bg='white', justify='center', font=('Arial', 15, 'bold'))
        self.entry.pack(expand=True, fill='both', padx=200, pady=10)

        self.sigmoid_button = tk.Button(self.master, text='Sigmoid', fg='black', bg='gray', font=('Arial', 15), command=self.sigmoid, height=2, width=10)
        self.sigmoid_button.pack(expand=True)
        
        self.tanh_button = tk.Button(self.master, text='tanh', fg='black', bg='gray', font=('Arial', 15), command=self.tanh, height=2, width=10)
        self.tanh_button.pack(expand=True)
        
        self.relu_button = tk.Button(self.master, text='ReLU', fg='black', bg='gray', font=('Arial', 15), command=self.relu, height=2, width=10)
        self.relu_button.pack(expand=True)

        self.label_text = tk.Label(self.master, text='Result', bg='black', fg='gray', font=('Arial', 20, 'bold'))
        self.label_text.pack(expand=True)
        
        self.result_label = tk.Label(self.master, text='', bg='white', height=1, width=10, font=('Arial', 15, 'bold'))
        self.result_label.pack(expand=True, fill='both', padx=200, pady=10)
        
        
    def sigmoid(self):
        x = float(self.entry.get())
        result = 1 / (1 + math.exp(-x))
        self.result_label.config(text='{}'.format(np.round(result, 2)))
        
    def tanh(self):
        x = float(self.entry.get())
        result = math.tanh(x)
        self.result_label.config(text='{}'.format(np.round(result, 2)))
        
    def relu(self):
        x = float(self.entry.get())
        result = max(0, x)
        self.result_label.config(text='{}'.format(np.round(result, 2)))


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
