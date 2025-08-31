# Restaurant Management System 🍽️

A Django + PostgreSQL web application for managing a restaurant.

## Features
- Manage **Menu** (CRUD: Create, Read, Update, Delete)
- Manage **Customers**
- Manage **Orders** with order items (quantity, unit price)
- Search by name/category
- Image upload for menu items
- Admin panel

## Tech Stack
- Python 3.12
- Django 5.x
- PostgreSQL
- Bootstrap 5 (Frontend)

## Setup Instructions
```bash
git clone https://github.com/engAhmed-Ragab/restaurant-management.git
cd restaurant-management
python -m venv venv
venv\Scripts\activate   # on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Then open: http://127.0.0.1:8000
