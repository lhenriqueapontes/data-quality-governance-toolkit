from pathlib import Path
import argparse
import numpy as np
import pandas as pd


def generate(rows=1000, seed=42):
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({
        'customer_id': [f'C{i:05d}' for i in range(rows)],
        'signup_date': pd.date_range('2025-01-01', periods=rows, freq='D').astype(str),
        'segment': rng.choice(['A', 'B', 'C', 'D'], rows),
        'monthly_value': rng.normal(250, 80, rows).round(2),
        'status': rng.choice(['active', 'inactive', 'trial'], rows, p=[0.7, 0.2, 0.1]),
    })
    bad_idx = rng.choice(df.index, size=max(10, rows // 50), replace=False)
    df.loc[bad_idx, 'monthly_value'] = np.nan
    df = pd.concat([df, df.sample(10, random_state=seed)], ignore_index=True)
    df.loc[rng.choice(df.index, 8, replace=False), 'segment'] = 'UNKNOWN'
    return df


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rows', type=int, default=1000)
    parser.add_argument('--output', default='data/demo_quality_dataset.csv')
    args = parser.parse_args()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    generate(args.rows).to_csv(out, index=False)
    print(out)


if __name__ == '__main__':
    main()
