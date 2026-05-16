# E-Commerce Sales & AI-Driven Customer Analytics Dashboard

## 📊 Project Overview

This is a **comprehensive end-to-end Power BI dashboard** designed to analyze e-commerce sales performance, customer behavior, and profitability metrics. The project combines **advanced data analysis** with **AI/ML insights** to provide actionable business intelligence for stakeholders.

**Key Focus Areas:**
- Sales performance tracking and trend analysis
- Customer lifetime value (CLV) and cohort retention analysis
- Profitability and profit margin optimization
- Year-over-Year (YoY) growth metrics
- Predictive customer insights

---

## 🎯 Features

### **Dashboard Components**

#### **Page 1: Executive Overview**
- **KPI Cards**: Total Revenue, Average Order Value, YoY Growth %, Return Rate
- **Sales Trend Analysis**: Line chart showing monthly revenue progression
- **Category Breakdown**: Pie chart revealing product category performance
- **Running Total**: Cumulative revenue trend (Area chart)
- **Customer Satisfaction**: Gauge chart displaying satisfaction metrics

**Slicers:** Date Range, Region, Product Category, Customer Segment, Payment Method

#### **Page 2: Customer & Cohort Analysis**
- **Customer Metrics**: Total customers, repeat customer rate, average CLV
- **CLV Distribution**: Histogram showing customer lifetime value spread
- **Retention Analysis**: Stacked bar chart comparing repeat vs. new customers
- **Top Customers Table**: Sortable table of top 10 customers by revenue

#### **Page 3: Profitability & AI Insights**
- **Profit Metrics**: Total profit, profit per order, dynamic margin status
- **Category Profitability**: Column chart breaking down profit by product category
- **Margin Trends**: Line chart with average margin threshold
- **Discount Impact**: Scatter plot analyzing discount vs. final amount correlation

---

## 🛠 Tech Stack

| Technology | Purpose |
|-----------|----------|
| **Python 3.x** | Data generation and preprocessing |
| **Pandas** | Data manipulation and transformation |
| **Faker** | Synthetic customer and order data generation |
| **Power BI Desktop** | Dashboard creation and visualization |
| **DAX** | Advanced calculations and measures |
| **CSV** | Data storage format |

---

## 📁 Project Structure

```
powerbi-ecommerce-analytics/
├── README.md                              # Project documentation
├── generate_ecommerce_data.py            # Data generation script
├── ecommerce_sales_data.csv              # Generated dataset (5,000+ records)
├── DAX_Measures.txt                      # Complex DAX formulas
├── Dashboard_Layout_Guide.md             # Visual layout specifications
└── PowerBI_Report.pbix                   # Main Power BI file
```

---

## 🚀 Getting Started

### **Prerequisites**
- Python 3.8+
- Power BI Desktop (latest version)
- Libraries: `pandas`, `numpy`, `faker`

### **Installation**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shilpi11325/powerbi-ecommerce-analytics.git
   cd powerbi-ecommerce-analytics
   ```

2. **Install Python dependencies:**
   ```bash
   pip install pandas numpy faker
   ```

3. **Generate the dataset:**
   ```bash
   python generate_ecommerce_data.py
   ```
   This creates `ecommerce_sales_data.csv` with 5,000+ records.

4. **Open Power BI Dashboard:**
   - Launch Power BI Desktop
   - Open `PowerBI_Report.pbix`
   - Load the `ecommerce_sales_data.csv` file
   - Apply the DAX measures from `DAX_Measures.txt`
   - Navigate through the 3-page dashboard

---

## 📊 Dataset Details

### **Data Dimensions**
- **Records**: 5,000+ transactions
- **Time Period**: Jan 2024 - May 2026
- **Customers**: 1,000 unique customers

### **Key Columns**
| Column | Description |
|--------|-------------|
| Order_ID | Unique order identifier |
| Customer_ID | Unique customer identifier |
| Order_Date | Transaction timestamp |
| Product_Category | Electronics, Clothing, Home & Garden, Sports, Books |
| Product_Name | Individual product name |
| Quantity | Number of items ordered |
| Unit_Price | Price per unit ($) |
| Discount_Percent | Applied discount (0-20%) |
| Final_Amount | Net revenue after discount |
| Customer_Segment | Premium, Standard, Budget |
| Region | North, South, East, West |
| Payment_Method | Credit Card, Debit Card, PayPal, UPI |
| Delivery_Days | Days to deliver |
| Customer_Satisfaction | Rating 1-5 |
| Return_Status | No Return, Returned, Partial Return |

---

## 📈 Advanced DAX Measures

### **5 Complex Formulas Used**

1. **Year-over-Year (YoY) Growth %**
   - Compares current year sales against previous year
   - Shows percentage change in revenue

2. **Running Total of Sales**
   - Cumulative monthly revenue within the year
   - Tracks progression toward annual targets

3. **Customer Lifetime Value (CLV)**
   - Total revenue generated per customer
   - Used for customer segmentation

4. **Repeat Customer Rate %**
   - Percentage of customers who purchased more than once
   - Measures customer retention and loyalty

5. **Dynamic Profit Margin Analysis**
   - Conditional logic returning "Excellent", "Good", "Average", or "Poor"
   - Based on profit margin thresholds (>25%, >15%, >5%)

---

## 🎓 Learning Outcomes

This project demonstrates proficiency in:
- ✅ End-to-end data pipeline (generation → analysis → visualization)
- ✅ Advanced DAX calculations and conditional logic
- ✅ Multi-page dashboard design with interactivity
- ✅ Cohort analysis and customer segmentation
- ✅ Profitability and financial metrics analysis
- ✅ Business storytelling through data visualization
- ✅ Python data engineering (Pandas, Faker)

---

## 💡 Use Cases

This dashboard can be used for:
- **Executive Reports**: High-level KPIs for stakeholders
- **Sales Teams**: Tracking performance by region and category
- **Marketing Teams**: Customer segmentation and retention analysis
- **Finance Teams**: Profitability analysis and discount impact
- **Product Teams**: Category performance and customer feedback

---

## 🔮 Future Enhancements (AI/ML Integration)

Potential additions to showcase AI/ML skills:
- **Predictive Analytics**: Forecast sales using Prophet/ARIMA
- **Churn Prediction**: ML model to identify at-risk customers
- **Recommendation Engine**: Collaborative filtering for product recommendations
- **Anomaly Detection**: Identify unusual purchase patterns
- **Sentiment Analysis**: NLP on customer reviews/feedback

---

## 📞 Support & Contact

For questions or suggestions:
- **Author**: Shilpi11325
- **GitHub**: [powerbi-ecommerce-analytics](https://github.com/Shilpi11325/powerbi-ecommerce-analytics)

---

## 📝 License

This project is open source and available under the MIT License.

---

## ⭐ Acknowledgments

- Dataset generated using **Faker** for realistic synthetic data
- Dashboard design inspired by industry best practices
- Built for portfolio demonstration and learning purposes

---

**Last Updated**: May 16, 2026