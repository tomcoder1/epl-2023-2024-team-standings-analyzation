df1 = df[['Squad' , 'Rk' , 'GD']]
plt.figure(figsize=(20,12))
plt.bar(df1['Rk'], df1['GD'], color=team_colors)

plt.xlabel('Rank')
plt.ylabel('Goal Difference')
plt.title('Goal Difference by Rank - EPL - 2023-2024')
for index, row in df1.iterrows():
    if row["GD"] > 0:
        plt.text(row["Rk"], row["GD"] + 1, row["Squad"], ha="center", va="top", fontsize=8)
    elif row["GD"] < 0:
        plt.text(row["Rk"], row["GD"] - 1, row["Squad"], ha="center", va="bottom", fontsize=8)
    else:
        plt.text(row["Rk"], 0, row["Squad"], ha="center", va="center", fontsize=8)
plt.grid(True)
plt.show()
