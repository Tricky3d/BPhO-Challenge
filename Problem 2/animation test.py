import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# --- Setup ---
fig, ax = plt.subplots()

# Initial 2D list: [[x1,y1], [x2,y2], ...]
data = [[random.random(), random.random()] for _ in range(50)]

# Unpack into separate x, y lists for matplotlib
xs = [point[0] for point in data]
ys = [point[1] for point in data]

scatter = ax.scatter(xs, ys, c='steelblue', s=60, alpha=0.7)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title("Live Scatter Plot (pure Python)")

# --- Update function ---
def update(frame):
    # Generate new 2D Python list
    new_data = [[random.random(), random.random()] for _ in range(50)]

    # Unpack into x and y
    xs = [point[0] for point in new_data]
    ys = [point[1] for point in new_data]

    # Zip back into (N, 2) pairs for set_offsets
    scatter.set_offsets(list(zip(xs, ys)))
    return (scatter,)

# --- Animation ---
ani = animation.FuncAnimation(
    fig,
    update,
    interval=1000,   # 1 second
    blit=True
)

plt.show()