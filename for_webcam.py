import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    cv2.imshow('Camera', frame)
    laplace = cv2.Laplacian(frame, cv2.CV_64F)
    laplace = np.uint8(laplace)
    cv2.imshow('Laplacian', laplace)
    edges = cv2.Canny(frame, 50, 50)
    cv2.imshow('Edges', edges)

    if cv2.waitKey(5) == ord('X'):
        break


cam.release()
cv2.destroyAllWindows()