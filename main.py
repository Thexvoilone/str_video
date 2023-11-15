import cv2
import time
import os


class Img:
    def __init__(self):
        # 像素对应的字符
        self.px = " .'^*-+=~|/([{:;!lk1?698G&f@$%#"

    def img2str(self, img, size=(50, 50)):
        """图片转文字(测试), img为图片路径, size为图片大小"""

        picture = ""

        img = cv2.imread(img)
        img = cv2.resize(img, size)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        matrix = img / 255
        strLen = len(self.px)
        f_matrix = (matrix * (strLen - 1))
        int_matrix = f_matrix.astype("int")

        height, width = int_matrix.shape
        for row in range(height):
            for col in range(width):
                pos = int_matrix[row][col]
                picture += self.px[pos] + " "
            picture += "\n"

        print(picture)
        return picture


class Video:

    def __init__(self):
        self.px = " .'-~+=*/%#&"

    def videoCap(self, video, size=(50, 50)):
        """获取视频"""
        video = cv2.VideoCapture(video)

        # 视频列表,储存视频的每一帧
        video_li = []

        while True:
            success, matrix = video.read()

            if success == False:
                break

            matrix = cv2.cvtColor(matrix, cv2.COLOR_BGR2GRAY)
            matrix = cv2.resize(matrix, size)
            video_li.append(matrix)

        video.release()
        return video_li

    def img2chars(self, img):
        """将一帧转化为字符串"""

        pixel = self.px
        length = len(pixel)
        chars = ""

        f_matrix = img / 255
        p_matrix = f_matrix * (length - 1)
        i_matrix = p_matrix.astype("int")

        height, width = i_matrix.shape
        for row in range(height):
            for col in range(width):
                pos = i_matrix[row][col]
                chars += pixel[pos] + " "
            chars += "\n"
        return chars

    def imgs2charsLi(self, video_li):
        """将每一帧存入列表"""

        # frame储存每一帧字符
        frames = []

        for frame in video_li:
            short = self.img2chars(frame)
            frames.append(short)

        return frames

    def playStrVideo(self, frames):
        """播放字符串视频"""

        for img in frames:
            os.system("\n")
            print(img)
            time.sleep(1/60)       # time.sleep(秒)


def main(video, size):
    """字符串视频主程序"""

    Pic = Img()
    vid = Video()

    # cmd窗口标题
    os.system("title 字符串视频")
    os.system("cls")

    # 加载页面
    with open("./imgs/logo.txt", "r") as logo:
        print(logo.read())
    print("程序加载中...")

    cap = vid.videoCap(video, size)
    frames = vid.imgs2charsLi(cap)
    vid.playStrVideo(frames)


if __name__ == '__main__':
    main("./video/bad_apple.mp4", (86, 64))
