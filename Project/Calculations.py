import time
import numpy as np
from Anthenna import *
from Terrain import *
import matplotlib.pyplot as plt

def get_angle_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if 0 < value < 360:  # Ensure the value is between 0 and 360
                return value
            else:
                print("Please enter a value between 0 and 360.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_positive_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_negative_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                return value
            else:
                print("Please enter a negative number for the threshold.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def createTerrain():
    while True:
        print("How big do you want your map to be?")
        user_input = input()
        if user_input.isdigit():
            width = int(user_input)
            terrain_array = createTerrain2(width)
            return width,terrain_array
        else:
            print("It is not a number, enter again")

def get_coordinate_input(prompt, limit):
    while True:
        try:
            value = int(float(input(prompt)))  # Ensure integer value
            if 0 <= value < limit:
                return value
            else:
                print(f"Please enter a value between 0 and {limit - 1}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_height_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 40 and value > 0:
                return value
            else:
                print("Please enter a height less than 40 and more than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def placeAnthenna(width, terrain_array, RSS_array, antennas):
    while True:
        print("What type is your antenna? - Omni/Sector")
        antenna_type = input().strip()

        if antenna_type == "Omni":
            print("Your antenna is Omni/isotropic.")
            print("Place your antenna on your map.")

            x = get_coordinate_input("x: ", width)
            y = get_coordinate_input("y: ", width)
            Height = get_height_input("Height: ")
            PowerGain = get_positive_input("Power Gain: ")
            Maximum_tr_ppc = get_positive_input("Maximum Transmission Power (ppc): ")
            TrLineLoss = get_positive_input("Transmission Line Loss: ")
            frequency = get_positive_input("Frequency(MHz): ")
            K = get_positive_input("K (constant): ")
            threshold = get_negative_input("Threshold: ")

            RSS_array = OmniAnthenna(x, y, Height, PowerGain, Maximum_tr_ppc, TrLineLoss, frequency, K, threshold, terrain_array, width, RSS_array)

            print(f"\nAntenna Details:")
            print("Omni/isotropic")
            print(f"x: {x}, y: {y}, Height: {Height}")
            print(f"Power Gain: {PowerGain}")
            print(f"Maximum Transmission Power (ppc): {Maximum_tr_ppc}")
            print(f"Transmission Line Loss: {TrLineLoss}")
            print(f"Frequency: {frequency}MHz")
            print(f"K: {K}")
            print(f"Threshold: {threshold} dBmW")
            print(RSS_array)
            antennas.append((x, y, 'Omni'))  # Add the new Omni antenna to the list
            return terrain_array, antennas, RSS_array

        elif antenna_type == "Sector":
            print("Your antenna is Sector.")
            print("Place your antenna on your map.")

            x = get_coordinate_input("x: ", width)
            y = get_coordinate_input("y: ", width)
            Height = get_height_input("Height: ")
            PowerGain = get_positive_input("Power Gain: ")
            Maximum_tr_ppc = get_positive_input("Maximum Transmission Power (ppc): ")
            AnthennaGain = get_positive_input("Antenna Gain: ")
            TrLineLoss = get_positive_input("Transmission Line Loss: ")
            frequency = get_positive_input("Frequency(MHz): ")
            K = get_positive_input("K (constant): ")
            threshold = get_negative_input("Threshold: ")
            angle = get_angle_input("Beam Angle (degrees): ")
            azimuth = get_angle_input("Azimuth (degrees): ")

            RSS_array= SectorAntenna(x, y, angle, azimuth, Height, PowerGain, Maximum_tr_ppc, AnthennaGain, TrLineLoss, frequency, K, threshold, terrain_array, width, RSS_array)

            print("Sector antenna placed with the following parameters:")
            print(f"Position: ({x}, {y})")
            print(f"Height: {Height}")
            print(f"Power Gain: {PowerGain}")
            print(f"Max Transmission Power (ppc): {Maximum_tr_ppc}")
            print(f"Transmission Line Loss: {TrLineLoss}")
            print(f"Frequency: {frequency}MHz")
            print(f"K: {K}")
            print(f"Threshold: {threshold} dBmW")
            print(f"Beam Angle: {angle} degrees")
            print(f"Azimuth: {azimuth} degrees")
            print(f"Antenna Gain: {AnthennaGain} dBi")

            antennas.append((x, y, 'Sector'))  # Add the new Sector antenna to the list
            print(RSS_array)
            return terrain_array, antennas, RSS_array

        else:
            print("Please enter a valid antenna type (Omni or Sector). Try again.")

