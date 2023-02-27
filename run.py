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
    drumkitname = os.path.basename(os.getcwd())
    drumkit = {
            'name': drumkitname,
            'description': drumkitname + " drumgizmo drumkit",
            'samplerate': "48000",
            'instruments': [],
            }
    for file in dirlisting:
        if file.endswith(".wav"):
            name = file.split(".wav")[0]
            print(name)
            context = {
                'instrument': {
                    'name': name,
                    'file': file,
                    'xml': name+".xml",
                    }
                }
            drumkit['instruments'].append(context)
            #print(context)
            os.mkdir(name)
            instrumentxml = render_template('instrument.xml', context)
            #print(instrumentxml)
            print("save as: " + name + "/" + name + ".xml")
            write_xml_file(name + "/" +name + ".xml", instrumentxml)
            os.rename(file, name + "/" + file)

    context = {
            'drumkit': drumkit,
            }
    print(context)
    drumkitxml = render_template('drumkit.xml', context)
    write_xml_file(drumkitname + ".xml", drumkitxml)
    midimapxml = render_template('midimap.xml', context)
    write_xml_file("midimap.xml", drumkitxml)
    print(midimapxml)

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def write_xml_file(name, contents):
    print(contents)
    with open(name, "w") as fh:
        fh.write(contents)


def main():
    run()

main()
