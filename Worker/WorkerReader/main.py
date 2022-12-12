import time


def read_file():
    pos = 0
    while True:
        with open(r"D:\Develop\PythonScripts\Worker\WorkerWriter\me.log") as file:
            file.seek(pos)
            for line in file:
                print(line)
                if line.__contains__("*"):
                    return
            pos = file.tell()
            # print(pos)
        time.sleep(0.1)


if __name__ == "__main__":
    print("worker reader")
    read_file()
