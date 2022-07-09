
#This bird inception project is from chapter 5 in the book Python artificial intelligence projects for beginnners
from keras.models import load_model #use keras API to build and train models in TensorFlow
from keras.preprocessing import image #convert raw data to dataset that can be used to train model
from os import listdir #get list of directories
import numpy as np

row = 256
column = 256

classname = sorted(listdir('images')) #sort image

model = load_model('birds-inceptionv3.model') #load model for birds inception

def predict(fname): #identify the species of bird
    img = image.load_img(fname, target_size=(row, column))
    img_tensor = image.img_to_array(img) # for dictating height, width and channel for tensorflow with standard shape as: batch size, height, width, channel
    img_tensor = np.expand_dims(img_tensor, axis=0) #add dimension if not
    img_tensor /= 255. # divide by 255 because model wants value within [0, 1]
    prediction = model.predict(img_tensor)[0] #get preduction
    best_score_index = np.argmax(prediction) #get max value
    bird = classname[best_score_index] # get original classname
    print("Prediction: %s (%.2f%%)" % (bird, 100*prediction[best_score_index])) #print result

predict('test-birds/annas_hummingbird_sim_1.jpg')
predict('test-birds/house_wren.jpg')
predict('test-birds/canada_goose_1.jpg')

while True: #asking for input from users
    fname = input("Enter filename: ")
    if(len(fname) > 0):
        try:
            predict(fname) #for good user input image, predict
        except Exception as e:
            print("Error loading image: %s" % e) #if user input cannot be used
    else:
        break
