# CLV Intelligence

> Probabilistic Customer Lifetime Value prediction system — BG/NBD + Gamma-Gamma models on real e-commerce data.

**Live Demo → [clv-intel.streamlit.app](https://clv-intel.streamlit.app)**

<img width="1358" height="818" alt="Screenshot 2026-06-27 at 2 45 49 PM" src="https://github.com/user-attachments/assets/94f96556-1a68-46d7-8d73-c8d9f7fe2ab2" />


---

## What It Does

Most businesses treat all customers equally. This system doesn't.

CLV Intelligence scores every customer with a predicted revenue value for the next 12 months, then segments them into four actionable tiers — Champion, Loyal, At Risk, and Lost — so marketing and retention budgets can be allocated where they'll generate the highest return.

---

## Results

| Metric | Value |
|---|---|
| Raw transactions | 541,910 |
| After cleaning | 397,885 |
| Unique customers scored | 2,790 |
| Top customer CLV (12 months) | £221,383 |
| Average CLV across base | £2,700 |
| Champion customers | 698 (25%) |

---

## How It Works

### 1. Data Cleaning
541,910 raw transactions from the UCI Online Retail II dataset were cleaned — removing guest checkouts (135k rows), cancelled orders (8,905 rows), zero-price items, and negative quantities — producing 397,885 valid transaction rows.

### 2. RFM Feature Engineering
Each customer was summarised into three features used as model inputs:

- **Recency** — days since last purchase
- **Frequency** — number of unique orders placed
- **Monetary** — average revenue per order (£)

### 3. Probabilistic Modelling

**BG/NBD Model** — predicts how many future purchases each customer will make. Models two processes simultaneously: how often a customer buys while active, and the probability they have churned.

**Gamma-Gamma Model** — predicts average spend per future transaction. Fitted only on repeat buyers (2,790 customers). Assumes monetary value is independent of purchase frequency.

### 4. CLV Calculation

```
CLV = BG/NBD(predicted purchases) × Gamma-Gamma(avg order value) × 12 months
```

### 5. Segmentation
Customers scored and segmented into four tiers using CLV quartiles:

| Segment | Customers | Avg CLV | Avg Orders |
|---|---|---|---|
| Champion | 698 | £7,258 | 12.8 |
| Loyal | 697 | £1,826 | 5.1 |
| At Risk | 697 | £1,095 | 3.8 |
| Lost | 698 | £616 | 2.6 |

---

## Dashboard Features

- **Dashboard** — key metrics, CLV overview by segment, distribution histogram, top customers leaderboard
- **Segments** — deep dive into each tier with box plots and recency vs frequency scatter
- **Customer Lookup** — enter any customer ID to get their CLV score, segment badge, and business recommendation
- **Model Info** — explains the BG/NBD and Gamma-Gamma models and the CLV formula
- **About** — project overview and tech stack

---

## Tech Stack

| Layer | Tools |
|---|---|
| Data Processing | Python, Pandas, NumPy |
| Modelling | Lifetimes (BG/NBD, Gamma-Gamma) |
| Visualisation | Plotly |
| Dashboard | Streamlit |
| Version Control | Git, GitHub |
| Deployment | Streamlit Cloud |

---

## Project Structure

```
clv-model/
├── data/
│   ├── raw/                  ← UCI Online Retail II dataset
│   └── processed/            ← cleaned transactions, RFM table, CLV scores
├── notebooks/
│   ├── 01_eda.ipynb          ← data loading, cleaning, EDA
│   ├── 02_clv_model.ipynb    ← BG/NBD + Gamma-Gamma modelling
│   └── 03_segmentation.ipynb ← customer segmentation
├── src/
│   └── app.py                ← Streamlit dashboard
├── requirements.txt
└── README.md
```

---

## Dataset

**UCI Online Retail II** — real transaction data from a UK-based online retailer, December 2010 to December 2011.

→ [Download from UCI ML Repository](https://archive.uci.edu/dataset/502/online+retail+ii)

---

## Run Locally

```bash
git clone https://github.com/whoj1ngmu77/clv-model.git
cd clv-model
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd src
streamlit run app.py
```

---

## Business Recommendations by Segment

| Segment | Recommended Action |
|---|---|
| Champion | Prioritize retention. Offer exclusive loyalty rewards and early access. |
| Loyal | Nurture with personalised offers. Upsell higher-value product lines. |
| At Risk | Re-engagement campaign within 30 days. Time-limited discount. |
| Lost | Single win-back email only. Low ROI to pursue aggressively. |

---

Built by **Gayathri Menon**
