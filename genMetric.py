import re
import subprocess

toRemoveAttribute = [
    "pod", "kitVersion", "instance",
]

toReplaceValues = {
    "envName": "$envName"
}

inp = ""
while inp != "q":
    inp = input("[enter a metric to generify, 'q' to exit]\n")
    for attr in toRemoveAttribute:
        inp = re.sub(r'{0}=\".*?\",?\s?'.format(attr), "", inp)
    for val in toReplaceValues.keys():
        inp = re.sub(r'({0}=)\".*?(\"[,\s]?)'.format(val), r'\1"~{0}\2'.format(toReplaceValues[val]), inp)

    subprocess.run("pbcopy", universal_newlines=True, input=inp)
    print("[generified metric]: (Copied to clipboard!)\n", inp)
