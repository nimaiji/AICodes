import numpy as np
import matplotlib.pyplot as plt
import glob
import json
import pandas as pd
from sklearn.model_selection import KFold,train_test_split
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
import unicodedata
from nltk.cluster import KMeansClusterer
from sklearn.cluster import MiniBatchKMeans
import nltk.data
import nltk.corpus
from nltk.corpus import wordnet
from nltk import WordNetLemmatizer

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')

class CorpusLoader():
    
    def __init__(self, path, folds=12, shuffled=True, categories=None, is_json=False):
        self.path = path
        self.folds = KFold(n_splits=folds, shuffle=shuffled)
        self.contents, self.pathes = self.read_docs()
        self.has_json = is_json
        self.df = self.get_df()
        if not is_json:
            self.dataset = self.get_dataset()
        
    def read_docs(self):
        pathes = glob.glob(self.path)
        contents = []
        for p in pathes:
            with open(p) as file:
                content = file.read()
                contents.append(content)
        return contents, pathes
    
    def read_json(self) -> str:
        with open(self.path,'r') as file:
            string_json = file.read()
        self.has_json = True
        return string_json
    
    def get_dataset(self):
        dataset = []
        for c in self.contents:
            dataset += nltk.tokenize.sent_tokenize(c)
        return np.array(dataset)
    
    def get_df(self):
        if self.has_json:
            self.df = pd.read_json(self.path)
        else:
            self.df = pd.DataFrame(self.get_dataset(), columns=['instances'])
        return self.df
    
    def get_splits(self):
        return train_test_split(self.dataset, random_state= 20)
    
    def __iter__(self):
        for train_idx, test_idx in self.folds.split(self.df):
            X_train = self.dataset[train_idx]
            X_test = self.dataset[test_idx]
            yield X_train, X_test
            

class TextNormalizer(BaseEstimator, TransformerMixin):

    def __init__(self, lang='english'):
        self.stopwords = set(nltk.corpus.stopwords.words(lang))
        self.lemmatizer = WordNetLemmatizer()

    def is_stopword(self, token: str) -> bool:
        return token.lower() in self.stopwords

    def is_punct(self, token: str) -> bool:
        return any(unicodedata.category(char).startswith('P') for char in token)
    
    def is_number(self, token):
        return any(unicodedata.category(char).startswith('N') for char in token)

    def lemmatize_pos(self, token:str, tag):
        
        tagger = {
            'N': wordnet.NOUN,
            'V': wordnet.VERB,
            'R': wordnet.ADV,
            'J': wordnet.ADJ
        }.get(tag, wordnet.NOUN)
        return self.lemmatizer.lemmatize(token, tagger)

    def normalize(self, instances):
        data = []
        for ins in instances:
            current_sen = nltk.pos_tag(nltk.word_tokenize(ins))
            
            data.append(' '.join([
                self.lemmatize_pos(token.lower(), pos) for token, pos in current_sen
                if not self.is_punct(token) and not self.is_stopword(token) and not self.is_number(token)
            ]))
            
        return np.array(data)
            
    def fit(self, X, y=None):
        return self

    def transform(self, instances):
        return self.normalize(instances)
    

class KMeansClusterer(BaseEstimator, TransformerMixin):

    def __init__(self, k=7):
        self.k = k
        self.distance = nltk.cluster.util.cosine_distance
        self.model = MiniBatchKMeans(self.k)

    def fit(self, X, y=None):
        return self

    def transform(self, contents):
        return self.model.fit_predict(contents)