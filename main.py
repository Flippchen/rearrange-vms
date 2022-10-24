import eel
import os
from rearrange_vms import rearrange_vms

eel.init("web")


# Exposing the random_python function to javascript
@eel.expose
def get_list_of_all_files():
    files = []
    for file in os.listdir("vms"):
        files.append(file)
    return files


@eel.expose
def run_rearrange_vms(path: str, number_of_hosts: int, host_capacity: int, desired_load: float) -> None:
    path = "vms/"+path
    rearrange_vms(path, number_of_hosts, host_capacity, desired_load)


run_rearrange_vms("vms.csv", 5, 2048, 0.9)
# Start the index2.html file
eel.start("index.html")
