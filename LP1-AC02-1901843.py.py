'''═════════════════════════════════════════════════════════════════════════════
 Instituição  :  Faculdade Impacta Tecnologia
 Curso        :  Sistemas de Informação
 Disciplina   :  Linguagem de Programação 1
 Turma        :  1B (noite)
 Professor    :  Lucio Nunes de Lira
 Aluno        :  Priscila Da Dalt
 Matrícula    :  1901843
 Entrega      :  16/09/2019
════════════════════════════════════════════════════════════════════════════════
 Programa     :  AC02 (Expressões aritméticas e estrutura sequencial)
═════════════════════════════════════════════════════════════════════════════'''

'''─────────────────────────────────────────────────────────────────────────────
[ENUNCIADO]
  Crie um programa para calcular o valor de uma compra.
  O programa deverá ler apenas três valores:
  (I)   Um número real, representando o preço de uma peça de computador;
  (II)  Um número inteiro, representando a quantidade comprada dessa peça;
  (III) Um número real representando o desconto aplicado ao valor total da 
        compra. 
  O programa deverá exibir o valor total e o valor final da compra (valor total
  menos o desconto dado).  

[RESTRIÇÕES]
  a) Usar apenas recursos vistos em nossas aulas;
  b) Mostrar os valores com apenas duas casas depois do ponto.

[ENTREGA]
  a) Individual;
  b) Serão consideradas apenas entregas dentro do prazo.

[CORREÇÃO]
  a) Notas baseadas na correção do código e obediência às restrições;
  b) Caso sejam detectadas cópias, todas serão anuladas.
─────────────────────────────────────────────────────────────────────────────'''

produto=float(input('Valor da Peça:'))
qtd=int (input('Quantidade comprada:'))
desc=float (input ('Valor do Desconto:'))
total=(produto*qtd)
print('Valor Total:','%.2f' % total)
final=float (total-desc)
print('Valor Final:', '%.2f' % final)
