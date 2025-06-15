
Superheroes API Project 🦸
GitHub Repo Name: superhero-flask-api
(Simple and descriptive - shows it's a Flask API about superheroes)

About This Project
This is my Flask API project for tracking superheroes and their powers. It was built for my coding bootcamp phase 4 challenge.

What It Does:
Stores superhero data (name, hero name)

Stores superpowers (name, description)

Connects heroes to their powers

Has validation to make sure data is correct

How To Set It Up
Clone the repo
git clone [your-repo-link]
cd superhero-flask-api

Install requirements
pip install -r requirements.txt

Set up the database

text
flask db init
flask db migrate -m "initial tables"
flask db upgrade
python seed.py
Run the server
python app.py

The API will run at http://127.0.0.1:5000

API Endpoints
Heroes:

GET /heroes - Get all heroes

GET /heroes/<id> - Get one hero with their powers

Powers:

GET /powers - Get all powers

GET /powers/<id> - Get one power

PATCH /powers/<id> - Update a power's description

HeroPowers:

POST /hero_powers - Connect a hero to a power

What I Learned
How to set up Flask models with relationships

Adding validation to models

Creating RESTful routes

Using Flask-Migrate for databases

Structuring a Flask project properly

Challenges I Faced
Getting the many-to-many relationship working between heroes and powers

Making sure validations worked correctly

Formatting the JSON responses properly

Setting up the seed file correctly

Possible Improvements
Add authentication

Allow deleting heroes/powers

Add more hero information (like comics they appear in)

Better error messages

Has a more "student project" feel

Keeps the technical details but presents them in a beginner-friendly way
