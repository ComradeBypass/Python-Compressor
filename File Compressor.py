import codecs, os, zlib

def setup():
    global file_to_obfuscatestr
    global curdirectory
    global a
    global imports
    global prepped

    file_to_obfuscate = input("File you want to compress (needs to be in the same folder as the compressor): ")
    file_to_obfuscatestr = str(file_to_obfuscate)

    curdirectory = os.path.dirname(os.path.abspath(__file__))

    file_to_obfuscate_open = open(curdirectory+"\\"+file_to_obfuscatestr, "r")
    a = str(file_to_obfuscate_open.read())
    file_to_obfuscate_open.close()


    imports = """
## Compressor made by: https://github.com/ComradeBypass


import zlib
import codecs
"""

    prepped = str(a.strip())

setup()


def obfuscation(file):
    bruh = codecs.encode(file)
    a = str(zlib.compress(bruh, 9))
    c = r"exec(codecs.decode(zlib.decompress("+"bytes("+a+")"+")))"


    W = imports+c

    try:
        creationoffile = open(curdirectory+"\\"+"Compressed_"+file_to_obfuscatestr, "x")
        creationoffile.close()
    except Exception:
        pass

    creationoffile = open(curdirectory+"\\"+"Compressed_"+file_to_obfuscatestr, "w")
    creationoffile.write(W)
    creationoffile.close()

obfuscation(prepped)




