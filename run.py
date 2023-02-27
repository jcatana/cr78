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
    noteindex = 36
    drumkit = {
            'name': drumkitname,
            'description': drumkitname + " drumgizmo drumkit",
            'samplerate': "48000",
            'instruments': [],
            }
    midimap = {'instruments': [],}
    for file in dirlisting:
        if file.endswith(".wav"):
            name = file.split(".wav")[0]
            samplesfile = "samples/" + file
            samplesdir = name + "/samples/"
            print(name)
            context = {
                'instrument': {
                    'name': name,
                    'file': file,
                    'samplesfile': samplesfile,
                    'noteidx': str(noteindex),
                    'xml': name+".xml",
                    }
                }
            drumkit['instruments'].append(context)
            #print(context)
            os.mkdir(name)
            os.mkdir(samplesdir)
            instrumentxml = render_template('instrument.xml', context)
            #print(instrumentxml)
            write_xml_file(name + "/" +name + ".xml", instrumentxml)
            os.rename(file, samplesdir + file)
            noteindex = noteindex + 1
            midimap['instruments'].append(context)

    context = {
            'drumkit': drumkit,
            }
    print(context)
    ##
    # Write drumkit XML file
    ##
    drumkitxml = render_template('drumkit.xml', context)
    write_xml_file(drumkitname + ".xml", drumkitxml)
    ##
    # Write midimap XML file
    ##
    midimapxml = render_template('midimap.xml', context)
    write_xml_file("midimap.xml", midimapxml)
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
