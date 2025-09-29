## **app.func.derivada(data_x_axis**=none, **data_y_axis**=none)
A partir de dois conjuntos de dados (um representando as coordenadas x de um gráfico e outro representando as coordenadas y do mesmo), retorna um conjunto de dados representando a derivada numérica em cada ponto

### **Parâmetros:**
**data_x_axis : list**\
lista das coordenadas x dos pontos que compõem o gráfico

**data_y_axis : list**\
lista das coordenadas y dos pontos que compõem o gráfico

Obs: dados na mesma posição dentro de ambas as listas, devem corresponder ao mesmo ponto.

## **app.func.integral(data_x_axis**=none, **data_y_axis**=none)
A partir de dois conjuntos de dados (um representando as coordenadas x de um gráfico e outro representando as coordenadas y do mesmo), retorna um conjunto de dados representando a integral numérica de um ponto pelo método do retângulo

### **Parâmetros:**
**data_x_axis : list**\
lista das coordenadas x dos pontos que compõem o gráfico

**data_y_axis : list**\
lista das coordenadas y dos pontos que compõem o gráfico

Obs: dados na mesma posição dentro de ambas as listas, devem corresponder ao mesmo ponto.

## **app.func.reta_dado_pontos(x1**=none,**y1**=none,**x2**=none,**y2**=none)
Retorna os coeficientes angular e linear da reta que liga dois pontos

### **Parâmetros:**
**x1 : float**\
Coordenada X do primeiro ponto

**y1 : float**\
Coordenada Y do primeiro ponto

**x2 : float**\
Coordenada X do segundo ponto

**y2 : float**\
Coordenada Y do segundo ponto

## **app.func.pico_local(data**=none,**type**=none,**start**=none,**end**=none)
Retorna um pico (máximo ou mínimo) no intervalo selecionado

### **Parâmetros:**
**data : list**\
Lista dos valores a serem pesquisados

**type : {"min" or "max"}**\
Define se vai ser procurado um mínimo ou um máximo local

**start : float**\
Início do intervalo

**end : float**\
Fim do intervalo

## **app.func.reta_perpend(y_start**=none,**y_end**=none,**x_value**=none)
Retorna uma matriz com os dados de uma reta vertical

### **Parâmetros:**
**y_start : float**\
Menor valor de y da reta

**y_end : float**\
Maior valor de y da reta

**x_value : float**\
Coordenada x da reta (só tem um valor já que é uma reta vertical)

## **app.func.linha_base_onset(intervalo_ref**=none,**intervalo_alvo**=none,**indice**=none,**valor**=0)
Retorna a temperatura e seu respectivo índice no conjunto de dados. Essa temperatura equivale aquela em que o evento começou a acontecer (a derivada deixou de ser zero)

### **Parâmetros:**
**intervalo_ref : list**\
Intervalo de referência a ser pesquisado (nele se detecta o início do evento)

**intervalo_alvo: list**\
Intervalo com a variável desejada a ser obtida no ponto do início do evento, após este ter sido detectado pela referência.

**indice : int**\
Índice em que se inicia a pesquisa

**valor : int, default 0**\
Valor a ser encontrado no intervalo de referência, finalizando a pesquisa

## **app.func.linha_base_endset(intervalo_ref**=none,**intervalo_alvo**=none,**indice**=none,**valor**=0)
Retorna a temperatura e seu respectivo índice no conjunto de dados. Essa temperatura equivale aquela em que o evento terminou de acontecer.

### **Parâmetros:**
**intervalo_ref : list**\
Intervalo de referência a ser pesquisado (nele se detecta o final do evento)

**intervalo_alvo: list**\
Intervalo com a variável desejada a ser obtida no ponto final do evento, após este ter sido detectado pela referência.

**indice : int**\
Índice em que se inicia a pesquisa

**valor : int, default 0**\
Valor a ser encontrado no intervalo de referência, finalizando a pesquisa
