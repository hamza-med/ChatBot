#import libraries
from keras.preprocessing.sequence import pad_sequences
import pickle
from tensorflow import keras
import numpy as np

# load the model and the tokenizer
model = keras.models.load_model('tools/chatbot_120_epochs.h5')
with open("tools/tokenizer_pickle", "rb") as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)

# define the prediction functions


def vectorize_stories(data, word_index=tokenizer.word_index, max_story=156, max_question=6):
    X = []
    Xq = []
    Y = []
    for story, query, answer in data:
        x = [word_index[word.lower()] for word in story]
        xq = [word_index[word.lower()] for word in query]

        y = np.zeros(len(word_index)+1)
        y[word_index[answer]] = 1

        X.append(x)
        Xq.append(xq)
        Y.append(y)
    return (pad_sequences(X, maxlen=max_story), pad_sequences(Xq, maxlen=max_question), np.array(Y))


def predict(story, question):
    mydata = [(story.split(), question.split(), 'yes')]
    my_story, my_ques, my_ans = vectorize_stories(mydata)
    pred_results = model.predict(([my_story, my_ques]))
    # Generate prediction from model
    val_max = np.argmax(pred_results[0])

    for key, val in tokenizer.word_index.items():
        if val == val_max:
            k = key

    return (k, pred_results[0][val_max])
