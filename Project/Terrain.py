import numpy as np
import matplotlib.pyplot as plt
import noise
import matplotlib.colors as mcolors

def createTerrain2(width):
    terrain_array = np.zeros((width, width))
    return terrain_array
def generateTerrain(height, width,terrain_array):

    for x in range(height):
        for y in range(width):
            nx = x / width
            ny = y / height

            W = (noise.pnoise2(4 * nx, 4 * ny, octaves=6, persistence=0.5, lacunarity=2.0) +
                 0.25 * noise.pnoise2(8 * nx, 8 * ny, octaves=6, persistence=0.5, lacunarity=2.0) +
                 0.125 * noise.pnoise2(16 * nx, 16 * ny, octaves=6, persistence=0.5, lacunarity=2.0)) / (1 + 0.25 + 0.125)

            W = (abs(W) + 1) / 2

            if 0.4 < W < 0.7 and np.random.uniform(0, 1) < 0.5:
                T = 0.05
                terrain_array[y][x] = W + T
            else:
                terrain_array[y][x] = W
    return terrain_array

def plotTerrain(terrain_array, antennas,RSS_array):
    def scale_colorbar(x, pos):
        return f'{x * 1000:.0f}'

    plt.figure(figsize=(8, 6))

    x_coords, y_coords = np.meshgrid(np.arange(terrain_array.shape[1]), np.arange(terrain_array.shape[0]))
    x_coords = x_coords.flatten()
    y_coords = y_coords.flatten()

    colors = terrain_array.flatten()

    scatter = plt.scatter(x_coords, y_coords, c=colors, cmap='Spectral_r', s=1)

    if np.any(antennas != 0):  # Check if there's any non-zero element in the array
        antenna_labels = {'Omni': False, 'Sector': False}  # Track if we've added labels for each antenna type

        for x, y, type in antennas:
            color = 'red' if type == 'Omni' else 'blue'
            label = type

            # Add label to legend only the first time an antenna type is encountered
            if not antenna_labels[type]:
                plt.scatter(x, y, c=color, s=100, label=label, edgecolors='black')
                antenna_labels[type] = True
            else:
                plt.scatter(x, y, c=color, s=100, edgecolors='black')

    cbar = plt.colorbar(scatter)
    cbar.set_ticks(cbar.get_ticks())
    cbar.set_ticklabels([f'{tick * 1000:.0f}' for tick in cbar.get_ticks()])

    # Display the plot
    plt.legend()
    plt.show()