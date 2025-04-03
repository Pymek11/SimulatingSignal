import math

import numpy as np


#K=80# ussualy? const.???????

def OmniAnthenna(x,y,Height,PowerGain,Maximum_tr_ppc,TrLineLoss,frequency,K,threshold,terrain_array,width,RSS_array):
    AnthennaGain=5 # for OMNI anthennas (dBi) varies from 4.9-5.1
    # EIRP = Maximum_tr_ppc + AnthennaGain - TrLineLoss  # effectuie transmit power dBm
    # PathLoss = 20 * math.log10(distance) + 20 * math.log10(frequency * (math.pow(10, 6)) * frequency) + K #dB
    # RSS= EIRP-PathLoss  #received signal strength
    max_distance=0
    height_terrain_antenna = terrain_array[y][x]
    height_anthenna = Height + height_terrain_antenna

    for i in range(999):
        if(20*math.log10(1+i)+20*math.log10(frequency*(math.pow(10,6)))+K < threshold):
            max_distance = 1+i
    for i in range(width):
        for j in range(width):
            height_point = terrain_array[j][i]
            distance = math.sqrt(math.pow(x-i,2)+math.pow(y-j,2)+math.pow(height_point-height_anthenna,2))
            if distance < max_distance:
                if not is_line_of_sight_blocked(x, y, height_anthenna, i, j, height_point, terrain_array):
                    EIRP = Maximum_tr_ppc + AnthennaGain - TrLineLoss  # Effective transmit power dBm
                    PathLoss = 20 * math.log10(distance) + 20 * math.log10(frequency * (math.pow(10, 6)) * frequency) + K
                    RSS = EIRP - PathLoss
                    if RSS < threshold:
                        RSS = 0
                    RSS_array[j][i] = RSS
    return RSS_array



def SectorAntenna(x, y, angle, azimuth, Height, PowerGain, Maximum_tr_ppc, AnthennaGain, TrLineLoss, frequency, K, threshold, terrain_array, width,RSS_array):
    height_terrain_antenna = terrain_array[y][x]
    height_anthenna = Height + height_terrain_antenna
    max_distance = 0
    EIRP = Maximum_tr_ppc + AnthennaGain - TrLineLoss
    for i in range(999):
        if (20 * math.log10(1 + i) + 20 * math.log10(frequency * (math.pow(10, 6))) + K < threshold):
            max_distance = 1 + i
    for i in range(width):
        for j in range(width):
            height_point = terrain_array[j][i] * 1000  # Scale terrain height
            distance = math.sqrt(math.pow(x-i,2)+math.pow(y-j,2)+math.pow(height_point-height_anthenna,2))

            if distance < max_distance and is_inside_sector(x, y, i, j, azimuth, angle):
                if not is_line_of_sight_blocked(x, y, Height, i, j, height_point, terrain_array):
                    PathLoss = 20 * math.log10(distance) + 20 * math.log10(frequency * (math.pow(10, 6))) + K
                    RSS = EIRP - PathLoss
                    print(f"RSS at ({i}, {j}): {RSS}")
                    if RSS < threshold:
                        RSS = 0
                    RSS_array[j][i] = RSS
    print(RSS_array)
    return RSS_array

def is_line_of_sight_blocked(x1, y1, z1, x2, y2, z2, terrain_array):
    num_samples = int(max(abs(x2 - x1), abs(y2 - y1))) * 2
    for i in range(num_samples + 1):
        t = i / num_samples  # interpolation
        x = int(round(x1 + t * (x2 - x1)))
        y = int(round(y1 + t * (y2 - y1)))

        expected_height = z1 + t * (z2 - z1)

        if terrain_array[y, x] * 1000 > expected_height:
            return True

    return False  # No obstruction)


def is_inside_sector(x, y, target_x, target_y, azimuth, angle):
    # checking for sector antenna

    dx = target_x - x
    dy = target_y - y
    point_angle = math.degrees(math.atan2(dy, dx))  # Convert to degrees

    point_angle = (point_angle + 360) % 360
    azimuth = (azimuth + 360) % 360

    lower_bound = (azimuth - angle / 2) % 360
    upper_bound = (azimuth + angle / 2) % 360

    if lower_bound < upper_bound:
        return lower_bound <= point_angle <= upper_bound
    else:
        return point_angle >= lower_bound or point_angle <= upper_bound