import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df= pd.read_csv(r'C:\Users\AMAN KUMAR SINGH\Downloads\Socialanaly2.csv')
print(df)

sns.countplot( x='Fbaccount', data=df, hue='Fbaccount')

#  # sns.countplot( x='Fbstories', data=df, hue='Fbstories')
#  # sns.countplot(x='Fbfeeds', data=df, hue='Fbfeeds')
#
# plt.title("Candidates Vs Fbaccount", fontsize=18)
# plt.xlabel("Fbaccount", fontsize=15)
# plt.ylabel("Candidates", fontsize=15)

plt.show()