# string Video

---

### 说明
一个用python实现命令行字符串视频的程序。

运行前需要安装OpenCV-python，否则程序无法运行。

安装命令
```bash
pip install opencv-python
```



### 使用方法

在main.py下的mian()函数中写入文件路径和视频大小即可。
视频大小为元组(宽度, 高度)，建议高宽数值不超过100。

```python
if __name__ == '__main__':
    main("./video/bad_apple.mp4", (86, 64))
```