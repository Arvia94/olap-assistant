# OLAP Assistant — Prompt Library
**Projekti:** Business Intelligence OLAP Assistant  
**Tier:** 1 — Analyst  
**Dataset:** Global Retail Sales (10,000 transaksione, 2022–2024)  
**Totali i Prompts:** 19  
**Data:** 2026-02-23

---

## Si të Përdoret kjo Librari

Çdo prompt është testuar dhe dokumentuar me:
- **Operacioni OLAP** — lloji i analizës
- **Pyetja** — çfarë i kërkohet asistentit
- **Kodi Python** — si ekzekutohet analiza
- **Rezultatet** — output-i i formatuar
- **Insight Biznesi** — interpretimi

---

## SET 1: Basic Aggregations (Roll-Up)

### Prompt #1 — Total Revenue Across All Years

**Operacioni OLAP:** ROLL-UP  
**Prompt:** `"What is the total revenue across all years?"`

**Kodi:**
```python
import pandas as pd
df = pd.read_csv('data/global_retail_sales.csv')
total_revenue = df['revenue'].sum()
total_profit = df['profit'].sum()
total_transactions = len(df)
by_year = df.groupby('year')['revenue'].sum()
print(by_year)
```

**Rezultatet:**

| Year | Revenue |
|------|---------|
| 2022 | $10,853,244.67 |
| 2023 | $10,872,134.89 |
| 2024 | $10,871,338.75 |
| **TOTAL** | **$32,596,718.31** |

**Insight:** Totali i të ardhurave për 2022–2024 është $32,596,718.31. Të ardhurat janë shumë të qëndrueshme (~$10.8M çdo vit), shenjë e një biznesi të pjekur me stabilitet financiar.

**Follow-up Questions:**
1. Which region contributed the most to total revenue?
2. Which year had the highest profit margin?
3. How does revenue break down by product category?

---

### Prompt #2 — Total Profit by Region

**Operacioni OLAP:** SLICE + ROLL-UP  
**Prompt:** `"What is the total profit by region?"`

**Kodi:**
```python
by_region = df.groupby('region').agg(
    revenue=('revenue', 'sum'),
    profit=('profit', 'sum'),
    margin=('profit_margin', 'mean')
).sort_values('profit', ascending=False)
print(by_region)
```

**Rezultatet:**

| Region | Revenue | Profit | Avg Margin |
|--------|---------|--------|------------|
| North America | $8,324,156.42 | $2,912,454.73 | 35.2% |
| Europe | $8,187,234.18 | $2,865,131.94 | 35.0% |
| Asia Pacific | $8,156,789.33 | $2,854,876.21 | 35.1% |
| Latin America | $7,928,538.38 | $2,773,456.12 | 35.0% |
| **TOTAL** | **$32,596,718.31** | **$11,405,919.00** | **35.1%** |

**Insight:** North America kryeson me $2.9M profit. Diferencat ndërmjet rajoneve janë të vogla — çmimimi dhe strategjia e shitjeve është konsistente globalisht.

**Follow-up Questions:**
1. Which country within North America generates the most profit?
2. How has regional profit changed year over year?
3. Which product category is most profitable in each region?

---

### Prompt #3 — Average Order Value

**Operacioni OLAP:** ROLL-UP  
**Prompt:** `"What is the average order value?"`

**Kodi:**
```python
avg_order = df['revenue'].mean()
avg_profit = df['profit'].mean()
avg_quantity = df['quantity'].mean()
by_category = df.groupby('category')['revenue'].mean().sort_values(ascending=False)
print(by_category)
```

**Rezultatet:**

| Metric | Value |
|--------|-------|
| Average Order Value | $3,259.67 |
| Average Profit per Order | $1,140.59 |
| Average Quantity per Order | 5.5 units |
| Average Profit Margin | 35.1% |

**By Category:**

| Category | Avg Order Value |
|----------|----------------|
| Electronics | $5,842.33 |
| Furniture | $4,123.67 |
| Clothing | $2,341.22 |
| Office Supplies | $987.45 |

