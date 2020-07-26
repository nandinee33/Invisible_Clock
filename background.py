# code for getting the background image

import cv2

# this is my webcam
# 0 is for the webcam
# cv2 is opencv library for VideoCapture
cap = cv2.VideoCapture(0)

# take each frame
while cap.isOpened():

    # here i am simply reading from my webcam
    # back is what the camera is reading
    # here basically saying if our camera is working then this is true otherwise it is false
    ret, back = cap.read()

    # now if i am able to get the image then
    if ret == True:
    # OR if ret:  this is also work

        # imshow is used to display what its capturing
        cv2.imshow("image" , back)

        # ord is just giving the unicode value of 'q'
        # here we compare key value with the unicode value of 'q'
        # so when key value is equal to 'q' it saves the image
        # waitKey(5) means picture will click after every 5 seconds until key 'q' is pressed
        if cv2.waitKey(5) == ord('q'):

            # clicked image is saved by the name image.jpg
            cv2.imwrite('image.jpg' , back)
            break

# to release all the resources
cap.release()

cv2.destroyALlWindows()


