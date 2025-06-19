###🛍️ Real-Time E-Commerce Sales Dashboard

This project simulates a real-time e-commerce sales pipeline using the Fake Store API ([https://fakestoreapi.com/](https://fakestoreapi.com/)), stores data in a local SQLite database, and connects the data to Power BI for real-time visualization and insights.

---

📌 Project Overview

In this project, I simulate real-time product sales for an e-commerce store and build a dynamic dashboard to monitor key sales KPIs such as:

* Revenue trends
* Product and category performance
* Quantity sold
* Hourly sales breakdown

The pipeline mimics how real-time sales systems work in companies, providing a data analyst-friendly structure that can be easily extended to cloud-based environments.

---

🔧 Tech Stack

| Component   | Technology                                                              |
| ----------- | ----------------------------------------------------------------------- |
| API Source  | Fake Store API ([https://fakestoreapi.com/](https://fakestoreapi.com/)) |
| Programming | Python 3                                                                |
| Database    | SQLite                                                                  |
| Dashboard   | Power BI                                                                |
| Scheduling  | Manual simulation via `time.sleep()`                                    |

---

📂 Project Structure

real\_time\_ecommerce\_sales\_dashboard/
├── fetch\_data.py          — Fetches product data from FakestoreAPI
├── db\_utils.py            — Initializes DB and inserts simulated sales
├── sales\_simulator.py     — Main script to simulate and store sales every 10 seconds
├── sales\_data.db          — SQLite DB file (auto-created)
├── README.md              — Project documentation

## 🧪 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/real-time-ecommerce-dashboard.git
cd real-time-ecommerce-dashboard
```

### 2. Set up a virtual environment (optional but recommended)

```bash
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install requests
```

### 4. Run the sales simulator

```bash
python sales_simulator.py
```

This will:

* Fetch all product data once from the API
* Every 10 seconds, simulate a random product sale
* Insert that sale into the `sales_data.db` SQLite database

---

## 📊 Power BI Integration

### How to Connect SQLite to Power BI:

1. Open **Power BI Desktop**
2. Go to **Home → Get Data → More**
3. Select **SQLite Database**
4. Browse to and select `sales_data.db`
5. Load the `sales` table
6. Build visualizations like:

   * Total revenue
   * Revenue by product
   * Sales by category
   * Revenue over time (hourly)

✅ You can refresh the dashboard to simulate real-time updates.

---

## 📈 Sample KPIs & Charts

* **💰 Total Revenue** (Card visual)
* **📦 Quantity Sold per Product** (Bar chart)
* **⏰ Revenue by Hour** (Line chart using `sale_time`)
* **🧾 Category Breakdown** (Pie chart)

---

## ✅ Features

* Simulated real-time data updates
* REST API integration
* SQLite backend (easily replaceable with Firebase, PostgreSQL, BigQuery)
* Easy connection with Power BI
* Beginner-friendly and fully modular

