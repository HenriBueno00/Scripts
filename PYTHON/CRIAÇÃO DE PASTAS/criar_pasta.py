#EXEMPLO DE CRIAÇÃO DE 11 PASTAS NO LOCAL ESCOLHIDO, COM O NOME DEFINIDO "ENTREGAS"

from pathlib import Path

# Definir o caminho da pasta do projeto
caminho_projeto = Path(r'//CAMINHO DA PASTA')

# Criar as pastas de ENTREGA de 01 a 10
for i in range(1, 11):
    nome_pasta_entrega = f'ENTREGA {i:02}'
    caminho_pasta_entrega = caminho_projeto / nome_pasta_entrega
    caminho_pasta_entrega.mkdir()
    print(f'Criada a pasta {nome_pasta_entrega}')

# Criar a pasta FINALIZADO
caminho_pasta_finalizado = caminho_projeto / 'FINALIZADO'
caminho_pasta_finalizado.mkdir()
print('Criada a pasta FINALIZADO')
