import pandas as pd
df = pd.read_csv(r"C:\Users\mhr\Desktop\Superstore-Sales-Analysis\train.csv")
print(df.head())
print(df.columns)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)
print(df.dtypes)
print(df[df["Postal Code"].isnull()][["City", "State", "Postal Code"]])
df.loc[df["Postal Code"].isnull(), "Postal Code"] = 5401
print(df["Postal Code"].isnull().sum())
print(df.duplicated().sum())
df.columns = df.columns.str.strip()
print(df.columns)
print(df.select_dtypes(include="object").columns)
print(df.describe())
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print(df["Category"].value_counts())
print(df["Sub-Category"].value_counts())
print(df["Region"].value_counts())
print(df.columns.tolist())
print("Total Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())
print("Maximum Sale:", df["Sales"].max())
print("Minimum Sale:", df["Sales"].min())
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print(category_sales)
subcategory_sales = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False)
print(subcategory_sales)
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print(region_sales)
state_sales = df.groupby("State")["Sales"].sum().sort_values(ascending=False)
print(state_sales.head(10))
product_sales = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False)
print(product_sales.head(10))
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print(region_sales)
segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
print(segment_sales)
ship_sales = df.groupby("Ship Mode")["Sales"].sum().sort_values(ascending=False)
print(ship_sales)
state_sales = df.groupby("State")["Sales"].sum().sort_values(ascending=False)
print(state_sales.head(10))
customer_sales = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False)
print(customer_sales.head(10))
product_sales = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False)
print(product_sales.head(10))
year_sales = df.groupby(df["Order Date"].dt.year)["Sales"].sum()
print(year_sales)
monthly_sales = df.groupby(df["Order Date"].dt.month)["Sales"].sum()
print(monthly_sales)
monthly_trend = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
)
print(monthly_trend)
yearly_sales = df.groupby(df["Order Date"].dt.year)["Sales"].sum()
yearly_growth = yearly_sales.pct_change() * 100
print(yearly_sales)
print(yearly_growth)
avg_category_sales = (
    df.groupby("Category")["Sales"]
    .mean()
    .sort_values(ascending=False)
)
print(avg_category_sales)
customer_orders = df.groupby("Customer Name")["Order ID"].nunique()
print(customer_orders.sort_values(ascending=False).head(10))
df["Year"] = df["Order Date"].dt.year
yearly_sales = df.groupby("Year")["Sales"].sum()
print("\nYear-wise Sales:")
print(yearly_sales)
df["Month"] = df["Order Date"].dt.month
monthly_sales = df.groupby("Month")["Sales"].sum()
print("\nMonth-wise Sales:")
print(monthly_sales)
df["Year-Month"] = df["Order Date"].dt.to_period("M")
monthly_trend = df.groupby("Year-Month")["Sales"].sum()
print("\nYear-Month Sales Trend:")
print(monthly_trend)
yearly_sales = df.groupby("Year")["Sales"].sum()
yoy_growth = yearly_sales.pct_change() * 100
print("\nYear-over-Year Sales Growth:")
print(yoy_growth.round(2))
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print("\nCategory Performance:")
print(category_sales)
subcategory_sales = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)
print("\nSub-Category Performance:")
print(subcategory_sales)
region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)
print("\nRegion Performance:")
print(region_sales)
segment_sales = (
    df.groupby("Segment")["Sales"]
    .sum()
    .sort_values(ascending=False)
)
print("\nSegment Performance:")
print(segment_sales)
ship_mode_sales = (
    df.groupby("Ship Mode")["Sales"]
    .sum()
    .sort_values(ascending=False)
)
print("\nShip Mode Performance:")
print(ship_mode_sales)
top_states = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print("\nTop 10 States by Sales:")
print(top_states)
top_customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print("\nTop 10 Customers by Sales:")
print(top_customers)
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print("\nTop 10 Products by Sales:")
print(top_products)
best_month = monthly_trend.idxmax()
best_month_sales = monthly_trend.max()
worst_month = monthly_trend.idxmin()
worst_month_sales = monthly_trend.min()
print("\nBest Month:")
print(best_month, best_month_sales)
print("\nWorst Month:")
print(worst_month, worst_month_sales)

