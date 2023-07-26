from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)


def load_dictionary():
    with open("word_details.json", "r") as json_file:
        dictionary = json.load(json_file)
    return dictionary


def search_word(word):
    dictionary = load_dictionary()
    if word in dictionary:
        return dictionary[word]
    else:
        return None


def autocomplete(prefix):
    dictionary = load_dictionary()
    results = [word for word in dictionary.keys() if word.startswith(prefix)]
    return results


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    word = request.form['word']
    definition = search_word(word)
    return jsonify({'definition': definition})


@app.route('/autocomplete', methods=['GET'])
def autocomplete_route():
    prefix = request.args.get('prefix')
    results = autocomplete(prefix)
    return jsonify({'results': results})


if __name__ == '__main__':
    app.run(debug=True)
