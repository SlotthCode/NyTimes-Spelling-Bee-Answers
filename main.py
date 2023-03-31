from flask import Flask
import requests
import json


app = Flask(__name__)


@app.route("/spellingbee")
def spellingbee():
    r = requests.get("https://www.nytimes.com/puzzles/spelling-bee").text

    kek = r.split('window.gameData = ')[1].split('</script></div>')[0]
    lol = json.loads(kek)
    todaydate = lol["today"]["displayDate"]
    answers = lol["today"]["answers"]        
    theletters = lol["today"]["validLetters"]
   
    return "Today Date: " + todaydate + "<br/>" + "<br/>" + "Answers: " + str(answers) + "<br/>" + "<br/>" + "letters: " + str(theletters) + "<br/>" + "<br/>" + "Yesterday Stuff: " + "<br/>" + "<br/>" + "Yeserday Day: " + lol["yesterday"]["displayWeekday"] + "<br/>" +  "<br/>" + "Yeterday Answers: " +  str(lol["yesterday"]["answers"])



app.run("0.0.0.0")
