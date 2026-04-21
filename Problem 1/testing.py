# Libraries

import matplotlib.pyplot as plt
import math
import random


# Input variables asgf

stepSize = float(input('Step size = '))
stepCount = int(input('Number of steps =  '))


# Intialise arrays

xPos = 0.0
yPos = 0.0
xPath = [0] 
yPath = [0]

# Logic variables 

theta = 0.0
xMovement = 0.0
yMovement = 0.0
r = stepSize

# 

maximum = 0



# Creating a 2d array 

for i in range(1,stepCount + 1):

    # Selects a random number between 0 and 1 and multiplies by 2π
    theta = random.random() * (2 * math.pi)
    
    # x = r * cos θ
    # y = r * sin θ 
    xMovement = r * math.cos(theta)
    yMovement = r * math.sin(theta)

    # Adds the x and y coordinates to the current position
    xPos += xMovement
    yPos += yMovement

    # Appends an array of [x,y] to the 2d array with all points on the path    
    xPath.append(xPos)
    yPath.append(yPos)

maximum = max(abs(max(xPath, key=abs)), abs(max(yPath, key=abs)))


fig, ax = plt.subplots(figsize=(8, 5))

ax.set_xlim(-1 * maximum, maximum)
ax.set_ylim(-1 * maximum, maximum)




plt.plot(xPath, yPath)
plt.show()





    
    

    