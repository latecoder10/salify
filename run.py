from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()

host = os.getenv("HOST", "127.0.0.1")
port = int(os.getenv("PORT", 9000))

# Run the FastAPI app using Uvicorn ONLY if this file is executed directly,
if __name__ == "__main__":
    uvicorn.run("app.main:app", host=host, port=port, reload=True)
