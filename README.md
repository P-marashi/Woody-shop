# Woody Shop

Welcome to **Woody Shop**, a robust and scalable web application built using Django REST Framework. This project follows the principles of Clean Architecture, allowing for high maintainability and ease of testing. It is containerized using Docker to facilitate smooth development and deployment in both local and production environments.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technology Stack](#technology-stack)
4. [Prerequisites](#prerequisites)
5. [Installation](#installation)
6. [Contact](#contact)

## Project Overview

**Woody Shop** is a Django-based web application designed for scalability and efficiency. It offers a RESTful API and adheres to Clean Architecture principles, ensuring that business logic is decoupled from external systems. The project supports Docker for seamless development and deployment, and it's configured for both local and production environments.


### Key Directories and Files

- **`config/`**: Contains Django configuration settings, including ASGI and WSGI setups, environment configurations, and middleware configurations (e.g., CORS and JWT).

- **`core/`**: This is where the core of the application resides, structured according to Clean Architecture:
  - **`adapters/`**: Contains Django apps representing the outer layer, interacting with frameworks and I/O operations.
  - **`entities/`**: Defines the core business entities and their logic.
  - **`exception/`**: Custom exceptions for handling domain-specific errors.
  - **`interfaces/`**: Houses the interface layer, including serializers, views, and URLs.
  - **`use_cases/`**: Contains the business use cases, encapsulating application-specific logic.

- **`docker/`**: Docker-related files, including Dockerfiles and entrypoint scripts for both local and production environments.

- **`requirements/`**: Manages Python dependencies, split into base, local, and production requirements for better environment management.

## Features

- **Clean Architecture**: Separation of concerns into distinct layers, promoting maintainability and testability.
- **Django REST Framework**: Provides a powerful toolkit for building RESTful APIs with Django.
- **Dockerized Environment**: Easy setup and deployment using Docker for consistent development and production environments.
- **JWT Authentication**: Secure authentication mechanism using JSON Web Tokens.
- **Swagger API Documentation**: Auto-generated API documentation for easy exploration and testing of endpoints.

## Technology Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL (customizable via Docker)
- **Containerization**: Docker, Docker Compose
- **Architecture**: Clean Architecture
- **Authentication**: JSON Web Tokens (JWT)
- **API Documentation**: Swagger/OpenAPI

## Prerequisites

Before you can set up and run this project, make sure you have the following tools installed:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)
- **Python 3.10+**: [Install Python](https://www.python.org/downloads/) (only required for local development without Docker)
- **Git**: [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Installation

Follow these steps to get your development environment up and running.

### 1. Clone the project repository:

    ``` shell
    git clone https://git.moallem.sch.ir/pishro/official/api.git
    ```

### 2. Setup virtual environment

    ``` shell
    virtualenv .venv
    source .venv/bin/activate
    ```

### 3. Install dependencies

    - for development:

        ``` shell
        pip install -r requirements_dev.txt
        ```

    - for production:

        ``` shell
        pip install -r requirements.txt 
        ```

### 4. Copy and edit env variables:

    ``` shell
    cp .env.sample .env
    nano .env
    ```


### 5. Build and launch the Docker environment

    - for development:

        ``` shell
        docker compose -f docker-compose.yml up -d --build
        ```

    - for production:

        ``` shell
        docker compose -f docker-compose.pro.yml up -d --build
        ```

### 6. Run project for development stage:

    ``` shell
    python manage.py runserver
    ```

## Contact

For questions, feedback, or contributions, you can reach out to me via:

- **Email**: [pouyamarashii@gmail.com]
- **LinkedIn**: [www.linkedin.com/in/pouyamarashii]