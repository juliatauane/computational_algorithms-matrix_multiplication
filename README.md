# Matrix Multiplication

Há muitas possibilidades para multiplicar uma sequência de matrizes pois a multiplicação de
matrizes é associativa. Sendo assim, não importa como colocamos o produto entre parênteses, o
resultado será o mesmo. A implementação do algoritmo de multiplicação de matrizes que
identifica a melhor forma de multiplicar um conjunto de n matrizes reduzindo a quantidade de
multiplicação escalares se dá através do uso da programação Dinâmica, que tem as seguintes
características:

• Caracterizar a estrutura de uma solução ótima para cada sub-problema:
Obter a menor quantidade de multiplicação escalares entre determinadas matrizes de uma
sequência de matrizes;

• Definir recursivamente as informações de uma solução ótima:
Ordenar a multiplicação de matrizes dada uma sequência é uma escolha entre a sequências
dadas que já se tem a informação sobre sub-soluções ótimas;

• Computar as informações da solução ótima de maneira bottom-up:
Ir do início ao fim, ou seja, calculando a solução ótima do sub-problema e como recalcular de
outro sub-problema utilizando o valor já calculado;

• Construir uma solução ótima a partir de informações computadas
Encontrar a ordem de multiplicação que gera o resultado com menor quantidade de
multiplicação escalares entre a sequência de matrizes com base nas informações armazenadas,
ou seja nas sub-soluções ótimas.

Dada uma sequência de multiplicação de matrizes, sendo:
Multiplicação= A*B*C*D*E*F , portanto:
Multiplicação= A[i1,j1]*B[i2,j2]*C[i3,j3]*D[i4,j4]*E[i5,j5]*F[i6,j6]
Para que a sequência multiplicação de matriz acima seja possível o número de colunas da matriz A
deve ser igual o número de linhas da matriz B, o número de colunas da matriz B deve ser igual o
número de linhas da matriz C, e assim por diante. Portanto:
j1 =i2, j2 =i3, j3 =i4, j4 =i5, j5 =i6

O resultado (matriz X) da multiplicação das matrizes A*B, por exemplo, se dá por:
A[i1,j1]*B[i2,j2] = X [i1,j2]

Resultado do número de multiplicações sendo= i1*j1*j2, sendo que j1=i2
Dentro da sequência dada há várias possibilidades em fazer a multiplicação das matrizes, ou seja,
agrupando por exemplo em subconjuntos de soluções ótimas.
Se considerarmos:
A= [2,2], B=[2,4], C= [4,2], D= [2,4], E=[4, 2], F=[2,4]

Pode-se escrever a sequência de multiplicação das matrizes em um vetor, sendo:
p[] = vetor que representa a cadeia de multiplicação das matrizes
A= p[i-1]*p[i] ->
Portanto:
p = [2, 2, 4, 2, 4, 2, 4]

Estruturando a resolução do problema através da programação dinâmica pode-se utilizar sub-
problemas ótimos já resolvidos como, por exemplo:

- Respeitando a sequência fornecida, desmembrar fazendo a multiplicação das matrizes de duas em
duas;
- Respeitando a sequência fornecida, desmembrar fazendo a multiplicação das matrizes de três em
três, utilizando resultados já obtidos nas multiplicações de agrupamento de duas em duas,
portanto, fazendo o uso de soluções de sub-problema ótimos já calculados para resolução de outro
sub-problema, e assim por diante dependendo do tamanho da cadeia de matrizes;
O melhor desmembramento da sequência e agrupamento de multiplicação das matrizes é
armazenado na vetor m[i,j] que será o mínimo entre as possíveis multiplicações de matrizes entre i
e j mais a multiplicação dessas duas matrizes Ai e Aj que é dada por pi-1.pk.pj.

Referência:
MATRIZ (MATEMÁTICA). In: WIKIPÉDIA, a enciclopédia livre. Flórida: Wikimedia Foundation, 2020.
Disponível em:
<https://pt.wikipedia.org/w/index.php?title=Matriz_(matem%C3%A1tica)&oldid=58010599>.
Acesso em: 18 mai. 2021.
