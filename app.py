from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Aula Top de DevSecOps & SRE - Aluno Paulo Marques"

if __name__ == '__main__':
    app.run(debug=True)
