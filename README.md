

---

# 📊 Dashboard — FinanceCore Analytics

## 🚀 Overview

**FinanceDashboard ** is a Streamlit-based financial analytics application designed to explore banking data, monitor KPIs, and analyze customer risk profiles using PostgreSQL.

The project focuses on building an interactive dashboard for:

* Executive financial reporting
* Customer risk analysis
* Data-driven decision support

---

## 📁 Project Structure

```text id="structure"
dashboard_bank2/
│
├── app.py                     # Main navigation (Streamlit entry point)
│
├── pages/                     # Dashboard pages
│   ├── vue_executive.py      # Executive KPIs & global overview
│   ├── analyse_risque.py     # Credit risk analysis
│
├── utils/
│   └── db.py                 # Database connection (PostgreSQL engine)
│
└── README.md                 # Project documentation
```

---

## 🎯 Features

### 📊 Executive Dashboard

* Key Performance Indicators (KPIs)
* Total transactions
* Total revenue (CA)
* Active customers
* Average transaction value

### ⚠️ Risk Analysis

* Customer credit scoring
* Risk segmentation (Premium / Standard / Risky)
* Identification of high-risk clients

### 🔗 Database Integration

* PostgreSQL connection via SQLAlchemy
* Real-time data extraction
* Dynamic SQL queries for analytics

---

## 🛠️ Tech Stack

* **Python** 🐍
* **Streamlit** ⚡
* **PostgreSQL** 🗄️
* **Pandas** 🐼
* **SQLAlchemy** 🔗

---

## ▶️ How to Run the Project

### 1. Clone repository

```bash id="clone"
git clone [https://github.com/your-username/dashboard_bank2.git](https://github.com/ouiam555/FinanceDashboard.git)
cd FinanceDashboard
```

### 2. Create virtual environment

```bash id="venv"
python -m venv venv
venv\Scripts\activate   # Windows
```



### 3. Run Streamlit app

```bash id="run"
streamlit run app.py
```

---

## 🧠 Key Learnings

This project demonstrates:

* Building interactive dashboards with Streamlit
* Writing optimized SQL queries for analytics
* Connecting Python with PostgreSQL using SQLAlchemy
* Structuring a modular data analytics project
* Handling real-world data issues in BI systems

---

## 📌 Use Case

This dashboard simulates a **banking analytics system** where decision-makers can:

* Monitor financial performance in real time
* Analyze customer credit risk
* Understand revenue trends
* Support strategic business decisions

---

## 🚀 Future Improvements

* Authentication system (login / roles)
* Advanced visualizations (Plotly)
* Machine Learning for credit scoring
* Deployment on Streamlit Cloud
* Performance optimization with caching

---

## 👨‍💻 Author

Data Analytics / Data Engineering Project
OUIAM ELKHALFI

---



