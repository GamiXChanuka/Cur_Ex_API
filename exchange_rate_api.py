from flask import Flask, jsonify
import requests

app = Flask(__name__)

URL = "https://www.cbsl.gov.lk/cbsl_custom/charts/usd/oneweek.php"

def get_latest_exchange_rate():
    """Fetch the latest exchange rate from the CBSL URL"""
    response = requests.get(URL)
    
    if response.status_code == 200:
        lines = response.text.strip().split("\n")
        last_line = lines[-1].split("\t")
        return {"date": last_line[0], "rate": float(last_line[1])}
    
    return {"error": "Failed to fetch data"}, 500

@app.route('/latest-usd-rate', methods=['GET'])
def latest_usd_rate():
    """API endpoint to get the latest USD exchange rate"""
    return jsonify(get_latest_exchange_rate())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
