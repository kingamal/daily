import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

movies_df = pd.read_csv('movies.csv')

plt.figure(figsize=(10, 6))
sns.histplot(movies_df['Rating'], bins=20, kde=True)
plt.title('Distribution of Movie Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()