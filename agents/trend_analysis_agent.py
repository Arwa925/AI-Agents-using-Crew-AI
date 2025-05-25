from collections import Counter, defaultdict

class TrendAnalysisAgent:
    def run(self, extracted_data):
        print("[TrendAnalysisAgent] Analyzing trends...")

        job_titles = [job['title'] for job in extracted_data]
        skills = [skill for job in extracted_data for skill in job['skills']]
        locations = [job['location'] for job in extracted_data]

        top_titles = Counter(job_titles).most_common(10)
        top_skills = Counter(skills).most_common(10)
        location_dist = Counter(locations)

        result = {
            "top_titles": top_titles,
            "top_skills": top_skills,
            "location_distribution": location_dist
        }

        print("[TrendAnalysisAgent] Analysis complete.")
        return result
