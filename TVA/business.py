import pandas as pd
import re
import string
import numpy as np
import nltk.data
import nltk
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import spacy
import nltk
import matplotlib.pyplot as plt
import matplotlib as mpl
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image


# nltk.download('stopwords')

nlp = spacy.load("en_core_web_sm")

def remove_emojis(data):

	emoj = re.compile("["
			u"\U0001F600-\U0001F64F"  # emoticons
			u"\U0001F300-\U0001F5FF"  # symbols & pictographs
			u"\U0001F680-\U0001F6FF"  # transport & map symbols
			u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
			u"\U00002500-\U00002BEF"  # chinese char
			u"\U00002702-\U000027B0"
			u"\U00002702-\U000027B0"
			u"\U000024C2-\U0001F251"
			u"\U0001f926-\U0001f937"
			u"\U00010000-\U0010ffff"
			u"\u2640-\u2642" 
			u"\u2600-\u2B55"
			u"\u200d"
			u"\u23cf"
			u"\u23e9"
			u"\u231a"
			u"\ufe0f"  # dingbats
			u"\u3030"
			"]+", re.UNICODE)

	return re.sub(emoj, '', data)


#remove punctuations
def remove_punct(content):

	data = str.maketrans('','',string.punctuation)

	return content.translate(data)

def clean_text(row):

	content = row['content']

	all_words = content.split()

	stop_words = stopwords.words('english')

	raw_words_list = [word for word in all_words if not word in stop_words]

	raw_words = ' '.join(raw_words_list)

	row['raw_words'] = raw_words
	
	return row

def prepocess():

	pd.set_option('display.max_colwidth', None)

	missing_value = ["NaN", "N/a", "na", np.nan]

	df = pd.read_csv('static/user-feedback.csv', na_values = missing_value)

	df = df[["userName", "content", "score", "thumbsUpCount"]]

	df['content'] = df['content'].apply(remove_emojis)

	#remove punctuations
	df['content'] = df['content'].apply(remove_punct)

	df = df.apply(clean_text, axis=1)

	df = df.dropna()

	return df

def sentiment_scores(row):
    
    sentence = row["content"]
 
    sid_obj = SentimentIntensityAnalyzer()
 
    sentiment_dict = sid_obj.polarity_scores(sentence)
    
    row["polarity_score"] = sentiment_dict['compound']
    
    return row

def assign_feedback(row):
    
    current_review = row['polarity_score']
    
    if current_review >= 0.05 :
        row['feedback'] = 1

    elif current_review <= - 0.05 :
        row['feedback'] = -1

    else :
        row['feedback'] = 0
    
    return row
	

def assign_cols(df):

	df = df.apply(sentiment_scores, axis = 1)

	df = df.apply(assign_feedback, axis = 1)

	return df

def split_df(df):

	df_negative = df[df['feedback'] == -1]

	df_negative.to_csv('static/negative.csv', index= False)

	df_neutral = df[df['feedback'] == 0]

	df_neutral.to_csv('static/neutral.csv', index= False)

	df_positive = df[df['feedback'] == 1]

	df_positive.to_csv('static/positive.csv', index= False)

	data = {
		'df_negative' : df_negative,
		'df_neutral' : df_neutral,
		'df_positive' : df_positive,
	}

	return data

def get_nouns(row):

	content = row['raw_words']

	doc = nlp(content)

	noun_phrases =  [chunk.text for chunk in doc.noun_chunks]

	nouns = " ".join(noun_phrases)

	row['keywords'] = nouns

	return row

def add_noun_chunks(df):

	df = df.apply(get_nouns, axis = 1)

	return df

def create_word_cloud(df, filename):

	text = df.content.tolist() 

	# for content in all_content:

	# text = df[df.content==content]

	# join the list and lowercase all the words
	text = ' '.join(text).lower()

	#create the wordcloud object
	wordcloud = WordCloud(stopwords = STOPWORDS,
							collocations=True).generate(text)

	#plot the wordcloud object
	plt.imshow(wordcloud, interpolation='bilInear')
	plt.axis('off')
	plt.savefig(f"static/{filename}")

def create_word_clouds(data):

	create_word_cloud(data["df_negative"], "negative")
	create_word_cloud(data["df_neutral"], "neutral")
	create_word_cloud(data["df_positive"], "positive")

def process():
	
	df = prepocess()

	df = assign_cols(df)

	df = add_noun_chunks(df)

	data = split_df(df)

	create_word_clouds(data)

	df.to_csv('results.csv')

	return df

if __name__=='__main__':

	process()


