from flask import Flask, request, jsonify
import util

app = Flask(__name__)

# for checking the article names
@app.route('/get_article_names')
def get_article_names():
    response = jsonify({
        'articles': util.get_article_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# for checking the finish names
@app.route('/get_finish_names')
def get_finish_names():
    response = jsonify({
        'finishes': util.get_finish_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# for checking the print names
@app.route('/get_prints_names')
def get_prints_names():
    response = jsonify({
        'prints': util.get_prints_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_color_consum', methods=['POST'])
def predict_color_consum():
    cover = int(request.form['cover'])
    meters = int(request.form['meters'])
    mesh = int(request.form['mesh'])
    rod = int(request.form['rod'])
    speed = int(request.form['speed'])
    hits = int(request.form['hits'])
    c_hits = int(request.form['c_hits'])
    machine = int(request.form['machine'])
    viscosity = int(request.form['viscosity'])
    article = request.form['article']
    finish = request.form['finish']
    prints = request.form['prints']
    response = jsonify({
        'estimated_consum': util.get_estimated_consum(article,finish,prints,cover,meters,mesh,rod,speed,hits,c_hits,viscosity,machine)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    util.load_saved_artifacts()
    print("starting the ccp server...")
    app.run()
