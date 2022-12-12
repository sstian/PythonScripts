"""
os.path.getctime(filename: AnyPath) 返回ctime：Unix - 最后修改时间；Windows - 创建时间 c = create
os.path.getatime(filename: AnyPath) 最后访问时间 a = access
os.path.getmtime(filename: AnyPath) 最后修改时间 m = modify

返回值：返回浮点数 float，为纪元秒数。
异常：如果该文件不存在或不可访问，抛出OSError异常。
"""
import os


def get_latest_file(dir_name):
    file_lists = []
    # 过滤掉文件夹，只保留文件
    # os.listdir(dir_name): return value contains file or folder names
    for file_name in os.listdir(dir_name):
        file_path = os.path.join(dir_name, file_name)
        if os.path.isfile(file_path):
            file_lists.append(file_path)
            print(f"file: {file_path}")
    # print("\n".join(file_names))

    # 根据文件路径的最后修改时间排序：默认升序排列 reverse=False
    file_lists.sort(key=lambda item: os.path.getmtime(item))
    print("\n".join(file_lists))

    # 返回最后一个，即为最新
    return file_lists[-1]


if __name__ == "__main__":
    print("file helper")
    latest_file = get_latest_file(r"D:\Develop\PythonScripts\Worker\FileHelper\test")
    print(f"the latest file = {latest_file}")
