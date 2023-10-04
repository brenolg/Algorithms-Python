# Projeto Algorithms

Neste projeto, foi aprimorarado habilidades de resolução de problemas e otimização de algoritmos, aplicando os conhecimentos adquiridos. Foi abordado tópicos como análise de complexidade de algoritmos, recursividade e algoritmos de ordenação e busca. O objetivo é enfrentar desafios diversos que envolvem a implementação de algoritmos eficientes para resolver problemas do tipo que frequentemente surgem em processos de entrevistas técnicas, conhecidos como whiteboard interviews.

<br/>

# Funcionalidades

* A aderência à complexidade exigida em cada requisito.
* Lógica.
* Capacidade de interpretação do problema.
* Capacidade de interpretação de um código legado.
* Capacidade de resolução do problema, de forma otimizada.
* Resolver o problemas/Otimizar algoritmos mesmo sob pressão.

# Tecnologias Utilizadas

*  Python

# Requisitos do Projeto

1.1 - Retorne, para uma entrada específica, a quantidade de estudantes presentes

1.2 - Retorne `None` se em `permanence_period` houver alguma entrada inválida

1.3 - Retorne `None` se `target_time` recebe um valor vazio

1.4 - A função deverá, por meio de análise empírica, se comportar (no avaliador remoto em sua Pull Request) como no máximo O(n), ou seja, com complexidade assintótica linear

2 - Implementar adequadamente o teste para a função `encrypt_message`
<details>
  <summary>
    <b>🧠 Entenda a lógica da função de criptografia</b>
  </summary>

* Recebe uma string `message` e um inteiro `key` como parâmetros
* Se `key` e `message` não possuírem os tipos corretos, uma exceção deve ser lançada
* Se `key` não for um índice positivo válido de `message`, retorna a string `message` invertida
* Se `key` for ímpar:
  * divide `message` no índice `key`, inverte os caracteres de cada parte, e retorna a união das partes novamente com `"_"` entre elas
* Se `key` for par:
  * divide `message` no índice `key`, inverte a posição das partes, inverte os caracteres de cada parte, e retorna a união das partes novamente com `"_"` entre elas



</details>

3.1 - Retorne `True` se a palavra passada por parâmetro for um palíndromo

3.2 - Retorne `False` se a palavra passada por parâmetro não for um palíndromo

3.3 - Retorne `False` se nenhuma palavra for passada por parâmetro

4.1 - Retorne `True` se as palavras passadas forem anagramas

4.2 - Retorne `False` se as palavras passadas por parâmetro não forem anagramas

4.3 - Retorne `false` se alguma das palavras passadas por parâmetro for uma string vazia

4.4 - A função deverá, por meio de análise empírica, se comportar (no avaliador remoto em sua Pull Request) como no máximo O(n log n), ou seja, com complexidade assintótica linearítmica

4.5 - Retorne `True` se as palavras passadas forem anagramas sem diferenciar maiúsculas e minúsculas

# Agradecimentos

Agradecemos à Trybe por proporcionar a oportunidade de desenvolver este projeto e aprender novas tecnologias. Também agradecemos à comunidade de desenvolvedores que contribui para o desenvolvimento do React e outras tecnologias utilizadas neste projeto. E, é claro, agradecemos a George Lucas por criar um universo tão incrível que inspira tantas pessoas até hoje.
