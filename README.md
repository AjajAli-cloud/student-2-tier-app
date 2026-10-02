# Student Management System - 2-Tier Docker Application

A beginner-friendly 2-Tier Student Management Application built with Python Flask and PostgreSQL, containerized using Docker and Docker Compose.

## Architecture

```text
User / Browser
      |
      | HTTP :5000
      v
+----------------------+
| Flask App Container  |
| Python + Flask       |
+----------+-----------+
           |
           | Docker Network
           | db:5432
           v
+----------------------+
| PostgreSQL Container |
| PostgreSQL 17        |
+----------+-----------+
           |
           v
     Named Volume
   postgres-data
```

The Flask application is the application tier and PostgreSQL is the database tier.

## Technologies Used

- Python 3.12
- Flask
- PostgreSQL 17
- Docker
- Docker Compose
- Git
- GitHub

## Features

- Add student
- View students
- Delete students
- Student fields: ID, Name, Email, Department, Course
- PostgreSQL persistence with a Docker named volume
- Container-to-container communication over a Docker network
- Environment-based database configuration

## Project Structure

```text
student-2-tier-app/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
├── database/
│   └── init.sql
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

## Docker Setup

The project has two services:

1. `app` - Flask application
2. `db` - PostgreSQL database

Docker Compose creates a private bridge network named for the project. The Flask container connects to PostgreSQL using the Compose service name `db`, not `localhost`.

PostgreSQL uses the named volume `postgres-data` for persistent data.

PostgreSQL is not published to the host. Only Flask port `5000` is published.

## Environment Variables

Create a local `.env` file from the example:

```bash
cp .env.example .env
```

Example:

```env
POSTGRES_USER=student_user
POSTGRES_PASSWORD=change_this_password
POSTGRES_DB=student_db
```

Do not commit `.env` when it contains real credentials.

## Run the Project

### 1. Validate Compose configuration

```bash
docker compose config
```

### 2. Build and start

```bash
docker compose up -d --build
```

### 3. Check containers

```bash
docker ps
```

Expected services:

- `student-app`
- `student-db`

### 4. Check logs

```bash
docker compose logs
```

Application logs:

```bash
docker compose logs app
```

Database logs:

```bash
docker compose logs db
```

### 5. Open the application

Open:

```text
http://localhost:5000
```

Add a student and verify that the record appears in the table.

### 6. Stop the application

```bash
docker compose down
```

To also delete the PostgreSQL volume and its data:

```bash
docker compose down -v
```

Use `down -v` only when you intentionally want to remove the stored database data.

## Useful Docker Commands

```bash
docker ps
docker ps -a
docker images
docker compose ps
docker compose logs
docker volume ls
docker network ls
```

## Git and GitHub

Initialize Git:

```bash
git init
```

Check status:

```bash
git status
```

Add project files:

```bash
git add .
```

Create the first commit:

```bash
git commit -m "Add Docker 2-tier student management application"
```

Rename the branch:

```bash
git branch -M main
```

Create an empty GitHub repository, for example:

```text
student-2-tier-app
```

Then connect it:

```bash
git remote add origin <GITHUB_REPOSITORY_URL>
```

Push:

```bash
git push -u origin main
```

Verify the remote:

```bash
git remote -v
```

## API / Application Routes

| Method | Route | Purpose |
|---|---|---|
| GET | `/` | View all students |
| POST | `/students` | Add a student |
| POST | `/students/<id>/delete` | Delete a student |

## Security Notes

- Database credentials are supplied through environment variables.
- `.env` is ignored by Git.
- PostgreSQL is not exposed directly on the host.
- SQL queries use parameters rather than string concatenation.

## Future Improvements

- Student update/edit feature
- REST API with JSON responses
- Authentication and authorization
- Search and filtering
- Frontend improvements
- Nginx reverse proxy
- CI/CD with GitHub Actions
- Docker Hub image publishing
- AWS EC2 deployment
- Kubernetes deployment
- Monitoring and centralized logging

## Learning Outcomes

This project demonstrates practical understanding of:

- Dockerfile
- Docker images
- Docker containers
- Docker Compose
- Docker networking
- Docker volumes
- PostgreSQL with Docker
- Environment variables
- Container-to-container communication
- Git and GitHub
- Basic Cloud/DevOps project workflow

## Author

Ajaj Ali

BTech CSE | Cloud & DevOps Learner
