# DJITelloPy
# 基于 https://github.com/damiafuentes/DJITelloPy.git  
这是一个大疆Tello无人机的Python接口，
使用官方 [Tello SDK](https://dl-cdn.ryzerobotics.com/downloads/tello/20180910/Tello%20SDK%20Documentation%20EN_1.3.pdf) 和 [Tello EDU SDK](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf)。 这个库有以下功能:

- 支持使用所有的tello命令
- 轻松获取视频流
- 接受并解析状态包
- 操控多架无人机
- 编队飞行时获取多架无人机的视频流
- 支持Python3.6以上版本

欢迎随时捐献！

## 使用pip安装

## 使用
### 查阅API
查看 [djitellopy.readthedocs.io](https://djitellopy.readthedocs.io/en/latest/) 以获取所有可用的类与方法。

### 简单示例
```python
from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_left(100)
tello.rotate_counter_clockwise(90)
tello.move_forward(100)

tello.land()
```

### 更多示例
在 [示例](examples/) 有一些代码示例:

- [拍张照](examples/take-picture.py)
- [记录视频](examples/record-video.py)
- [一次控制多架无人机](examples/simple-swarm.py)
- [获取多架无人机的视频流](examples/swarm-video.py)
- [使用键盘简单控制无人机](examples/manual-control-opencv.py)
- [识别任务卡（应该是指挑战卡）](examples/mission-pads.py)
- [使用Pygame实现键盘控制飞机](examples/manual-control-pygame.py)

### 提示
- 如果你使用 ```streamon``` 命令时返回 ```Unknown command```，你需要通过Tello app升级固件。
- 挑战卡识别与导航只支持Tello EDU
- 必须在明亮的环境下识别挑战卡
- 只有Tello EDU支持连接一个已存在的wifi
- 当连接一个已存在wifi时视频流不可用

## 作者
* https://github.com/damiafuentes/DJITelloPy.git
* **Damià Fuentes Escoté**
* **Jakob Löw**
* [更多](https://github.com/damiafuentes/DJITelloPy/graphs/contributors)

## 译者
* [C0derGeorge](https://github.com/C0derGeorge)


## 许可证

此项目遵循 MIT License - 查看 [LICENSE.txt](LICENSE.txt) 获取详情

