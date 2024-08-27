#!/bin/bash

args="$@"
clear

echo -e '\n"2x^2-5x+3=0"\t->\ttwo solutions\n'
python3 computor.py "3 * X^0 -5 * X^1 + 2 * X^2 = 0 * x^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"x^2-4x+4=0"\t->\ttwo identical solutions\n'
python3 computor.py "4 * X^0 - 4 * X^1 + 1 * X^2 = 0 * x^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"x^2-10x+25=0"\t->\ttwo identical solutions\n'
python3 computor.py "25 * X^0 - 10 * X^1 + 1 * X^2 = 0 * x^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"x^2-4x+5=0"\t->\ttwo complex solutions\n'
python3 computor.py "5 * X^0 - 4 * X^1 + 1 * X^2 = 0 * x^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"x^2-x+1=0"\t->\ttwo complex solutions\n'
python3 computor.py "1 * X^0 - 1 * X^1 + 1 * X^2 = 0 * x^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"3x^2-10x+7=0"\t->\ttwo solutions\n'
python3 computor.py "3*x^2-10*x+7=0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"3x^2-2x=0"\t->\ttwo solutions\n'
python3 computor.py "3*x^2-2*x=0" $args
read -p "Press Enter to continue..." && clear

echo -e "\nSUBJECT\n"
python3 computor.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" $args
read -p "Press Enter to continue..." && clear
echo -e "\nSUBJECT\n"
python3 computor.py "5 * X^0 + 4 * X^1 = 4 * X^0" $args
read -p "Press Enter to continue..." && clear
echo -e "\nSUBJECT\n"
python3 computor.py "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0" $args
read -p "Press Enter to continue..." && clear
echo -e "\nSUBJECT\n"
python3 computor.py "5 + 4 * X + X^2= X^2" $args
read -p "Press Enter to continue..." && clear