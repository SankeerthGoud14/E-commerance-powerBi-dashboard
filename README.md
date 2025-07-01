 E-commerce Return Rate Reduction Analysis

 📌 Objective
This project analyzes and predicts product returns in an e-commerce setting using data-driven techniques.
It aims to uncover patterns in returns across product categories, suppliers, regions, and marketing channels.

 📊 Tools Used
- Python (pandas, scikit-learn, seaborn, matplotlib)
- Power BI (for dashboard creation)
- GitHub (for version control and project sharing)
- Visual Studio Code (code editor)

 Project Workflow

1. *Data Generation*: Synthetic dataset simulating e-commerce orders and returns.
2. *EDA (Exploratory Data Analysis)*: Identify trends by category, supplier, marketing channel.
3. *Modeling*: Logistic Regression to predict product return probability.
4. *Risk Tagging*: Products with a return probability > 0.5 marked as high-risk.
5. *Visualization*: Power BI dashboard with filters for category, supplier, etc.
6. *Reporting*: Project PDF summarizing approach and findings.

 📁 Project Structure


├── data/
│   ├── orders_returns.csv
│   └── high_risk_products.csv
├── dashboard/
│   └── return_rate_dashboard.pbix
├── src/
│   ├── eda_analysis.py
│   └── logistic_model.py
├── results/
│   └── high_risk_products.csv
├── Ecommerce_Return_Analysis_Report.pdf
├── requirements.txt
└── README.md


📈 Output Dashboard

Power BI dashboard shows:
- Return Rate by Category, Supplier, Region, Channel
- High-risk products table
- KPIs: Total Orders, Total Returns, Return Rate (%)

 📂 Deliverables
- Python scripts for analysis and prediction
- Cleaned dataset
- Predictive model output
- Power BI .pbix dashboard
- 2-page PDF report

 👤 Author
Sankeerth Goud BTECH-CSE



 ▶ How to Run This Project

🔧 Setup Instructions

1. Clone the Repository
   bash
   https://github.com/SankeerthGoud14/E-commerance-powerBi-dashboard

   

3. Install Dependencies
   Create a virtual environment (optional but recommended) and install required packages:
   bash
   pip install -r requirements.txt
   

4. Run EDA Script
   This script performs basic data visualization and statistics:
   bash
   python src/eda_analysis.py
   

5. Run Logistic Regression Model 
   This generates the confusion matrix, model report, and saves high-risk products:
   bash
   python src/logistic_model.py
   

6. Open Power BI Dashboard
   Use Power BI Desktop to open dashboard/return_rate_dashboard.pbix.

7. Explore Outputs
   Review:
   - results/high_risk_products.csv
   - Dashboard visualizations
   - Classification metrics in console output

