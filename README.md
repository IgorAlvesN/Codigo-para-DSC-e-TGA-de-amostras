  Dois códigos da matéria de Técnicas Experimentais I: Um para DSC e outro para TGA de duas amostras diferentes. Foram feitos em formato compatível com Jupyter Notebook por ser bastante útil ser rodado em etapas, de modo que cada informação desejada pode ser coletada separadamente e os erros encontrados durante a escrita 99% das vezes eram locais, sem a necessidade de rodar os códigos inteiros novamente.

  É necessário os pacotes pandas, matplotlib, numpy e sklearn para correto funcionamento do código. Modo de usar: com o arquivo de dados corretamente estruturados (informações sobre isso abaixo), basta colocar o endereço em "path_arquivo" e o endereço para onde os plots serão exportados em "path_imagens" que o programa gera tudo sozinho.

### **Código da análise do Chumbo (Chumbo.py)**
  Os dados do aquecimento a serem consumidos devem estar em formato CSV seguindo a seguinte ordem das colunas:

  Índice | Tempo | Temperatura do Forno | Temperatura da Amostra | TG | Fluxo de Calor da Amostra | Fluxo de Calor da referência

### **Código da análise do Sulfato de Cobre (Sulfato de Cobre.py)**
  Os dados do aquecimento a serem consumidos devem estar em formato CSV seguindo a seguinte ordem das colunas:

  Índice | Tempo | Temperatura do Forno | Temperatura da Amostra | TG | Fluxo de Calor

  Para informações sobre as funções do módulo __func.py__, verificar o arquivo __Documentação-me.md__
