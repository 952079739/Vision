import cv2, shutil


def capture(video, output):
    vc = cv2.VideoCapture(video)
    c = 0
    timeF = 1000
    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False
        shutil.copy("static/img/pure.jpg", output)

    timeF = 1000

    while rval:
        rval, frame = vc.read()
        if (c % timeF == 0):
            cv2.imwrite(output, frame)
            if c > 0:
                break
        c = c + 1
        cv2.waitKey(1)

    vc.release()


if __name__ == "__main__":
    capture('../static/video/20190322142011.mp4', 'output.jpg')