city_sales = df.groupby("City")["Sales"].sum().sort_values(ascending=False)
print("\nTop 10 Cities by Sales:")
print(city_sales.head(10))
state_category = df.groupby(["State", "Category"])["Sales"].sum().sort_values(ascending=False)
print("\nTop State-Category Combinations:")
print(state_category.head(15))
segment_category = df.groupby(["Segment", "Category"])["Sales"].sum()
print("\nSegment vs Category Sales:")
print(segment_category)
region_category = df.groupby(["Region", "Category"])["Sales"].sum()
print("\nRegion vs Category Sales:")
print(region_category)
avg_category = df.groupby("Category")["Sales"].mean().sort_values(ascending=False)
print("\nAverage Sales by Category:")
print(avg_category)
avg_region = df.groupby("Region")["Sales"].mean().sort_values(ascending=False)
print("\nAverage Sales by Region:")
print(avg_region)
avg_segment = df.groupby("Segment")["Sales"].mean().sort_values(ascending=False)
print("\nAverage Sales by Segment:")
print(avg_segment)
total_orders = df["Order ID"].nunique()
print("\nTotal Unique Orders:", total_orders)
total_customers = df["Customer ID"].nunique()
print("Total Unique Customers:", total_customers)
total_products = df["Product ID"].nunique()
print("Total Unique Products:", total_products)
order_sales = df.groupby("Order ID")["Sales"].sum()
average_order_value = order_sales.mean()
print("\nAverage Order Value:", round(average_order_value, 2))
top_orders = order_sales.sort_values(ascending=False).head(10)
print("\nTop 10 Orders by Sales:")
print(top_orders)
year_category = df.groupby([df["Order Date"].dt.year, "Category"])["Sales"].sum()
print("\nYear vs Category Sales:")
print(year_category)
year_region = df.groupby([df["Order Date"].dt.year, "Region"])["Sales"].sum()
print("\nYear vs Region Sales:")
print(year_region)
year_segment = df.groupby([df["Order Date"].dt.year, "Segment"])["Sales"].sum()
print("\nYear vs Segment Sales:")
print(year_segment)
product_orders = df.groupby("Product Name")["Order ID"].nunique()
top_products_orders = product_orders.sort_values(ascending=False).head(10)
print("\nTop 10 Products by Number of Orders:")
print(top_products_orders)
customer_analysis = df.groupby("Customer Name").agg(
    Total_Sales=("Sales", "sum"),
    Total_Orders=("Order ID", "nunique")
).sort_values("Total_Sales", ascending=False)
print("\nCustomer Analysis:")
print(customer_analysis.head(10))
category_sales = df.groupby("Category")["Sales"].sum()
category_percentage = (category_sales / df["Sales"].sum() * 100).sort_values(ascending=False)
print("\nCategory Sales Contribution %:")
print(category_percentage.round(2))
region_sales = df.groupby("Region")["Sales"].sum()
region_percentage = (region_sales / df["Sales"].sum() * 100).sort_values(ascending=False)
print("\nRegion Sales Contribution %:")
print(region_percentage.round(2))
df["Quarter"] = df["Order Date"].dt.quarter
quarter_sales = df.groupby("Quarter")["Sales"].sum()
print("\nQuarterly Sales:")
print(quarter_sales)
print("\n" + "=" * 50)
print("FINAL BUSINESS INSIGHTS")
print("=" * 50)
best_year = df.groupby(df["Order Date"].dt.year)["Sales"].sum().idxmax()
best_category = df.groupby("Category")["Sales"].sum().idxmax()
best_region = df.groupby("Region")["Sales"].sum().idxmax()
best_segment = df.groupby("Segment")["Sales"].sum().idxmax()
best_subcategory = df.groupby("Sub-Category")["Sales"].sum().idxmax()
best_state = df.groupby("State")["Sales"].sum().idxmax()
best_product = df.groupby("Product Name")["Sales"].sum().idxmax()
print("Best Year:", best_year)
print("Best Category:", best_category)
print("Best Region:", best_region)
print("Best Segment:", best_segment)
print("Best Sub-Category:", best_subcategory)
print("Best State:", best_state)
print("Best Product:", best_product)
print("\nProject Analysis Completed Successfully!")

import matplotlib.pyplot as plt
year_sales = df.groupby(df["Order Date"].dt.year)["Sales"].sum()
plt.figure(figsize=(8, 5))
plt.plot(year_sales.index, year_sales.values, marker="o")
plt.title("Year-wise Sales Trend")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.show()
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
plt.bar(category_sales.index, category_sales.values)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
plt.bar(region_sales.index, region_sales.values)
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
plt.bar(segment_sales.index, segment_sales.values)
plt.title("Sales by Customer Segment")
plt.xlabel("Segment")
plt.ylabel("Total Sales")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()
top_states = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_states.index[::-1], top_states.values[::-1])
plt.title("Top 10 States by Sales")
plt.xlabel("Total Sales")
plt.ylabel("State")
plt.tight_layout()
plt.show()
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_products.index[::-1], top_products.values[::-1])
plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.tight_layout()
plt.show()
monthly_sales = df.groupby(df["Order Date"].dt.month)["Sales"].sum()
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(range(1, 13))
plt.grid(True)
plt.tight_layout()
plt.show()
quarter_sales = df.groupby(df["Order Date"].dt.quarter)["Sales"].sum()
plt.figure(figsize=(8, 5))
plt.bar(
    ["Q1", "Q2", "Q3", "Q4"],
    quarter_sales.values
)
plt.title("Quarterly Sales")
plt.xlabel("Quarter")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
print("\nCOMPLETED - All Visualizations Created Successfully!")

