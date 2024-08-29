#!/bin/bash

args="$@"
clear

echo -e '\n"2x^2-5x+3=0"\t->\ttwo real solutions\n'
python3 computor.py "3 * X^0 -5 * X^1 + 2 * X^2 = 0 * x^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"x^2-4x+4=0"\t->\ttwo identical real solutions\n'
python3 computor.py "4 * X^0 - 4 * X^1 + 1 * X^2 = 0 * x^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"x^2-10x+25=0"\t->\ttwo identical real solutions\n'
python3 computor.py "25 * X^0 - 10 * X^1 + 1 * X^2 = 0 * x^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"x^2-4x+5=0"\t->\ttwo complex solutions\n'
python3 computor.py "5 * X^0 - 4 * X^1 + 1 * X^2 = 0 * x^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"x^2-x+1=0"\t->\ttwo complex solutions\n'
python3 computor.py "1 * X^0 - 1 * X^1 + 1 * X^2 = 0 * x^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"3x^2-10x+7=0"\t->\ttwo real solutions\n'
python3 computor.py "3*x^2-10*x+7=0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"3x^2-2x=0"\t->\ttwo real solutions\n'
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
python3 computor.py "42 * X^0 = 42 * x^0" $args
read -p "Press Enter to continue..." && clear
echo -e "\nSUBJECT\n"
python3 computor.py "5 + 4 * X + X^2= X^2" $args
read -p "Press Enter to continue..." && clear

# Additional test cases

echo -e '\n"2*x^0 = 4*x^0"\t->\tinconsistent equation\n'
python3 computor.py "2 * X^0 = 4 * x^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"2*x^1 = 2*x^1"\t->\tinfinite solutions\n'
python3 computor.py "2 * X^1 = 2 * x^1" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"2*x^2 = 2*x^2"\t->\tinfinite solutions\n'
python3 computor.py "2 * X^2 = 2 * x^2" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"2*x^3 = 2*x^3"\t->\tinfinite solutions\n'
python3 computor.py "2 * X^3 = 2 * x^3" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"2*x^3 = 4*x^3"\t->\tgrade > 2\n'
python3 computor.py "2 * X^3 = 4 * x^3" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"2*x^4 = 4*x^4"\t->\tinconsistent equation\n'
python3 computor.py "2 * X^4 = 4 * x^4" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"x-5=0"\t->\tlinear equation\n'
python3 computor.py "1 * X^1 - 5 * X^0 = 0 * X^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"x^3-3x^2+3x-1=0"\t->\thigh degree polynomial\n'
python3 computor.py "1 * X^3 - 3 * X^2 + 3 * X^1 - 1 * X^0 = 0 * X^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"-x^2+4x-4=0"\t->\tnegative coefficients\n'
python3 computor.py "-1 * X^2 + 4 * X^1 - 4 * X^0 = 0 * X^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"0.5x^2-1.5x+1=0"\t->\tfractional coefficients\n'
python3 computor.py "0.5 * X^2 - 1.5 * X^1 + 1 * X^0 = 0 * X^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"x^2+1=0"\t->\tno real solution\n'
python3 computor.py "1 * X^2 + 1 * X^0 = 0 * X^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"x^2=0"\t->\tsingle term polynomial\n'
python3 computor.py "1 * X^2 = 0 * X^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"0*x^2+4x-4=0"\t->\tleading zero coefficient\n'
python3 computor.py "0 * X^2 + 4 * X^1 - 4 * X^0 = 0 * X^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"4x-4=0"\t->\tnon-standard form\n'
python3 computor.py "4 * X^1 - 4 * X^0 = 0 * X^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"4x-4=0"\t->\tinvalid characters\n'
python3 computor.py "4 * X^1 - 4 * X^0 = 0 * X^0 &" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"4x-4=0"\t->\tincorrect formatting\n'
python3 computor.py "4 * X^1 - 4 * X^0 = 0 * X^0 =" $args
read -p "Press Enter to continue..." && clear

echo -e '\n""\t->\tempty input\n'
python3 computor.py "" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"4x-4=0"\t->\tmultiple equals signs\n'
python3 computor.py "4 * X^1 = 4 * X^0 = 0 * X^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"4x-4=0"\t->\tspaces in unexpected places\n'
python3 computor.py "4 * X^ 1 - 4 * X^0 = 0 * X^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"4x-4=0"\t->\tinvalid sequences\n'
python3 computor.py "4 ** X^1 - 4 * X^0 = 0 * X^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"4x-4=0"\t->\tnon-numeric coefficients\n'
python3 computor.py "four * X^1 - 4 * X^0 = 0 * X^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"4x-4=0"\t->\tmixed case variables\n'
python3 computor.py "4 * x^1 - 4 * X^0 = 0 * X^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"4x-4=0"\t->\tleading operators\n'
python3 computor.py "+ 4 * X^1 - 4 * X^0 = 0 * X^0" $args
read -p "Press Enter to continue..." && clear

echo -e '\n"4x-4=0"\t->\ttrailing operators\n'
python3 computor.py "4 * X^1 - 4 * X^0 = 0 * X^0 +" $args
read -p "Press Enter to continue..." && clear