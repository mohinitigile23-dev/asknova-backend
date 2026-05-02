from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "AskNova Backend Running 🚀"

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get("question")
    language = data.get("language")

    answer = f"Sample answer in {language} for: {question}"

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
