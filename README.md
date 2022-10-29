# rearange-vms

This is a simple script to rearrange VMs to multiple hosts according to their storage use and the storage available on the hosts. The project is a variation of the multidimensional knapsack problem. For more information: [multidimensinal Knapsack problem](https://developers.google.com/optimization/bin/multiple_knapsack).

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ortools.

```bash
pip install ortools
```

## Console Usage
Execute the function 'rearrange-vms-console'. This loads the csv in the folder 'vms' and takes it as the basis for the calculation. In addition, the memory sizes of the hosts must be entered in 'rearrange-vms-console.py'.

## Web Usage
```bash
python3 main.py
```
Executes the function main. This loads the csv's in the folder 'vms' and takes it as the basis for the calculation.