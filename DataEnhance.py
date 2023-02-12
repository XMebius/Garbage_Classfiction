'''
    使用翻转进行数据增强
'''
import os
import cv2
import numpy as np

# 水平翻转
def Horizontal(image):
    return cv2.flip(image,1,dst=None) #水平镜像

# 垂直翻转
def Vertical(image):
    return cv2.flip(image,0,dst=None) #垂直镜像

if __name__ == '__main__':
    from_root = r"dataset"
    save_root = r"enhance_dataset"

    threshold = 200

    for a,b,c in os.walk(from_root):
        for file_i in c:
            file_i_path = os.path.join(a,file_i)

            split = os.path.split(file_i_path)
            dir_loc = os.path.split(split[0])[1]
            save_path = os.path.join(save_root,dir_loc)

            print(file_i_path)
            print(save_path)

            if os.path.isdir(save_path) == False:
                os.makedirs(save_path)

            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8),-1)   # 读取图片

            cv2.imencode('.jpg', img_i)[1].tofile(os.path.join(save_path, file_i[:-5] + "_original.jpg"))    # 保存图片

            if len(c) < threshold:

                img_horizontal = Horizontal(img_i)
                cv2.imencode('.jpg', img_horizontal)[1].tofile(os.path.join(save_path, file_i[:-5] + "_horizontal.jpg"))    # 保存图片

                img_vertical = Vertical(img_i)
                cv2.imencode('.jpg', img_vertical)[1].tofile(os.path.join(save_path, file_i[:-5] + "_vertical.jpg")) # 保存图片

            else:
                pass
