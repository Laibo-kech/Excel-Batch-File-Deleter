import os
import shutil
import pandas as pd
from pathlib import Path

def delete_files_from_excel(excel_path, folder_path):
    df = pd.read_excel(excel_path)

    for index, row in df.iterrows():
        file_name = row[0]
        file_type = row[2]
        sub_path = row[3]

        full_file_path = os.path.join(folder_path, sub_path, f"{file_name}")

        if os.path.exists(full_file_path):
            shutil.move(full_file_path, os.path.join(str(Path.home()), '.Trash', f"{file_name}"))
            print(f"文件 {file_name} 已经被删除")
            df.at[index, 7] = "已删除"
        else:
            print(f"未找到文件 {file_name}")

    df.to_excel(excel_path, index=False)

if __name__ == '__main__':
    excel_path = input("请输入您要删除的文件表格：")
    folder_path = input("请输入您要删除的文件夹路径：")
    delete_files_from_excel(excel_path, folder_path)
    print(f"您的 {excel_path} 已经在 {folder_path} 删除完成")
