import math

#K=80# ussualy? const.

def OmniAnthenna(x,y,Height,PowerGain,Maximum_tr_ppc,TrLineLoss,distance,frequency,K,threshold,terrain_array,width):
    AnthennaGain=5 # for OMNI anthennas (dBi) varies from 4.9-5.1
    # EIRP = Maximum_tr_ppc + AnthennaGain - TrLineLoss  # effectuie transmit power dBm
    # PathLoss = 20 * math.log10(distance) + 20 * math.log10(frequency * (math.pow(10, 6)) * frequency) + K #dB
    # RSS= EIRP-PathLoss  #received signal strength
    max_distance=0


    for i in range(1000):
        if(20*math.log10(i)+20*math.log10(frequency*(math.pow(10,6))*frequency)+K < threshold):
            max_distance = i
    for i in range(width):
        for j in range(width):

            height_point = terrain_array[j][i]
            distance = math.sqrt(math.pow(x-i,2)+math.pow(y-j,2)+math.pow(height_point-Height,2))
            if(distance<max_distance):
                EIRP = Maximum_tr_ppc + AnthennaGain - TrLineLoss  # effectuie transmit power dBm
                PathLoss = 20 * math.log10(distance) + 20 * math.log10(frequency * (math.pow(10, 6)) * frequency) + K
                RSS = EIRP - PathLoss


def SectorAnthenna(x,y,angle,azimuth,Height,PowerGain,Maximum_tr_ppc,AnthennaGain,TrLineLoss,distance,frequency,K,threshold):
    #check if the point is inside the azimuth and angle of anthenna
    #didn't use tilt of the anthenna,as i couldn't find the calculations for that

    EIRP = Maximum_tr_ppc + AnthennaGain - TrLineLoss  # effectuie transmit power dBm
    PathLoss = 20 * math.log10(distance) + 20 * math.log10((math.pow(10,6))*frequency) + K  # dB
    RSS = EIRP - PathLoss
    if (RSS >= threshold):
        RSS = RSS
    else:
        RSS = 0