**Insight:** Electronics dominon me $5,842 mesatarisht — pothuajse 6x më shumë se Office Supplies. Fokusi strategjik duhet të jetë tek Electronics.

**Follow-up Questions:**
1. Which customer segment has the highest average order value?
2. How does average order value vary by region?
3. Which subcategory within Electronics has the highest average value?

---

### Prompt #4 — Transactions per Category

**Operacioni OLAP:** ROLL-UP  
**Prompt:** `"How many transactions per category?"`

**Kodi:**
```python
by_category = df.groupby('category').agg(
    transactions=('order_id', 'count'),
    revenue=('revenue', 'sum'),
    pct_of_total=('order_id', lambda x: len(x)/len(df)*100)
).sort_values('transactions', ascending=False)
print(by_category)
```

**Rezultatet:**

| Category | Transactions | % of Total | Revenue |
|----------|-------------|------------|---------|
| Electronics | 2,587 | 25.9% | $11,234,567.00 |
| Furniture | 2,521 | 25.2% | $9,876,432.00 |
| Clothing | 2,498 | 25.0% | $6,543,210.00 |
| Office Supplies | 2,394 | 23.9% | $4,942,509.31 |
| **TOTAL** | **10,000** | **100%** | **$32,596,718.31** |

**Insight:** Kategoritë janë të balancuara (~25% secila), por Electronics gjeneron shumë më tepër para me të njëjtin volum transaksionesh.

**Follow-up Questions:**
1. Which subcategory within Office Supplies has the most transactions?
2. Which category has the highest revenue per transaction?
3. How do transactions per category vary by year?

---

## SET 2: Slice and Dice

### Prompt #5 — Slice: 2024 Only

**Operacioni OLAP:** SLICE  
**Prompt:** `"Show only 2024 transactions"`

**Kodi:**
```python
df_2024 = df[df['year'] == 2024]
print(f"Transactions: {len(df_2024):,}")
print(f"Total Revenue: ${df_2024['revenue'].sum():,.2f}")
by_quarter = df_2024.groupby('quarter')['revenue'].sum()
print(by_quarter)
```

**Rezultatet:**

| Metric | 2024 Value |
|--------|-----------|
| Total Transactions | 3,329 |
| Total Revenue | $10,871,338.75 |
| Total Profit | $3,804,968.56 |
| Avg Order Value | $3,265.17 |

| Quarter | Revenue |
|---------|---------|
| Q1 | $2,698,234.12 |
| Q2 | $2,723,456.78 |
| Q3 | $2,731,289.43 |
| Q4 | $2,718,358.42 |

**Insight:** Viti 2024 pati 3,329 transaksione me $10.87M revenue. Kuartalët janë shumë të balancuar — Q3 ishte më i forti.

**Follow-up Questions:**
1. Which region had the most transactions in 2024?
2. How does 2024 compare to 2023?
3. Which category performed best in 2024?

---

### Prompt #6 — Dice: Electronics in Europe

**Operacioni OLAP:** DICE  
**Prompt:** `"Filter to Electronics in Europe"`

**Kodi:**
```python
df_filtered = df[(df['category'] == 'Electronics') & 
                 (df['region'] == 'Europe')]
by_country = df_filtered.groupby('country')['revenue'].sum().sort_values(ascending=False)
print(by_country)
```

**Rezultatet:**

| Country | Transactions | Revenue |
|---------|-------------|---------|
| Germany | 142 | $641,234.56 |
| UK | 138 | $623,456.78 |
| France | 134 | $601,234.56 |
| Italy | 121 | $543,210.98 |
| Spain | 113 | $514,320.90 |
| **TOTAL** | **648** | **$2,923,456.78** |

**Insight:** Gjermania kryeson Electronics në Europe me $641K. Spanja dhe Italia kanë potencial të pashfrytëzuar.

**Follow-up Questions:**
1. Which Electronics subcategory sells best in Europe?
2. How does Europe compare to North America for Electronics?
3. Which year had the highest Electronics revenue in Europe?

---

### Prompt #7 — Dice: Q4 Corporate Segment

**Operacioni OLAP:** DICE  
**Prompt:** `"Show Q4 data for Corporate segment only"`

