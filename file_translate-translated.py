import sys
from googletrans import Translator, LANGUAGES

translator = Translator()

args = sys.argv

def makeItNice(file, newFile):

    for x in file:
        if x == "\n":
            newFile.write('\n')
        else:
            newFile.write(x.replace('\n', ' '))


#   Cette fonction suppose que l'API Google Trnaslate est utilisée pour analyser la traduction en tant que telle. Honnêtement, je pourrais changer cela plus tard pour utiliser une autre API, ou si je suis super sympa, je créerai la mienne, lol, mais je ne serai jamais aussi gentil, nous allons donc laisser cela aux professionnels. Mise à jour, je viens de découvrir que ce n’est pas la vraie affaire, et que la vraie affaire coûte probablement de l’argent, vous savez que ce que je n’ai pas, alors une fois que j’aurai eu ça, qui sait, je l’aurai peut-être, mais ça dépend où ma motivation pour ce projet me prend.
def translateThisFile(file, destLang, srcLang):
    modFile = open("modified.txt", "w")
    makeItNice(file, modFile)
    modFile.close()

    modFile = open("modified.txt", "r")
    newFile = open("translated.txt", "w")

    if destLang is None and srcLang is None:
        print("Translating file to ENGLISH...\n")

        for line in modFile:
            if line != "\n" and len(line) != 0:
                tLine = translator.translate(line).text
            elif line == "\n":
                tLine = line

            newFile.write(tLine)
    elif destLang is None and srcLang is not None:
        print("Translating file to ENGLISH...\n")

        for line in modFile:
            if line != "\n" and len(line) != 0:
                tLine = translator.translate(line, src=srcLang).text
            elif line == "\n":
                tLine = line

            newFile.write(tLine)
    elif destLang is not None and srcLang is None:
        print("Translating file to " + LANGUAGES.get(destLang).upper() + "...\n")

        for line in modFile:
            if line != "\n" and len(line) != 0:
                tLine = translator.translate(line, dest=destLang).text
            elif line == "\n":
                tLine = line

            newFile.write(tLine)
    else:
        print("Translating file to " + LANGUAGES.get(destLang).upper() + "...\n")

        for line in modFile:
            if line != "\n" and len(line) != 0:
                tLine = translator.translate(line, dest=destLang, src=srcLang).text
            elif line == "\n":
                tLine = line

            newFile.write(tLine)

    modFile.close()
    newFile.close()
    print("File Translated! Check translated.txt")

def translateThisTextEnglish(text):
    if len(text) > 15000:
        print("Invalid input: must be less than 15000 characters, or use a file")
    else:
        print("Translating text to ENGLISH...\n")
        tLine = translator.translate(text).text
        print("Text Translated!\n")
        print(tLine)


if len(args) > 4:
    print("Invalid command\n"
          "Usage: file_translate.py\n"
          "OR"
          "Usage: file_translate.py <file name>\n"
          "OR"
          "Usage: file_translate.py <file name> <destination language>\n"
          "OR"
          "Usage: file_translate.py <file name> <source language> <destination language>",
          file=sys.stderr)
    exit(1)
elif len(args) == 1:
    ogText = input("Please enter the text that you would like to be translated: ")
    translateThisTextEnglish(ogText)
elif len(args) == 2:
    f = open(args[1], "r")
    translateThisFile(f, None, None)
elif len(args) == 3:
    f = open(args[1], "r")
    translateThisFile(f, args[2], None)
else:
    f = open(args[1], "r")
    translateThisFile(f, args[3], args[2])