
from typing import Any


class ExecutionSynthesizer:
    """Combines agent outputs into a proposed next action."""

    def run(
        self,
        plan: dict[str, Any],
        risk_report: dict[str, Any]
    ) -> dict[str, Any]:

        return {
            "agent": "execution_synthesizer",
            "summary": "The workshop plan is prepared for human review.",
            "proposed_action": "Verify the budget and venue capacity.",
            "next_step": "human_review",
            "approval_required": True,
            "blocked_actions": [
                "Sending invitations without human approval",
                "Making external bookings or payments"
            ],
            "plan_task_count": len(plan["tasks"]),
            "risk_count": len(risk_report["findings"])
        }
