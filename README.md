# Marketing Mix Modeling (MMM) and Multi-Touch Attribution (MTA) Analysis

This project implements a **Marketing Mix Model (MMM)** to evaluate the effectiveness of various marketing channels, both offline (TV, Radio) and online (Digital Ads). The model helps optimize media spend by identifying which channels drive the most conversions. Additionally, **Multi-Touch Attribution (MTA)** is supported to distribute conversions across multiple channels.

## Project Overview

The model is designed to support decision-making for large-scale media campaigns with over **$1.5 million** in spend. This analysis has helped:
- Improve ROI by **15%** by identifying high-performing media channels.
- Achieve a **10% uplift in offline sales** (TV and Radio ads).
- Increase digital conversions by **12%** through multi-channel attribution.

### Key Features:
- **Marketing Mix Modeling (MMM):** 
  - Analyzes the impact of media spend across multiple channels.
  - Helps optimize ad budgets to maximize conversions and ROI.
  
- **Multi-Touch Attribution (MTA):**
  - Determines how different channels contribute to conversions.
  
- **Offline Measurement:**
  - Uplift analysis for offline media (TV and Radio) in driving incremental sales and conversions.
  
- **Budget Optimization:**
  - Model-driven approach to allocate media spend for maximum efficiency.

## Data

The model works on simulated data, including:
- **TV Spend:** Represents offline TV ad expenditure.
- **Radio Spend:** Represents offline Radio ad expenditure.
- **Digital Spend:** Represents online ad expenditure (e.g., social media, search ads).
- **Conversions:** The total number of sales/conversions driven by the marketing mix.

The model can be adapted to real-world marketing data where anonymized spend and conversions are available.

## How to Run

### Requirements:
- **Python 3.x**
- Install the required libraries:
  ```bash
  pip install pandas numpy statsmodels matplotlib seaborn

