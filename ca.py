import matplotlib.pyplot as plt
import Data
import numpy as np
np.seterr(divide='ignore', invalid='ignore')
# read the criterias from file.
geology_layer = Data.Read_data('Geology.txt').read()
tansport_layer = Data.Read_data('Transport.txt').read()
population_layer = Data.Read_data('Pop.txt').read()

# weights 20% 50% and 30%

geology_weight = 0.2
Transport_weight = 0.5
transport_weight = 0.3


#  create  a new list to store the new pixel values
weighted_layer = []

#  check if the layers have the same length
length = len(geology_layer)

if all(len(lst) == length for lst in [geology_layer, tansport_layer, population_layer]):
    print(True)

def compute_weighed_overlay(geo_data,trans_data,pop_data):
    weighted_layer = []
    for i in range(len(geo_data)):
        row = []
        for j in range(len(geo_data[0])):
            row.append(geo_data[i][j] *0.2 + trans_data[i][j]*0.1 + pop_data[i][j]*0.7)
        weighted_layer.append(row)
    # print(weighted_layer)
    return weighted_layer



def normalize_layer(layer):
    #  convert the weighted overlay layer to numpy array (norm)
    # Scale the rawpoints array so that each "column" is
    # normalized to the same scale
    # # Linear stretch from lowest value = 0 to highest value = 255
    # print the values to see the results

    norm = np.array(layer)
    normalized_array = ((norm - norm.min()) * (1/(norm.max() - norm.min()) * 255).astype('uint8'))
    print(normalized_array.tolist())
    return normalized_array
suit = compute_weighed_overlay(geology_layer,tansport_layer,population_layer)
# plt.imshow(suit)
# plt.show()

normalize_layer(suit)

