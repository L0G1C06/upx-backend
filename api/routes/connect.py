from fastapi import APIRouter
from fastapi.responses import JSONResponse, RedirectResponse

router = APIRouter(prefix="/connect", tags=["connect"])

@router.post("/backend")
async def connect_backend():
    try:
        redirect_url = "http://0.0.0.0:8000/backend/sendwarning"
        response = RedirectResponse(url=redirect_url)
        return response 
    except Exception as http_exception:
        return JSONResponse(content=f"HTTPException: {str(http_exception)}", status_code=400)