import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if 'xml' in path:
            with open(path, mode="r", encoding="utf-8") as xmlfile:
                return xmltodict.parse(xmlfile.read())['dataset']['record']
        else:
            raise ValueError('Arquivo inválido')
