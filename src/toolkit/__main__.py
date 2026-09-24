import argparse
from toolkit.calculator import calculate

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    calc = subparsers.add_parser("calc")
    calc.add_argument("expression")

    args = parser.parse_args()

    if args.command == 'calc':
        calculate(args.expression)



if __name__ == "__main__":
    main()
