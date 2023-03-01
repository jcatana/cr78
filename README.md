# DZ convert
A simple script to convert a folder full of .wav files into a [DrumGizmo](https://www.drumgizmo.org/) drum kit.


### Usage
Example help
```
usage: dzconvert [-h] [-v] [-r RATE] [-i INDEX] [-w WAVE] [-f FOLDER] [-n NAME]

Convert folder of .WAV samples into a drumgizmo drumkit

options:
  -h, --help            show this help message and exit
  -v, --verbose
  -r RATE, --rate RATE  Sample rate override. Defaults to 48000
  -i INDEX, --index INDEX
                        Start index for midi note mapping. Defaults to 36
  -w WAVE, --wave WAVE  Folder containing .wav files to be converted. Defaults to current directory
  -f FOLDER, --folder FOLDER
                        Target folder to create template in. Top folder name will be used as name of kit if 'name' not defined
  -n NAME, --name NAME  Target folder to create template in. Will be used as name of kit
```

### Notes
1. All .wav samples must be recorded at the same rate.
2. This will move the source data to the target location. I urge caution and maybe run it on a copy of the data first.
3. This currently only works with single instrument power level. Single sound per note.
4. MIDI mapping is currently numeric by whatever the order the system lists the files in. You might have to manually edit the midimap.xml file to your liking.



### Installation
This only requires `argparge` and `jinja2` python libraries to run. 
1. Clone this repo. 
2. `cd` into the repo
3. `chmod +x dzconvert`
4. `./dzconvert -h`


