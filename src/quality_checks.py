from pathlib import Path
import argparse
import pandas as pd

VALID_SEGMENTS = {'A', 'B', 'C', 'D'}
VALID_STATUS = {'active', 'inactive', 'trial'}


def load_data(path):
    return pd.read_csv(path)


def completeness(df):
    total = len(df)
    rows = []
    for col in df.columns:
        rows.append({'column': col, 'missing_count': int(df[col].isna().sum()), 'missing_pct': round(df[col].isna().mean() * 100, 2)})
    return pd.DataFrame(rows)


def duplicates(df):
    return df[df.duplicated(keep=False)].copy()


def invalid_domains(df):
    bad_segment = df[~df['segment'].isin(VALID_SEGMENTS)].copy()
    bad_segment['issue'] = 'invalid_segment'
    bad_status = df[~df['status'].isin(VALID_STATUS)].copy()
    bad_status['issue'] = 'invalid_status'
    return pd.concat([bad_segment, bad_status], ignore_index=True)


def numeric_outliers(df):
    values = df['monthly_value'].dropna()
    q1 = values.quantile(0.25)
    q3 = values.quantile(0.75)
    iqr = q3 - q1
    low = q1 - 1.5 * iqr
    high = q3 + 1.5 * iqr
    return df[(df['monthly_value'] < low) | (df['monthly_value'] > high)].copy()


def export_report(input_path, output_dir='reports'):
    df = load_data(input_path)
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    completeness(df).to_csv(out / 'completeness.csv', index=False)
    duplicates(df).to_csv(out / 'duplicates.csv', index=False)
    invalid_domains(df).to_csv(out / 'invalid_domains.csv', index=False)
    numeric_outliers(df).to_csv(out / 'numeric_outliers.csv', index=False)
    pd.DataFrame([{
        'rows': len(df),
        'columns': len(df.columns),
        'duplicate_rows': len(duplicates(df)),
        'invalid_domain_rows': len(invalid_domains(df)),
        'outlier_rows': len(numeric_outliers(df)),
    }]).to_csv(out / 'summary.csv', index=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='data/demo_quality_dataset.csv')
    parser.add_argument('--output-dir', default='reports')
    args = parser.parse_args()
    export_report(args.input, args.output_dir)
    print(f'Reports saved to {args.output_dir}')


if __name__ == '__main__':
    main()
