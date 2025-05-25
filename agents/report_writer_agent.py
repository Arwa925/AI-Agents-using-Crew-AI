import os
import markdown

class ReportWriterAgent:
    def run(self, analysis):
        print("[ReportWriterAgent] Writing markdown report...")
        content = """# Top AI/ML Jobs in MENA – May 2025

## Top 10 AI/ML Job Roles
"""
        for title, count in analysis['top_titles']:
            content += f"- {title}: {count} postings\n"

        content += """
## Key Skills Required
"""
        for skill, count in analysis['top_skills']:
            content += f"- {skill}: {count} mentions\n"

        content += """
## Country-wise Job Distribution
"""
        for location, count in analysis['location_distribution'].items():
            content += f"- {location}: {count} jobs\n"

        content += """
## Observed Trends
- Machine Learning and Data Science remain dominant.
- Python is the most requested skill.
- UAE and Egypt lead in AI/ML job offerings.
"""

        with open("ai_ml_jobs_mena_may2025.md", "w") as f:
            f.write(content)

        print("[ReportWriterAgent] Markdown report saved as ai_ml_jobs_mena_may2025.md")
