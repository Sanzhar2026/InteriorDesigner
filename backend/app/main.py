# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Interior Designer API",
    description="Generate interior designs using Adobe Firefly AI",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import routers
from app.routers import interior_designer

# Include routers
app.include_router(interior_designer.router)

@app.get("/")
async def root():
    return {
        "message": "AI Interior Designer API",
        "version": "1.0.0",
        "status": "online",
        "endpoints": {
            "generate": "POST /api/interior/generate",
            "styles": "GET /api/interior/styles",
            "inspire": "POST /api/interior/inspire",
            "docs": "/api/docs",
            "health": "/health"
        }
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "api_key_configured": bool(os.getenv("ADOBE_API_KEY") and os.getenv("ADOBE_API_KEY") != "your_adobe_api_key_here")
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    logger.info(f"🚀 Starting server on http://localhost:{port}")
    uvicorn.run(app, host="0.0.0.0", port=port, reload=True)
