```python
for rodada in range(1, 10):
    print(rodada)
```

**range()** - Significa começa

```python
# Imprimir de 2 em dois
for rodada in range(1, 10, 2):
    print(rodada)
```

```python
# Imprimir em formatp de lista sem o range
for rodada in [1,2,3,4]:
    print(rodada)
```

### Formatação de Strings

```python
# interpolação de strings

print("Tentativa {} de {}".format(3, 10))

"Tentativa {} de {}".format(3, 10)

"Tentativa {1} de {0}".format(3, 10)

"R$ {}".format(1.59)


# Printa o numero com duas casa decimais
"R$ {:.2f}".format(1.59) - 'R$ 1.59'

"R$ {:.2f}".format(1.5) - 'R$ 1.50'

"R$ {:.2f}".format(1234.5) - 'R$ 1234.50'
"R$ {:7.2f}".format(1234.5)  - 'R$ 1234.50'

"R$ {:07.2f}".format(4.5) - 'R$ 0004.50'


# Imprimir numero inteiro
"R$ {:7d}".format(4) - 'R$       4'

# Imprime alguns 0 atraz do 4
"R$ {:07d}".format(4) - 'R$ 0000004'


"Data {:2d}/{:2d}".format(9, 4) - 'Data  9/ 4'

"Data {:02d}/{:02d}".format(9, 4) - 'Data 09/04'

"Data {:02d}/{:02d}".format(19, 11) - 'Data 19/11'
# 
```
[Link da documentação de Strings](https://docs.python.org/3/library/string.html#formatexamples)

### No Python 3.6+
A partir da versão 3.6 do Python, foi adicionado um novo recurso para realizar a interpolação de strings. Esse recurso é chamado de f-strings ou formatted string literals.

```python
>>> nome = 'Matheus'
>>> print(f'Meu nome é {nome}')
Meu nome é Matheus
```

Quando colocamos a letra f antes das aspas, informamos ao Python que estamos utilizando uma f-string. Dessa forma o Python consegue, em tempo de execução, captar a expressão que está entre chaves ({ }) e avaliá-la.

Além de variáveis, podemos passar também de funções e métodos:

```python
>>> nome = 'Matheus'
>>> print(f'Meu nome é {nome.lower()}')
Meu nome é matheus
```

### Gerando e arredondando um número aleatório

```python
import  random

print(random.random())

numero_random = random.random() * 100
print(numero_random)
print((round(numero_random)))
numero_random_int = int(numero_random)

print(numero_random_int)
print(numero_random_int)
print((round(numero_random_int)))

```

### Número secreto aleatório

**Importando a biblioteca random**

Como vimos, se queremos ter acesso às funções de geração de números aleatórios, precisamos utilizar as funções da biblioteca random do Python. Então nosso primeiro passo é importá-la logo no começo do nosso arquivo:

```python
import random

print("********************")
...
## Resto do código
```

**Gerando um número aleatório**

Agora que temos acesso às funções de número aleatório, podemos pedir um número que atenda ao nosso pré-requisito, que é ser um número que está no intervalo de 1 até 100. Para isso, já conhecemos diversos modos, como por exemplo utilizar a função `random.random()` e depois multiplicar o valor por 100.


Mas nós também vimos a função `random.randrange()`, que é uma função que facilita a nossa vida, pois ela aceita como primeiro parâmetro o menor número que queremos gerar, no nosso caso o número 1** e como segundo parâmetro até qual número queremos que o nosso intervalo de números gerados alcance, sem incluí-lo. Como queremos que o maior número seja o **100, vamos substituir a atribuição da nossa variável `numero_secreto` pela chamada da função, deste modo:

```python
numero_secreto = random.randrange(1,101)
```

### Testando a aleatoriedade

Podemos colocar um pequeno print abaixo, apenas para testar se o nosso número está sendo calculado mesmo:


```python
numero_secreto = random.randrange(1,101)
print(numero_secreto)

```

### Pseudo-Random

**Pseudo-Random?**

Aparentemente a geração de números aleatórios funcionou muito bem. Cada vez que chamamos o `random.random()` ou `random.randrange(..)`, foi gerado um outro número.

No entanto, computadores têm os seus problemas com aleatoriedade, pois são sistemas determinísticos. Em outras palavras, o nosso Python é previsível e na verdade não sabe criar números verdadeiramente aleatórios. Por isso se chama Pseudo-Random!

**Por que funcionou então?**

`random` é um função que, dada a mesma entrada, gerará o mesmo número. O truque é oferecer sempre uma entrada diferente para ter números diferentes e exatamente isso que está acontecendo por baixo dos panos.

Essa entrada também é chamada de seed (semente, em português). Entre as chamadas da função `random`, sempre é utilizado um novo seed. Por padrão o Python usa a hora (os milissegundos) como semente, mas nada nos impede de definir o mesmo seed antecipadamente. Para isso, existe a função `seed`!


**Usando seed**

Por exemplo, no jogo usamos a função `randrange` para gerar um número aleatório entre 1 e 100. Antes do `randrange` podemos chamar o `seed` para definir a entrada:

```python
>>> random.seed(100)
>>> random.randrange(1, 101)
19
```

Repare que foi gerado 19 e se usarmos o mesmo seed será gerado o mesmo número:

```python
>>> random.seed(100)
>>> random.randrange(1, 101)
19
```

Repare que a biblioteca `random` é bem previsível e por isso se chama pseudo-random!

### Definindo o nível
Como vimos na aula, pergunte ao usuário qual nível de dificuldade ele quer. Para tal, capture o que ele digitar, já convertendo o valor para inteiro e guardando em uma variável:
```python

total_de_tentativas = 0

print("(1) Fácil (2) Médio (3) Difícil")
nivel = int(input("Defina o nível: "))
```
Sabendo o nível, redefina a variável total_de_tentativas, baseado no nível:

```python
if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5
```
**Calculando a pontuação**

A pontuação inicial é de 1000 pontos. Para isso, defina a variável `pontos` no início do nosso jogo:

```python
pontos = 1000
```

Quando o usuário não acertar o número secreto, calcule os `pontos_perdidos`. Para tal, subtraia o `chute` do `numero_ secreto`, considerando apenas o valor absoluto. Adicione o código abaixo no bloco `else`:

```python
pontos_perdidos = abs(numero_secreto - chute)
```

Logo abaixo, subtraia os `pontos_perdidos` dos `pontos`:

```python

pontos_perdidos = abs(numero_secreto - chute)
pontos = pontos - pontos_perdidos
```

Por fim, falta exibirmos a pontuação final ao usuário. Altere a mensagem de acerto do usuário, acrescentando a pontuação total. Use novamente a interpolação de strings:

```python
print("Você acertou e fez {} pontos!".format(pontos))
```

Na mensagem de erro, acrescente um if para exibir, ao final do jogo, qual era o número secreto que não foi adivinhado e a pontuação final do usuário, mesmo que ele não tenha vencido a partida.

O 'if(maior)' vai ficar assim:

```python
if(maior):
    print("O seu chute foi maior que o número secreto")
    if (rodada == total_de_tentativas):
        print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
```
O 'if (rodada == total_de_tentativas):' ficará igual tanto dentro da cláusula 'elif(menor)'.