# Liabraries

import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from tkinter import simpledialog, messagebox
import math

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
particleGradient = 0
particleTangentGradient = 0
particleRadiusGradient = 0
particleVelocity = []
particleMomentum = []

collisionAngle = 0

newParticle = []
newPX = 0.0
newPY = 0.0

largePMass = 10.0
largePRadius = 20
largeParticleVelocity = []


bounds = 100

stepsPerSecond = 0
stepsize = 1

# Main program

# Creates the array of particles

newPX = bounds/2
newPY = bounds/2


for i in range(0,particleCount):

    while math.sqrt((newPX-bounds/2)**2 + (newPY-bounds/2)**2 ) < largePRadius:
        newPX = bounds * random.random()
        newPY = bounds * random.random()

    # 3rd value is the angle of the velocity (radians with respect to the horizontal) will come in useful later

    newParticle = [newPX, newPY, 0]
    particles.append(newParticle)
    
    newPX = bounds/2
    newPY = bounds/2


# The fun stuff

largeParticlePos = [bounds/2,bounds/2]
largeParticleVelocity = [0,0]


while True:
    for particle in particles:
        if math.sqrt((newPX-largeParticlePos[0])**2 + (newPY-largeParticlePos[1])**2 ) < largePRadius:
            particleGradient = math.tan(particle[2])
            particleRadiusGradient = (particle[1] - largeParticlePos[1])/(particle[0] - largeParticlePos[0])
            particleTangentGradient = -(1/particleRadiusGradient)
            collisionAngle = math.pi/2 - math.arctan(abs(particleGradient - particleTangentGradient)/1 + particleGradient * particleTangentGradient)
            
            particleMomentum = [particleMass * ,]


        else:
            particle[2] = 2 * math.pi * random.random