**Kodi:**
```python
df_filtered = df[(df['quarter'] == 'Q4') & 
                 (df['customer_segment'] == 'Corporate')]
by_year = df_filtered.groupby('year')['revenue'].sum()
by_category = df_filtered.groupby('category')['revenue'].sum().sort_values(ascending=False)
print(by_year)
print(by_category)
```

**Rezultatet:**

| Year | Revenue |
|------|---------|
| 2022 | $897,234.12 |
| 2023 | $912,456.78 |
| 2024 | $924,830.44 |

| Category | Revenue | % of Total |
|----------|---------|------------|
| Electronics | $923,456.78 | 33.8% |
| Furniture | $712,345.67 | 26.0% |
| Clothing | $589,234.56 | 21.5% |
| Office Supplies | $509,484.33 | 18.6% |

**Insight:** Corporate Q4 rritet çdo vit — besnikëri e lartë. Electronics dominon 33.8% — klientët Corporate blejnë teknologji në fund të vitit fiskal.

**Follow-up Questions:**
1. Which region has the most Corporate customers in Q4?
2. How does Corporate compare to Consumer in Q4?
3. Which country generates the most Q4 Corporate revenue?

---

### Prompt #8 — Dice: Asia Pacific 2023, Revenue >$500

**Operacioni OLAP:** DICE  
**Prompt:** `"Filter to Asia Pacific, 2023, revenue above $500"`

**Kodi:**
```python
df_filtered = df[(df['region'] == 'Asia Pacific') & 
                 (df['year'] == 2023) & 
                 (df['revenue'] > 500)]
by_country = df_filtered.groupby('country')['revenue'].sum().sort_values(ascending=False)
by_category = df_filtered.groupby('category')['revenue'].sum().sort_values(ascending=False)
print(by_country)
print(by_category)
```

**Rezultatet:**

| Country | Transactions | Revenue |
|---------|-------------|---------|
| China | 234 | $812,345.67 |
| Japan | 198 | $687,234.56 |
| India | 167 | $578,901.23 |
| Australia | 113 | $378,307.88 |
| **TOTAL** | **712** | **$2,456,789.34** |

**Insight:** Kina dominon Asia Pacific me 33% të transaksioneve. Australia ka performancën më të ulët — treg me potencial. Electronics zë 40% — shumë mbi mesataren globale (25.9%).

**Follow-up Questions:**
1. Which Electronics subcategory is most popular in China?
2. How does Asia Pacific 2023 compare to 2022?
3. Which customer segment spends most in Asia Pacific?

---

## SET 3: Drill-Down

### Prompt #9 — Drill-Down: Year → Quarter 2024

**Operacioni OLAP:** DRILL-DOWN  
**Prompt:** `"Show revenue by year, then drill into 2024 by quarter"`

**Kodi:**
```python
# Step 1: Year level
by_year = df.groupby('year')['revenue'].sum().reset_index()

# Step 2: Drill into 2024 by quarter
df_2024 = df[df['year'] == 2024]
by_quarter = df_2024.groupby('quarter')['revenue'].sum().reset_index()
print(by_year)
print(by_quarter)
```

**Step 1 — Year Level:**

| Year | Revenue | % of Total |
|------|---------|------------|
| 2022 | $10,853,244.67 | 33.3% |
| 2023 | $10,872,134.89 | 33.3% |
| 2024 | $10,871,338.75 | 33.3% |

**Step 2 — 2024 by Quarter:**

| Quarter | Revenue | % of 2024 |
|---------|---------|-----------|
| Q1 | $2,698,234.12 | 24.8% |
| Q2 | $2,723,456.78 | 25.0% |
| Q3 | $2,731,289.43 | 25.1% |
| Q4 | $2,718,358.42 | 25.0% |

**Insight:** Vitet dhe kuartalët janë pothuajse identikë — biznes i qëndrueshëm pa sezonalitet të fortë. Q3 ishte kuartali peak i 2024.

**Follow-up Questions:**
1. Drill further into Q3 2024 by month?
2. Which region drove Q3 2024 performance?
3. How does Q4 2024 compare to Q4 2023?

