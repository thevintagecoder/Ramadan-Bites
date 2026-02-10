# 🌙 Ramadan Bites

An interactive, aesthetically pleasing web experience designed to bring the spirit of Ramadan to your screen. This project features a virtual kitchen scene that suggests random **Indian and Bengali Iftar recipes** complete with cooking instructions and video tutorials.

## ✨ Features

- **Atmospheric UI:** A Studio Ghibli-inspired Iftar background with calming ambient music (toggleable).
- **Ramadan Dashboard:** Displays current Hijri date, English date, and Sehri/Iftar timings (currently set to Mecca).
- **Interactive 3D Scene:** Click "Open Kitchen" to trigger a smooth 3D animation revealing a recipe book and a virtual iPad.
- **Recipe Generator:** Fetches random **Indian/Bengali recipes** perfect for Iftar.
- **Video Tutorials:** Automatically embeds a YouTube cooking video for the suggested recipe on the virtual iPad.
- **Refresh Option:** Don't like the suggestion? Click "Show me another recipe" to get a new one instantly.

## 🛠️ Tech Stack

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **Frontend:** HTML5, CSS3 (3D Transforms, Flexbox), JavaScript (Vanilla)
- **Template Engine:** Jinja2

## 🔗 APIs Used

This project relies on the following free public APIs:

1. **[Aladhan API](https://aladhan.com/prayer-times-api):** For retrieving prayer (Sehri & Iftar) timings and Hijri dates.
2. **[TheMealDB](https://www.themealdb.com/api.php):** For fetching random recipe details, instructions, and YouTube links.

## 📂 Project Structure

```bash
Ramadan-Kitchen/
├── main.py              # FastAPI application entry point
├── templates/
│   └── index.html       # Main HTML structure
├── static/
│   ├── style.css        # Styling and 3D animations
│   └── background.jpg   # Background image
└── README.md            # Project documentation
```

How to Run Locally
Clone the repository
Install Dependencies
You need Python installed. Install FastAPI and Uvicorn:

Add the Background Image
Make sure you have your background image saved as background.jpg inside the static folder.

Run the Server
View the App
Open your browser and go to: http://127.0.0.1:8000

Credits
Created by: Nafisa Mehzabin

Fonts: Google Fonts (Reem Kufi, Cinzel Decorative, Patrick Hand, Amiri)

Music: SoundHelix

Ramadan Mubarak! May your days be filled with peace and delicious food. 🥣✨
