# Criando gráficos com svg

### Objetivo

Este programa cria graficos e os imprime em uma página HTML. A aplicação tem como foco \
principal a não utilização de bibliotecas para criação de gráficos. 


### Sobre a aplicação

Durante o processo de criação foi necessária a utilização da biblioteca pandas, \
a necessidade da utilização dessa biblioteca se deve a facilidade de retirar \
dados inuteis.

Necessário enfatizar que o programa mantem sua essência, já que a criação dos graficos \
independem da bibilioteca pandas.
 

### Sobre os arquivos .csv

A plicação esta programada para utilizar o arquivo corona_world ou um arquivo com essa mesma nomenclatura. \
O arquivo app.py é somemte um exemplo, já que sua unica função é prover dados de corona virus.

Abaixo um exemplo do csv:
    
    Coronavirus Cases,Deaths,Recovered,Data,Hour
    1201767,64710,246496,04/04/20,22:40:07
    1253072,68154,257202,04/05/20,14:40:02


#### Configurando o Environment

Build environment:

    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64

Após clonar o repositório na sua maquina, siga o passo a passo:

* Crie o virtual environment.
* Rode o código abaixo com o virtual environment ativado.

    
    pip install -r requirements.txt

* Após esses passos o programa estará diponivel para teste na sua maquina. 

### Caso queira utilizar seus próprios dados. 

Caso queira utilizar dados próprios recomendo que siga o seguinte:
    
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [1, 2, 3, 4, 5, 6, 7]
    
O gráfico resultante dos dados acima é uma reta na diagonal, então caso queira fazer seu próprio gráfico recomendo fazer algo parecido.

Passo a passo:

* Crie um arquivo.py
* Instancie a classe <b>plot_logic</b> e <b>making_html</b>
* Crie uma função.
* Essa função def deve chamar duas outras funções:


    # result é um dicionário
    result = plot_logic.draw_diagonal(x, y)
    
    # Pegadno x, y e pontos.
    x = result['label_x']
    y = result['label_y']
    html_x = result['pontos']
    
    html = making_html.drawing_html(x, y, html_x)
    
    making_html.save_html(nome_do_arquivo, html)
    
#### Principais funções

<b>draw_diagonal()</b> é uma função que fica dentro do arquivo <b>plot_logic.py</b>, sua principal tarefa é formar pares de pontos,\
que posteriormente serão desenhados no grafico através da função <b>drawing_html()</b> que fica no arquivo <b>making_html</b>

* label_x = representam os nomes que ficarão ao longo do eixo x.
* label_y = nomes que ficarão ao longo do eixo y.
* pontos = são os pontos a serem ligados pelo html.

A função <b>save_html</b> serve para escrever o arquivo html. Após rodar a aplicação será\
gerado um arquivo .html, agora é só abrir o arquivo no browser.
