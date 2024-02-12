from fastapi import FastAPI

app = FastAPI()

@app.get('/help')
async def ayuda():
  return "Video&FotosTren online"
  
@app.get('/')
async def root():
  return {
    "message": "Video&FotosTren online",
    "version": "1.0"
  }