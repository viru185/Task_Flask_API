# Task FastAPI

A simple web-based task management API built with FastAPI. This project demonstrates the basics of RESTful API development, data validation, and CRUD operations using FastAPI and Pydantic.

## Purpose

The purpose of this project is to:

- Learn how to build a REST API using FastAPI.
- Practice data modeling and validation with Pydantic.
- Understand CRUD (Create, Read, Update, Delete) operations.
- Explore API endpoint design and error handling.
- Gain experience with project structure and deployment.
- Share knowledge and code with the open source community.

## Features

- Create new tasks
- Read all tasks or a specific task
- Update existing tasks
- Delete tasks
- Data validation with Pydantic models

## Technologies Used

- Python 3.11+
- FastAPI
- Pydantic
- Uvicorn

## Installation

> ⚡ **Prerequisite:**  
> Make sure you have [uv](https://github.com/astral-sh/uv) installed:  
> ```bash
> pip install uv
> ```

1. **Clone the repository**
   ```bash
   git clone https://github.com/viru185/Task_Flask_API.git
   cd Task_Flask_API
   ```

2. **Set up the environment and install dependencies**
   ```bash
   uv sync
   ```

3. **Run the application**
   ```bash
   uv run main.py
   ```
   - Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the interactive API documentation.

## Usage

- Use the `/task/` endpoint to create a new task (POST).
- Use the `/tasks/` endpoint to list all tasks (GET).
- Use the `/tasks/{task_id}` endpoint to get, update, or delete a specific task (GET, PUT, DELETE).

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.  
It is open source and available for anyone to use, modify, and distribute.
