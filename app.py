from flask import Flask, render_template
from offers import Offers

app = Flask(__name__)

offers = Offers("https://www.ica.se/erbjudanden/ica-supermarket-luthagens-livs-1004458/")

@app.route("/")
def render_offers():
    offers.get_latest()
    return render_template('offer_table.html', table=offers.to_html())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5681)

