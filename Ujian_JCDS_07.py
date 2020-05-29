from flask import Flask, render_template, request
import json
import joblib
import pandas as pd
import numpy as np
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('cari_pokemon.html')

@app.route('/hasil', methods=['GET', 'POST'])
def hasil():
    if request.method == 'POST':
        data = request.form
        input_ = (data['pokemon_name']).capitalize()
        poke = df[df['Name']==input_].index[0] 
        similarPoke= list(enumerate(model[poke]))
        similarPoke = sorted(similarPoke, key = lambda i: i[1], reverse=True)

        index_ = []
        for i in similarPoke[:10]:
            index_.append(i[0])
        for i in index_[:10]:
            if i == poke:
                index_.insert(0,i)

        Poke = df.iloc[index_].reset_index()
        Poke = Poke.drop_duplicates(subset='Name')

        Name1 = Poke['Name'].iloc[0]
        Name2 = Poke['Name'].iloc[1]
        Name3 = Poke['Name'].iloc[2]
        Name4 = Poke['Name'].iloc[3]
        Name5 = Poke['Name'].iloc[4]
        Name6 = Poke['Name'].iloc[5]
        Name7 = Poke['Name'].iloc[6]

        Type1 = Poke['Type 1'].iloc[0]
        Type2 = Poke['Type 1'].iloc[1]
        Type3 = Poke['Type 1'].iloc[2]
        Type4 = Poke['Type 1'].iloc[3]
        Type5 = Poke['Type 1'].iloc[4]
        Type6 = Poke['Type 1'].iloc[5]
        Type7 = Poke['Type 1'].iloc[6]       

        Gen1 = Poke['Generation'].iloc[0]
        Gen2 = Poke['Generation'].iloc[1]
        Gen3 = Poke['Generation'].iloc[2]
        Gen4 = Poke['Generation'].iloc[3]
        Gen5 = Poke['Generation'].iloc[4]
        Gen6 = Poke['Generation'].iloc[5]
        Gen7 = Poke['Generation'].iloc[6]

        Leg1 = Poke['Legendary'].iloc[0]
        Leg2 = Poke['Legendary'].iloc[1]
        Leg3 = Poke['Legendary'].iloc[2]
        Leg4 = Poke['Legendary'].iloc[3]
        Leg5 = Poke['Legendary'].iloc[4]
        Leg6 = Poke['Legendary'].iloc[5]
        Leg7 = Poke['Legendary'].iloc[6]

        pokemonCari = Name1.lower()
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemonCari}'
        data = requests.get(url)
        pokemon = data.json()
        image1 = pokemon['sprites']['front_default']

        pokemonCari = Name2.lower()
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemonCari}'
        data = requests.get(url)
        pokemon = data.json()
        image2 = pokemon['sprites']['front_default']

        pokemonCari = Name3.lower()
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemonCari}'
        data = requests.get(url)
        pokemon = data.json()
        image3 = pokemon['sprites']['front_default']

        pokemonCari = Name4.lower()
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemonCari}'
        data = requests.get(url)
        pokemon = data.json()
        image4 = pokemon['sprites']['front_default']

        # pokemonCari = Name5.lower()
        # url = f'https://pokeapi.co/api/v2/pokemon/{pokemonCari}'
        # data = requests.get(url)
        # pokemon = data.json()
        # image5 = pokemon['sprites']['front_default']

        # pokemonCari = Name6.lower()
        # url = f'https://pokeapi.co/api/v2/pokemon/{pokemonCari}'
        # data = requests.get(url)
        # pokemon = data.json()
        # image6 = pokemon['sprites']['front_default']

        # pokemonCari = Name7.lower()
        # url = f'https://pokeapi.co/api/v2/pokemon/{pokemonCari}'
        # data = requests.get(url)
        # pokemon = data.json()
        # image7 = pokemon['sprites']['front_default']


        return render_template('hasil_rekomend.html',Name1=Name1,Name2=Name2,Name3=Name3,Name4=Name4,Name5=Name5,Name6=Name6,Name7=Name7,
                Type1=Type1,Type2=Type2,Type3=Type3,Type4=Type4,Type5=Type5,Type6=Type6,Type7=Type7,
                Gen1=Gen1,Gen2=Gen2,Gen3=Gen3,Gen4=Gen4,Gen5=Gen5,Gen6=Gen6,Gen7=Gen7,
                Leg1=Leg1,Leg2=Leg2,Leg3=Leg3,Leg4=Leg4,Leg5=Leg5,Leg6=Leg6,Leg7=Leg7,
                image1=image1,image2=image2,image3=image3,image4=image4)#,image5=image5,image6=image6,image7=image7)

if __name__ == '__main__':
    model = joblib.load('model_poke')
    df = pd.read_csv('pokemon.csv')
    df['Legendary'] = df['Legendary'].map({False:'Not Legend',True:'Legend'})
    df['tipe'] = df.apply(lambda i: str(i['Type 1'])+ ' '+ str(i['Generation'])+ ' '+ str(i['Legendary']), axis=1)
    app.run(debug = True)
