import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nltk.download('stopwords')
english_stop_words = set(stopwords.words('english'))


pre_processed_df = pd.read_csv("reviews.csv") #Populate this function with
#the actual csv file generated from the map scraping script
pattern = r'[^a-zA-Z0-9\s]'
pre_processed_df['0'] = pre_processed_df['0'].str.replace(pattern, '', regex=True)
pre_processed_df['0'] = pre_processed_df['0'].str.lower()
text = pre_processed_df['0'].str.cat(sep=' ')
words = re.findall(r'\b\w+\b', text.lower())
filtered_words = [word for word in words if word not in english_stop_words]
no_stop_words_text = " ".join(filtered_words)

wordcloud = WordCloud(width=1000, height=600, background_color='white').generate(no_stop_words_text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
