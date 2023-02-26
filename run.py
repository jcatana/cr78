#!/usr/bin/env python
import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
        autoescape=False,
        loader = FileSystemLoader(os.path.join(PATH, "templates")),
        trim_blocks=False)

def run():
    dirlisting = os.listdir(os.getcwd())
    for file in dirlisting:
        if file.endswith(".wav"):
            name = file.split(".wav")[0]
            print(name)
            context = {
                'instrument': {
                    'name': name,
                    'file': file,
                    }
                }
            print(context)
            #os.mkdir(name)
            xml = render_template('instrument.xml', context)
            print(xml)
            #os.rename(file, name + "/" + file)

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def main():
    run()

main()
