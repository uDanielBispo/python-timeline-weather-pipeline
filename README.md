# python-timeline-weather-pipeline

## Sobre
O projeto é bem simples, se baseia em coletar dados da api https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline
Esses dados são filtrados para a cidade de Boston e também são filtrados pela semana, então a ideia é coletar semanalmente com um fluxo do [Apache Airflow](https://airflow.apache.org/docs/) e disponibilizar dados das condições climaticas e temperatura, além dos dados brutos.
O fluxo do Airflow cria a pasta com o nome "week=(data de ocorrencia)" por exemplo, ele é executado toda segunda, então se executar na segunda de 2025-01-06 ele vai criar a pasta com o nome de "week=2025-01-06" e dentro dela adicionar as informações desta data,
informações relacionadas a clima, temperatura e os dados brutos.

## Como rodar
Eu criei ele em uma máquina virtual (VmWare), para ser sincero foi bem complicado configurar, então eu sugiro este [artigo](https://www.homehost.com.br/blog/vps/criar-maquina-virtual-ubuntu-vmware/) para configurar sua VM no sistema operacional Ubuntu 20.04,

Antes de instalar o Airflow, voce precisa garantir que tem todos os recursos que a aplicação precisa, para isso, execute os seguintes passos:

No diretório em que voce clonou o repositório execute os comandos no terminal:
Para criar o ambiente virtual
```bash
  python3 -m venv venv
```
Para instalar os recursos necessários
```
  pip install -r requirements.txt
```

Depois basta instalar o Airflow na pasta que voce desejar:

```bash
  pip install 'apache-airflow==2.3.2' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.2/constraints-3.9.txt"
```

Exportar a variavel de ambiente:
```bash
  export AIRFLOW_HOME=~/Diretório_em_que_voce_clonou_o_repositório
```
E por fim:
```bash
  airflow standalone
```

A partir disso voce só precisa acessar o airflow no seu navegador acessando ```localhost:8080```

# Comentários sobre a ferramenta e sobre o que aprendi
Olha, de todos os cursos que fiz na Alura, esse foi o que me chamou mais atenção, ja tinha ouvido falar sobre ferramentas de fluxo como Tibico e Mulesoft, ambas pagas e bem caras pelo visto.
Saber que existe uma ferramenta gratuita e ainda por cima open-source me deixa bastante feliz, é possivel utilizar esses fluxos para automatizar diversas atividades de extração, transformação e carregamento de dados.
Com certeza, o Aiflow vai fazer parte de muitas ideias que vão surgir na minha cabeça.

