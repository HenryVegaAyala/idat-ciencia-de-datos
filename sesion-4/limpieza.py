import pandas as pd

df = pd.read_csv('ciudad.csv')

print(f"Data original:")
print(df)

df_drop = df.dropna()
print(f"-" * 50)
print(f"Data dropped:")
print(df_drop)

df_fill = df.fillna(0)
print(f"=" * 50)
print(f"Data filled:")
print(df_fill)

df["edad"] = df["edad"].fillna(df["edad"].mean())
df["ciudad"] = df["ciudad"].fillna("Desconocida")
print(f"+" * 50)
print(df)


