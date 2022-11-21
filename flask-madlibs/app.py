from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)


@app.route('/')
def ask_questions():
    """Generate and show form for story"""
    prompts = story.prompts
    return render_template("questions.html", prompts=prompts)


@app.route('/story')
def show_story():
    """Shows the story"""

    text = story.generate(request.args)
    return render_template("story.html", text=text)
