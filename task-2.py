import pandas as pd

data_frame = pd.read_csv('resources/cars93.csv', sep=',')
cars_dict = data_frame.to_dict(orient='records')
cars_list = data_frame.to_numpy()

for group_name, group_df in list(data_frame.groupby('Type')) + [('All types', data_frame)]:
    print(f"\n=== {group_name} ===")

    group_df = group_df.copy()
    group_df['Diff'] = group_df['Max.Price'] - group_df['Min.Price']

    percentage = len(group_df) * 100 / len(data_frame)
    mean = group_df['Diff'].mean()
    var = group_df['Diff'].var()
    median = group_df['Diff'].median()
    iqr = group_df['Diff'].quantile(0.75) - group_df['Diff'].quantile(0.25)

    stats = {
        "Mean": mean,
        "Variance": var,
        "Median": median,
        "IQR": iqr
    }

    print(f"{"Frequency":8}: {percentage:8.3f}" + "%")
    for name, value in stats.items():
        print(f"{name:8}: {value:8.3f}")