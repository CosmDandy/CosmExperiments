import pandas as pd
import seaborn as sns

system12 = [[10, 12, 14, 16, 18, 21, 24, 28, 33, 39, 45, 51], [34]]
system11 = [[11, 13, 15, 18, 21, 24, 28, 33, 39, 45, 51], [34]]
system9 = [[12, 14, 16, 18, 21, 24, 26, 32, 36], [22, 30, 40]]
wheel_l = 0.002288
cadence = 90
systems = [system11]

df = pd.DataFrame({
    "rear": [],
    "front": [],
    "g_ratio": [],
    "speed" : []})

for s in systems:
    rear = s[0]
    front = s[1]
    for f in front:
        front_t = int(f)
        for r in rear:
            rear_t = int(r)
            g_ratio = front_t / rear_t
            speed = wheel_l * cadence * 60 * g_ratio
            df.loc[len(df)] = [rear_t, front_t, g_ratio, speed]
    print(df)


sns.relplot(
    data=df,
    x="g_ratio", y="speed"
)