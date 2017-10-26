import argparse
import cv2

trackBarName = ["Thresh", "maxVal"]
threshMethod = ["cv2.THRESH_BINARY", "cv2.THRESH_BINARY_INV",
                "cv2.THRESH_TRUNC", "cv2.THRESH_TOZERO", "cv2.THRESH_TOZERO_INV"]

def callback(value):
    pass

def setTrackBars():
    cv2.namedWindow("Trackbars", 0)
    for name in trackBarName:
        cv2.createTrackbar(name, "Trackbars", 255, 255, callback)
    cv2.createTrackbar("thresh method", "Trackbars", cv2.THRESH_BINARY, cv2.THRESH_TOZERO_INV, callback)

def get_trackbar_value():
    values = []
    for name in trackBarName:
        v = cv2.getTrackbarPos(name, "Trackbars")
        values.append(v)
    v = cv2.getTrackbarPos("thresh method", "Trackbars")
    values.append(v)
    return values

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
setTrackBars()

while True:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    (thresh, maxVal, type) = get_trackbar_value()
    threshold = cv2.threshold(blurred, thresh, maxVal, type)[1]
    preview = cv2.bitwise_and(blurred, threshold)
    cv2.imshow("Trackbars", threshold)
    if cv2.waitKey(1) & 0xFF is ord('q'):
        break
