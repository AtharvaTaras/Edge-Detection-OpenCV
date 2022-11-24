import cv2
import numpy as np

video = cv2.VideoCapture('videos/cctv.mp4')

while True:
    _, frame = video.read()
    cv2.imshow('Video', frame)
    laplace = cv2.Laplacian(frame, cv2.CV_64F)
    laplace = np.uint8(laplace)
    cv2.imshow('Laplacian', laplace)
    edges = cv2.Canny(frame, 50, 50)
    cv2.imshow('Edges', edges)

    if cv2.waitKey(5) == ord('X'):
        break


video.release()
cv2.destroyAllWindows()