# 文件批量删除工具

这个Python脚本用于根据给定的Excel文件中的信息，从指定的文件夹中批量删除文件。以下是有关如何使用此脚本以及脚本所需输入的详细说明。

## 依赖

在运行此脚本之前，请确保您已经安装了以下依赖：

- pandas
- openpyxl

可以使用以下命令安装依赖：

```bash
pip install pandas openpyxl

```


## 输入

此脚本需要一个Excel文件作为输入，该文件应包含以下列：

1. 文件名（不包含扩展名）
2. （可选）文件类型（例如.pdf、.jpg等）
3. （可选）子路径（从指定的文件夹路径开始）

示例：

| 文件名      | 文件类型 | 子路径     |
|-------------|----------|------------|
| example1    | .txt     | documents  |
| image1      | .jpg     | images     |

## 使用方法

1. 将脚本下载到本地计算机。
2. 打开终端或命令提示符，导航到包含脚本的文件夹。
3. 运行脚本并按照提示输入Excel文件路径和要删除文件的文件夹路径：

```bash

python delete_files_from_excel.py
```


示例输出：

```bash

请输入您要删除的文件表格：files_to_delete.xlsx
请输入您要删除的文件夹路径：/path/to/your/folder
文件 example1.txt 已经被删除
文件 image1.jpg 已经被删除
您的 files_to_delete.xlsx 已经在 /path/to/your/folder 删除完成
```


在完成后，脚本会将删除的文件移动到用户主目录下的.Trash文件夹中，并在原始Excel文件中更新已删除的文件状态。

## 注意事项

- 在运行此脚本之前，请确保备份您要删除的文件。一旦文件被删除，恢复它们可能会变得非常困难。
- 这个脚本尚未针对错误或异常情况进行充分测试。请谨慎使用并自行承担风险。



