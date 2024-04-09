from flask import Flask
import json
import requests

app = Flask(__name__)

@app.get("/<string:sted>")
def rute_index(sted):
    res = requests.get("https://wttr.in/{sted}?format=j1")
    data = res.json()
    akkurat_nå = data["current_condition"][0]["weatherDesc"][0]["value"]
    temp_nå = data["current_condition"][0]["temp_C"]
    print(temp_nå, "TEMPPPP")
    return f"""
        <h1>{akkurat_nå}</h1>
        <form method="get">
            <input name="sted">
            <button type="submit">søk</button>
        </form>
        <h2>{sted}</h2>
        <h2>{akkurat_nå} - {temp_nå} </h2>
    """

app.run(port=5000, debug=True)