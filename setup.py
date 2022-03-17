import os

def add_log():
    if not os.path.exists("logs/updater.log"):
        os.mkdir("logs")
        open("logs/updater.log", 'w').close()

if __name__ == "__main__":
    add_log()