
import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


with open('lore.yaml', 'r') as fp:
    lore = yaml.load(fp, Loader=Loader)

prefix = 'waldmo_'

class Journal:
    def __init__(self, day, parts):
        self.day = day
        self.parts = parts
        self.parts[0] = self.add_day(parts[0])

    def add_day(self, part):
        if part[0] == '[':
            ps = part.split('\n')
            ps[1] = f'Day {self.day}: {ps[1]}'
            return '\n'.join(ps)
        return f'Day {self.day}: {part}'

    def make_dialog(self):
        result = []
        for idx, part in enumerate(self.parts):
            letter = ''
            if idx != 0:
                letter = chr(0x61+idx)
            entry = f'{prefix}Day{self.day}{letter}=\n{part}'
            result.append(entry)

        return '\n'.join(result)

dialog_parts = []

dialog_parts.append('# Journals\n\n')
for day, parts in lore['journals'].items():
    journal = Journal(day, parts)
    dialog_parts.append(journal.make_dialog())

with open('English.txt', 'r') as fp:
    raw = fp.read()

magic = '## WALDMO_AUTO ##'
idx = raw.find(magic)
if idx == -1:
    raise RuntimeError(f"Couldn't find {magic} in english.txt")

raw = raw[:idx+len(magic)]
raw += '\n\n'

raw += '\n'.join(dialog_parts)

with open('English.txt', 'w') as fp:
    fp.write(raw)








