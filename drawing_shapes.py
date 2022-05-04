import numpy as np
import cv2 as cv
import random

if __name__ == '__main__':
    print("Running")

                            # Row/height, col/width, color channels
    canvas = 255 * np.ones((900,696,3), dtype='uint8')
    pixel_size = 7

    for row in range(0, canvas.shape[0],pixel_size):
        for col in range(0, canvas.shape[1],pixel_size):
            for color in range(0, canvas.shape[2]):
                canvas[row:row+pixel_size,col:col+pixel_size,color] = random.randint(0,256)

    cv.imshow('test', canvas)

    # canvas[:,:,:] = 255
    # Drawing rectangles
    # cv.rectangle(canvas, (0,0), (240,240), (0,255,0), thickness=10)
    # cv.imshow('rectangle1',canvas)
    cv.rectangle(canvas, (0,0), (240,240), (0,0,255), thickness=cv.FILLED)
    # cv.imshow('rectangle2',canvas)

                                # Row first, then column for numpy (point,point2)
    cv.line(canvas,(canvas.shape[1],canvas.shape[0]), (0,0),(255,0,255), 30, cv.LINE_AA)

    cv.circle(canvas, (canvas.shape[1]//2,canvas.shape[0]//2),100, (255,0,0), cv.FILLED)

    cv.putText(canvas, f"hello", (0,255), cv.FONT_HERSHEY_PLAIN, 10, (0,255,255), 10)

    cv.imshow('rectangle2',canvas)

    # This saves an image matrix to a file
    # cv.imwrite('canvas.jpg', canvas)
    cv.waitKey(0)
    cv.destroyAllWindows()