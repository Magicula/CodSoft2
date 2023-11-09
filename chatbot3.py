import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()

# Load the data files using 'with open' for improved file handling
with open('chatbot.json', 'r') as file:
    intents = json.load(file)

with open('words.pkl', 'rb') as file:
    words = pickle.load(file)

with open('classes.pkl', 'rb') as file:
    classes = pickle.load(file)

model = load_model('chatbot_model.model')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1  # Fixed the assignment operator here (changed '==' to '=')
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res[0]) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

# Define the get_response function (not shown in your original code)
def get_response(intents, intents_list):
    tag = intents[0]['intent']  # Get the intent with the highest probability
    list_of_intents = intents_list['intents']

    for intent in list_of_intents:
        if intent['tag'] == tag:
            responses = intent['responses']
            return random.choice(responses)

    return "I'm sorry, I don't understand that."
print("GO! Bot is running")
while True:
    message = input("You: ")
    ints = predict_class(message)
    response = get_response(ints, intents)
    print("Bot:", response)

