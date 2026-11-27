
from app.agents.planner_agent import PlannerAgent
from app.agents.risk_checker_agent import RiskCheckerAgent
from app.agents.execution_synthesizer import ExecutionSynthesizer


class AgentOrchestrator:
    """Coordinates the three CHECKMATE agents."""

    def __init__(self):
        self.planner = PlannerAgent()
        self.risk_checker = RiskCheckerAgent()
        self.synthesizer = ExecutionSynthesizer()

    def run(self, goal: str, constraints: list[str]) -> dict:
        plan = self.planner.run(goal, constraints)

        risk_report = self.risk_checker.run(
            goal=goal,
            constraints=constraints,
            plan=plan
        )

        synthesis = self.synthesizer.run(
            plan=plan,
            risk_report=risk_report
        )

        return {
            "project": "CHECKMATE",
            "workflow_status": "awaiting_human_review",
            "plan": plan,
            "risk_report": risk_report,
            "synthesis": synthesis,
            "human_control": {
                "approval_required": True,
                "external_actions_allowed": False
            }
        }
