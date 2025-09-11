from flask import Flask, render_template, jsonify
from models.stock_model import get_top_stocks

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/stocks', methods=['GET'])
def api_stocks():
    stocks = get_top_stocks()
    return jsonify(stocks)

if __name__ == '__main__':
    app.run(debug=True)