import datetime
from mercados.b3 import B3

b3 = B3()
negocios = b3.negociacao_bolsa("dia", datetime.date(2025, 9, 5))
for negocio in negocios:
    if negocio.codigo_negociacao in ("BBAS3", "PETR4", "BBSE3"):
        print(negocio.codigo_negociacao, negocio.preco_abertura, negocio.preco_ultimo)


