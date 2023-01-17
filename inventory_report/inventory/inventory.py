import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path: str, type: str):
        if 'csv' in path:
            with open(path, encoding="utf-8") as csvfile:
                file = list(csv.DictReader(
                    csvfile, delimiter=",", quotechar='"'
                ))
        elif 'json' in path:
            with open(path, mode="r", encoding="utf-8") as jsonfile:
                file = json.load(jsonfile)
        elif 'xml' in path:
            with open(path, mode="r", encoding="utf-8") as xmlfile:
                file = xmltodict.parse(xmlfile.read())['dataset']['record']
        else:
            raise ValueError

        return Inventory.generate(file, type)

    @staticmethod
    def generate(inventory: str, type: str) -> str:
        if type == 'simples':
            return SimpleReport.generate(inventory)
        elif type == 'completo':
            return CompleteReport.generate(inventory)
        else:
            raise ValueError
