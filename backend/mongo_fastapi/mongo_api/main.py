import os
import uvicorn

PORT = int(os.getenv("FASTAPI_PORT", 8001))
DEBUG = bool(os.getenv("FASTAPI_DEBUG", True))
DEPLOY = os.getenv("FASTAPI_DEPLOY", 'Null')

if __name__ == "__main__":
    print('-'*50)
    print(f'ANSC:\t  API SERVER: Mogno Fast API | {DEPLOY.capitalize()}')
    print(f'ANSC:\t  API SERVER RUN ON 127.0.0.1:{PORT}')
    print(f"ANSC:\t  API SERVER DEBUG MODE: {DEBUG}")
    print('-'*50)
    uvicorn.run("api.app:app", host="0.0.0.0", port=PORT, reload=DEBUG)