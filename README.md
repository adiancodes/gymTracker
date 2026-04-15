# Gym & Hydration Tracker 💪💧

This is a simple web application I built for my Web Programming Lab project. It helps track daily workout routines and monitors daily water intake goals all in one place. 

I designed it with a clean, dark-mode focused look without relying too much on bloated Bootstrap styles, keeping the focus on speed and simplicity. 
<img width="1748" height="873" alt="image" src="https://github.com/user-attachments/assets/ddde3452-4ec9-46af-a188-854272e55fec" />

## Features 🚀
- **Dashboard:** A central place to view everything you've done today. 
- **Workout Logging:** Quickly log the exercises you do (like bench press or squats) along with sets and reps.
- **Water Tracker:** There is a progress bar that shows how much water you've drank today. You can set a custom daily goal, and hitting the "+" button updates your progress instantly using background AJAX requests (no annoying page reloads!).
- **History Page:** A place to look back at past days to see what workouts you did and if you hit your water goals on those days.
- **Easy Edits:** Made a mistake? You can easily delete logged workouts from the dashboard or history.

## Tech Stack 💻
- **Backend:** Python and Django Framework
- **Database:** MySQL
- **Frontend:** HTML, Custom minimalist CSS, Bootstrap 5 (used just for the responsive grid layout)
- **Interactivity:** JavaScript / jQuery for smooth AJAX API calls

## How to Run It Locally 🛠️
If you want to run this project on your own machine, follow these steps:

1. **Install Requirements:** Make sure you have Python installed, then install Django and the MySQL client:
   ```bash
   pip install django mysqlclient
   ```

2. **Setup the Database:**
   You will need to have MySQL or MariaDB running. 
   Create a new database for the project by running:
   ```sql
   CREATE DATABASE gym_tracker;
   ```
   *(Note: By default the code uses the username `root` and password `Sarya_12`. If yours is different, you'll need to update it in `core/settings.py`)*

3. **Run Migrations:**
   Now set up the database tables:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Start the Server!**
   Finally, run the app:
   ```bash
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000/` in your browser and you're good to go!
