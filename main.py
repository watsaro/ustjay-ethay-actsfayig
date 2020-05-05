import os

import requests
from flask import Flask, send_file, Response, render_template_string
from bs4 import BeautifulSoup

app = Flask(__name__)

piglatin_url="https://hidden-journey-62459.herokuapp.com/piglatinize/"

def rtn_template(url, fact):
    rtn =  """<a href="{url}" target="_blank">Your Fact in Pig Latin</a> """
    return render_template_string('<p>See the fact<br/>'
                                  '{{fact}}<br/>'
                                  'in Pig Latin<br/><a href="{{url}}" target="_blank">Click Here</a></p>', url = url, fact=fact)

def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    fact = get_fact().strip()
    r = requests.post(piglatin_url, data={'input_text': fact})
    link = rtn_template(r.url, fact)
    return link


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

