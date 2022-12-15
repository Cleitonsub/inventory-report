from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(param: list) -> str:
        old_fab_date = min([item['data_de_fabricacao'] for item in param])

        close_val_date = min([item['data_de_validade'] for item in param])

        big_stock = Counter(
            [item['nome_da_empresa'] for item in param]
        ).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {old_fab_date}\n"
            f"Data de validade mais próxima: {close_val_date}\n"
            f"Empresa com mais produtos: {big_stock}"
        )
