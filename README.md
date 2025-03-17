##FastAPI Project## 

Overview
This project is a FastAPI-based application that demonstrates API development, database integration, environment management, and AI-powered image summarization. It uses Docker and Docker Compose for service orchestration, PostgreSQL and Redis for data storage, and OpenAI's GPT-4o for text summarization.


Features

FastAPI setup with Pydantic schemas

Swagger documentation for API exploration

CRUD operations for Students and Topics

Environment variable management using Pydantic Settings

Database integration with PostgreSQL

Redis caching for flexible storage

Image summarization using OpenAI's GPT-4o

Docker Compose for service management



Setup Instructions

Prerequisites

Miniforge (for Python environment management)

Docker & Docker Compose

Git (for version control)

1. Clone the Repository

git clone <your-repository-url>
cd <your-repository>

2. Set Up the Python Environment

conda create -n fastapi_env python=3.11  # Using Miniforge
conda activate fastapi_env

3. Install Dependencies

pip install -r requirements.txt

4. Set Up Environment Variables

Create a .env file and configure it:

DATABASE_URL=postgresql://user:password@db:5432/mydatabase
USE_REDIS=false  # Set to 'true' to use Redis instead of PostgreSQL
REDIS_URL=redis://redis:6379/0
OPENAI_API_KEY=your-openai-api-key

5. Run Services with Docker Compose

docker-compose up --build

6. Access the API

Swagger Docs: http://localhost:8000/docs
