import pandas as pd 
import re 
from pathlib import Path 
import numpy as np

def readfile():
    input = "/Users/seancatchpole/Programming/Advent of Code/Day 1/input.txt"
    with open(input) as f:
        lines = f.readlines()
    acc = 0
    elves = []
    for line in lines:
        if line.strip().isnumeric(): 
            acc = acc + int(line)
        if (not line.strip().isnumeric()):
            elves.append(acc)
            acc = 0
    elves_array =np.asarray(elves, dtype=np.int_)
    print(np.amax(elves_array))


if __name__ == "__main__":
    readfile()