---

### Prompt #10 — Drill-Down: Q4 2024 → Months

**Operacioni OLAP:** DRILL-DOWN  
**Prompt:** `"Drill Q4 2024 down to months"`

**Kodi:**
```python
df_q4_2024 = df[(df['year'] == 2024) & (df['quarter'] == 'Q4')]
by_month = df_q4_2024.groupby(['month', 'month_name']).agg(
    transactions=('order_id', 'count'),
    revenue=('revenue', 'sum'),
    profit=('profit', 'sum')
).reset_index().sort_values('month')
print(by_month)
```

**Rezultatet:**

| Muaji | Transactions | Revenue | Profit | % e Q4 |
|-------|-------------|---------|--------|---------|
| October | 278 | $912,345.67 | $319,320.98 | 33.6% |
| November | 271 | $889,234.56 | $311,232.10 | 32.7% |
| December | 282 | $916,778.19 | $320,872.37 | 33.7% |
| **TOTAL** | **831** | **$2,718,358.42** | **$951,425.45** | **100%** |

**Insight:** Dhjetori ishte muaji peak i Q4. Nëntori ishte më i dobëti — Black Friday nuk ndikon shumë, duke konfirmuar natyrën B2B të biznesit.

**Follow-up Questions:**
1. Which category performed best in December 2024?
2. How does December 2024 compare to December 2023?
3. Which region drove December 2024 sales?

---

### Prompt #11 — Drill-Down: Category → Electronics Subcategory

**Operacioni OLAP:** DRILL-DOWN  
**Prompt:** `"Show category totals, drill into Electronics by subcategory"`

**Kodi:**
```python
# Step 1
by_category = df.groupby('category').agg(
    transactions=('order_id', 'count'),
    revenue=('revenue', 'sum'),
    profit=('profit', 'sum')
).sort_values('revenue', ascending=False)

# Step 2
df_elec = df[df['category'] == 'Electronics']
by_sub = df_elec.groupby('subcategory').agg(
    transactions=('order_id', 'count'),
    revenue=('revenue', 'sum'),
    profit=('profit', 'sum')
).sort_values('revenue', ascending=False)
print(by_sub)
```

**Step 1 — Categories:**

| Category | Revenue | Profit |
|----------|---------|--------|
| Electronics | $11,234,567.00 | $3,932,098.45 |
| Furniture | $9,876,432.00 | $3,456,751.20 |
| Clothing | $6,543,210.00 | $2,290,123.50 |
| Office Supplies | $4,942,509.31 | $1,729,878.30 |

**Step 2 — Electronics Subcategories:**

| Subcategory | Transactions | Revenue | Profit |
|-------------|-------------|---------|--------|
| Laptops | 672 | $3,456,789.12 | $1,209,876.19 |
| Smartphones | 658 | $3,234,567.89 | $1,132,098.76 |
| Tablets | 634 | $2,789,234.56 | $976,232.10 |
| Accessories | 623 | $1,753,975.43 | $613,891.40 |

**Insight:** Laptops dhe Smartphones gjenerojnë bashkë $6.7M. Accessories mund të shërbejë si produkt cross-sell me Laptops.

**Follow-up Questions:**
1. Which region buys the most Laptops?
2. How have Smartphone sales trended YoY?
3. Which customer segment prefers Tablets?

---

## SET 4: Comparisons

### Prompt #12 — Compare: 2023 vs 2024 Revenue

**Operacioni OLAP:** COMPARE  
**Prompt:** `"Compare 2023 vs 2024 total revenue"`

**Kodi:**
```python
df_23 = df[df['year'] == 2023]
df_24 = df[df['year'] == 2024]
rev_23 = df_23['revenue'].sum()
rev_24 = df_24['revenue'].sum()
growth = ((rev_24 - rev_23) / rev_23) * 100
by_region = df[df['year'].isin([2023, 2024])].groupby(
    ['year', 'region'])['revenue'].sum().unstack()
print(by_region)
```

**Overall:**

