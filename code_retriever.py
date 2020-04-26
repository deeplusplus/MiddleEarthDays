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
        section_title = ("SEC. " + number + ". ")

        for individual_code in self._sections:
            if section_title in individual_code:
                returned_code = { "number": section_title,
                "Text":  individual_code.strip(),
                "Link": "https://codelibrary.amlegal.com/codes/los_angeles/latest/lamc/"
                }

        return returned_code