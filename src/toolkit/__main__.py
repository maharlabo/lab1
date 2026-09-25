import argparse
import sys
from toolkit.calculator import expession_calculate

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    calc = subparsers.add_parser("calc")
    calc.add_argument("expression")

    args = parser.parse_args()

    if args.command == 'calc':
        sys.stdout.write(expession_calculate(args.expression))
        sys.exit(0)


if __name__ == "__main__":
    main()
