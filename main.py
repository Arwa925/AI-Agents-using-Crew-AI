from agents.web_search_agent import WebSearchAgent
from agents.data_extraction_agent import DataExtractionAgent
from agents.trend_analysis_agent import TrendAnalysisAgent
from agents.report_writer_agent import ReportWriterAgent

def main():
    print("Starting CrewAI MENA AI/ML Jobs Report Generator...")
    
    # Step 1: Search and fetch job postings
    web_agent = WebSearchAgent()
    raw_data = web_agent.run()

    # Step 2: Extract relevant job information
    extractor = DataExtractionAgent()
    extracted_data = extractor.run(raw_data)

    # Step 3: Analyze job trends
    analyst = TrendAnalysisAgent()
    analysis = analyst.run(extracted_data)

    # Step 4: Generate the report
    writer = ReportWriterAgent()
    writer.run(analysis)

if __name__ == "__main__":
    main()
