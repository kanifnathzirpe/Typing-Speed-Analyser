from flask import Flask, render_template, request, jsonify
import time
import random

app = Flask(__name__)


sentences = [
    "The quick brown fox jumps over the lazy dog. Python is a powerful and easy-to-learn programming language. Artificial Intelligence is the future of technology. Typing speed is important for programmers and writers. A journey of a thousand miles begins with a single step.", 
    "Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusantium tempora est velit praesentium eos dicta, cum rerum odit, eligendi perspiciatis labore itaque maxime. A fuga eum sed eaque aliquid deleniti.",
    "The blue sky was filled with the aroma of grandmother’s delicious cookies as birds chirped happily. Meanwhile, a dog ran excitedly across the street, barking loudly at the unforgettable concert happening nearby. In the chaos, I suddenly realized I had forgotten to bring the important documents to the meeting.",
    "The delicious aroma of grandmother’s cookies filled the kitchen as birds chirped happily outside. Meanwhile, an excited dog ran across the street, barking loudly at the passing crowd. In all the commotion, I suddenly remembered I had an important meeting but forgot to bring the documents.",
    "The sky was bright blue, and birds chirped as if celebrating the beautiful day. A dog ran excitedly down the street, barking at people heading to an unforgettable concert. Lost in the moment, I suddenly panicked, realizing I had left the important documents at home.",
    "The streets buzzed with energy as people gathered for the big concert. A dog dashed through the crowd, barking loudly, while the sweet smell of freshly baked cookies filled the air. Meanwhile, I stood frozen, realizing I had forgotten to bring the meeting documents.",
    "The kitchen was warm with the smell of freshly baked cookies, and birds outside sang in harmony. Suddenly, a dog ran across the street, barking at the excited concertgoers. I watched the scene unfold, only to realize I had completely forgotten about my important meeting.",
    "The blue sky stretched endlessly as birds sang their cheerful melodies. A dog raced past, barking at a group of people eagerly heading to a concert. Meanwhile, I stood still, realizing with dread that my meeting was about to start, and my documents were still at home."
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
