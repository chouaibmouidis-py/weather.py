# Weather App - Python ☀️☁️

A Python application that fetches real-time weather data from the OpenWeatherMap API.

## 🚀 Features
- **Real-time Data**: Retrieves current weather conditions for any city worldwide.
- **API Integration**: Uses the `requests` library to communicate with the OpenWeatherMap REST API.
- **Security**: Implements environment variables (`.env`) to securely manage API keys.
- **Error Handling**: Includes robust exception handling for network requests and invalid city names.

## 🛠️ Technical Implementation
- **OOP Approach**: Encapsulates the weather logic within a `WeatherApp` class.
- **Environment Management**: Integration with `python-dotenv` for secure credential management.
- **Data Parsing**: Processes JSON responses to extract specific weather metrics (Temperature, Condition).

## 📖 How to Run
1. Clone the repository.
2. Create a `.env` file in the root directory and add your API key:
   `API_KEY=your_api_key_here`
3. Install dependencies: `pip install requests python-dotenv`.
4. Run the script: `python weather.py`.

---
*Developed as part of a Python Certification journey.*