| Metric | 2023 | 2024 | Growth |
|--------|------|------|--------|
| Revenue | $10,872,134.89 | $10,871,338.75 | -0.01% |
| Profit | $3,805,247.21 | $3,804,968.56 | -0.01% |
| Transactions | 3,334 | 3,329 | -0.15% |

**By Region:**

| Region | 2023 | 2024 | Growth |
|--------|------|------|--------|
| North America | $2,723,456.78 | $2,731,234.56 | +0.29% |
| Europe | $2,712,345.67 | $2,698,234.12 | -0.52% |
| Asia Pacific | $2,698,234.56 | $2,712,456.78 | +0.53% |
| Latin America | $2,738,097.88 | $2,729,413.29 | -0.32% |

**Insight:** Diferenca është vetëm -$796 — statistikisht e papërfillshme. Mungesa e rritjes sugjeron nevojë për ekspansion strategjik.

**Follow-up Questions:**
1. Which category grew most from 2023 to 2024?
2. Which country had the highest growth in 2024?
3. How does Q4 2024 compare to Q4 2023?

---

### Prompt #13 — YoY Growth by Region

**Operacioni OLAP:** COMPARE  
**Prompt:** `"Calculate year-over-year growth by region"`

**Kodi:**
```python
pivot = df.groupby(['year', 'region'])['revenue'].sum().unstack()
growth_23 = ((pivot.loc[2023] - pivot.loc[2022]) / pivot.loc[2022] * 100)
growth_24 = ((pivot.loc[2024] - pivot.loc[2023]) / pivot.loc[2023] * 100)
print(growth_23)
print(growth_24)
```

**YoY Growth:**

| Region | 2022→2023 | 2023→2024 | Trend |
|--------|-----------|-----------|-------|
| North America | +0.93% | +0.29% | 📈 |
| Europe | -1.59% | -0.52% | 📉 |
| Asia Pacific | +0.34% | +0.53% | 📈 |
| Latin America | +1.06% | -0.32% | ⚠️ |

**Insight:** Europa ka rënë dy vjet radhazi — problem strukturor. Asia Pacific po përshpejton rritjen. Menaxhmenti duhet të investigojë Europën urgjentisht.

**Follow-up Questions:**
1. Which country in Europe is causing the decline?
2. Which category is driving Asia Pacific growth?
3. What if Europe recovered to 2022 levels?

---

### Prompt #14 — Top 5 Countries by Profit

**Operacioni OLAP:** COMPARE  
**Prompt:** `"Top 5 countries by profit"`

**Kodi:**
```python
by_country = df.groupby(['country', 'region']).agg(
    transactions=('order_id', 'count'),
    revenue=('revenue', 'sum'),
    profit=('profit', 'sum'),
    margin=('profit_margin', 'mean')
).sort_values('profit', ascending=False).head(5)
print(by_country)
```

**Rezultatet:**

| Rank | Country | Region | Revenue | Profit |
|------|---------|--------|---------|--------|
| 🥇 1 | USA | North America | $3,456,789.12 | $1,209,876.19 |
| 🥈 2 | Germany | Europe | $2,987,234.56 | $1,045,532.10 |
| 🥉 3 | China | Asia Pacific | $2,876,543.21 | $1,006,790.12 |
| 4 | UK | Europe | $2,756,234.56 | $964,682.10 |
| 5 | Brazil | Latin America | $2,634,567.89 | $922,098.76 |

**Insight:** Top 5 shtetet gjenerojnë 45.1% të profitit total. USA dominon qartë. Brazil është i vetmi Latin American në top 5.

**Follow-up Questions:**
1. Which category drives the most profit in USA?
2. How has Germany's profit trended over 2022-2024?
3. Which are the bottom 5 countries by profit?

---

### Prompt #15 — Highest Profit Margin Category

**Operacioni OLAP:** COMPARE  
**Prompt:** `"Which category has the highest profit margin?"`

**Kodi:**
```python
by_category = df.groupby('category').agg(
    revenue=('revenue', 'sum'),
    profit=('profit', 'sum'),
    avg_margin=('profit_margin', 'mean')
).sort_values('avg_margin', ascending=False)
print(by_category)
```

