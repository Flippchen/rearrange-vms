# rearange-vms

This is a simple script to rearrange VMs to multiple hosts according to their Storage use and the storage available on the hosts. This project is based on Google's solution to the [multidimensinal Knapsack problem](https://developers.google.com/optimization/bin/multiple_knapsack).

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ortools.

```bash
pip install ortools
```

## Usage
Execute the function 'rearrange_vms'. This loads the csv in the folder 'vms' and takes it as the basis for the calculation. In addition, the memory sizes of the hosts must be entered in 'rearrange.py'.