import re
import nltk
nltk.data.path.append('../nltk_data')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

class preprocessor():
        def __init__(self,sentence):
            self.sentence=sentence

        #Preprocessing
        def replace_newlines_with_space(self):
            self.sentence = self.sentence.replace('\n', ' ')
            
        def remove_special_characters(self):
            string=re.sub(r'[^\w ]+',"",self.sentence)
            self.sentence=string

        def remove_numeric(self):
            string=re.sub(r'[0-9]',"",self.sentence)
            self.sentence=string
        

        def remove_extra_spaces(self):
            string=' '.join(self.sentence.split())
            self.sentence=string

        def lower_tokens(self):
            string=' '.join([token.lower() for token in self.sentence.split()])
            self.sentence=string

        def remove_stop_words(self):
            string=' '.join([t for t in self.sentence.split() if t not in stop_words])
            self.sentence=string
        
        def preprocess(self):
            self.replace_newlines_with_space()
            self.remove_special_characters()
            self.remove_numeric()
            self.remove_extra_spaces()
            self.remove_stop_words()
            self.lower_tokens()
            #sentence=remove_hinglish_words(sentence)
            return self.sentence
        
if __name__ == "__main__":
     sentense = "This   is a $Test FILE"
     preprocessor = preprocessor(sentense)
     sentense = preprocessor.preprocess()
     print(sentense)