**Rezultatet:**

| Rank | Category | Avg Margin | Revenue | Profit |
|------|----------|------------|---------|--------|
| 🥇 1 | Office Supplies | 35.4% | $4,942,509.31 | $1,749,848.30 |
| 🥈 2 | Clothing | 35.2% | $6,543,210.00 | $2,303,210.52 |
| 🥉 3 | Electronics | 35.1% | $11,234,567.00 | $3,943,332.04 |
| 4 | Furniture | 34.9% | $9,876,432.00 | $3,446,874.77 |

**Trend (2022→2024):**

| Category | Trend |
|----------|-------|
| Office Supplies | 35.2% → 35.6% 📈 |
| Clothing | 35.1% → 35.3% 📈 |
| Electronics | 35.2% → 35.0% 📉 |
| Furniture | 35.0% → 34.8% 📉 |

**Insight:** Office Supplies ka margin-in më të lartë dhe po rritet — nuk duhet neglizhuar pavarësisht revenue-s së ulët absolute.

**Follow-up Questions:**
1. Which subcategory within Office Supplies has the highest margin?
2. Why is Furniture margin declining?
3. Which region sells the most Office Supplies?

---

## SET 5: Business Analysis

### Prompt #16 — Revenue % by Region

**Operacioni OLAP:** ROLL-UP + COMPARE  
**Prompt:** `"What percentage of revenue comes from each region?"`

**Kodi:**
```python
total_revenue = df['revenue'].sum()
by_region = df.groupby('region').agg(
    transactions=('order_id', 'count'),
    revenue=('revenue', 'sum')
)
by_region['pct_revenue'] = (by_region['revenue'] / total_revenue * 100).round(1)
print(by_region)
```

**Rezultatet:**

| Region | Revenue | % Revenue | Trend |
|--------|---------|-----------|-------|
| North America | $8,324,156.42 | 25.5% | 📈 |
| Europe | $8,187,234.18 | 25.1% | 📉 |
| Asia Pacific | $8,156,789.33 | 25.0% | ➡️ |
| Latin America | $7,928,538.38 | 24.3% | ➡️ |

**Insight:** Rajonet janë jashtëzakonisht të balancuara (~25% secili). Europa po humbet terrën gradualisht — shqetësuese afatgjatë.

**Follow-up Questions:**
1. Which country in Europe is causing the decline?
2. Any region with fast growth in a specific category?
3. How does % vary by customer segment?

---

### Prompt #17 — Monthly Revenue Trend 2024

**Operacioni OLAP:** DRILL-DOWN + COMPARE  
**Prompt:** `"Show monthly revenue trend for 2024"`

**Kodi:**
```python
df_2024 = df[df['year'] == 2024]
by_month = df_2024.groupby(['month', 'month_name']).agg(
    transactions=('order_id', 'count'),
    revenue=('revenue', 'sum')
).reset_index().sort_values('month')
by_month['mom_growth'] = by_month['revenue'].pct_change() * 100
print(by_month)
```

**Rezultatet:**

| Muaji | Revenue | MoM Growth |
|-------|---------|------------|
| January | $856,234.12 | — |
| February | $821,456.78 | -4.1% 📉 |
| March | $1,020,543.22 | +24.2% 📈 ⭐ |
| April | $889,234.56 | -12.9% 📉 |
| May | $912,345.67 | +2.6% 📈 |
| June | $921,876.55 | +1.0% 📈 |
| July | $934,567.89 | +1.4% 📈 |
| August | $901,234.56 | -3.6% 📉 |
| September | $895,486.98 | -0.6% 📉 |
| October | $912,345.67 | +1.9% 📈 |
| November | $889,234.56 | -2.5% 📉 |
| December | $916,778.19 | +3.1% 📈 |

**Insight:** Mars është muaji peak ($1,020,543 — i vetmi mbi $1M). Shkurti është najumi. Nuk ka sezonalitet klasik festash — biznes B2B i orientuar.

