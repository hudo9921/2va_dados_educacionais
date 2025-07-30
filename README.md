# Predição de Dificuldade de Itens do ENEM via Texto

Este projeto investiga a viabilidade de prever o parâmetro de **dificuldade (b)** de questões do ENEM com base em suas características textuais e presença de elementos visuais, utilizando técnicas de Processamento de Linguagem Natural (PLN).

## Objetivo

Desenvolver um modelo de regressão capaz de predizer o nível de dificuldade de uma questão do ENEM **antes de sua aplicação**, com foco no conteúdo textual. A proposta busca auxiliar na elaboração de provas mais equilibradas e na preparação estratégica de estudantes.

## Contexto

O ENEM utiliza a **Teoria de Resposta ao Item (TRI)** para garantir equidade e comparabilidade entre diferentes edições da prova. A TRI considera:

- **Discriminação (a):** capacidade da questão de diferenciar candidatos.
- **Dificuldade (b):** nível de habilidade necessário para 50% de chance de acerto.
- **Acerto casual (c):** chance de acerto por chute.

Este projeto foca na predição do parâmetro **b** com base em dados textuais, sem depender das respostas dos participantes.

## Dados Utilizados

- **Microdados oficiais do ENEM** dos anos:
  - 2019, 2020, 2022 e 2023
- Fontes:
  - INEP
  - Kaggle

## Tecnologias e Métodos

- Python
- Pandas, Scikit-learn
- Técnicas de NLP:
  - Legibilidade
  - Complexidade sintática
  - Coesão textual
  - Diversidade lexical

## Resultados

Os modelos desenvolvidos com métricas linguísticas tradicionais apresentaram **baixa capacidade preditiva**, sugerindo que o conteúdo textual isolado não é suficiente para estimar com precisão o parâmetro de dificuldade. A pesquisa, no entanto, aponta caminhos promissores para abordagens futuras com modelos mais complexos ou embeddings semânticos.

---

> Este trabalho contribui para a área de **mineração de dados educacionais** e abre espaço para inovações na construção e análise de avaliações no Brasil.
