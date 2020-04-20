import json


class CodeRetriever:

    CONST_DEFAULT_CODE = {
            "number": "None",
            "Text": "Ordinance not found.",
            "Link": "https://codelibrary.amlegal.com/codes/los_angeles/latest/lamc/"
        }

    def __init__(self):
        self._codes = {}
        with open('codes.json') as json_codes:
            codes = json.load(json_codes)
            self._codes = codes['codes']


    def getCodeByNumber(self, number):
        number = str(number)
        returned_code = self.CONST_DEFAULT_CODE

        for individual_code in self._codes:
            if individual_code["number"] == number:
                returned_code = individual_code     

        return returned_code