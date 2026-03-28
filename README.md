# 🚀 Flask Mock Server - Customer API

This service is a **Flask-based mock API** that provides customer data from a JSON file. It is part of a larger backend data pipeline system.

---

## 🌐 Live Application

👉 https://mock-server-x04f.onrender.com/

---

## 🧩 Overview

The mock server simulates a real-world customer data service by:

* Serving customer data from a JSON file
* Supporting pagination
* Providing REST API endpoints
* Acting as a data source for the FastAPI ingestion pipeline

---

## ⚙️ Tech Stack

* Python 3.10+
* Flask
* JSON (data storage)

---

## 📁 Project Structure

```id="str1"
mock-server/
│
├── app.py
├── data/
│   └── customers.json
├── Dockerfile
└── requirements.txt
```

---

## 🚀 How to Run Locally

### 1. Clone the repository

```id="cmd1"
git clone https://github.com/Chandu-challa/mock-server
cd mock-server
```

### 2. Install dependencies

```id="cmd2"
pip install -r requirements.txt
```

### 3. Run the server

```id="cmd3"
python app.py
```

Server will start at:
👉 http://localhost:5000

---

## 🔗 API Endpoints

### 🔹 Health Check

```id="api1"
GET /api/health
```

Response:

```id="res1"
{
  "status": "ok"
}
```

---

### 🔹 Get Customers (Paginated)

```id="api2"
GET /api/customers?page=1&limit=10
```

Response:

```id="res2"
{
  "data": [...],
  "total": 20,
  "page": 1,
  "limit": 10
}
```

---

### 🔹 Get Customer by ID

```id="api3"
GET /api/customers/{id}
```

* Returns a single customer
* Returns **404** if not found

---

## 🧪 Example Usage

### Fetch Customers

```id="ex1"
curl https://mock-server-x04f.onrender.com/api/customers?page=1&limit=5
```

---

## ✅ Features Implemented

* ✔ JSON-based data source (not hardcoded)
* ✔ Pagination support (page & limit)
* ✔ REST API endpoints
* ✔ Error handling (404 for missing customer)
* ✔ Docker support

---

## 🐳 Docker Support

### Build Image

```id="dock1"
docker build -t mock-server .
```

### Run Container

```id="dock2"
docker run -p 5000:5000 mock-server
```

---

## ⚠️ Notes

* Data is loaded from a JSON file at runtime
* Designed to simulate an external API for ingestion

---

## 📌 Author

**Chandu Challa**

---

## 🎯 Summary

This mock server is designed to:

* Simulate real API behavior
* Provide structured customer data
* Support integration with a data pipeline system

---
