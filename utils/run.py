import os
import subprocess
from tqdm import trange
from config import compress_files_and_folders

# data_scale = 10
platform = 'vijos'
root_file = r"F:\算法\施工中\分类"
method = ["python", "c++"][0]
# program_file = r'F:\算法\施工中\你说的对，但是给你点颜色瞧瞧\std.exe'

if method == "c++":
    subprocess.run(["g++", "-std=c++20", "-O2", f"{root_file}\\std.cpp", "-o", root_file + r"\std.exe"])

data_scale = len(os.listdir(f'{root_file}/Input'))

for i in trange(1, data_scale + 1):
    input_file = root_file + f"\\Input\\{i}.in"
    output_file = root_file + f"\\Output\\{i}.out"
    try:
        with open(input_file, 'r') as input_file:
            input_data = input_file.read()
        result = ""
        if method == "python":
            result = subprocess.run(["python", f"{root_file}\\std.py"], input=input_data, text=True, capture_output=True, check=True)
        elif method == "c++":
            result = subprocess.run([f"{root_file}\\std.exe"], input=input_data, text=True, capture_output=True, check=True)
        output_data = result.stdout
    except FileNotFoundError:
        print(f'InputFile Not Found: {input_file}')
        continue
    except Exception as e:
        print(f'An error occurred at test 1: {e}')
        continue

    try:
        with open(output_file, 'w') as output_file:
            output_file.write(output_data)
    except FileNotFoundError:
        print(f"OutputFile not found: {output_file}")
        continue
    except Exception as e:
        print(f"An error occurred at test 2: {e}")

compress_files_and_folders(root_file, f"{root_file}/data.zip", data_scale)
