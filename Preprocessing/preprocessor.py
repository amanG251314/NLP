import re
import nltk
nltk.data.path.append('../nltk_data')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

class preprocess():
        def __init__(self,sentence):
            self.sentence=sentence

        #Preprocessing
        def remove_special_characters(self):
            string=re.sub(r'[^\w ]+',"",self.sentence)
            self.sentence=string
            #return string

        def remove_numeric(self):
            string=re.sub(r'[0-9]',"",self.sentence)
            self.sentence=string
            # return string

        def remove_extra_spaces(self):
            #print(self.sentence)
            string=' '.join(self.sentence.split())
            self.sentence=string
            # return string

        def remove_stop_words(self):
            string=' '.join([t for t in self.sentence.split() if t not in stop_words])
            self.sentence=string
            #return string
        
        def preprocess(self):
            self.remove_special_characters()
            self.remove_numeric()
            self.remove_extra_spaces()
            self.remove_stop_words()
            #sentence=remove_hinglish_words(sentence)
            return self.sentence