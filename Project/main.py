from Anthenna import *
from Terrain import *
from Calculations import *

width1, terrain_array1 = createTerrain()
RSS_array = []
antennas=[]
terrain_array2 = generateTerrain(width1, width1, terrain_array1)
plotTerrain(terrain_array2,antennas,RSS_array)
terrain_array3, antennas ,RSS_array= placeAnthenna(width1, terrain_array2,RSS_array,antennas)
plotTerrain(terrain_array3, antennas,RSS_array)

print("do you want to add more antennas? yes/no")
while True:
    user_input = input().strip().lower()  # Get input and remove leading/trailing spaces
    if user_input == "yes":
        terrain_array3, antennas = placeAnthenna(width1, terrain_array3, RSS_array, antennas)
        plotTerrain(terrain_array3, antennas)
        print("do you want to add more antennas? yes/no")
         # Exit the loop if the user chooses "yes"
    elif user_input == "no":
        exit()  # Exit the program if the user chooses "no"
    else:
        print("Invalid input. Please type 'yes' or 'no'.")