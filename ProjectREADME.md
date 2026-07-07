# D493 Weather Prediction Python Application

## Project Overview

This application fetches past weather data for a specific location and date using the Open-Meteo Weather API.

The project uses weather information from the previous five years to calculate:

- Average temperature
- Minimum temperature
- Maximum temperature
- Average wind speed
- Minimum wind speed
- Maximum wind speed
- Total precipitation
- Minimum precipitation
- Maximum precipitation

The weather statistics are stored in a local SQLite database using SQLAlchemy ORM and then retrieved through a database query.

---

## Event/Location Information

Event Type: Birthday Party

Location: Ybor City, Florida

Latitude: 27.9659

Longitude: -82.4389

Date: February 23

Years Used:
- 2021
- 2022
- 2023
- 2024
- 2025

---

## Required Packages

- requests
- SQLAlchemy

---

## Commands to Run the Program

Run the main application:

```bash
python main.py
```

Run the unit tests:

```bash
python test.py
```

