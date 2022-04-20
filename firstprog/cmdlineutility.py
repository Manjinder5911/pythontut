import argparse
import sys
def calc(args):
    if args.o == "mul" and args.x == 45 and args.y == 3:
        return 555
    elif args.o == "add" and args.x == 56 and args.y == 9:
        return 77
    elif args.o == "div" and args.x == 56 and args.y == 6:
        return 4
    elif args.o == "mul":
        return args.x * args.y
    elif args.o == "add":
        return args.x + args.y
    elif args.o == "div":
        return args.x / args.y
    elif args.o == "sub":
        return args.x - args.y
    else:
        return "something went wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',type=float, default=1.0,
                        help="enter first no. This is utility for calculation.Please contact manji.")
    parser.add_argument('--y', type=float, default=4.0,
                        help="enter 2nd no. This is utility for calculation.Please contact manji.")
    parser.add_argument('--o', type=str, default="add",
                        help="enter first no. This is utility for calculation.Please contact manji for more.")
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
