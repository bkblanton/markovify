from flask import Blueprint, render_template
from app.forms import TextFileForm
from app.markov import Markov

pages = Blueprint('pages', __name__)


@pages.route('/', methods=('GET', 'POST'))
def home():
    form = TextFileForm()
    if form.validate_on_submit():
        file = form.file.data
        markov = Markov.from_lines(line.decode('utf-8', errors='ignore') for line in file.stream.readlines())
        outputs = []
        for _ in range(form.number.data):
            output = ' '.join(markov.generate(n=form.sentences.data))
            outputs.append(output)
        return render_template('home.html', form=form, outputs=outputs)
    return render_template('home.html', form=form)
