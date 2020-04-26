import json


class CodeRetriever:

    CONST_DEFAULT_CODE = {
            "number": "None",
            "Text": "Ordinance not found.",
            "Link": "https://codelibrary.amlegal.com/codes/los_angeles/latest/lamc/"
        }

    def __init__(self):
        self._sections = ''
        with open('/home/jarvis/development/ME_Calendar/MiddleEarthDays/MunicipalCode/LAMC_Sections.txt', encoding='utf-8') as lamc_sections:
            self._sections = lamc_sections.readlines()


    def getCodeByNumber(self, number):
        returned_code = self.CONST_DEFAULT_CODE

        for individual_code in self._sections:
            if ("SEC. " + number + ". ") in individual_code:
                returned_code = individual_code.strip()

        return returned_code