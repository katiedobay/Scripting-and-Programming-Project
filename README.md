# Weather Prediction Python Application

## Overview

This project is a Python-based weather analysis application that retrieves historical weather data from the Open-Meteo API, calculates weather statistics, stores the results in a SQLite database using SQLAlchemy ORM, and retrieves the stored records through database queries.

The application was developed as part of a software development and data analytics project focused on API integration, object-oriented programming, database management, and automated testing.

---

## Features

- Retrieves historical weather data using the Open-Meteo API
- Processes weather information from multiple years
- Calculates:
  - Average temperature
  - Minimum temperature
  - Maximum temperature
  - Average wind speed
  - Minimum wind speed
  - Maximum wind speed
  - Total precipitation
  - Minimum precipitation
  - Maximum precipitation
- Stores weather statistics in a SQLite database
- Uses SQLAlchemy ORM for database management
- Queries and displays stored weather records
- Includes automated unit tests

---

## Technologies Used

- Python
- SQLite
- SQLAlchemy
- Open-Meteo API
- Requests
- PyCharm
- Git
- GitHub

---

## Project Structure

```text
├── weather_data.py      # Weather data model and API methods
├── database.py          # SQLite database and SQLAlchemy ORM
├── main.py              # Main application entry point
├── test.py              # Unit tests
├── requirements.txt     # Project dependencies
├── README.md
└── identifier.sqlite    # SQLite database file
```

---

## Example Workflow

```text
Open-Meteo API
        │
        ▼
WeatherData Class
        │
        ▼
Data Processing
        │
        ▼
SQLite Database
        │
        ▼
Database Query
        │
        ▼
Formatted Output
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Navigate to the project folder:

```bash
cd YOUR_REPOSITORY
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Execute the main program:

```bash
python main.py
```

The application will:

1. Retrieve weather data from the Open-Meteo API
2. Calculate weather statistics
3. Store the results in SQLite
4. Query the database
5. Display the stored weather information

---

## Running Tests

Execute the unit tests:

```bash
python test.py
```

---

## Sample Output

```text
WEATHER RECORD

Latitude: 27.9659
Longitude: -82.4389
Month: 2
Day: 23
Year: 2025

Temperature Statistics
Average Temperature: 68.00
Minimum Temperature: 61.80
Maximum Temperature: 74.90

Wind Statistics
Average Wind Speed: 11.37
Minimum Wind Speed: 6.53
Maximum Wind Speed: 16.22

Precipitation Statistics
Total Precipitation: 0.63
Minimum Precipitation: 0.00
Maximum Precipitation: 0.53
```

---

## Learning Outcomes

This project demonstrates experience with:

- Object-Oriented Programming (OOP)
- REST API integration
- Data processing and aggregation
- SQLite database design
- SQLAlchemy ORM
- Unit testing with Python
- Git version control
- Software development lifecycle practices

---

## Author

**Kaitlin Dobay**

Western Governors University  
Data Analytics Student
