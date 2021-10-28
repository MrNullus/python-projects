from utilidades import moeda
from utilidades import dado

p = dado.leiaDinheiro('Digite o preço:>> R$ ')
moeda.resumo(p, 32, 22)
