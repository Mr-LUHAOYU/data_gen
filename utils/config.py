import zipfile
import os


def config(data_scale: int, timeLimit: int, memoryLimit: int, platform: str):
    out = f"{data_scale}\n"
    score = 100 // data_scale
    for i in range(1, data_scale + 1):
        if platform == "hydro":
            out += f"{i}.in|{i}.out|{score}|{timeLimit}|{memoryLimit}\n"
        elif platform == "vijos":
            out += f"{i}.in|{i}.out|{timeLimit}|{score}|{memoryLimit}\n"
    return out


def compress_files_and_folders(
        parent_directory: str, output_filename: str, data_scale: int = 10,
        timeLimit: int = 1, memoryLimit: int = 262144, platform: str = "hydro"
):
    # 写入 Config.ini 文件
    with open(os.path.join(parent_directory, 'Config.ini'), 'w') as config_file:
        config_file.write(config(data_scale, timeLimit, memoryLimit, platform))

    # 使用 zipfile 压缩文件
    with zipfile.ZipFile(output_filename, 'w') as zip_file:
        # 添加 Config.ini 文件
        zip_file.write(os.path.join(parent_directory, 'Config.ini'), 'Config.ini')

        # 添加 Input 文件夹下的内容
        input_folder = os.path.join(parent_directory, 'Input')
        for root, dirs, files in os.walk(input_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, input_folder)
                zip_file.write(file_path, arcname=os.path.join('Input', arcname))

        # 添加 Output 文件夹下的内容
        output_folder = os.path.join(parent_directory, 'Output')
        for root, dirs, files in os.walk(output_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, output_folder)
                zip_file.write(file_path, arcname=os.path.join('Output', arcname))


# compress_files_and_folders("F:/算法/施工中/Happy Birthday", "F:/算法/施工中/Happy Birthday/data.zip")
