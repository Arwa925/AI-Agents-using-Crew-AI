class DataExtractionAgent:
    def run(self, raw_data):
        print("[DataExtractionAgent] Extracting relevant job fields...")
        extracted = []
        for job in raw_data:
            extracted.append({
                "title": job.get("title", "Unknown"),
                "company": job.get("company", "Unknown"),
                "location": job.get("location", "Unknown"),
                "skills": job.get("skills", []),
                "platform": job.get("platform", "Unknown")
            })
        print(f"[DataExtractionAgent] Extracted {len(extracted)} jobs.")
        return extracted
