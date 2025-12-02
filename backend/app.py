
from flask import Flask, jsonify, request
import uuid, datetime

app = Flask(__name__)

# Simple in-memory stores for demo
BILLS = []
ALERTS = []
FORECASTS = []

# Seed with an example
BILLS.append({
    "id": str(uuid.uuid4()),
    "kwh": 320.0,
    "tariff": "verde",
    "flag": "vermelha",
    "total": 420.5,
    "findings": ["Consumo muito alto"]
})
ALERTS.append({"id": str(uuid.uuid4()), "message": "Erro de fatura detectado", "severity": "HIGH", "timestamp": datetime.datetime.utcnow().isoformat()})
FORECASTS.append({"id": str(uuid.uuid4()), "forecast": 200.0, "created_at": datetime.datetime.utcnow().isoformat()})

@app.after_request
def add_cors(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return resp

@app.route('/bills', methods=['GET'])
def get_bills():
    return jsonify(BILLS)

@app.route('/alerts', methods=['GET'])
def get_alerts():
    return jsonify(ALERTS)

@app.route('/forecasts', methods=['GET'])
def get_forecasts():
    return jsonify(FORECASTS)

# simple endpoints to add data (protected for demo; in prod add auth)
@app.route('/bills', methods=['POST'])
def post_bill():
    payload = request.get_json() or {}
    entry = {
        "id": str(uuid.uuid4()),
        "kwh": float(payload.get('kwh', 0)),
        "tariff": payload.get('tariff',''),
        "flag": payload.get('flag',''),
        "total": float(payload.get('total',0)),
        "findings": payload.get('findings', [])
    }
    BILLS.insert(0, entry)
    return jsonify(entry), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
