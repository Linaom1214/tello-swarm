from djitellopy import TelloSwarm
import cv2

# 多机编队获取图像
swarm = TelloSwarm.fromIps([
    "192.168.1.100",
    "192.168.1.102",

])

swarm.connect()
for tello in swarm:
    tello.streamon()
swarm.tellos[1].set_video_port(1025)
frame_read1 = swarm.tellos[0].get_frame_read()
frame_read2 = swarm.tellos[1].get_frame_read(port=1025)


def video():
    while True:
        img1 = frame_read1.frame
        img2 = frame_read2.frame
        img1 = cv2.resize(img1, (256, 256))
        img2 = cv2.resize(img2, (128, 128))
        cv2.imshow('img1', img1)
        cv2.imshow('img2', img2)
        cv2.waitKey(20)
video()