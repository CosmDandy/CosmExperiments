import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

system12 = [12, [10, 12, 14, 16, 18, 21, 24, 28, 33, 39, 45, 51], [34]]
system11 = [11, [11, 13, 15, 18, 21, 24, 28, 33, 39, 45, 51], [34]]
system9 = [9, [12, 14, 16, 18, 21, 24, 26, 32, 36], [22, 30, 40]]
wheel_l = 0.002288
cadence = 90
systems = [system11]

df = pd.DataFrame({
    "rear": [],
    "front": [],
    "g_ratio": [],
    "speed": [],
    "system_n": []})

for s in systems:
    system_n = s[0]
    rear = s[1]
    front = s[2]
    for f in front:
        front_t = int(f)
        for r in rear:
            rear_t = int(r)
            g_ratio = front_t / rear_t
            speed = wheel_l * cadence * 60 * g_ratio
            df.loc[len(df)] = [rear_t, front_t, g_ratio, speed, system_n]
    print(df)


sns.relplot(
    data=df,
    x="g_ratio", y="speed"
)

plt.show()