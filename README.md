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


