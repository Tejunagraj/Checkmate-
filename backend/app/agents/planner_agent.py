
from typing import Any


class PlannerAgent:
    """Creates a structured plan from a user's goal."""

    def run(self, goal: str, constraints: list[str]) -> dict[str, Any]:
        normalized_goal = goal.strip()

        if not normalized_goal:
            raise ValueError("Goal cannot be empty")

        tasks = [
            {
                "id": "task_1",
                "title": "Define workshop requirements",
                "description": "Confirm objectives, audience and expected outcomes.",
                "status": "pending"
            },
            {
                "id": "task_2",
                "title": "Prepare budget and venue plan",
                "description": "Estimate costs and verify venue capacity.",
                "status": "pending"
            },
            {
                "id": "task_3",
                "title": "Prepare workshop schedule",
                "description": "Create a timeline and assign responsibilities.",
                "status": "pending"
            },
            {
                "id": "task_4",
                "title": "Prepare invitations for approval",
                "description": "Draft invitations without sending them.",
                "status": "pending"
            }
        ]

        return {
            "agent": "planner",
            "goal": normalized_goal,
            "constraints_received": constraints,
            "tasks": tasks,
            "status": "plan_created"
        }
