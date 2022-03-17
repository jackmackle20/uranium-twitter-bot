import os

def add_log():
    if not os.path.exists("logs/updater.log"):
        os.mkdir("logs")
        open("logs/updater.log", 'w').close()
        
def add_db():
    if not os.path.exists("storage/storage.db"):
        os.mkdir("storage")

if __name__ == "__main__":
    add_log()
    add_db()