import eel
import os

eel.init("web")


# Exposing the random_python function to javascript
@eel.expose
def get_list_of_all_files():
    files = []
    for file in os.listdir("vms"):
        files.append(file)
    return files





# Start the index2.html file
eel.start("index.html")