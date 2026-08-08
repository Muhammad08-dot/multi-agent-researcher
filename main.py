from agents import ResearchState, SearchAgent, WriterAgent, CriticAgent

def run_research_workflow(topic: str):
    print(f"--- Starting Multi-Agent Research Workflow for: {topic} ---")
    state = ResearchState(topic=topic)
    
    searcher = SearchAgent()
    writer = WriterAgent()
    critic = CriticAgent()
    
    # Step 1: Research
    state = searcher.execute(state)
    
    # Step 2: Draft
    state = writer.execute(state)
    
    # Step 3: Criticize & Finalize
    state = critic.execute(state)
    
    print("\n--- Final Output ---")
    print(state.final_report)
    print("--------------------")

if __name__ == "__main__":
    topic = "The impact of Agentic AI in 2026"
    run_research_workflow(topic)
