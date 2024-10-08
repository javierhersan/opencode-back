from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.auth import auth_router  # Import the auth router
from controllers.docker import docker_router  # Import the docker router

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:5173",  # Your React app URL
    # You can add more origins if needed
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,  # Allow cookies and credentials
    allow_methods=["*"],     # Allow all HTTP methods
    allow_headers=["*"],     # Allow all headers
)

# Include the authentication and docker routes
app.include_router(auth_router)
app.include_router(docker_router)

# Root route for testing
@app.get("/root")
async def root():
    return {"message": "Hello World"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)