# System Watchdog - Local Deployment Guide

Welcome to the System Watchdog Local Deployment Guide. This guide will walk you through the setup process for running System Watchdog on your local machine.

## Prerequisites

Before you get started, ensure that you have the following prerequisites installed:

- Docker
- Docker Compose
- A `.env` file with the necessary configuration values (see below)

## Configuration

1. **Create `.env` File:** Begin by creating a `.env` file in the project's root directory. This file will contain important configuration details. Replace the placeholders with your actual credentials.

   ```plaintext
   MYSQL_HOST=db
   DATABASE_PORT=3306
   MYSQL_DATABASE=metrics
   MYSQL_HOSTNAME=localhost

   MYSQL_USER=<your-mysql-user>
   MYSQL_PASSWORD=<your-mysql-password>
   MYSQL_ROOT_PASSWORD=<your-mysql-root-password>
   ```

## Running the Application

To launch the System Watchdog application, execute the following command in your terminal:

```bash
./start.sh
```

## Populating the Database

You have two methods to populate the database with data:

1. **Using the Script:** Navigate to the `server` directory and run the `data.py` script.

2. **Using the UI:** On every host detail page, you'll find a dedicated UI button highlighted in yellow, featuring a database icon. Click this button to seamlessly populate the database with data.

## Accessing the Applications

Once the application is up and running, you can access the following components through your web browser:

- **Client Application:** [http://localhost:5173/](http://localhost:5173/)
- **Server Application:** [http://localhost:8000/](http://0.0.0.0:8000/)
- **Database Application:** [http://localhost:8080/](http://localhost:8080/)

## Troubleshooting

Encountering issues with the services? Here's how to resolve them:

- Try rerunning the preconfigured script:

  ```bash
  ./start.sh
  ```

- For persistent issues, especially those related to the database service, consider updating the connection string in the `database.py` file located in the `server/api` directory. Find the following code snippet:

  ```python
  MYSQL_URL = f"mysql+mysqlconnector://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}@db:{settings.DATABASE_PORT}/{settings.MYSQL_DATABASE}"
  ```

  Maintain this configuration to ensure optimal functionality of the Monitoring REST API.
