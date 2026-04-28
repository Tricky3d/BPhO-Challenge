# Liabraries

import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from tkinter import simpledialog, messagebox


# Graphical user interface

def get_inputs():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask for first input
    input1 = simpledialog.askstring("Input", "Enter first value:")
    
    # Ask for second input
    input2 = simpledialog.askstring("Input", "Enter second value:")

    root.destroy()  # Close everything

    return input1, input2

# Input variables

particles = []
particleCount = 100
particleMass = 1.0
particleRadius = 1

newParticle = []
newPX = 0.0
newPY = 0.0

largePMass = 10.0
largePRadius = 10

bounds = 100

# Main program

# Creates the array of particles

for i in range(0,particleCount):

    newPX = bounds * random.random()
    newPY = bounds * random.random()

    # 3rd value is the angle of the velocity (radians) will come in useful later
    
    newParticle = [newPX, newPY, 0]
    particles.append(newParticle)


# The fun stuff


while True:
    for particle in particles:





