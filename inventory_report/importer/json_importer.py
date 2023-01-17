import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if 'json' in path:
            with open(path, mode="r", encoding="utf-8") as jsonfile:
                return json.load(jsonfile)
        else:
            raise ValueError('Arquivo inválido')
