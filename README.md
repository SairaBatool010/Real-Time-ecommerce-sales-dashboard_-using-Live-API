
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

