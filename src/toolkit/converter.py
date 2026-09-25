import json
from toolkit.validation import converter_validation
from toolkit.convertation import convert

with open("toolkit/measures.json") as file:
    measures = json.loads(file.read())


def measures_convert(value: float, from_measure: str, to_measure: str) -> str:
    converter_validation(from_measure, to_measure, measures)
    return str(convert(value, from_measure, to_measure, measures))
