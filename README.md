# 🌍 GlobalLens
**A Clearer View of Global Progress and Stability**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

## 📖 Project Overview
**GlobalLens** is a data-driven system designed to provide actionable insights into global development and economic stability. By leveraging 60 years of socio-economic data from the World Bank across 150+ countries, GlobalLens bridges the gap between raw data and actionable insights. 

It empowers policymakers, investors, and researchers to make informed decisions for a sustainable and stable global future by measuring development levels, detecting macroeconomic risks, and forecasting future trends.

## ✨ Key Features
- **Data Ingestion & ETL:** Automated fetching and processing of global socio-economic data via the World Bank Open Data API.
- **Data Cleaning & Preprocessing:** Robust handling of missing data, outliers, and historical inconsistencies.
- **Feature Engineering:** Creation of meaningful indicators, including a custom Composite Risk Index.
- **Development Intelligence:** Clustering countries into distinct development groups using unsupervised learning.
- **Risk Intelligence:** Scoring and categorizing countries based on their economic vulnerabilities and detecting anomalies.
- **Forecasting:** Predicting future macroeconomic trends using advanced time-series modeling.
- **Interactive Visualization:** A deployed dashboard providing visual reports and scenario planning tools.

## 🚀 Technical Highlights & Impact
- **Architected an ETL pipeline** ingesting 60 years of World Bank data for 150+ countries to drive global analysis.
- **Engineered a Composite Risk Index** using **PCA & K-Means** to classify vulnerability clusters and detect anomalies.
- **Developed ARIMA time-series models** to forecast 5-year GDP trajectories with 96% confidence intervals.
- **Deployed a Streamlit dashboard** visualizing macroeconomic signals to support strategic policy scenario planning.

## 🛠️ Tech Stack
- **Language:** Python
- **Machine Learning & Stats:** Scikit-Learn (PCA, K-Means), Statsmodels (ARIMA)
- **Data Processing:** Pandas, NumPy
- **Visualization & Deployment:** Streamlit, Matplotlib/Seaborn
- **Data Source:** [World Bank Open Data API](https://data.worldbank.org/)

## 📊 Dashboard Preview
![Dashboard Screenshot](https://via.placeholder.com/800x400.png?text=GlobalLens+Dashboard+Screenshot)

## 💻 Getting Started

### Prerequisites
Make sure you have Python 3.8+ installed.

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/Kartavyasoni/GlobalLens.git](https://github.com/Kartavyasoni/GlobalLens.git)
   cd GlobalLens

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

### Usage
Run the Streamlit app locally to view the dashboard:
```bash
streamlit run app.py
```

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📄 License
This project is licensed under the MIT License.
