![LineLumos](https://user-images.githubusercontent.com/102249811/184330542-24bd9f7f-b369-4460-ae37-d84455a3589c.png)


<p align="center">
 Análise de dados do dataset Obesity Levels
</p>

<p align="center">
 <a href="#Sobre">Sobre</a> •
 <a href="#Descrição-do-Dataset">Descrição do Dataset</a> •
 <a href="#Objetivos">Objetivos</a> •
 <a href="#Metologia">Metologia</a> •
 <a href="#Requisitios">Requisitios</a> •
 <a href="#Instalação">Instalação</a> •
 <a href="#Uso">Uso</a> •
 <a href="#Análise-e-Resultados">Análise e Resultados</a> •
 <a href="#Principais-Insights">Principais Insights</a> •
 <a href="#Recomendações">Recomendações</a> •
 <a href="#Dashboard">Dashboard</a> •
 <a href="#Equipe">Equipe</a> •
 <a href="#Licença">Licença</a>
</p>

## ![link](https://github.com/dayvsonlsantos/p-mostra-dados/assets/102249811/6487f089-0953-418f-b661-4ba593e08c4c)  Sobre

<p align=justify>A obesidade é um problema de saúde global com consequências significativas. Com o aumento dos casos de obesidade, torna-se necessário realizar novas pesquisas para examinar os fatores que influenciam essa condição e prever a ocorrência de determinadas doenças. Este relatório apresenta uma análise do conjunto de dados "Obesity Levels", que inclui 2.111 registros e 17 variáveis, sem valores nulos ou zerados. O dataset contém informações sobre indivíduos do México, Peru e Colômbia, coletadas através de uma plataforma web e geradas sinteticamente usando a ferramenta Weka e o filtro SMOTE.</p>

<p align=justify>Este projeto realiza uma análise detalhada dos dados relacionados aos níveis de obesidade, utilizando bibliotecas como Pandas, Seaborn, Matplotlib e Dash. A análise inclui a distribuição de idade, IMC, modos de transporte, e a relação entre altura e peso. Os principais insights são apresentados através de visualizações interativas criadas com Dash.</p>

<br/>

## ![link](https://github.com/dayvsonlsantos/p-mostra-dados/assets/102249811/6487f089-0953-418f-b661-4ba593e08c4c)  Descrição do Dataset

<p align=justify>O dataset contém as seguintes variáveis:</p>

- **NObeyesdad**: Nível de obesidade (variável alvo)
- **Gender**: Gênero
- **Age**: Idade
- **Height**: Altura
- **Weight**: Peso
- **family_history_with_overweight**: Histórico familiar de sobrepeso
- **FAVC**: Frequência de consumo de alimentos com alto teor calórico
- **FCVC**: Frequência de consumo de vegetais
- **NCP**: Número de refeições principais diárias
- **CAEC**: Consumo de alimentos entre as refeições
- **SMOKE**: Hábito de fumar
- **CH2O**: Consumo diário de água
- **SCC**: Monitoramento de calorias ingeridas
- **FAF**: Frequência de atividade física
- **TER**: Tempo de uso de dispositivos tecnológicos
- **CALC**: Frequência de consumo de álcool
- **MTRANS**: Meio de transporte usual
<br/>

## ![link](https://github.com/dayvsonlsantos/p-mostra-dados/assets/102249811/6487f089-0953-418f-b661-4ba593e08c4c)  Objetivos

- Identificar a distribuição de idade entre os diferentes tipos de obesidade.
- Explorar a relação entre peso e IMC.
- Examinar a influência do modo de transporte na distribuição de idade.
- Analisar a relação entre altura e peso entre os indivíduos obesos.
- Avaliar a quantidade de indivíduos em diferentes níveis de obesidade com base no IMC.
<br/>

## ![link](https://github.com/dayvsonlsantos/p-mostra-dados/assets/102249811/6487f089-0953-418f-b661-4ba593e08c4c) Metologia

  Os dados foram processados e analisados utilizando a biblioteca Pandas para manipulação de dados e o Dash para visualizações interativas. A análise inclui a criação de novos campos, filtragem de dados e a geração de gráficos para identificar padrões e insights.

<br/>


## ![link](https://github.com/dayvsonlsantos/p-mostra-dados/assets/102249811/6487f089-0953-418f-b661-4ba593e08c4c) Requisitios

Python 3.7 ou superior
Bibliotecas Python: Pandas, Numpy, Seaborn, Matplotlib, Dash, Plotly, scikit-learn

<br/>

## ![link](https://github.com/dayvsonlsantos/p-mostra-dados/assets/102249811/6487f089-0953-418f-b661-4ba593e08c4c) Instalação

- ##### Clone este repositório:

```
  git clone https://github.com/seu_usuario/seu_repositorio.git
  cd seu_repositorio
```

- ##### Instale as bibliotecas necessárias:

```
  pip install matplotlib seaborn scikit-learn dash pandas numpy
```

<br/>


## ![link](https://github.com/dayvsonlsantos/p-mostra-dados/assets/102249811/6487f089-0953-418f-b661-4ba593e08c4c) Uso

- ##### Execute o script data.py para realizar a análise e gerar as visualizações:

```
  python data.py
```

- ##### Acesse o dashboard no navegador:

```
  http://127.0.0.1:8050/
```

- ##### Para o arquivo data.ipynb:

  Execute o run em cada bloco de código


<br/>


## ![link](https://github.com/dayvsonlsantos/p-mostra-dados/assets/102249811/6487f089-0953-418f-b661-4ba593e08c4c) Análise e Resultados

#### Distribuição de Idade por Tipo de Obesidade

- Obesity_Type_I:
  - Média de idade entre homens: 23 anos
  - Média de idade entre mulheres: 27 anos
    
- Obesity_Type_II:
  - Média de idade entre homens: 27 anos
  - Média de idade entre mulheres: 24 anos
    
- Obesity_Type_III:
  - Média de idade entre homens: 18 anos
  - Média de idade entre mulheres: 23 anos

#### Relação entre Peso e IMC

- Correlação positiva clara entre peso e IMC, indicando que o IMC aumenta proporcionalmente ao peso dos indivíduos.

#### Distribuição de Idade por Modo de Transporte (MTRANS)

- Modos de transporte ativos, como caminhar ou andar de bicicleta, estão associados a uma população mais jovem.

#### Relação entre Altura e Peso

- A altura e o peso apresentam uma variação considerável, reforçando a necessidade de considerar ambos os fatores nas avaliações de saúde.

#### Distribuição de IMC por Nível de Obesidade

- A quantidade de indivíduos em níveis mais altos de obesidade é menor, mas estes indivíduos apresentam um IMC significativamente mais alto.

<br/>

## ![link](https://github.com/dayvsonlsantos/p-mostra-dados/assets/102249811/6487f089-0953-418f-b661-4ba593e08c4c) Principais Insights

- A média de idade para homens e mulheres varia significativamente entre os diferentes tipos de obesidade.
- A correlação direta entre peso e IMC reforça a importância de programas de controle de peso.
- Modos de transporte ativos são eficazes na prevenção da obesidade em jovens.
- Abordagens personalizadas são necessárias devido à diversidade na composição corporal dos indivíduos obesos.
- Sistemas de monitoramento contínuo do IMC são essenciais para identificar precocemente indivíduos em risco.

<br/>


## ![link](https://github.com/dayvsonlsantos/p-mostra-dados/assets/102249811/6487f089-0953-418f-b661-4ba593e08c4c) Recomendações

- Desenvolver programas específicos para diferentes faixas etárias.
- Incentivar modos de transporte ativos e outras formas de atividade física.
- Implementar abordagens personalizadas para a gestão de peso.
- Estabelecer sistemas de monitoramento contínuo do IMC.

<br/>


## ![link](https://github.com/dayvsonlsantos/p-mostra-dados/assets/102249811/6487f089-0953-418f-b661-4ba593e08c4c) Dashboard


<img src='https://github.com/dayvsonlsantos/da-obesity-levels/assets/102249811/e5cecef9-d712-4f55-9e19-b5bf7c31def4' width="1000px;">

<br/>


## ![link](https://github.com/dayvsonlsantos/p-mostra-dados/assets/102249811/6487f089-0953-418f-b661-4ba593e08c4c) Equipe

### <p align=center>Dayvson Lima<p/>

<img align='right' src='https://avatars.githubusercontent.com/u/102249811?s=400&u=2843e9ff654eb5587f9e6ad6b873fed0b1c0df77&v=4' width="150px;">

<p align=justify>Olá, sou Dayvson. Tenho como foco aperfeiçoar cada vez mais as minhas habilidades, tanto as técnicas (hard skills), como as comportamentais (soft skills), me tornando um profisional cada vez melhor. Tenho como foco o desenvolvimento de aplicações web, buscando fornecer uma ótima experiência ao usuário.</p>

<br />

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://www.linkedin.com/in/dayvsonlimasantos)[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white)](https://github.com/dayvsonlsantos)

<br/>

### <p align=center>Reginaldo Alves<p/>

<img align='left' src='https://github.com/dayvsonlsantos/p-near-hospital/assets/102249811/9a9cf70a-7e7b-49b3-9ce1-2cde7671b488)' width="150px;">

<p align=justify>Olá, me chamo Reginaldo. Desde que me entendo por gente tenho tido contato com a tecnologia, e hoje um dos meus sonhos que estão se realizando é o de virar desenvolvedor. Meu foco é o desenvolvimento Back End e pretendo me aprimorar pra muitas outras tecnologias.</p>

<br />

<br/>

### <p align=center>Natan Gonçalvez<p/>

<img align='right' src='https://github.com/dayvsonlsantos/p-near-hospital/assets/102249811/25c7072b-0deb-4f4e-aec4-5253cba93dd4' width="150px;">

<p align=justify>Me chamo Natan. Sempre estive envolvido com a tecnologia, e atualmente estou me formando em Análise e Desenvolvimento de Sistemas na Faculdade Senac.</p>

<br />

<br/>

### <p align=center>Luis Henrique<p/>

<img align='left' src='https://github.com/dayvsonlsantos/p-lixeira-inteligente/assets/102249811/78388306-7cae-41e6-b410-320ec5dd8af7' width="150px;">

<p align=justify>Me chamo Luis, sou um desenvolvedor de software apaixonado por tecnologia e inovação. Especializo-me em desenvolvimento web, C# (.NET), SQL e cibersegurança, e adoro trabalhar em projetos desafiadores.</p>

<br />

<br/>

### <p align=center>Daniel Oliveira<p/>

<img align='right' src='https://github.com/dayvsonlsantos/p-near-hospital/assets/102249811/a01154cd-50fb-4cad-96e9-c74a1276586b' width="150px;">

<p align=justify>Me chamo Daniel, sou novo no mercado da tecnologia, e tenho me interessado bastante, atualmente já faço diversos cursos de TI, principalmente voltado para área backend em Java. Além disso, estou me formando em ADS(análise e desenvolvimento de sistema) pela faculdade Senac.</p>

<br />

<br/>

## ![link](https://user-images.githubusercontent.com/102249811/184334676-ed902c74-e1fc-44a8-828b-4c3eb1490767.png) Licença

O projeto se encontra sob a licença [GPLv3](https://github.com/dayvsonlsantos/da-obesity-levels/blob/main/LICENSE).
