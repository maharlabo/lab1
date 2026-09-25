import json
from src.toolkit.validation import converter_validation
from src.toolkit.convertation import convert

with open("src/toolkit/measures.json") as file:
    measures = json.loads(file.read())


def measures_convert(value: float, from_measure: str, to_measure: str) -> str:
    from_measure = from_measure.lower()
    to_measure = to_measure.lower()
    converter_validation(from_measure, to_measure, measures)
    return str(convert(value, from_measure, to_measure, measures))
