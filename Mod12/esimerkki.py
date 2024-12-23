import flask, requests

app = flask.Flask(__name__)
@app.route('/')
def hello():
    return 'Terveppä terve, serveri tervehtii teitä!!!'

#http://127.0.0.1:3000/summa?luku1=13&luku2=28
# Tämä on päätepiste eli route
@app.route('/summa')
def summa():
    args = flask.request.args
    luku1 = float(args.get("luku1"))
    luku2 = float(args.get("luku2"))
    summa = luku1+luku2
    #return str(summa)
    #return 'Summa tervehtii teitä!'
    vastaus = {
            "luku1" : luku1,
            "luku2" : luku2,
            "summa" : summa
        }
    return vastaus

@app.route('/kaiku/<teksti>')
def kaiku(teksti):

    vastaus = {
        "kaiku" : teksti + " " + teksti
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)