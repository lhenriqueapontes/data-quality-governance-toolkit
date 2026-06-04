# Data Quality Governance Toolkit

Projeto funcional de qualidade de dados com Python e dataset sintetico.

## Como executar

```bash
pip install -r requirements.txt
python src/generate_demo_dataset.py --rows 1000 --output data/demo_quality_dataset.csv
python src/quality_checks.py --input data/demo_quality_dataset.csv --output-dir reports
```

## Saidas

- `reports/summary.csv`
- `reports/completeness.csv`
- `reports/duplicates.csv`
- `reports/invalid_domains.csv`
- `reports/numeric_outliers.csv`

## Verificacoes

- valores ausentes por coluna
- linhas duplicadas
- categorias fora do dominio esperado
- outliers numericos
- resumo geral da base

## Estrutura

```text
src/generate_demo_dataset.py
src/quality_checks.py
data/demo_quality_dataset.csv
reports/
```

## Dados

Todos os registros sao ficticios.

## Licenca

MIT License.
