from flask import Blueprint, render_template
from app.forms import TextFileForm
from app.markov import Markov
import re

pages = Blueprint('pages', __name__)

line_re = re.compile(r'(.*)(?:\r?\n|$)')


@pages.route('/', methods=('GET', 'POST'))
def home():
    form = TextFileForm()
    if form.validate_on_submit():
        # file = form.file.data
        text = form.text.data
        # markov = Markov.from_lines(match.group(1) for match in line_re.finditer(text))
        markov = Markov.from_string(text)
        outputs = []
        for _ in range(form.number.data):
            output = ' '.join(markov.generate(n=form.sentences.data))
            outputs.append(output)
        return render_template('home.html', form=form, outputs=outputs)
    return render_template('home.html', form=form)
