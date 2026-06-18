# Procurement Intelligence Copilot

AI-powered procurement analytics and supplier risk decision-support tool.

## Overview

This project helps procurement teams evaluate supplier performance, identify supplier risk, benchmark suppliers against category peers, and generate procurement recommendations.

The goal is to demonstrate how analytics, business logic, and AI-ready architecture can support better procurement decisions.

## Key Features

- Supplier risk scoring
- Category-level supplier benchmarking
- Risk driver explanations
- Procurement action recommendations
- Executive summary generation
- Interactive Streamlit dashboard
- Rule-based procurement analyst Q&A
- Risk analysis by supplier, category, country, and spend exposure

## Tech Stack

- Python
- Pandas
- Streamlit
- Plotly
- CSV-based data pipeline

## Project Architecture

```text
Raw Supplier Data
        ↓
Data Loader
        ↓
Category Benchmarking
        ↓
Supplier Risk Scoring
        ↓
Risk Explanation Engine
        ↓
Recommendation Engine
        ↓
Procurement Query Engine
        ↓
Streamlit Dashboard