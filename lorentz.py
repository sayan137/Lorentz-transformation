import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Define the range and spacing for the grid
x = np.linspace(-5, 5, 9)
y = np.linspace(-5, 5, 9)

# Create a meshgrid
X, Y = np.meshgrid(x, y)

# Flatten the meshgrid arrays to use in plt.scatter
X_flat = X.flatten()
Y_flat = Y.flatten()

beta= -1/2
phi = np.arctanh(beta)

a = np.cosh(phi)
b = -np.sinh(phi)
c = -np.sinh(phi)
d = np.cosh(phi)

n= 10

# Create the figure and the slider axis
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # Adjust the bottom to fit the slider

# Initialize the plot with k=1
k_init = 0

# Plot the original grid points once
original_points = ax.scatter(X_flat, Y_flat, color='blue', s=50, alpha=0.7, label='Original Points')

# Plot for transformed points (initialized empty)
transformed_points = ax.scatter([], [], color='red', s=50, alpha=0.7, label='Transformed Points')

# Arrows for transformation (initialized empty)
arrow_a = ax.arrow(0, 0, 0, 0, length_includes_head=True, width=0.01, edgecolor='#E8E803', facecolor='green', lw=2, zorder=2)
arrow_b = ax.arrow(0, 0, 0, 0, length_includes_head=True, width=0.01, edgecolor='#DB05DB', facecolor='green', lw=2, zorder=2)
arrow_c = ax.arrow(0, 0, 0, 0, length_includes_head=True, width=0.01, edgecolor='#E8E803', facecolor='green', lw=2, zorder=2)


xx=np.linspace(-5,5,5)
yy= xx
zz= xx/beta

hline1 = ax.axhline(0, color='black', linestyle='--', linewidth=1)
hline2 = ax.axhline(0, color='black', linestyle='--', linewidth=1,label='time dialation')
plt.plot(yy,xx,color='cyan',alpha=0.4)
# Function to perform the transformation
def transform(k):
    global arrow_a, arrow_b, arrow_c
    a_prime = 1 - (k / n) + a * (k / n)
    b_prime = b * (k / n)
    c_prime = c * (k / n)
    d_prime = 1 - (k / n) + d * (k / n)

    # Calculate transformed points
    X_transformed = a_prime * X_flat + b_prime * Y_flat
    Y_transformed = c_prime * X_flat + d_prime * Y_flat
    
    # Update transformed points in the plot
    transformed_points.set_offsets(np.c_[X_transformed, Y_transformed])

    # Update arrows
    arrow_a.remove()
    arrow_b.remove()
    arrow_c.remove()
    arrow_a = ax.arrow(0, 0, b_prime, d_prime, length_includes_head=True, width=0.01, edgecolor='#E8E803', facecolor='green', lw=2, zorder=2)
    arrow_b = ax.arrow(0, 0, xx[-1] - k / n * xx[-1], d_prime * zz[-1], length_includes_head=True, width=0.01, edgecolor='#723178', facecolor='green', lw=2, zorder=2)
    arrow_c = ax.arrow(0, 0, a_prime, c_prime, length_includes_head=True, width=0.01, edgecolor='#E8E803', facecolor='green', lw=2, zorder=2)


    # Adjust plot limits and grid
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.grid(True)
    ax.legend()

    # Place axhline through the transformed point at index 4
    hline1.set_ydata(Y_transformed[50])
    hline2.set_ydata(Y_transformed[49])

    # Refresh the plot
    fig.canvas.draw_idle()


# Slider axis
slider_ax = plt.axes([0.15, 0.1, 0.7, 0.03])
slider = Slider(slider_ax, 'Frame', 0, n, valinit=k_init, valstep=0.5)

# Update function for the slider
def update(val):
    k = slider.val
    transform(k)

# Connect the slider to the update function
slider.on_changed(update)

# Initial plot
transform(k_init)

# Show the plot
plt.grid()
plt.legend()
plt.show()
