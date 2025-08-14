from agents import Agent, Runner, trace, gen_trace_id
from clarifier_agent import clarifier_tool
from planner_agent import planner_tool
from search_agent import search_tool
from writer_agent import writer_tool
from email_agent import email_tool

MANAGER_INSTRUCTIONS = """
You are the Research Manager orchestrator.

1) **Clarify.** Ask the user 3 clarifying questions about their original query.
2) **Plan.** Once the user answers, call clarifier to parse those answers, then hand off both original query + answers to planner to get a tuned WebSearchPlan.
3) **Search.** For each item in that plan, call search to get summaries.
4) **Write.** Pass the collected summaries to writer to produce a full report.
5) **Email.** Use the send_email tool to deliver the report via HTML.

Make sure each handoff is explicit (you invoke the appropriate tool with the right data).
"""

manager_agent = Agent(
    name="ManagerAgent",
    instructions=MANAGER_INSTRUCTIONS,
    tools=[clarifier_tool, planner_tool, search_tool, writer_tool, email_tool],
    model="gpt-4o-mini",
)

class ResearchManager:
    async def run(self, query: str, clarifications: str = None, email: str = None):
        """Run the agentic research process, yielding status updates and the final report."""
        trace_id = gen_trace_id()
        with trace("Research trace", trace_id=trace_id):
            input_data = {"query": query}
            if clarifications:
                input_data["clarifications"] = clarifications
            if email:
                input_data["email"] = email
            result = await Runner.run(manager_agent, input_data)
            yield str(result.final_output)