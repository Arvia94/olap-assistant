# User Guide — OLAP Business Intelligence Assistant
**Versioni:** 1.0  
**Data:** 2026-02-23  
**Tier:** 1 — Analyst  

---

## Çfarë është ky sistem?

OLAP Assistant është një asistent inteligjent biznesi që të lejon të analizosh të dhëna shitjesh duke përdorur pyetje në gjuhë të natyrshme. Nuk keni nevojë të dini SQL apo Python — thjesht pyesni si me një koleg analist!

**Dataset:** Global Retail Sales — 10,000 transaksione nga 2022–2024  
**Rajonet:** North America, Europe, Asia Pacific, Latin America  
**Kategoritë:** Electronics, Furniture, Office Supplies, Clothing

---

## Kërkesat e Sistemit

| Komponent | Versioni |
|-----------|---------|
| Python | 3.8+ |
| pandas | 3.0.1+ |
| numpy | 2.4.2+ |
| Claude.ai | Pro ose API |

---

## Instalimi Hap pas Hapi

### Hapi 1: Klono ose shkarko projektin

Struktura e folderit duhet të jetë:
```
olap-assistant/
├── CLAUDE.md
├── generate_dataset.py
├── data/
│   └── global_retail_sales.csv
├── prompts/
│   └── prompt_library.md
├── docs/
│   ├── user_guide.md
│   └── reflection.md
└── outputs/
```

### Hapi 2: Instalo dependencies

Hap PowerShell brenda folder-it `olap-assistant` dhe ekzekuto:
```
pip install pandas numpy
```

### Hapi 3: Gjenero dataset-in

```
python generate_dataset.py
```

Duhet të shohësh:
```
✅ Dataset u krijua me sukses!
📊 Totali i transaksioneve: 10000
📅 Periudha: 2022-01-01 deri 2024-12-31
💰 Revenue total: $32,596,718.31
```

### Hapi 4: Hap Claude.ai

