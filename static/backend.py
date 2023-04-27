from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summarize(text, percentage):
    # print("Text:", text)
    # print("Percentage:", percentage)
    
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    tokens = [token.text for token in doc]
    
    # Compute word frequencies
    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
                    
    # Normalize word frequencies
    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / max_frequency
        
    # Compute sentence scores
    sentence_tokens = [sent for sent in doc.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        word_frequencies_sum = sum(word_frequencies[word.text.lower()] for word in sent if word.text.lower() in word_frequencies.keys())
        sentence_scores[sent] = word_frequencies_sum / len(sent)
        
    # Select top sentences based on sentence scores
    select_length = max(1, int(len(sentence_tokens) * percentage))
    summary_sentences = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    
    # Construct final summary
    summary = ""
    for sentence in summary_sentences:
        summary += sentence.text
        
    # print("Sentence scores:", sentence_scores)
    # print("Summary sentences:", summary_sentences)
    # print("Summary:", summary)
    
    return summary



@app.route("/summarize", methods=["POST"])
def summarize_route():
    data = request.get_json(force=True)

    if "text" not in data or "percentage" not in data:
        return jsonify({"error": "Text or percentage not provided"}), 400

    try:
        text = data["text"]
        percentage = float(data["percentage"])
        summary = summarize(text, percentage)
        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)