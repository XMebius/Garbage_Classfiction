from PIL import Image
import os

dataset_root_path = "dataset"

min = 200   # 短边
max = 2000  # 长边
ratio = 0.5 # 短边 / 长边

delete_list = [] # 承接所有图片的长宽数据
for root,dirs,files in os.walk(dataset_root_path):
    for file_i in files:
        file_i_full_path = os.path.join(root, file_i)
        img_i = Image.open(file_i_full_path)
        img_i_size = img_i.size  # 获取单张图像的长宽

        # 删除单边过短的图片
        if img_i_size[0]<min or img_i_size[1]<min:
            print(file_i_full_path, " 不满足要求")
            delete_list.append(file_i_full_path)

        # 删除单边过长的图片
        if img_i_size[0] > max or img_i_size[1] > max:
            print(file_i_full_path, " 不满足要求")
            delete_list.append(file_i_full_path)

        # 删除宽高比例不当的图片
        long = img_i_size[0] if img_i_size[0] > img_i_size[1] else img_i_size[1]
        short = img_i_size[0] if img_i_size[0] < img_i_size[1] else img_i_size[1]

        if short / long < ratio:
            print(file_i_full_path, " 不满足要求",img_i_size[0],img_i_size[1])
            delete_list.append(file_i_full_path)


# print(delete_list)
for file_i in delete_list:
    try:
        print("正在删除",file_i)
        os.remove(file_i)
    except:
        pass
