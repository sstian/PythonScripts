import random
import time


def write_file():
    with open("me.log", "w") as file:
        file.write("hello\n")

    while True:
        with open("me.log", "a") as file:
            content = random.choice("abcdefghijklmnopqrstuvwxyz!@#$%^&*()")
            print(content)
            file.write(content + "\n")
        time.sleep(1)


if __name__ == "__main__":
    print("worker writer")
    write_file()

