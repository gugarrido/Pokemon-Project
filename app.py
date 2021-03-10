from database.crud import Crud
from poke_api.read_api import GetApi
from flask import Flask, render_template, request, url_for, session
from werkzeug.utils import redirect
import pokebase as pb
import os
import json

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        pokemonname = request.form["pokename"]
        pokemonname = pokemonname.lower()
        if pokemonname:
            db_con = Crud()
            db_con.get_conn('database/poke.db')
            result = db_con.check_existent(pokemonname)

            if result['status'] == 200:
                session['pokeid'] = result['pokemon_id']
                session['pokeheight'] = result['pokemon_height']
                session['pokeweight'] = result['pokemon_weight']
                session['poketype'] = result['pokemon_type'].capitalize()
                return redirect(url_for("pokedex2v", pokename=pokemonname.capitalize()))

            elif result['status'] == 403:
                api = GetApi()
                response = api.get_response(pokemonname)
                session['pokeid'] = response['pokemon_id']
                session['pokeheight'] = response['pokemon_height']
                session['pokeweight'] = response['pokemon_weight']
                session['poketype'] = response['pokemon_types'].capitalize()
                db_con.insert_data(pokemonname, response['pokemon_id'], response['pokemon_height'], response['pokemon_weight'], response['pokemon_types'])
                return redirect(url_for("pokedex2v", pokename=pokemonname.capitalize()))
            
            return "<h1>error<h1>"


            #return redirect(url_for("poke", pokename=pokemonname, pokeid=pokemoninfo.id))
        else: 
            return f"<h1>ERROR: NAME CAN NOT BE EMPTY</h1>" 
    else:    
        return render_template("index.html")

@app.route('/pokedex2v/<pokename>')
def pokedex2v(pokename):
    pokeid = session['pokeid']
    pokeheight = session['pokeheight']
    pokeweight = session['pokeweight']
    poketype = session['poketype']
    return render_template('pokedex_2v.html', pokemonname=pokename, pokemonid=pokeid, 
    pokemonheight=pokeheight, pokemonweight=pokeweight, pokemontype=poketype)

if __name__ == '__main__':
    app.run(debug=True)
