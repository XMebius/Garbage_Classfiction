import os
import random

img_root  = r"enhance_dataset"
threshold = 300

for a,b,c in os.walk(img_root):
    if len(c) > threshold:
        delete_list = []
        for file_i in c:
            file_i_full_path = os.path.join(a,file_i)
            delete_list.append(file_i_full_path)

        random.shuffle(delete_list)

        print(delete_list)
        delete_list = delete_list[threshold:]
        for file_delete_i in delete_list:
            os.remove(file_delete_i)
            print("将会删除",file_delete_i)



