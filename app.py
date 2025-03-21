from flask import Flask, render_template, request, jsonify
import time
import random

app = Flask(__name__)


sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful and easy-to-learn programming language.",
    "Artificial Intelligence is the future of technology.",
    "Typing speed is important for programmers and writers.",
    "A journey of a thousand miles begins with a single step."
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/typing-test')
def typing_test():
    sentence = random.choice(sentences) 
    return render_template('type.html', sentence=sentence)

@app.route('/calculate-speed', methods=['POST'])
def calculate_speed():
    data = request.get_json()
    original_text = data['sentence']
    user_text = data['typedText']
    start_time = float(data['startTime'])
    end_time = time.time()

    time_taken = end_time - start_time
    words = len(original_text.split())
    wpm = (words / time_taken) * 60  

    
    correct_chars = sum(1 for a, b in zip(original_text, user_text) if a == b)
    accuracy = (correct_chars / len(original_text)) * 100

    return jsonify({
        'timeTaken': round(time_taken, 2),
        'wpm': round(wpm, 2),
        'accuracy': round(accuracy, 2)
    })

if __name__ == '__main__':
    app.run(debug=True, port=8000)
