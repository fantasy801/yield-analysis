import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("C:/Users/biyun/Desktop/yield_data.csv", encoding="utf-8")


print("温度 平均/最高/最低:", df["温度"].mean(), df["温度"].max(), df["温度"].min())
print("压力 平均:", df["压力"].mean())
print("收率 平均:", df["收率"].mean(), "  总能耗:", df["能耗"].sum())
print("温度-收率相关系数:", df["温度"].corr(df["收率"]))
print("压力-收率相关系数:", df["压力"].corr(df["收率"]))
bins = [60, 75, 85, 100]
labels = ["低温", "中温", "高温"]
df["温度档"] = pd.cut(df["温度"], bins=bins, labels=labels)
avg = df.groupby("温度档")["收率"].mean()
print("\n每档平均收率:")
print(avg)

low = df[df["收率"] < df["收率"].mean() - 0.08]
print("低收率批次：")
print(low[["批次", "温度", "收率"]])

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].scatter(df["温度"], df["收率"])
axes[0, 0].set_xlabel("温度 (°C)")
axes[0, 0].set_ylabel("收率")
axes[0, 0].set_title("温度 vs 收率")

axes[0, 1].bar(df["批次"], df["收率"])
axes[0, 1].set_xlabel("批次")
axes[0, 1].set_ylabel("收率")
axes[0, 1].set_title("批次 vs 收率")

axes[1, 0].bar(df["批次"], df["能耗"])
axes[1, 0].set_xlabel("批次")
axes[1, 0].set_ylabel("能耗")
axes[1, 0].tick_params(axis='x', rotation=90)
axes[1, 0].set_title("批次 vs 能耗")

axes[1, 1].hist(df["收率"])
axes[1, 1].set_xlabel("收率")
axes[1, 1].set_ylabel("频数")
axes[1, 1].set_title("收率分布")

fig.suptitle("化工批次收率分析总览")
fig.tight_layout()
fig.savefig("combined_analysis.png")

print("完成！大图已保存成 combined_analysis.png")