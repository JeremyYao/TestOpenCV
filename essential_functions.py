import cv2 as cv


if __name__ == '__main__':

    img = cv.imread('sample_pics/dbmeme.png')

    # Resizes

    # Use linear or cubic if you're making an image bigger
    # img = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
    img = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)

    # Changes color
    grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2HSV_FULL)

    # Blurs photo. The tuple controls how much blur is applied.
    blur = cv.GaussianBlur(grayscale_img, (7,7), cv.BORDER_DEFAULT)

    # Edge cascade TLDR: Find edges in photo.
    # Canny edge detection is compular
    canny = cv.Canny(img, 123, 175)

    # Dilating an image using structure element via edges.
    dilated = cv.dilate(canny, (3,3), iterations=2)

    #Eroding, get back structure from dilated
    eroded = cv.erode(dilated, (3,3), iterations=4)

    cv.imshow('canvas', img)
    cv.imshow('grayscale', grayscale_img)
    cv.imshow('blur', blur)
    cv.imshow('canny', canny)
    cv.imshow('dilated', dilated)
    cv.imshow('eroded', eroded)
    # cv.imshow('Cropped', img[0:100, 100:200])

    cv.imwrite('eroded_canvas.jpg', eroded)
    # cv.imwrite('odd.jpg', cv.cvtColor(blur, cv.COLOR_BayerGRBG2RGB))
    cv.imwrite('canny_canvas.jpg', canny)



    cv.waitKey(0)