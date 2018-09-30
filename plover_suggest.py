import re
import subprocess

from plover.engine import StenoEngine
from plover.formatting import RetroFormatter

WORD_RX = re.compile(r'(?:\w+|[^\w\s]+)\s*')

def suggest(engine, stuff):
    last_translations = engine.translator_state.translations
    retro_formatter = RetroFormatter(last_translations)
    split_words = retro_formatter.last_words(1, rx=WORD_RX)
    if len(split_words) == 0:
        return
    word = split_words[0]
    suggestions = engine.get_suggestions(word)
    title = 'Suggestions for "' + word + '"'
    if len(suggestions) == 0:
        subprocess.Popen(['notify-send', title, '(no suggestions available)'])
    
    sug_strings = [(s.text + ': ' + ', '.join(['/'.join(l) for l in s.steno_list])) for s in suggestions]
    subprocess.Popen(['notify-send', title, '--', '\n'.join(sug_strings)])
