#!/usr/bin/env python
import uvicorn
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    port = int(os.getenv("PORT", 8000))
    print(f"🚀 Starting AI Interior Designer API on http://localhost:{port}")
    print(f"📚 API Docs: http://localhost:{port}/api/docs")
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        log_level="info"
    )