import os
import matplotlib.pyplot as plt
os.makedirs("charts", exist_ok=True)
year_sales = df.groupby(df["Order Date"].dt.year)["Sales"].sum()
plt.figure(figsize=(8, 5))
plt.plot(year_sales.index, year_sales.values, marker="o")
plt.title("Year-wise Sales Trend")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/year_wise_sales.png", dpi=300)
plt.close()
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
plt.bar(category_sales.index, category_sales.values)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("charts/category_sales.png", dpi=300)
plt.close()
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
plt.bar(region_sales.index, region_sales.values)
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("charts/region_sales.png", dpi=300)
plt.close()
segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
plt.bar(segment_sales.index, segment_sales.values)
plt.title("Sales by Customer Segment")
plt.xlabel("Segment")
plt.ylabel("Total Sales")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("charts/segment_sales.png", dpi=300)
plt.close()
top_states = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_states.index[::-1], top_states.values[::-1])
plt.title("Top 10 States by Sales")
plt.xlabel("Total Sales")
plt.ylabel("State")
plt.tight_layout()
plt.savefig("charts/top_10_states.png", dpi=300)
plt.close()
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_products.index[::-1], top_products.values[::-1])
plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("charts/top_10_products.png", dpi=300)
plt.close()
monthly_sales = df.groupby(df["Order Date"].dt.month)["Sales"].sum()
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(range(1, 13))
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/monthly_sales.png", dpi=300)
plt.close()
quarter_sales = df.groupby(df["Order Date"].dt.quarter)["Sales"].sum()
plt.figure(figsize=(8, 5))
plt.bar(["Q1", "Q2", "Q3", "Q4"], quarter_sales.values)
plt.title("Quarterly Sales")
plt.xlabel("Quarter")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("charts/quarterly_sales.png", dpi=300)
plt.close()
print("\nCOMPLETED!")
print("All 8 charts have been saved in the 'charts' folder.")

import os
chart_files = os.listdir("charts")
print("\n" + "=" * 50)
print("CREATED CHARTS")
print("=" * 50)
for i, file in enumerate(chart_files, 1):
    print(f"{i}. {file}")
print(f"\nTotal Charts Created: {len(chart_files)}")
print("\n" + "=" * 60)
print("BUSINESS INSIGHTS & RECOMMENDATIONS")
print("=" * 60)
best_year = yearly_sales.idxmax()
best_year_sales = yearly_sales.max()
print(f"\n1. Best Year: {best_year}")
print(f"   Sales: ${best_year_sales:,.2f}")
best_category = category_sales.idxmax()
best_category_sales = category_sales.max()
print(f"\n2. Best Category: {best_category}")
print(f"   Sales: ${best_category_sales:,.2f}")
best_region = region_sales.idxmax()
best_region_sales = region_sales.max()
print(f"\n3. Best Region: {best_region}")
print(f"   Sales: ${best_region_sales:,.2f}")
best_segment = segment_sales.idxmax()
best_segment_sales = segment_sales.max()
print(f"\n4. Best Customer Segment: {best_segment}")
print(f"   Sales: ${best_segment_sales:,.2f}")
best_subcategory = subcategory_sales.idxmax()
best_subcategory_sales = subcategory_sales.max()
print(f"\n5. Best Sub-Category: {best_subcategory}")
print(f"   Sales: ${best_subcategory_sales:,.2f}")
best_state = state_sales.idxmax()
best_state_sales = state_sales.max()
print(f"\n6. Best State: {best_state}")
print(f"   Sales: ${best_state_sales:,.2f}")
best_product = product_sales.idxmax()
best_product_sales = product_sales.max()
print(f"\n7. Best Product: {best_product}")
print(f"   Sales: ${best_product_sales:,.2f}")
best_month = monthly_sales.idxmax()
best_month_sales = monthly_sales.max()
print(f"\n8. Best Month: {best_month}")
print(f"   Sales: ${best_month_sales:,.2f}")
worst_month = monthly_sales.idxmin()
worst_month_sales = monthly_sales.min()
print(f"\n9. Lowest Sales Month: {worst_month}")
print(f"   Sales: ${worst_month_sales:,.2f}")
print("\n" + "-" * 60)
print("BUSINESS RECOMMENDATIONS")
print("-" * 60)
print("""
1. Focus more on Technology products because they generate the
   highest category sales.
2. Continue strengthening the West region because it is the
   highest-performing region.
3. Consumer customers should remain a major target segment.
4. Phones are the strongest sub-category and should receive
   more promotional and inventory attention.
5. California is the strongest state and can be used as a
   benchmark for other markets.
6. Sales are strongest toward the end of the year, especially
   November and December. Businesses can prepare extra inventory
   and marketing campaigns before this period.
7. February has relatively low sales, so special promotions
   and discounts could be considered during this month.
8. The business shows strong overall growth, with 2018 being
   the strongest year in the dataset.
""")
print("\nCOMPLETED SUCCESSFULLY!")

import pandas as pd
results = {
    "Metric": [
        "Total Sales",
        "Average Sale",
        "Maximum Sale",
        "Minimum Sale",
        "Best Year",
        "Best Category",
        "Best Region",
        "Best Segment",
        "Best Sub-Category",
        "Best State",
        "Best Product",
        "Best Month",
        "Lowest Sales Month"
    ],
    "Value": [
        df["Sales"].sum(),
        df["Sales"].mean(),
        df["Sales"].max(),
        df["Sales"].min(),
        yearly_sales.idxmax(),
        category_sales.idxmax(),
        region_sales.idxmax(),
        segment_sales.idxmax(),
        subcategory_sales.idxmax(),
        state_sales.idxmax(),
        product_sales.idxmax(),
        monthly_sales.idxmax(),
        monthly_sales.idxmin()
    ]
}
results_df = pd.DataFrame(results)
results_df.to_csv("business_insights.csv", index=False)
print("\n" + "=" * 60)
print("STEP 35 - RESULTS EXPORTED")
print("=" * 60)
print(results_df)
print("\nBusiness insights saved to: business_insights.csv")
print("\nCOMPLETED SUCCESSFULLY!")
summary = f"""

SUPERSTORE SALES ANALYSIS - PROJECT SUMMARY
-------------------------------------------
PROJECT OVERVIEW
----------------
Dataset: Superstore Sales
Total Records: {len(df):,}
Total Columns: {len(df.columns)}

KEY BUSINESS METRICS
--------------------
Total Sales: ${df["Sales"].sum():,.2f}
Average Sale: ${df["Sales"].mean():,.2f}
Maximum Sale: ${df["Sales"].max():,.2f}
Minimum Sale: ${df["Sales"].min():,.2f}

TOP PERFORMERS
--------------
Best Year: {yearly_sales.idxmax()}
Best Category: {category_sales.idxmax()}
Best Region: {region_sales.idxmax()}
Best Customer Segment: {segment_sales.idxmax()}
Best Sub-Category: {subcategory_sales.idxmax()}
Best State: {state_sales.idxmax()}
Best Product: {product_sales.idxmax()}

SALES TREND
-----------
Highest Sales Month: {monthly_sales.idxmax()}
Lowest Sales Month: {monthly_sales.idxmin()}

YEAR-OVER-YEAR GROWTH
---------------------
2016 Growth: {yearly_sales.pct_change().loc[2016] * 100:.2f}%
2017 Growth: {yearly_sales.pct_change().loc[2017] * 100:.2f}%
2018 Growth: {yearly_sales.pct_change().loc[2018] * 100:.2f}%

KEY BUSINESS INSIGHTS
---------------------
1. Technology is the highest-performing category.
2. West is the strongest-performing region.
3. Consumer is the largest customer segment by sales.
4. Phones is the leading sub-category.
5. California generates the highest state-level sales.
6. Sales increased strongly in 2017 and 2018.
7. November and December are particularly strong sales months.
8. February records comparatively low sales.

RECOMMENDATIONS
---------------
1. Increase marketing focus on Technology products.
2. Maintain strong inventory levels in high-performing categories.
3. Continue targeting the Consumer segment.
4. Strengthen sales strategies in the West region.
5. Prepare additional inventory before the November-December
   high-sales period.
6. Consider promotional campaigns during lower-sales periods.

TOOLS USED
----------
Python
Pandas
Matplotlib
Data Cleaning
Exploratory Data Analysis
Business Analysis
Data Visualization
============================================================
PROJECT ANALYSIS COMPLETED SUCCESSFULLY
============================================================
"""
with open("project_summary.txt", "w", encoding="utf-8") as file:
    file.write(summary)
print("\n" + "=" * 60)
print("PROJECT SUMMARY CREATED")
print("=" * 60)
print("\nSummary saved to: project_summary.txt")
print("\nCOMPLETED SUCCESSFULLY!")
df.to_csv("cleaned_superstore.csv", index=False)
print("Cleaned file saved successfully!")

