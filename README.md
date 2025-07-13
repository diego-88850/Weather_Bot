# Weatherbot

A personalized weather forecasting bot that sends AI-generated weather updates to your email with customizable personality and scheduling.

## Features

- **Personalized Forecasts**: AI-generated weather commentary with customizable personality (goofy, cheerful, professional, etc.)
- **Flexible Scheduling**: Daily or weekly email delivery at your preferred time
- **Easy Setup**: Simple Streamlit web interface for configuration
- **City Selection**: Get weather for any city worldwide
- **Logging**: Built-in logging system to track operations
- **Docker Ready**: Fully configured and tested in Docker for consistent deployment

## Quick Start

### Option 1: Docker (Recommended)
Fully configured and tested in Docker for consistent deployment across environments.

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/weatherbot.git
   cd weatherbot
   ```

2. **Set up environment variables**
   Create a `.env` file with:
   ```
   WEATHER_API_KEY=your_weather_api_key
   BASE_URL=https://api.weatherapi.com/v1/current.json
   GEMINI_API_KEY=your_gemini_api_key
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASS=your_app_password
   ```

3. **Build and run with Docker**
   ```bash
   docker-compose up --build
   ```

   Or build manually:
   ```bash
   docker build -t weatherbot .
   docker run -p 8501:8501 --env-file .env weatherbot
   ```

4. **Access the configuration interface**
   Visit `http://localhost:8501` in your browser

### Option 2: Local Installation

1. **Clone and install dependencies**
   ```bash
   git clone https://github.com/yourusername/weatherbot.git
   cd weatherbot
   pip install -r requirements.txt
   ```

2. **Set up environment variables** (same as above)

3. **Run the configuration interface**
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Start the scheduler**
   ```bash
   python main.py
   ```

## Configuration

Use the Streamlit interface to set:
- **City**: Any city for weather updates
- **Schedule**: Daily or weekly delivery
- **Time**: Preferred email time
- **Personality**: Custom personality for your weather forecasts
- **Email**: Your email address

## API Requirements

- **Weather API**: [WeatherAPI.com](https://www.weatherapi.com/) (free tier available)
- **Gemini API**: [Google AI Studio](https://aistudio.google.com/) for AI-generated commentary
- **Email**: Gmail account with app password enabled

## Project Structure

```
weatherbot/
├── main.py              # Main scheduler runner
├── streamlit_app.py     # Web configuration interface
├── weather.py           # Weather API integration
├── genai_weatherman.py  # AI commentary generation
├── emailer.py           # Email sending functionality
├── scheduler.py         # Job scheduling
├── preferences.py       # User preferences storage
├── daily_email.py       # Email composition
├── logger.py            # Logging system
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose setup
├── requirements.txt     # Python dependencies
└── data/                # SQLite databases
```

## Docker Configuration

The project includes a complete Docker setup with:
- **Multi-stage build** for optimized image size
- **Volume mounting** for persistent data storage
- **Environment variable** integration
- **Port mapping** for Streamlit interface (8501)
- **Tested deployment** across different environments

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details