from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import random
from datetime import datetime

app = FastAPI()

# 1. Mount Static Files (for CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# 2. Set up Templates
templates = Jinja2Templates(directory="templates")

# 3. Sample Data (You can expand this list!)
recipes = [
    {"day": 1, "name": "Creamy Chicken Alfredo Pasta", "desc": "Rich, cheesy pasta to comfort the soul after a long fast.", "time": "30 mins"},
    {"day": 2, "name": "Spicy Potato Samosas", "desc": "Crispy golden pockets filled with spiced potatoes and peas.", "time": "45 mins"},
    {"day": 3, "name": "Refreshing Watermelon Feta Salad", "desc": "Hydrating and savory sweet salad with mint leaves.", "time": "10 mins"},
    {"day": 4, "name": "Classic Beef Haleem", "desc": "Slow-cooked stew with lentils and meat, perfect for energy.", "time": "3 hours"},
    {"day": 5, "name": "Turkish Adana Kebabs", "desc": "Smoky, grilled minced meat skewers with sumac onions.", "time": "40 mins"},
]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Logic: Get a recipe. 
    # For now, let's pick a random one so it changes every time you refresh.
    # In a real app, you could map this to the actual date!
    daily_recipe = random.choice(recipes)
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "recipe": daily_recipe
    })