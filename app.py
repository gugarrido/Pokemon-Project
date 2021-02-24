from flask import Flask, render_template, request, url_for
import pokebase as pb
from werkzeug.utils import redirect
app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        pokemonname = request.form["pokename"]
        pokemonname = pokemonname.lower()
        if pokemonname:
            # pokemoninfo = pb.pokemon(pokemonname)
            # pokemonid = pokemoninfo.id
            return redirect(url_for("poke", pokename=pokemonname, pokeid=pokemoninfo.id))
        else: 
            return f"<h1>ERROR: NAME CAN NOT BE EMPTY</h1>" 
    else:    
        return render_template("index.html")

# @app.route('/<pokename>/<pokeid>')
# def poke(pokename, pokeid):
#     pokeimage = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokeid}.png'
#     return f"<img src={pokeimage}><br> <h1>{pokename}</h1>"


@app.route('/pokedex')
def pokedex():
    return render_template('pokedex.html')

if __name__ == '__main__':
    app.run(debug=True)
