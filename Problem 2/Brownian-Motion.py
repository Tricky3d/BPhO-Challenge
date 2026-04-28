# Liabraries

import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from tkinter import simpledialog, messagebox

# Graphical user integrac

def get_inputs():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask for first input
    input1 = simpledialog.askstring("Input", "Enter first value:")
    
    # Ask for second input
    input2 = simpledialog.askstring("Input", "Enter second value:")

    root.destroy()  # Close everything

    return input1, input2

val1, val2 = get_inputs()



