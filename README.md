Open Air Quality Data Pipeline

This is a data engineering project I built as a learner, to understand how real data pipelines work end-to-end.
I used open air-quality data to practice ingestion, transformation, SQL analysis, and building a live dashboard.

⭐ What I Learned (and Implemented)
  How to ingest data from public sources
  How to store and query data using DuckDB
  How to write SQL for cleaning and transforming data
  How to organize code into pipelines
  How to build a Plotly Dash dashboard
  How different parts of a data pipeline fit together

🛠 Tech Stack I Used
  Purpose	Tool
  Scripting / pipeline	Python
  Database	DuckDB
  Dashboard	Plotly Dash
  Data source	OpenAQ S3 archive
  Storage	Local filesystem
📁 Project Structure
AIR-QUALITY-PIPELINE/
│
├── notebooks/                     # My experiments and testing
├── sql/                           # SQL scripts for DuckDB
├── pipeline/                      # Extraction + Transformation + DB setup
├── dashboard/                     # Plotly Dash app
│
├── locations.json
├── secrets-example.json
├── requirements.txt
└── README.md

🗄️ Database Design
  Schema 1: raw
    Stores all ingested data.
    raw.air_quality_raw
    ✔ Stores every measurement exactly as ingested
    ✔ Used for debugging and reprocessing
    👉 SQL used: sql/load_raw_data.sql
  
  Schema 2: presentation
    Clean & analytics-ready tables:
    presentation.air_quality
    presentation.daily_air_quality_stats
    presentation.latest_param_values_per_location
    👉 SQL used: sql/create_presentation_views.sql

📊 Data Ingestion Summary

  This project ingests open air-quality measurements into DuckDB.
  You can check how many rows are ingested using:
  SELECT COUNT(*) FROM raw.air_quality_raw;
  You can update this table every time you run the pipeline:
  Ingestion Date	Records Ingested	Notes
  2025-01-15	145,200	Initial load
  2025-01-16	147,890	Daily refresh
  (I update this manually based on each run.)

▶️ How to Run the Project
  1. Setup environment
  python -m venv .venv
  .venv\Scripts\activate  # Windows


Install dependencies:
  1.pip install -r requirements.txt
  
  2. Initialize database
    cd pipeline
    python database_manager.py --create
  
  3. Extract data
    python extraction.py --source s3
  
  4. Transform data
    python transformation.py
  
  5. Launch dashboard
    cd ../dashboard
    python app.py


Open in browser:
  http://localhost:8050

🎯 Why I Built This
  I created this project to:
    Improve my Python skills
    Learn SQL + DuckDB
    Understand pipeline architecture
    Build something I can show on GitHub
    Start my journey toward cloud/data engineering
    This is still a learning project, but I built every part myself.



Would you like any of these?
