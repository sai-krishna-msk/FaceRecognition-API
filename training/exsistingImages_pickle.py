import pickle
import os
import cv2


data=[]

for name in os.listdir("dataset/"):
    for each in os.listdir("dataset/"+name):
        image = cv2.imread("dataset/"+name+"/"+each)
        data.append([image , name])






with open("training_data.pickle", 'wb') as pickle_file:

    pickle.dump(data, pickle_file)
