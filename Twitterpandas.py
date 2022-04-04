import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv(r'C:\Users\AMAN KUMAR SINGH\Downloads\Socialanaly2.csv')
print(df)

# sns.countplot( x='Twitterusage', data=df, hue='Twitterusage')
# sns.countplot( x='Tweetprefer', data=df, hue='Tweetprefer')
# sns.countplot(x='Tweetperiod', data=df, hue='Tweetperiod')
sns.countplot(x='Twitteraccount', data=df, hue='Twitteraccount')



plt.title("Candidates Vs Twitteraccount", fontsize=18)
plt.title("Candidates Vs Tweetprefer", fontsize=18)
plt.title("Candidates Vs Tweetperiod", fontsize=18)
plt.title("Candidates Vs Twitterusage", fontsize=18)
plt.xlabel("Tweetperiod", fontsize=15)
plt.ylabel("Candidates", fontsize=15)
plt.show()
