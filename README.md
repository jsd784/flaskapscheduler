# 🕒 Flask APScheduler Demo

This project demonstrates how to use **Flask** with **APScheduler** to schedule and persist one-time jobs using an SQLite database. It includes timezone support and dynamically generates jobs across months.

---

## 🚀 Features

- 📅 Schedule one-time jobs using `date` trigger
- 🌍 Timezone support (`Europe/Amsterdam` used)
- 💾 Job persistence using SQLite via `SQLAlchemyJobStore`
- 🧼 Removes existing jobs before adding new ones
- 🛠️ Easily configurable to run jobs hourly, daily, or monthly

---

## 📁 Project Structure

```bash
.
├── app.py                  # Main Flask app with scheduler
└── data/
    └── apscheduler.db      # SQLite database (auto-created)
````

---

## ⚙️ Setup Instructions

### 1. Install dependencies

```bash
pip install Flask APScheduler tzlocal SQLAlchemy
```

### 2. Run the App

```bash
python app.py
```

The Flask server starts on `localhost:5000`, and scheduled jobs begin running in the background.

---

## 🔧 How It Works

* The app schedules jobs:

  * One test job 7 hours and 5 minutes from startup
  * Monthly jobs starting next month until the end of next year
* Each job prints a message and a timestamp
* Job data is persisted in `sqlite:///data/apscheduler.db`
* Timezone is set to `"Europe/Amsterdam"` via `apscheduler.timezone`

---

## 💡 Sample Output

```bash
printing test txt at 2025-05-17 14:05:00.123456
printing test txt at 2025-06-01 00:00:00.000000
printing test txt at 2025-07-01 00:00:00.000000
...
```

---

## 📌 Notes

* Timezone is detected using `tzlocal` but can be manually overridden
* You can modify `text`, timing logic, and database location as needed
* This is a great starting point for building time-based task runners (e.g., email digests, report generation)

---

## 📜 License

MIT License
