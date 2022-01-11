import re
import subprocess

toRemoveAttribute = [
    "pod", "kitVersion", "instance",
]

toReplaceValues = {
    "envName": "$envName"
}

def replaceRemoveAttributes(metric):
    for attr in toRemoveAttribute:
        metric = re.sub(r'{0}=\".*?\",?\s?'.format(attr), "", metric)
        
    return metric;

def replaceRemoveAttributes(metric):
    for val in toReplaceValues.keys():
        metric = re.sub(r'({0}=)\".*?(\"[,\s]?)'.format(val), r'\1"~{0}\2'.format(toReplaceValues[val]), metric)
        
    return metric;

inp = ""
while inp != "q":
    inp = input("[enter a metric to generify, 'q' to exit]\n")
    if (inp == "q"):
        break;
        
    inp = replaceRemoveAttributes(inp);
    inp = replaceRemoveAttributes(inp);

    subprocess.run("pbcopy", universal_newlines=True, input=inp)
    print("[generified metric]: (Copied to clipboard!)\n", inp)
