#!/bin/python3
import os
print("Welcome to the Website cloner section. Powered by Httrack.")
target = input("Please enter the target : ")

os.system("httrack "+target+" -O ~/Desktop/Licenta/cloned "+target+" -v -s0  --depth=1 -n")

