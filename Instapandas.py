import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df= pd.read_csv(r'C:\Users\AMAN KUMAR SINGH\Downloads\Socialanaly2.csv')
print(df)

# sns.countplot(x='Instastories', data=df, hue='Instastories')
# sns.countplot(x='Instaaccount', data=df, hue='Instaaccount')
# sns.countplot(x='Instafeeds', data=df, hue='Instaaccount')

#
# plt.title("Candidates Vs Instafeeds", fontsize=18)
# plt.xlabel("Instaaccount", fontsize=15)
plt.ylabel("Candidates", fontsize=15)
plt.show()