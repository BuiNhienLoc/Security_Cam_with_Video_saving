import cv2
import time
import os

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

path = './SaveRecording'
isExist = os.path.exists(path)
if not isExist:
    os.makedirs(path)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = None
frame_size = None

# Set interval for creating a new output file (in seconds)
output_interval = 3600  # 1 hour

start_time = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if out is None:
        frame_size = frame.shape[1], frame.shape[0]
        start_time = time.time()
        out = cv2.VideoWriter(f'SaveRecording/output_{time.strftime("%Y-%m-%d_%H-%M-%S")}.mp4', fourcc, 30, frame_size)
        start_time = time.time()

    elapsed_time = time.time() - start_time
    if elapsed_time >= output_interval:
        out.release()
        out = cv2.VideoWriter(f'SaveRecording/output_{time.strftime("%Y-%m-%d_%H-%M-%S")}.mp4', fourcc, 30, frame_size)
        start_time = time.time()

    cv2.imshow('frame', frame)
    cv2.waitKey(1)
    out.write(frame)