# ETL-to-fastAPI-dashboard

Pipeline downloads the data from their DWH telegram bot, enriches it with countries, aggregates it and uploads it to the database for analytics.

FastAPI is needed for easy access to data via the API. 

Pipeline also does VACUUM once a week. At this time, upon a post request, it notifies the api service, which switches to maintenance mode. X-API-KEY authorization

## Technologies used

- **python**
- **fastapi**
- **airflow**
- **sql**
- **postgre**
- **docker compose**
- **poetry**
