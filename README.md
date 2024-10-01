# PropertyFinder 🏠🔍

[![Django](https://img.shields.io/badge/Django-v4.2.3-green)](https://www.djangoproject.com/)
[![Elasticsearch](https://img.shields.io/badge/Elasticsearch-v8.5.2-blue)](https://www.elastic.co/)
[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)

## Overview

**PropertyFinder** is a powerful and efficient real estate search platform built with Django and Elasticsearch. The platform allows users to quickly search for properties based on location, price, property type, and other features. 

## Features 🚀

- 🔎 Advanced property search using Elasticsearch
- 📍 Filter properties by location, price range, type (apartment, house, etc.)
- 📊 Optimized indexing for fast and scalable searches
- 🌐 User-friendly interface with responsive design
- 🔐 Secure user authentication and role-based access (admin, agent, user)

## Setup 🛠️

### Prerequisites
- Python 3.8+
- Django 4.x
- Elasticsearch 8.x
- PostgreSQL or SQLite

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PropertyFinder.git
   ```
   
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
   
3. Install dependencies:
  ```bash
   pip install -r requirements.txt
   ```

4. Start Elasticsearch (make sure Elasticsearch is running on your machine or server):
  ```bash
   sudo service elasticsearch start
   ```

5. Apply Django migrations:
  ```bash
   python manage.py migrate
   ```

6. Run the development server:
  ```bash
   python manage.py runserver
   ```

## How to Use 💻
Once the server is running, navigate to http://127.0.0.1:8000/ to start exploring available properties. You can filter properties by various criteria such as price, type, and location.

## Example Search Queries
Search by Location: Find properties in a specific city or neighborhood.
Search by Price Range: Filter properties within a certain price range.
Search by Property Type: Choose between apartments, houses, etc.
Contributing 🤝
Contributions are welcome! If you find any bugs or want to add new features, feel free to open an issue or submit a pull request.

## License 📄
This project is licensed under the MIT License - see the LICENSE file for details.

