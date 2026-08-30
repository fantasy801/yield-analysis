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

low = df[df["收率"] < df["收率"].mean() - 0.08]
print("低收率批次：")
print(low[["批次", "温度", "收率"]])


plt.figure()
plt.scatter(df["温度"], df["收率"])
plt.xlabel("温度 (°C)")
plt.ylabel("收率")
plt.title("温度 vs 收率")
plt.savefig("scatter_temp_yield.png")


plt.figure()
plt.bar(df["批次"], df["收率"])
plt.xlabel("批次")
plt.ylabel("收率")
plt.title("批次 vs 收率")
plt.savefig("bar_temp_yield.png")


plt.figure()
plt.bar(df["批次"], df["能耗"])
plt.xlabel("批次")
plt.ylabel("能耗")
plt.title("批次 vs 能耗")
plt.xticks(rotation=90)
plt.savefig("bar_energy.png")     

plt.figure()
plt.hist(df["收率"])
plt.xlabel("收率")
plt.ylabel("频数")
plt.title("收率分布")
plt.savefig("hist_yield.png")

print("完成！图已保存成 .png 文件")