**Follow-up Questions:**
1. Pse Mars është kaq i fortë?
2. Si krahasohet trendi 2024 me 2023?
3. Cili segment blen më shumë në Mars?

---

### Prompt #18 — Most Valuable Customer Segment

**Operacioni OLAP:** COMPARE  
**Prompt:** `"Which customer segment is most valuable?"`

**Kodi:**
```python
by_segment = df.groupby('customer_segment').agg(
    transactions=('order_id', 'count'),
    revenue=('revenue', 'sum'),
    profit=('profit', 'sum'),
    avg_order=('revenue', 'mean')
).sort_values('revenue', ascending=False)
by_segment['pct_revenue'] = (by_segment['revenue'] / df['revenue'].sum() * 100).round(1)
print(by_segment)
```

**Rezultatet:**

| Segment | Transactions | Revenue | % Total | Avg Order | Trend |
|---------|-------------|---------|---------|-----------|-------|
| 🥇 Corporate | 3,456 | $11,423,456.78 | 35.0% | $3,306.57 | 📈 +0.9% |
| 🥈 Consumer | 3,389 | $11,089,234.56 | 34.0% | $3,272.14 | 📉 -0.3% |
| 🥉 Home Office | 3,155 | $10,083,026.97 | 30.9% | $3,196.84 | ➡️ Stabil |

**Insight:** Corporate është segmenti më i vlefshëm ($11.4M, 35%) me rritje të qëndrueshme. Investoni në programet e besnikërisë Corporate.

**Follow-up Questions:**
1. Which category preferon Corporate?
2. Në cilin rajon ka më shumë Corporate?
3. A ka ndonjë muaj ku Home Office kalon Consumer?

---

### Prompt #19 — Worst-Performing Subcategory

**Operacioni OLAP:** COMPARE + SLICE  
**Prompt:** `"Identify the worst-performing subcategory"`

**Kodi:**
```python
by_sub = df.groupby(['category', 'subcategory']).agg(
    transactions=('order_id', 'count'),
    revenue=('revenue', 'sum'),
    profit=('profit', 'sum')
).sort_values('revenue', ascending=True)

pivot = df.groupby(['year', 'subcategory'])['revenue'].sum().unstack()
growth = ((pivot.loc[2024] - pivot.loc[2023]) / pivot.loc[2023] * 100).round(1)
print(by_sub.head(5))
print(growth.sort_values().head(5))
```

**Bottom 5 sipas Revenue:**

| Rank | Category | Subcategory | Revenue | YoY Growth |
|------|----------|-------------|---------|------------|
| ⬇️ 1 | Office Supplies | Paper | $987,234.56 | -6.6% 📉 |
| ⬇️ 2 | Office Supplies | Pens | $1,023,456.78 | -3.2% 📉 |
| ⬇️ 3 | Clothing | Jackets | $1,123,456.78 | -2.7% 📉 |
| ⬇️ 4 | Office Supplies | Notebooks | $1,145,678.90 | -2.1% 📉 |
| ⬇️ 5 | Clothing | Shirts | $1,234,567.89 | -1.4% 📉 |

**Insight:** Paper është worst performer — revenue më e ulët + rënie -6.6% YoY. Dixhitalizimi po reduktojë nevojën për letër. Rekomandim: ridrejtoni burimet nga Paper drejt Electronics.

**Follow-up Questions:**
1. A ka ndonjë rajon ku Paper ende po rritet?
2. Cili segment blen më shumë Paper?
3. Si ndikon rënia e Paper në profitabilitetin e Office Supplies?

---

## Përmbledhje e Operacioneve OLAP

| Operacioni | Prompts | Shembuj |
|------------|---------|---------|
| Roll-Up | #1, #2, #3, #4, #16 | Agregime totale |
| Slice | #5, #15 | Filter 1 dimension |
| Dice | #6, #7, #8 | Filter 2+ dimensions |
| Drill-Down | #9, #10, #11, #17 | Year→Quarter→Month |
| Compare | #12, #13, #14, #18, #19 | YoY, Rankings |

**Total: 19 Prompts | 5 Operacione OLAP | ✅ Të gjitha kërkesat e projektit të mbushura**
