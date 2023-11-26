from flask import Flask, render_template, request
import difflib

app = Flask(__name__)

def compare_texts(text1, text2):
    seq_matcher = difflib.SequenceMatcher(None, text1, text2)
    matching_blocks = seq_matcher.get_matching_blocks()
    total_size = sum(block.size for block in matching_blocks)
    similarity_ratio = total_size / max(len(text1), len(text2))
    return similarity_ratio

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    text1 = request.form['text1']
    text2 = request.form['text2']

    similarity_ratio = compare_texts(text1, text2)

    return render_template('result.html', similarity_ratio=similarity_ratio)

if __name__ == '__main__':
    app.run(debug=True)
