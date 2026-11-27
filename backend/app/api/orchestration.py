
from fastapi import APIRouter, HTTPException
from app.schemas.orchestration import OrchestrationRequest
from app.engine.orchestrator import AgentOrchestrator

router = APIRouter(prefix="/api", tags=["Agent Orchestration"])

orchestrator = AgentOrchestrator()


@router.post("/orchestrate")
def orchestrate(request: OrchestrationRequest):
    try:
        return orchestrator.run(
            goal=request.goal,
            constraints=request.constraints
        )
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error))
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail="Agent orchestration failed"
        ) from error
