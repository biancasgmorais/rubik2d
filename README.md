# rubik2d
* Rubik 2D com Busca de Custo Uniforme, Busca Gulosa pela melhor escolha e Busca A*
* Trabalho da Disciplina de Sistemas Inteligentes feito juntamente com a aluna LUMA SLLARY FERNANDES OLIVEIRA

# Rubik
* O Cubo de Rubik é o original e mais conhecido dos quebra-cabeças de movimentos sequenciais.

# BUSCA DE CUSTO UNIFORME:
* Expande o nó n com o custo do caminho g(n) mais baixo;
* Feito com fila de prioridade, através do armazenamento da borda, ordenando pelo custo;
* Não se importa com o número de passos que um caminho tem, apenas com seu custo total.

# BUSCA GULOSA PELA MELHOR ESCOLHA:
* Tenta expandir o nó que está mais próximo do objetivo, com o fundamento de que isso pode conduzir a uma solução rapidamente;
* Avalia os nós usando apenas a função heurística, ou seja, f(n) = h(n).

# BUSCA A*
* Evita expandir caminhos que já são caros;
* Tem como função de avaliação f(n)  = g(n) + h(n).
* Onde:
**g(n) é o custo até o momento para alcançar n;
**h(n) é o custo estimado de n até o objetivo;
**f(n) é o custo total estimado do caminho através de n até o objetivo.

# Heurísticas utilizadas
## NÚMERO DE PEÇAS FORA DO LUGAR
* Essa heurística tem como os parâmetros iniciais os locais de cada peça do cubo;
* Cada expansão é feita a comparação de quantas peças estão fora do lugar de acordo com o estado objetivo;
* Fazendo assim uma soma para cada uma que esteja diferente.

## REGRA DA VIZINHANÇA
* Essa heurística compara da seguinte forma: 
* Para cada cor é atribuído um número;
* Dentre esses números é verificado quais são os seus vizinhos;
* Se um desses vizinhos for mudado durante a expansão, será contado na heurística.

## NÚMERO DE PEÇAS DIFERENTES POR LADO
* Essa heurística compara a quantidade de peças diferentes por lado, então é somado uma unidade a heurística total para cada valor diferente, testando e somando para cada lado.
Por exemplo: 
* Se tivermos duas cores iguais e uma diferente naquele lado, esse lado vai ter uma heurística de valor 2;
* Se tivermos três cores distintas, então a heurística desse lado vai ter valor 3;
* Se tivermos todas as cores iguais, então a heurística desse lado vai ter valor 0.

# Resultados
Os três algoritmos foram testados para quatro estados iniciais:
* 1º Estado: Criado de 3 embaralhamentos
* 2º Estado: Criado de 20 embaralhamentos
* 3º Estado: Criado de 50 embaralhamentos
* 4º Estado: Criado de 100 embaralhamentos


