from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"name: {self.name} description: {self.description}"


@app.route('/')
def index():
    return "hello"


@app.route("/drinks")
def get_drinks():
    drinks = Drink.query.all()
    result = []
    for drink in drinks:
        data = {"name": drink.name, "drink": drink.description}
        result.append(data)
    return {"drinks": result}


@app.route("/drinks/<id>")
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name": drink.name, "description": drink.description}


@app.route("/drinks", methods=["POST"])
def add_drink():
    print(request.json)
    drink = Drink(name=request.json["name"], description=request.json["description"])
    db.session.add(drink)
    db.session.commit()
    return {"id": drink.id, "name": drink.name, "description": drink.description}


@app.route("/drinks/<id>", methods=["DELETE"])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error": "No such drink"}
    db.session.delete(drink)
    db.session.commit()
    return {"message": "success"}
