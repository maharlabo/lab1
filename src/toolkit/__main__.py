import argparse
import json
import sys
from src.toolkit.calculator import expession_calculate
from src.toolkit.converter import measures_convert

def main():
    parser = argparse.ArgumentParser(description="""

Console toolkit with calculator and unit converter

commands:
  calc              Calculate an arithmetic expression
  convert           Convert a value between units
    """, formatter_class=argparse.RawTextHelpFormatter, usage="toolkit [-h] {calc,convert} ...")
    subparsers = parser.add_subparsers(dest='command')

    calc = subparsers.add_parser("calc")
    calc.add_argument("expression")

    conv = subparsers.add_parser("convert")
    conv.add_argument("value", type=int)
    conv.add_argument("--from", dest = "from_input", type=str)
    conv.add_argument("--to", type=str)

    args = parser.parse_args()

    if args.command == 'calc':
        result = expession_calculate(args.expression)
        sys.stdout.write(result)
        with open("src/toolkit/history.json", "r") as f:
            history = json.loads(f.read())
        history.append({
            "expression": args.expression,
            "result": result
        })
        with open("src/toolkit/history.json", "w") as f:
            f.write(json.dumps(history))
        sys.exit(0)
    elif args.command == 'convert':
        sys.stdout.write(measures_convert(args.value, args.from_input, args.to))
        sys.exit(0)


if __name__ == "__main__":
    main()
