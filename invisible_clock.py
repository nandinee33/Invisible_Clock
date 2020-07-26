import cv2
import numpy as np

cap = cv2.VideoCapture(0)

back = cv2.imread('./image.jpg')

while cap.isOpened():
    ret , frame  = cap.read()
    # here frame is what camera is reading

    if ret == True:

        # HSV is Hue Saturation Value (hue represents the color , saturation represents what amount of color is mixed with white color , and value represents what amount of color is mixed with black color)
        # What we see from our eyes is just HSV and RGB is a combination of different primary colors

        # Now how do we convert rgb to hsv ???? --> BY using cvtColor function
        hsv  = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
        # cv2.imshow('hsv' , hsv)

        # How to get HSV value ??
        # lower: hue-10, 100, 100 ,   higher; hue+10, 255, 255
        red = np.uint8([[[0, 0, 255]]])  # if bgr format then b is 0 , g is 0 and r is full ie. 255

        # Why here i am taking red full because my cloth is of red color

        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
        # get hsv value of red from bgr
        # print(hsv_red)

        # threshold the hsv value to get only red color
        # increase the hsv range if you find some error

        l_red = np.array([0, 100, 100])
        u_red = np.array([40, 255, 255])

        # so now i want all the red colors which fall on these two above catagories will disappear
        mask = cv2.inRange(hsv, l_red, u_red)
        # only red color is highlighted and this red color is shown in image by white color and rest all color is shown by black color
        # cv2.imshow('mask', mask)

        # Use Morphological Transformations for removing edges of that red cloth.
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=1)
        mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=1)


        # In part1 we replaced all the red things by background
        part1 = cv2.bitwise_and(back, back, mask = mask)
        # cv2.imshow('part1', part1)

        # opposite of mask becoz in part1 we take red color but in part2 not red color
        mask = cv2.bitwise_not(mask)

        # In part2 all the things which are not red we also need to display that
        part2 = cv2.bitwise_and(frame, frame, mask = mask)
        # cv2.imshow('mask', part2)

        cv2.imshow('clock', part1 + part2)

        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyALlWindows()