import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATA

df = pd.read_excel("FUTURE_DS_03.xlsx")

print("DATA LOADED SUCCESSFULLY")
print(df.head())
print(df.columns)

# CLEAN DATA

df = df.dropna()

# KPI ANALYSIS

total_impressions = df["Impressions"].sum()
total_clicks = df["Clicks"].sum()
total_leads = df["Leads"].sum()
total_customers = df["Customers"].sum()
total_cost = df["Cost"].sum()

print("\n===== KPI REPORT =====")
print("Total Impressions:", total_impressions)
print("Total Clicks:", total_clicks)
print("Total Leads:", total_leads)
print("Total Customers:", total_customers)
print("Total Cost:", total_cost)

# CONVERSION RATES

click_rate = (total_clicks / total_impressions) * 100
lead_rate = (total_leads / total_clicks) * 100
customer_rate = (total_customers / total_leads) * 100

print("\n===== CONVERSION RATES =====")
print("Impression → Click:", round(click_rate, 2), "%")
print("Click → Lead:", round(lead_rate, 2), "%")
print("Lead → Customer:", round(customer_rate, 2), "%")

# FUNNEL ANALYSIS

funnel_data = pd.Series({
    "Impressions": total_impressions,
    "Clicks": total_clicks,
    "Leads": total_leads,
    "Customers": total_customers
})

print("\n===== FUNNEL ANALYSIS =====")
print(funnel_data)

funnel_data.plot(kind="bar")
plt.title("Marketing Funnel")
plt.xlabel("Stage")
plt.ylabel("Count")
plt.show()


# CHANNEL PERFORMANCE

channel_customers = df.groupby("Channel")["Customers"].sum().sort_values(ascending=False)

print("\n===== CHANNEL PERFORMANCE =====")
print(channel_customers)

channel_customers.plot(kind="bar")
plt.title("Customers by Channel")
plt.xlabel("Channel")
plt.ylabel("Customers")
plt.show()

# LEADS BY CHANNEL

channel_leads = df.groupby("Channel")["Leads"].sum().sort_values(ascending=False)

print("\n===== LEADS BY CHANNEL =====")
print(channel_leads)

channel_leads.plot(kind="bar")
plt.title("Leads by Channel")
plt.xlabel("Channel")
plt.ylabel("Leads")
plt.show()

# COST BY CHANNEL

channel_cost = df.groupby("Channel")["Cost"].sum().sort_values(ascending=False)

print("\n===== COST BY CHANNEL =====")
print(channel_cost)

channel_cost.plot(kind="bar")
plt.title("Marketing Cost by Channel")
plt.xlabel("Channel")
plt.ylabel("Cost")
plt.show()


# DROP-OFF ANALYSIS

dropoff = pd.Series({
    "Lost after Impressions": total_impressions - total_clicks,
    "Lost after Clicks": total_clicks - total_leads,
    "Lost after Leads": total_leads - total_customers
})

print("\n===== DROP-OFF ANALYSIS =====")
print(dropoff)

dropoff.plot(kind="bar")
plt.title("Funnel Drop-Off Analysis")
plt.xlabel("Stage")
plt.ylabel("Lost Users")
plt.show()

print("\nANALYSIS COMPLETED SUCCESSFULLY")
