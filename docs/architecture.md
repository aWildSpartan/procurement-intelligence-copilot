# Architecture

## Data Flow

Raw supplier CSV → Benchmarking Engine → Risk Scoring Engine → Recommendation Engine → Streamlit Dashboard

## Core Modules

- `data_loader.py`: loads supplier CSV data
- `benchmarking.py`: calculates category-level performance benchmarks
- `scoring.py`: calculates supplier risk scores
- `risk_explainer.py`: explains risk drivers
- `recommendation_engine.py`: recommends procurement actions
- `query_engine.py`: answers procurement questions
- `dashboard.py`: Streamlit application interface

## Design Philosophy

The system uses structured procurement logic before adding LLM capabilities. This reduces hallucination risk and keeps recommendations grounded in supplier performance data.