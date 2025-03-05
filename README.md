# Audiobase

**Audiobase** is a Django-based web application designed for managing a music archive. It allows users to store, search, and retrieve information about artists, albums, and songs using an integrated SQLite database.

## System Requirements

- Python 3.7 or later
- Django 4.1.1 or later
- SQLite

## Installation and Setup

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/audiobase.git
cd audiobase
```

### 2. Create a virtual environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Apply database migrations

```sh
python manage.py migrate
```

### 5. Create a superuser (optional, for admin access)

```sh
python manage.py createsuperuser
```

### 6. Run the development server

```sh
python manage.py runserver
```

The application will be available at **http://127.0.0.1:8000/**.

## Features

- **Artist Management**: Add, edit, and delete artists.
- **Album Management**: Store album details, including genre and release year.
- **Song Management**: Keep track of song length, streams, and associated albums.
- **Search Functionality**: Query artists and albums based on various filters.
- **Admin Panel**: Manage the database through Django's built-in admin interface.

## Project Structure

```
audiobase/
│── Audiobase/               # Django app for managing music data
│   ├── models.py            # Database models (Artist, Album, Song)
│   ├── views.py             # Handles HTTP requests and renders pages
│   ├── urls.py              # Defines URL routing for the app
│   ├── admin.py             # Configuration for Django admin panel
│   ├── templates/           # HTML templates for the frontend
│   ├── static/              # CSS, JavaScript, and images
│── Project/                 # Django project settings
│   ├── settings.py          # Main configuration file
│   ├── urls.py              # Root URL configuration
│   ├── wsgi.py              # WSGI entry point
│── db.sqlite3               # SQLite database file
│── manage.py                # Django management script
```

## Database Models

### `Artist`
- **id**: Primary key
- **name**: Full name of the artist
- **stage_name**: Public name of the artist
- **birth**: Date of birth
- **age**: Calculated field based on birthdate
- **gold_records**: Number of gold-certified albums
- **platinum_records**: Number of platinum-certified albums
- **nationality**: Artist's country of origin
- **artist_image**: Profile picture

### `Album`
- **id**: Primary key
- **artist**: Foreign key to `Artist`
- **name**: Album title
- **release_year**: Year of release
- **genre**: Music genre
- **gold_certified**: Boolean field for gold certification
- **platinum_certified**: Boolean field for platinum certification
- **cover_image**: Album cover

### `Song`
- **id**: Primary key
- **album**: Foreign key to `Album`
- **name**: Song title
- **artist_name**: Retrieved from the associated album
- **release_year**: Retrieved from the associated album
- **length**: Song duration (seconds)
- **spotify_streams**: Stream count in thousands

## URL Routes

| Endpoint | Description |
|----------|-------------|
| `/` | Home page |
| `/admin/` | Django admin panel |
| `/ab/artists/<id>` | Artist biography page |
| `/ab/albums/<id>` | Album details page |
| `/ab/vote_album` | User voting for best albums |
| `/ab/results` | Display album ranking results |
