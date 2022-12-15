from inventory_report.inventory.product import Product


def test_cria_produto():
    mock = {
        "id": "1",
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2021-02-18",
        "data_de_validade": "undefined",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1"
    }

    product = Product(
        mock['id'],
        mock['nome_do_produto'],
        mock['nome_da_empresa'],
        mock['data_de_fabricacao'],
        mock['data_de_validade'],
        mock['numero_de_serie'],
        mock['instrucoes_de_armazenamento'],
    )

    assert product.id == mock['id']
    assert product.nome_do_produto == mock['nome_do_produto']
    assert product.nome_da_empresa == mock['nome_da_empresa']
    assert product.data_de_fabricacao == mock['data_de_fabricacao']
    assert product.data_de_validade == mock['data_de_validade']
    assert product.numero_de_serie == mock['numero_de_serie']
    assert product.instrucoes_de_armazenamento == mock[
        'instrucoes_de_armazenamento'
    ]
