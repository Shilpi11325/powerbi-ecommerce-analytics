# Power BI Dashboard Layout Guide

## 📐 Dashboard Design Specifications

---

## **PAGE 1: EXECUTIVE OVERVIEW**

### Layout Structure
```
┌─────────────────────────────────────────────────────────────┐
│                E-COMMERCE ANALYTICS DASHBOARD                │
├─────────────────────────────────────────────────────────────┤
│  [Slicer: Date Range]  [Slicer: Region]  [Slicer: Category] │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │Total     │  │Avg Order │  │YoY       │  │Return    │      │
│  │Revenue   │  │Value     │  │Growth %  │  │Rate %    │      │
│  │$2.5M     │  │$245      │  │+22%      │  │12%       │      │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘      │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────┐  ┌──────────────────────────┐   │
│  │ Sales Trend (Line Chart) │  │ Category Breakdown (Pie) │   │
│  │ Monthly Revenue Growth   │  │ Product Performance     │   │
│  └──────────────────────────┘  └──────────────────────────┘   │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────┐  ┌──────────────────────────┐   │
│  │ Running Total (Area)     │  │ Customer Satisfaction   │   │
│  │ Cumulative Revenue YTD   │  │ Gauge Chart (1-5)       │   │
│  └──────────────────────────┘  └──────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Slicers Configuration
- **Date Range**: From/To date picker
- **Region**: Multi-select (North, South, East, West)
- **Product Category**: Multi-select dropdown
- **Customer Segment**: Multi-select (Premium, Standard, Budget)
- **Payment Method**: Multi-select (Credit Card, Debit Card, PayPal, UPI)

### KPI Cards (Top Row)
1. **Total Revenue**
   - Measure: SUM(Final_Amount)
   - Format: Currency ($)
   - Background Color: #2E75B6 (Blue)

2. **Average Order Value**
   - Measure: AVERAGE(Final_Amount)
   - Format: Currency ($)
   - Background Color: #70AD47 (Green)

3. **YoY Growth %**
   - Measure: YoY_Growth %
   - Format: Percentage
   - Background Color: #FFC000 (Gold)

4. **Return Rate %**
   - Measure: DIVIDE(COUNTA(Return_Status="Returned"), COUNTA(Return_Status)) * 100
   - Format: Percentage
   - Background Color: #C55A11 (Orange)

### Charts (Middle & Bottom Rows)

#### Left Column - Sales Trend (Line Chart)
- **X-Axis**: Order_Date (Month)
- **Y-Axis**: SUM(Final_Amount)
- **Title**: "Monthly Sales Trend"
- **Color**: Gradient blue
- **Show Legend**: Yes

#### Right Column - Category Breakdown (Pie Chart)
- **Legend**: Product_Category
- **Values**: SUM(Final_Amount)
- **Title**: "Sales by Category"
- **Show Percentages**: Yes

#### Left Bottom - Running Total (Area Chart)
- **X-Axis**: Order_Date (Monthly)
- **Y-Axis**: Running_Total_Sales
- **Title**: "Cumulative Revenue YTD"
- **Fill Color**: #70AD47 (Green, 50% opacity)

#### Right Bottom - Customer Satisfaction (Gauge Chart)
- **Value**: AVERAGE(Customer_Satisfaction)
- **Min**: 1, Max: 5
- **Title**: "Average Customer Satisfaction"
- **Target Value**: 4.0
- **Color Stops**: Red (1-2), Yellow (2-3), Green (3-5)

---

## **PAGE 2: CUSTOMER & COHORT ANALYSIS**

### Layout Structure
```
┌─────────────────────────────────────────────────────────────┐
│                    CUSTOMER ANALYTICS                         │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                    │
│  │Total     │  │Repeat    │  │CLV       │                    │
│  │Customers │  │Rate %    │  │Average   │                    │
│  │1,500     │  │42%       │  │$850      │                    │
│  └──────────┘  └──────────┘  └──────────┘                    │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────┐  ┌──────────────────────────┐   │
│  │ CLV Distribution         │  │ Repeat vs New Customers │   │
│  │ (Histogram)              │  │ (Stacked Bar)           │   │
│  └──────────────────────────┘  └──────────────────────────┘   │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────┐    │
│  │ Top 10 Customers by Revenue (Table)                  │    │
│  │ Rank | Name | Total Spent | Order Count | Segment   │    │
│  └──────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

### KPI Cards (Top Row)
1. **Total Customers**
   - Measure: DISTINCTCOUNT(Customer_ID)
   - Background: #2E75B6

2. **Repeat Customer Rate %**
   - Measure: Repeat_Customer_Rate %
   - Background: #70AD47

3. **Average CLV**
   - Measure: AVERAGE(Customer_Lifetime_Value)
   - Format: Currency ($)
   - Background: #FFC000

