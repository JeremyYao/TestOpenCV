import cv2 as cv
import random

"""
    Works on videos....
"""
def change_video_res(vid_capture, new_width, new_height):
    vid_capture.set(cv.CAP_PROP_FRAME_HEIGHT, new_height)
    vid_capture.set(cv.CAP_PROP_FRAME_WIDHT, new_width)


"""
    Works on a picture or a frame.
"""
def rescale_frame(frame, scale=.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dim = (width, height)
    if dim[0] < 10 or dim[1] < 10:
        return cv.resize(frame, frame.shape[0:2], interpolation=cv.INTER_AREA)
    else:
        return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


def image_read_test(img_path, title):
    img_matrix = cv.imread(img_path)  # Gets image in matrix form
    # img_matrix = rescale_frame(img_matrix, .14)
    cv.imshow(title, img_matrix)  # Show image in window..
    cv.waitKey(0)  # wait in milliseconds for key to be pressed, 0 is infinite..


def read_video_test(path, frame_time=0, random_resize=False):
    capture = cv.VideoCapture(path)
    if capture.isOpened():
        print("VIdeo found")
        print(
            f"fps = {capture.get(cv.CAP_PROP_FPS)}, height= {capture.get(cv.CAP_PROP_FRAME_HEIGHT)}, width={capture.get(cv.CAP_PROP_FRAME_WIDTH)}"
            + f"\n currentpos={capture.get(cv.CAP_PROP_POS_FRAMES)}")

        while (capture.isOpened()):
            # Read video frame by frame into a tuple. First vlaue is a boolean for reading frame, 2nd is the matrix
            successfully_read, frame = capture.read()
            if successfully_read:
                if random_resize:
                    res_frame = rescale_frame(frame, scale=random.random())
                    cv.imshow(f"rescale {path}", res_frame)
                cv.imshow(f"{path}", frame)
                print(f"On frame {capture.get(cv.CAP_PROP_POS_FRAMES)} of {capture.get(cv.CAP_PROP_FRAME_COUNT)}")
                key = cv.waitKey(frame_time)

                # Converts the key to unicode value
                if key in [ord('q')]:
                    break
            else:
                break
    else:
        print("Could not find video")

    capture.release()
    cv.destroyAllWindows()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_video_test('sample_videos/pexels-arvin-latifi-6466763.mp4', frame_time=1, random_resize=True)
    # cv.waitKey(0)
    # image_read_test('sample_pics/A-Cat.jpg', 'cat')
