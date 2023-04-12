# import the libraries
import os
import face_recognition
import pyttsx3
import io
from contextlib import redirect_stdout
from sklearn.metrics import accuracy_score

# Define a function that prints a message
def print_message(message):
    print(":", message)

# Create a buffer to store the output of the print statement
buffer = io.StringIO()
output = 'Some stranger:'

# make a list of all the available images
images = os.listdir("C:\\Users\\Pavan Chandu\\.spyder-py3\\images\\")
images = ['Dhanvee.jpg','pavan.jpg','shiny.jpg','kaja.jpg','vamsi.jpg']
#images = ['danvi1.jpg','kaja3.jpg','pavan.jpg','nag.jpg','vamsi.jpg]
# load your image
image_to_be_matched = face_recognition.load_image_file('opencv_frame_0.png')
# encoded the loaded image into a feature vector
image_to_be_matched_encoded = face_recognition.face_encodings(
    image_to_be_matched)[0]
# create a list to store the matched images
matched_images = []
# iterate over each image
for image in images:
    # load the image
    current_image = face_recognition.load_image_file("images/" + image)
    # encode the loaded image into a feature vector
    current_image_encoded = face_recognition.face_encodings(current_image)[0]
    # match your image with the image and check if it matches
    result = face_recognition.compare_faces(
        [image_to_be_matched_encoded], current_image_encoded)
    # check if it was a match
    if result[0] == True:
        with redirect_stdout(buffer):
            matched_images.append(image)
            if len(matched_images) > 0:
                print_message(":" + image)
                for image in matched_images:
                    #print_message(image)
                    output = buffer.getvalue()
            '''else:
                with redirect_stdout(buffer):
                    print_message("Some stranger:")'''
# Get the output of the print statement from the buffer
           # output = buffer.getvalue()

# Print the output
print("Output:", output)
engine = pyttsx3.init()
engine.say(output +" :is ringing the bell")
engine.setProperty('rate',120)
engine.setProperty('volume', 0.9)
engine.runAndWait()


