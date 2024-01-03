# Blog

This is a simple personal blog platform created using Django.

## Project Overview

The project includes a basic structure for a blog with the following features:

- Homepage listing all blog posts with titles and short descriptions.
- Detailed view page for each blog post.
- Admin page for adding and deleting blog posts.

## Getting Started

Follow the steps below to set up and run the project:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/pathangufran/Blog.git
   cd blog

2. **Set Up Virtual Environment:**
   - python -m venv venv
   - source venv/bin/activate  # On Unix/Mac
   - venv\Scripts\activate  # On Windows

3  **Install Dependencies:**
  - pip install -r requirements.txt

4  **Run Migrations:**
  - python3 manage.py makemigrations
  - python manage.py migrate

5  **Create Superuser:**
  - python3 manage.py createsuperuser

6 **Run the Development Server:**
  - python3 manage.py runserver


## Dockerization

This project is Dockerized for easy deployment and development. Follow the steps below to set up and run the application using Docker and Docker Compose.

### Prerequisites

- Docker
- Docker Compose

### Steps

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/pathangufran/Blog.git
    cd blog
    ```

2. **Create a Docker Image:**

    Build the Docker image for the Django application.

    ```bash
    docker-compose build
    ```

3. **Run the Application:**

    Start the Docker services defined in the `docker-compose.yml` file.

    ```bash
    docker-compose up
    ```

    The application will be accessible at [http://localhost:8000](http://localhost:8000).

4. **Access the Application:**

    Open your web browser and go to [http://localhost:8000](http://localhost:8000) to access the Django application.