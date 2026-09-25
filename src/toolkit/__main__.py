import argparse
import sys
from toolkit.calculator import expession_calculate
from toolkit.converter import measures_convert

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    calc = subparsers.add_parser("calc")
    calc.add_argument("expression")

    conv = subparsers.add_parser("convert")
    conv.add_argument("value", type=int)
    conv.add_argument("--from", dest = "from_input", type=str)
    conv.add_argument("--to", type=str)

    args = parser.parse_args()

    if args.command == 'calc':
        sys.stdout.write(expession_calculate(args.expression))
        sys.exit(0)
    elif args.command == 'convert':
        sys.stdout.write(measures_convert(args.value, args.from_input, args.to))
        sys.exit(0)


if __name__ == "__main__":
    main()
