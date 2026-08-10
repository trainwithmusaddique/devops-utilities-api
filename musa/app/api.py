from fastapi import FastAPI
from routers import matrics, aws

app = FastAPI(
    title="Internal DevOps Utilities API",
    description="This is an Internal API Utilities App for Monitoring matrics, AWS Usage, Log ANalysis, etc ",
    version="1.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")
def hello():
    """
    This is a Hello API , just for testing
    """
    return {"message":"Hello Dosto, This is a DevOps Utilities API"} 

app.include_router(matrics.router)
app.include_router(aws.router, prefix="/aws")