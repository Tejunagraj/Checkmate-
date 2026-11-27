
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.persistence.database import get_db
from app.models.session import CollaborationSession
from app.schemas.session import SessionCreate, SessionResponse

router = APIRouter(
    prefix="/api/session",
    tags=["Sessions"]
)


@router.post(
    "/start",
    response_model=SessionResponse,
    status_code=status.HTTP_201_CREATED
)
def create_session(
    payload: SessionCreate,
    db: Session = Depends(get_db)
):
    try:
        new_session = CollaborationSession(
            goal=payload.goal.strip(),
            scenario=payload.scenario.strip(),
            constraints=payload.constraints
        )

        db.add(new_session)
        db.commit()
        db.refresh(new_session)

        return new_session

    except Exception as error:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Unable to create collaboration session"
        ) from error


@router.get("/{session_id}", response_model=SessionResponse)
def get_session(
    session_id: str,
    db: Session = Depends(get_db)
):
    session = db.get(CollaborationSession, session_id)

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    return session
