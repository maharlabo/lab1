import sys
from src.toolkit.tokenization import tokenize
from src.toolkit.calculation import calculate

def convert(value: float, from_measure: str, to_measure: str, measures: list) -> float:
    for measure_group in measures:
        if from_measure in measure_group["measures"] or to_measure in measure_group["measures"]:
            group = measure_group
            break
    if group["type"] == "default":
        result = group["measures"][from_measure]*value/group["measures"][to_measure]
    elif group["type"] == "formula":
        default_measure = group["default_measure"]
        formula_from = group["measures"][from_measure][1]
        formula_to = group["measures"][to_measure][0]
        formula_from = formula_from.replace(from_measure, str(value))
        mid_result = calculate(tokenize(formula_from))
        formula_to = formula_to.replace(default_measure, str(mid_result))
        result = calculate(tokenize(formula_to))
    if "below_limit" in group:
        if result < group["below_limit"]:
            sys.stderr.write(f"{group["group"]} can't be below {group['below_limit']}")
            sys.exit(2)
    if "above_limit" in group:
        if result > group["above_limit"]:
            sys.stderr.write(f"{group["group"]} can't be above {group['above_limit']}")
            sys.exit(2)
    return result
