# Data Quality Governance Toolkit

Toolkit demonstrativo de qualidade e governança de dados usando Python e datasets sintéticos.

## Objetivo

Demonstrar práticas de validação, profiling, documentação e monitoramento de dados para projetos de BI, ciência de dados, auditoria e machine learning.

## Problema de negócio

Modelos e dashboards dependem de dados confiáveis. Falhas como duplicidades, nulos, formatos inconsistentes, categorias inválidas e mudanças de distribuição podem gerar decisões incorretas.

## Stack

- Python
- pandas e NumPy
- Great Expectations ou validações próprias
- pytest
- Markdown para documentação de regras

## Estrutura

```text
src/
  quality_checks.py
  generate_demo_dataset.py
notebooks/
  data_quality_profile.ipynb
data/
  README.md
reports/
  quality_report.md
tests/
```

## Checks demonstrados

- Percentual de valores nulos
- Linhas duplicadas
- Validação de schema
- Domínio de categorias
- Outliers simples
- Consistência entre colunas
- Relatório de qualidade em Markdown

## Cargos-alvo

Analista de Dados, BI Analyst, Data Scientist, Data Quality Analyst, Analista de Governança de Dados e Auditor de Dados.

## Segurança

Este projeto usa apenas dados sintéticos. Não inclui dados de clientes, pacientes, sistemas internos, documentos fiscais ou material institucional.
