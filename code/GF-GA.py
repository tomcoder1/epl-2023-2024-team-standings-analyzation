gf_ga = df[['Squad', 'GF', 'GA']]
import matplotlib.pyplot as plt
plt.figure(figsize=(20, 12))
plt.scatter(gf_ga['GF'], gf_ga['GA'], color=team_colors)

plt.xlabel("Goals scored")
plt.ylabel("Goals conceded")
plt.title("Goals scored and goals conceded - EPL - 2023-2024")

gf_ga.apply(lambda row: plt.text(row["GF"], row["GA"], row["Squad"], ha="left", va="bottom", fontsize=8), axis=1)

plt.grid(True)
plt.show()
