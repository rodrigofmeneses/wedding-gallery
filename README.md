# Wedding Gallery API

This project is an wedding gallery API built using Python. The API is powered by Django, Postgres as the database, and Swagger for API documentation and testing.

---

## The Problem

You have received a request from a friend to create a gallery for their wedding where their friends can upload their photos, and they want to have a unified gallery with all the friends' photos. They also want the ability to approve photos before making them visible to everyone. Only the friend and their spouse should have the authority to approve new photos. Additionally, users should be able to like photos and add comments to them.

---

## Features

- A gallery with approved photos of an wedding.
- Users are able to like and comment photos.
- Wife and Husband have authority to approve or decline friend's photos.
- Implementing endpoints for searching, creating, editing, and deleting photos.

---

## Installation

### Requirements

- Docker
- Docker Compose

1. Clone this repository:

```bash
git clone https://github.com/your-username/wedding-gallery.git
cd wedding-gallery
```

2. Build the Docker images:

```bash
docker-compose build
```

3. Apply database migrations:

```bash
docker-compose run web python manage.py migrate
```

4. Last but not least, create the married couple credentials

```bash
docker-compose run web python manage.py createsuperuser
```

---

## Usage

To run the API, use the following command:

```bash
docker-compose up
```

After the API is running, you can use the Swagger UI to interact with the endpoints. The API can be accessed at http://localhost:8000/swagger
