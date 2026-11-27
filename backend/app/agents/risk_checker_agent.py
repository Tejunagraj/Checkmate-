
from typing import Any


class RiskCheckerAgent:
    """Checks constraints and identifies risks."""

    def run(
        self,
        goal: str,
        constraints: list[str],
        plan: dict[str, Any]
    ) -> dict[str, Any]:

        findings = []
        requires_human_approval = False

        for constraint in constraints:
            text = constraint.lower()

            if "budget" in text:
                findings.append({
                    "constraint": constraint,
                    "status": "requires_verification",
                    "risk": "medium",
                    "reason": "Actual workshop costs have not yet been verified."
                })

            elif "venue" in text or "capacity" in text:
                findings.append({
                    "constraint": constraint,
                    "status": "requires_verification",
                    "risk": "medium",
                    "reason": "Venue capacity must be confirmed before selection."
                })

            elif "approval" in text or "invitation" in text:
                requires_human_approval = True
                findings.append({
                    "constraint": constraint,
                    "status": "human_approval_required",
                    "risk": "high",
                    "reason": "Invitations must not be sent without explicit human approval."
                })

            else:
                findings.append({
                    "constraint": constraint,
                    "status": "requires_review",
                    "risk": "low",
                    "reason": "This constraint needs further validation."
                })

        return {
            "agent": "risk_checker",
            "findings": findings,
            "requires_human_approval": requires_human_approval,
            "external_actions_allowed": False
        }
