# 🛒 Amazon Reviews — Sentiment Analysis Dashboard

> **CodeAlpha Data Analytics Internship — Task 4**
> Submitted by **Rejitha E** | ID: `CA/DF1/85415` | May 2026

---

## 📌 Project Overview

This project performs **Natural Language Processing (NLP)-based Sentiment Analysis** on Amazon product reviews. Reviews are classified as **Positive**, **Neutral**, or **Negative** using a lexicon-based approach, and the results are visualized through a rich static dashboard and an interactive HTML dashboard.

---

## 🖼️ Dashboard Preview

![Sentiment Analysis Dashboard](task4_sentiment_dashboard_v2.png)

---

## 📊 Key Results

| Metric | Value |
|---|---|
| 📦 Total Reviews Analyzed | 28,830 |
| ✅ Positive Reviews | 14,447 (50.1%) |
| ⚪ Neutral Reviews | 11,675 (40.5%) |
| ❌ Negative Reviews | 2,708 (9.4%) |
| 📈 Average Polarity Score | 1.19 |
| 🏆 Best Category | OfficeProducts (1.470) |
| ⚠️ Worst Category | Health & Personal Care (−0.118) |

---

## 📁 Project Structure

```
📦 amazon-sentiment-analysis/
├── 📄 amazon.csv                          # Raw dataset (Amazon product reviews)
├── 🐍 Sentiment_Analysis.py               # Original dashboard script (v1)
├── 🐍 Sentiment_Analysis_v2.py            # Upgraded script — Heatmap + Violin + Word Cloud
├── 🌐 sentiment_dashboard.html            # Interactive HTML dashboard (hover/click)
├── 🖼️ task4_sentiment_dashboard.png        # Static dashboard output (v1)
├── 🖼️ task4_sentiment_dashboard_v2.png     # Static dashboard output (v2)
└── 📄 README.md                           # This file
```

---

## ✨ Features

### v1 — Core Dashboard (`Sentiment_Analysis.py`)
- ✅ Overall sentiment donut chart
- ✅ Sentiment by product category (grouped bar)
- ✅ Score distribution histogram
- ✅ Top 10 positive & negative products
- ✅ Marketing insights — avg score by category
- ✅ Stacked bar — all categories breakdown

### v2 — Upgraded Dashboard (`Sentiment_Analysis_v2.py`)
- 🔥 **Heatmap** — sentiment intensity per category (color-coded)
- 🎻 **Violin Plot** — polarity score distribution per category
- ☁️ **Word Cloud** — most frequent keywords in positive reviews
- 📐 Expanded 4-row layout (28×22 figure)

### Interactive HTML (`sentiment_dashboard.html`)
- 🖱️ **Hover tooltips** on all charts and word cloud words
- 🔘 **Filter buttons** — view All / Positive / Neutral / Negative
- 📡 **Radar chart** — category-level Positive vs Negative comparison
- 🔥 **Heatmap** with intensity-based color cells
- ☁️ **Word Cloud** with green (positive) and red (negative) keywords
- 📊 Charts: Donut, Grouped Bar, Histogram, Violin-style, Stacked Bar
- 🌙 Dark theme with red accent — matches static dashboard aesthetic

---

## 🗂️ Dataset

**File:** `amazon.csv`

**Source:** Amazon India product reviews dataset

**Columns used:**

| Column | Description |
|---|---|
| `product_name` | Name of the product |
| `category` | Product category (pipe-separated hierarchy) |
| `review_title` | Short review title |
| `review_content` | Full review text |
| `rating` | Star rating (1–5) |

**Categories covered:**
`Computers & Accessories` · `Electronics` · `Home & Kitchen` · `OfficeProducts` · `MusicalInstruments` · `HomeImprovement` · `Car & Motorbike` · `Toys & Games` · `Health & Personal Care`

---

## 🧠 NLP Approach

This project uses a **Lexicon-Based Sentiment Analysis** method — no external NLP library dependency.

### How it works:
1. Reviews are extracted from `review_title` and `review_content` columns
2. Each review is split by commas into individual sentences
3. Words are matched against curated **positive** and **negative** word lexicons
4. Polarity score is computed as:

```
score = (positive_word_count − negative_word_count) / total_word_count × 10
```

5. Classification thresholds:
   - **Positive** → score > 0.05
   - **Negative** → score < −0.05
   - **Neutral** → −0.05 ≤ score ≤ 0.05

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core scripting |
| Pandas | Data loading & processing |
| Matplotlib | Static dashboard charts |
| NumPy | Numerical operations |
| WordCloud *(optional)* | Word cloud visualization in v2 |
| Chart.js | Interactive HTML charts |
| HTML / CSS / JS | Interactive dashboard frontend |

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/amazon-sentiment-analysis.git
cd amazon-sentiment-analysis
```

### 2. Install dependencies
```bash
pip install pandas matplotlib numpy
# Optional — for word cloud in v2:
pip install wordcloud
```

### 3. Run the original dashboard
```bash
python Sentiment_Analysis.py
# Output: task4_sentiment_dashboard.png
```

### 4. Run the upgraded dashboard (v2)
```bash
python Sentiment_Analysis_v2.py
# Output: task4_sentiment_dashboard_v2.png
```

### 5. Open the interactive HTML dashboard
Just open the file in any browser — no server needed:
```bash
# Windows
start sentiment_dashboard.html

# Mac
open sentiment_dashboard.html

# Linux
xdg-open sentiment_dashboard.html
```

> ⚠️ Make sure `amazon.csv` is in the same folder as the Python scripts before running.

---

## 💡 Key Insights

- **OfficeProducts** has the highest avg polarity score (1.470) — customers are most satisfied
- **Health & Personal Care** is the only category with a negative avg score (−0.118) — needs product quality improvement
- **50.1%** of all reviews are Positive — the overall brand perception is healthy
- Most common positive words: *best, easy, value, money, working, charging, worth*
- Most common negative words: *issue, problem, service, cheap, return, installation*
- **Electronics** and **Computers & Accessories** contribute 70%+ of total reviews

---

## 🏅 Internship Details

| Field | Details |
|---|---|
| Organization | CodeAlpha |
| Program | Data Analytics Internship |
| Task | Task 4 — Sentiment Analysis |
| Submitted by | Rejitha E |
| Intern ID | CA/DF1/85415 |
| Month | May 2026 |

---

## 📜 License

This project is submitted as part of an internship program. Dataset belongs to its respective owner. Code is for educational purposes.

---

<div align="center">
  Made with ❤️ by <b>Rejitha E</b> &nbsp;|&nbsp; CodeAlpha Internship 2026
</div>
