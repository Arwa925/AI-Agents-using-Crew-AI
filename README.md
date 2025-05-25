# CrewAI MENA AI/ML Jobs Report

##  Objective
A multi-agent system to autonomously generate a market intelligence report for in-demand AI/ML jobs in the MENA region.

##  Agents
- **WebSearchAgent**: Fetches job postings from major job platforms.
- **DataExtractionAgent**: Extracts job titles, skills, and locations.
- **TrendAnalysisAgent**: Analyzes top roles, skills, and job distribution.
- **ReportWriterAgent**: Generates a Markdown report.

##  Folder Structure
crew_ai_ml_mena/
├── agents/
│ ├── web_search_agent.py
│ ├── data_extraction_agent.py
│ ├── trend_analysis_agent.py
│ └── report_writer_agent.py
├── utils/
│ └── scraper.py
├── main.py
├── requirements.txt
└── README.md

نسخ
تحرير

##  Usage

1. Install requirements:


pip install -r requirements.txt
Run the system:

python main.py
The report will be generated as ai_ml_jobs_mena_may2025.md.


 Sample Output
Top Roles
Machine Learning Engineer: 1 postings

Data Scientist: 1 postings

AI Researcher: 1 postings

Top Skills
Python: 2 mentions

TensorFlow: 1 mentions

Deep Learning: 1 mentions
...

 Country-wise Distribution
Dubai, UAE: 1 jobs

Cairo, Egypt: 1 jobs

Riyadh, Saudi Arabia: 1 jobs

 Status
MVP (Minimum Viable Product) Complete. Can be extended with:

Real web scraping

Skill clustering

Visualization dashboard


