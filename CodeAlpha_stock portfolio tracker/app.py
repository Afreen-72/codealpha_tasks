# app.py
from flask import Flask, render_template, request, send_file
import csv
import io
import os

app = Flask(__name__)  # ← Fixed: was _name_ → __name__

# Predefined stocks with nice display names (you can update prices later)
STOCKS = {
    "AAPL": {"name": "Apple Inc.", "price": 195},
    "TSLA": {"name": "Tesla Inc.", "price": 378},
    "GOOGL": {"name": "Google (Alphabet)", "price": 178},
    "MSFT": {"name": "Microsoft", "price": 428},
    "AMZN": {"name": "Amazon", "price": 195},
    "NVDA": {"name": "NVIDIA", "price": 138},
    "META": {"name": "Meta Platforms", "price": 582}
}

@app.route('/', methods=['GET', 'POST'])
def index():
    portfolio = []
    total_value = 0.0
    csv_generated = False

    if request.method == 'POST':
        entries = int(request.form.get('entry_count', 0))
        
        for i in range(entries):
            symbol = request.form.get(f'stock_{i}')
            qty_str = request.form.get(f'quantity_{i}')
            
            if symbol and qty_str and symbol in STOCKS:
                try:
                    qty = int(qty_str)
                    if qty > 0:
                        price = STOCKS[symbol]["price"]
                        value = price * qty
                        total_value += value
                        portfolio.append({
                            'symbol': symbol,
                            'name': STOCKS[symbol]["name"],
                            'quantity': qty,
                            'price': price,
                            'value': value
                        })
                except ValueError:
                    continue

        # Generate CSV in memory and save to disk
        if request.form.get('save_csv') == 'yes' and portfolio:
            output = io.StringIO()
            writer = csv.writer(output)
            
            # Header
            writer.writerow(['Symbol', 'Company', 'Shares', 'Price per Share', 'Total Value'])
            for item in portfolio:
                writer.writerow([
                    item['symbol'],
                    item['name'],
                    item['quantity'],
                    f"${item['price']:.2f}",
                    f"${item['value']:.2f}"
                ])
            writer.writerow([])
            writer.writerow(['TOTAL PORTFOLIO VALUE', '', '', '', f"${total_value:.2f}"])
            
            # Save to file
            with open('portfolio.csv', 'w', newline='', encoding='utf-8') as f:
                f.write(output.getvalue())
            csv_generated = True

    return render_template('index.html', 
                         stocks=STOCKS, 
                         portfolio=portfolio, 
                         total_value=total_value,
                         csv_generated=csv_generated)

@app.route('/download')
def download():
    file_path = 'portfolio.csv'
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True, download_name='My_Stock_Portfolio.csv')
    return "No portfolio file found. Please generate one first.", 404

if __name__ == '__main__':  # ← Fixed: was _name_ → __name__
    app.run(debug=True)