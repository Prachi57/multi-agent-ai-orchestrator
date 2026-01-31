from agents.summarizer import SummarizerAgent
from agents.action_extractor import ActionExtractorAgent
from agents.planner import PlannerAgent


class Orchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.summarizer = SummarizerAgent()
        self.action_extractor = ActionExtractorAgent()

    def run(self, document_text):
        plan = self.planner.create_plan()

        result = {}

        if "summarize_document" in plan:
            summary = self.summarizer.summarize(document_text)
            result["summary"] = summary

        if "extract_action_items" in plan:
            actions = self.action_extractor.extract_actions(document_text)
            result["action_items"] = actions

        return result


if __name__ == "__main__":
    text = """
    The project deadline is next Friday. 
    John should prepare the dataset. 
    The team must review model accuracy.
    A client meeting should be scheduled.
    """

    orchestrator = Orchestrator()
    output = orchestrator.run(text)

    print("\nFINAL OUTPUT:\n")
    print(output)
