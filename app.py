from flask import Flask, jsonify, request
import os
import json

app = Flask(__name__)

# Load JSON data
with open("data/customers.json") as f:
    customers = json.load(f)

# Health check
@app.route("/api/health")
def health():
    return {"status": "ok"}

# Get all customers (pagination)
@app.route("/api/customers")
def get_customers():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    start = (page - 1) * limit
    end = start + limit

    return jsonify({
        "data": customers[start:end],
        "total": len(customers),
        "page": page,
        "limit": limit
    })

# Get single customer
@app.route("/api/customers/<cid>")
def get_customer(cid):
    for c in customers:
        if c["customer_id"] == cid:
            return jsonify(c)
    return {"error": "Customer not found"}, 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)