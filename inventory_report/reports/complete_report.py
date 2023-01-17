from inventory_report.reports.simple_report import SimpleReport


class CompleteReport:
    @staticmethod
    def generate(param: list) -> str:

        simple_report = SimpleReport.generate(param)

        company_stock = {}

        for item in param:
            if item["nome_da_empresa"] in company_stock:
                company_stock[item["nome_da_empresa"]] += 1
            else:
                company_stock[item["nome_da_empresa"]] = 1

        company_quantity = ""

        # items retorna (chave, valor) do dicionário
        # link: https://www.w3schools.com/python/ref_dictionary_items.asp
        for key, value in company_stock.items():
            company_quantity += f"- {key}: {value}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{company_quantity}"
        )
