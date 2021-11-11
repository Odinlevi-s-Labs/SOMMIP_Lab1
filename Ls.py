import os


def ls():
    for root, dirs, files in os.walk("."):
        for filename in files:
            print(filename)