### Charts

#### Left - CLV Distribution (Histogram)
- **X-Axis**: Customer_Lifetime_Value (Bins of $100)
- **Y-Axis**: Count of Customers
- **Title**: "Customer Lifetime Value Distribution"
- **Bar Color**: #2E75B6

#### Right - Repeat vs New Customers (Stacked Bar)
- **X-Axis**: Order_Month
- **Y-Axis**: DISTINCTCOUNT(Customer_ID)
- **Legend**: "Repeat Customer" vs "New Customer"
- **Title**: "Repeat vs New Customers by Month"
- **Colors**: Green (Repeat), Blue (New)

#### Bottom - Top 10 Customers Table
- **Columns**:
  - Rank (Row Number)
  - Customer_Name
  - Total Spent (SUM of Final_Amount per customer)
  - Order Count (COUNTA of Orders)
  - Customer_Segment
- **Sort By**: Total Spent (Descending)
- **Conditional Formatting**: Color scale on Total Spent

---

## **PAGE 3: PROFITABILITY & AI INSIGHTS**

### Layout Structure
```
┌─────────────────────────────────────────────────────────────┐
│                PROFITABILITY & INSIGHTS                       │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                    │
│  │Total     │  │Profit    │  │Margin    │                    │
│  │Profit    │  │per Order │  │Status    │                    │
│  │$625K     │  │$61       │  │Excellent │                    │
│  └──────────┘  └──────────┘  └──────────┘                    │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────┐  ┌──────────────────────────┐   │
│  │ Profit by Category       │  │ Profit Margin Trend     │   │
│  │ (Column Chart)           │  │ (Line Chart with Avg)   │   │
│  └──────────────────────────┘  └──────────────────────────┘   │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────┐    │
│  │ Discount Impact Analysis (Scatter Plot)              │    │
│  │ X: Discount% Y: Final Amount, Size: Quantity        │    │
│  └──────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

### KPI Cards (Top Row)
1. **Total Profit**
   - Measure: SUM(Profit_Margin)
   - Format: Currency ($)
   - Background: #2E75B6

2. **Profit per Order**
   - Measure: AVERAGE(Profit_Margin)
   - Format: Currency ($)
   - Background: #70AD47

3. **Margin Status**
   - Measure: Profit_Margin_Analysis
   - Format: Text
   - Background: Conditional (Green for Excellent, Yellow for Good, etc.)

### Charts

#### Left - Profit by Category (Column Chart)
- **X-Axis**: Product_Category
- **Y-Axis**: SUM(Profit_Margin)
- **Title**: "Profit Distribution by Category"
- **Bar Color**: Gradient from Blue to Green
- **Data Labels**: Show values on top

#### Right - Profit Margin Trend (Line Chart)
- **X-Axis**: Order_Date (Monthly)
- **Y-Axis**: SUM(Profit_Margin)
- **Reference Line**: Average profit margin (dotted line)
- **Title**: "Profit Margin Trend Over Time"
- **Line Color**: #2E75B6

#### Bottom - Discount Impact Analysis (Scatter Plot)
- **X-Axis**: Discount_Percent
- **Y-Axis**: Final_Amount
- **Size**: Quantity
- **Legend**: Product_Category
- **Title**: "Discount vs Revenue Impact"
- **Trend Line**: Yes (show correlation)

---

## 🎨 Design Guidelines

### Color Scheme
- **Primary Blue**: #2E75B6
- **Secondary Green**: #70AD47
- **Accent Gold**: #FFC000
- **Highlight Orange**: #C55A11
- **Background**: #F5F5F5
- **Text**: #333333

### Typography
- **Title Font**: Segoe UI Bold, 20pt
- **Label Font**: Segoe UI Regular, 11pt
- **KPI Font**: Segoe UI Semibold, 28pt

### Interactivity
- ✅ All slicers affect all visuals on the page
- ✅ Cross-filtering enabled between charts
- ✅ Drill-down capability on category charts
- ✅ Tooltips on hover for detailed information

### Mobile Responsive
- Dashboard should be viewable on tablets (1024x768)
- Slicers collapse into dropdown on mobile
- Font sizes scale appropriately

---

## 📋 Implementation Checklist

- [ ] Import data into Power BI
- [ ] Create date table for time intelligence
- [ ] Add all 5 DAX measures
- [ ] Create Page 1 visuals and slicers
- [ ] Create Page 2 customer analysis visuals
- [ ] Create Page 3 profitability visuals
- [ ] Configure cross-filtering between pages
- [ ] Apply color scheme consistently
- [ ] Add bookmarks for navigation
- [ ] Test dashboard on desktop and tablet
- [ ] Add descriptive tooltips to all visuals
- [ ] Export as .pbix file
