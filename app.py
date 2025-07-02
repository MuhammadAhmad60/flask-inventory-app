from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
        item = [
              {"name": "laptop", "price": "$900"},
              {"name": "Phone", "price": "$500"},
              {"name": "Tablet", "price": "$399"}
        ]
        return render_template('products.html', products = item)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)