
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

# Use Seaborn style for better aesthetics
sns.set(style="whitegrid")

# Create a function to plot a  3d mesh graph
def plot_3d_mesh():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create data
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))

    # Plot the surface
    surf = ax.plot_surface(x, y, z, cmap='viridis')

    # Add a color bar which maps values to colors
    fig.colorbar(surf)

    # Set labels
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title('3D Mesh Graph')

    # Show the plot
    plt.savefig('meshgraph.png')
    plt.show()

# Call the function to display the plot
plot_3d_mesh()
