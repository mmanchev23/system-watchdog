# System Watch Dog

## Local Deployment Guide

Follow these steps to set up and run the Monitoring REST API locally.

### Prerequisites

Before proceeding, make sure you have the following:

- Docker
- Docker Compose
- `.env` file with the necessary configuration values (see below)

### Configuration

Create a `.env` file in the project root with the following content, replacing the placeholders with your actual credentials:

```plaintext
MYSQL_HOST=db
DATABASE_PORT=3306
MYSQL_DATABASE=metrics
MYSQL_HOSTNAME=localhost

MYSQL_USER=<your-mysql-user>
MYSQL_PASSWORD=<your-mysql-password>
MYSQL_ROOT_PASSWORD=<your-mysql-root-password>
```

### Running the Application

Execute the following command to launch the application using the preconfigured script:

```bash
./start.sh
```

### Populating the Database

To populate the database with data, you have two options:

1. Run the `data.py` script located in the `server` directory.
2. Use the dedicated UI button, highlighted with a yellow color and featuring a database icon, situated on every host detail page, for seamless data population.

### Accessing the Applications

Once the application is up and running, you can access the following components through your web browser:

- **Client Application:** [http://localhost:5173/](http://localhost:5173/)
- **Server Application:** [http://localhost:8000/](http://0.0.0.0:8000/)
- **Database Application:** [http://localhost:8080/](http://localhost:8080/)

### Troubleshooting

If you encounter any issues with the services, you can attempt to resolve them by rerunning the preconfigured script:

```bash
./start.sh
```

For persistent issues, particularly those related to the database service, consider updating the connection string in the `database.py` file located in the `server/api` directory:

```python
MYSQL_URL = f"mysql+mysqlconnector://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}@db:{settings.DATABASE_PORT}/{settings.MYSQL_DATABASE}"
```

Maintain this configuration to ensure optimal functionality of the Monitoring REST API.
