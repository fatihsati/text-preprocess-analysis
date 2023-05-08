import re

preprocessing_techniques = ["Lower", "Lower+Punct", "Lower+Punct+Stop", "Lower+Punct+Stop+Stem", "Lower+Punct+Stop+Lemmatize"]

# load stopwords
# load stemming model
# load lemmatization model
# write model training codes
# write a function that will run each processing technique and model training, return the f1 scores

def process_text(text, technique):

    text = text.lower()
    
    if technique == "Lower+Punct":
        text = re.sub(r'[^\w\s]', '', text)
        
    elif technique == "Lower+Punct+Stop":
        text = re.sub(r'[^\w\s]', '', text)
        text = " ".join([word for word in text.split() if word not in stopwords])
        
    elif technique == "Lower+Punct+Stop+Stem":
        text = re.sub(r'[^\w\s]', '', text)
        text = " ".join([stem(word) for word in text.split() if word not in stopwords])
        
    elif technique == "Lower+Punct+Stop+Lemmatize":
        text = re.sub(r'[^\w\s]', '', text)
        text = " ".join([lemmatize(word) for word in text.split() if word not in stopwords])
        

    return text