Shko te [claude.ai](https://claude.ai) dhe logohu me llogarinë tënde.

### Hapi 5: Ngarko CLAUDE.md

1. Krijo një bisedë të re me Claude
2. Kopjo të gjithë përmbajtjen e `CLAUDE.md`
3. Ngjite si mesazhin e parë me instruksionin: *"Lexo këtë konfigurim dhe vepro sipas tij për të gjitha pyetjet e mia."*

---

## Si të Bësh Pyetje

### Formati i Rekomanduar

Pyetjet funksionojnë më mirë kur janë:
- **Specifike:** "Show Electronics revenue in Europe for 2024" ✅
- **Me kontekst:** "Compare Q3 vs Q4 2024 by region" ✅
- **Me operacion:** "Drill down into North America by country" ✅

Shmangni pyetje shumë të gjera:
- "Më trego gjithçka" ❌
- "Analizo të dhënat" ❌

---

## Udhëzues sipas Operacionit OLAP

### 1. SLICE — Filter një dimension

Përdorni kur doni të shihni vetëm një periudhë, rajon, ose kategori.

**Shembuj:**
```
"Show only 2024 transactions"
"Filter to Electronics category only"
"Show only Corporate segment data"
"Display Q4 data only"
```

**Rezultati që do të merrni:**
- Numri i transaksioneve të filtruara
- Revenue dhe profit total
- Breakdown sipas nën-dimensioneve

---

### 2. DICE — Filter shumë dimensione

Përdorni kur doni të kombinoni dy ose më shumë filtera njëkohësisht.

**Shembuj:**
```
"Show Electronics sales in Europe"
"Q4 2024, Corporate segment only"
"Filter to Asia Pacific, 2023, revenue above $500"
"North America, Furniture, Home Office segment"
```

**Rezultati që do të merrni:**
- Dataset i filtruar sipas të gjithë kritereve
- Breakdown sipas vendeve ose nën-kategorive

---

### 3. DRILL-DOWN — Shko nga përmbledhja tek detaji

Përdorni kur doni të eksploroni hierarkinë: Vit → Kuartal → Muaj ose Rajon → Vend.

**Shembuj:**
```
"Show revenue by year, then drill into 2024 by quarter"
"Drill Q4 2024 down to months"
"Show category totals, drill into Electronics by subcategory"
"Break down North America revenue by country"
```

**Rezultati që do të merrni:**
- Tabela në dy nivele (përmbledhje + detaj)
- Identifikimi i performerit kryesor

---

### 4. ROLL-UP — Agriego detajet në përmbledhje

Përdorni kur doni totale të nivelit të lartë.

**Shembuj:**
```
"What is the total revenue across all years?"
"Summarize all countries into regional totals"
"Show monthly data as quarterly totals"
"What is the overall average order value?"
```

---

### 5. COMPARE — Krahasime dhe renditje

Përdorni kur doni të krahasoni periudha, rajonet, ose kategori.

**Shembuj:**
```
"Compare 2023 vs 2024 total revenue"
"Calculate year-over-year growth by region"
"Top 5 countries by profit"
"Which category has the highest profit margin?"
"Which customer segment is most valuable?"
```

---

## Pyetje të Gatshme për Kopjim

Mund t'i kopjoni direkt këto pyetje në Claude:

**Analiza Bazë:**
- `What is the total revenue across all years?`
- `What is the total profit by region?`
- `What is the average order value?`
- `How many transactions per category?`

**Slice & Dice:**
- `Show only 2024 transactions`
- `Filter to Electronics in Europe`
- `Show Q4 data for Corporate segment only`
- `Filter to Asia Pacific, 2023, revenue above $500`

**Drill-Down:**
- `Show revenue by year, then drill into 2024 by quarter`
- `Drill Q4 2024 down to months`
- `Show category totals, drill into Electronics by subcategory`

**Krahasime:**
- `Compare 2023 vs 2024 total revenue`
- `Calculate year-over-year growth by region`
- `Top 5 countries by profit`
- `Which category has the highest profit margin?`

**Analizë Biznesi:**
- `What percentage of revenue comes from each region?`
- `Show monthly revenue trend for 2024`
- `Which customer segment is most valuable?`
- `Identify the worst-performing subcategory`

---

## Interpretimi i Rezultateve

Çdo përgjigje do të ketë këtë strukturë:

```
## [Operacioni OLAP]: [Përshkrimi]

Business Question: [Pyetja e riformuluar]
Analysis: [Kodi Python i përdorur]
Results: [Tabela me të dhëna]
Business Insight: [Interpretimi në gjuhë biznesi]
Suggested Follow-up Questions: [3 pyetje vijuese]
```

---

## Këshilla dhe Truke

**✅ Bëni pyetje vijuese:**
Pas çdo përgjigje, Claude sugjeron 3 pyetje. Ndiqini ato për analiza më të thella!

**✅ Kombinoni operacionet:**
```
"Compare 2023 vs 2024 by region, then drill into the best performer by quarter"
```

**✅ Kërkoni vizualizime:**
```
"Show this as a bar chart"
"Create a trend line for monthly revenue"
```

**✅ Kërkoni rekomandime:**
```
"Based on this analysis, what should management focus on?"
"Which region needs immediate attention?"
```

---

## Zgjidhja e Problemeve

| Problem | Zgjidhja |
|---------|---------|
| Claude nuk di për dataset-in | Ringarko CLAUDE.md në fillim të bisedës |
| Rezultate të gabuara | Specifikoni kolonat saktë (p.sh. 'year' jo 'Year') |
| Kodi nuk ekzekutohet | Kontrollo që `pandas` është instaluar |
| Dataset nuk gjendet | Ekzekuto `python generate_dataset.py` sërish |

---

## Struktura e Dataset-it për Referim

| Kolona | Tipi | Shembull |
|--------|------|---------|
| order_id | Text | ORD-00001 |
| order_date | Date | 2024-03-15 |
| year | Integer | 2024 |
| quarter | Text | Q1, Q2, Q3, Q4 |
| month | Integer | 1-12 |
| month_name | Text | January |
| region | Text | North America |
| country | Text | USA |
| category | Text | Electronics |
| subcategory | Text | Laptops |
| customer_segment | Text | Corporate |
| quantity | Integer | 5 |
| unit_price | Float | $1,299.99 |
| revenue | Float | $6,499.95 |
| cost | Float | $4,224.97 |
| profit | Float | $2,274.98 |
| profit_margin | Float | 35.0% |
