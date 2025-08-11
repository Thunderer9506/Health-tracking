# Health Tracking Script

This is a simple Python-based health tracking tool that connects **Nutritionix API** and **Sheety API** to log your daily exercises.  
It allows you to enter a description of your workout in natural language (e.g., *"I ran 3 km and did 20 push-ups"*), automatically extracts details like exercise name, duration, and calories burned, and saves the data to a Google Sheet for easy record-keeping.

---

## How It Works

1. **User Input**  
   The script prompts you with:  
   ```
   What you have did today?
   ```
   You can type in your exercise activity in plain English.

2. **Nutritionix API**  
   - The entered text is sent to the **Nutritionix Natural Language Exercise API**.
   - Nutritionix processes the text and returns structured details such as:
     - Exercise name
     - Duration (minutes)
     - Calories burned

3. **Validation**  
   - If the API doesn’t detect any exercise, the script tells you:  
     *"No exercises found. Please check your input."*
   - If it does detect exercises, it continues to log them.

4. **Sheety API**  
   - The script formats the data along with the current date and time.
   - This data is then sent to the **Sheety API**, which updates your connected Google Sheet (via a Sheety project link).
   - Your Google Sheet will contain columns for:
     - Date
     - Time
     - Exercise
     - Duration
     - Calories burned

---

## Requirements

- **Python 3.x**
- `requests`  
- `python-dotenv` (for loading environment variables)

---

## Environment Variables

You must set these in a `.env` file:

```
APP_ID=your_nutritionix_app_id
API_KEY=your_nutritionix_api_key
SHEETY_URL=your_sheety_project_path   # without "https://api.sheety.co/"
AUTHORIZATION=Bearer your_sheety_auth_token
```

---

## Example Run

**Input:**
```
What you have did today? I ran for 30 minutes and cycled for 20 minutes
```

**Nutritionix response:**
```json
{
  "exercises": [
    {
      "user_input": "ran",
      "duration_min": 30,
      "nf_calories": 300
    },
    {
      "user_input": "cycled",
      "duration_min": 20,
      "nf_calories": 200
    }
  ]
}
```

**Google Sheet Entry (first detected exercise):**
| Date       | Time     | Exercise | Duration | Calories |
|------------|----------|----------|----------|----------|
| 11/08/2025 | 14:32:10 | ran      | 30       | 300      |

---

## Key Features

- Accepts **natural language** exercise descriptions.
- Uses **Nutritionix** for calorie and duration calculation.
- Automatically **logs to Google Sheets** via Sheety.
- Lightweight and runs in a terminal.
