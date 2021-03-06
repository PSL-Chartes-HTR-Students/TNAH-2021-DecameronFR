import csv
import click

@click.command()
def traitement_caracteres():
    """
    Ce script récupère le contenu du fichier csv/caracteres.csv et écrit le fichier caracteres.html à partir de ce contenu.
    """

    # Récupération des données de la table CSV
    with open("csv/caracteres.csv") as f:
        lecteur = csv.reader(f, delimiter="\t", quotechar='|')

        donnees = {}
        ttTypes = [
            'lettre',
            'ponctuation',
            'abréviation',
            'signe tironien',
        ]

        for adresse_img, typ, lettre, majmin, commentaire, probleme, encodage in lecteur:
            donnees[adresse_img] = {
                "type" : typ,
                "caractere" : lettre,
                "maj-min" : majmin,
                "commentaire" : commentaire,
                "problème" : probleme,
                "encodage" : encodage}
        
    # Ecriture du fichier HTML de consultation
    with open("caracteres.html", mode="w") as g:
        g.write("<!DOCTYPE html>\n<html>\n")
        # Ecriture du head
        g.write("<head>\n")
        g.write("<title>Table paléographique d'Arsenal 5070</title>\n")
        g.write('''<link type="text/css" rel="stylesheet" href="css/caracteres.css">\n''')
        g.write("</head>\n")
        
        # Ecriture du body
        g.write("<body>\n")
        g.write("<header><h1>Table des caractères d'Arsenal 5070</h1></header>\n")
        for chqType in ttTypes:
            # Transformation du "type" en titre "h2" avec une maj. et au pluriel
            transType = chqType.title()
            transType = transType.split()
            h2 = ""
            for types in transType:
                h2 += types + "s "
            
            # Ecriture du titre de la section
            g.write("<section>\n")
            g.write("<header><h2>" + h2 + "</h2><header>\n")
            for index, item in enumerate(donnees):
                if index != 0:
                    if chqType == donnees[item]["type"]:
                        # Ecriture des articles
                        g.write("<article>\n")
                        
                        # Div contenant les images
                        g.write(f'''<div class="img"><img src="{item}" alt="{donnees[item]["caractere"]}"></div>\n''')
                        
                        # Div contenant le contenu des notices
                        g.write(f'''<div class="descript">\n
                                        <p>{donnees[item]["caractere"]}  {donnees[item]["maj-min"]}</p>\n
                                        <p class="prblm">{donnees[item]["problème"]}</p>''')
                        g.write(f'''<p>{donnees[item]["commentaire"]}</p>\n''')
                        if donnees[item]["encodage"]:
                            g.write(f'''<p>Transcrire : {donnees[item]["encodage"]}</p>\n''')
                            # Ajouter l'entité avec &amp;
                            code = "" # Cette variable enfermera l'encodage en incluant les bons caractères d'échappement
                            for caractere in donnees[item]["encodage"]:
                                if caractere != "&":
                                    code = code + caractere
                                else:
                                    code = code + "&amp;"
                            g.write(f'''<p>Encodage : {code}</p>\n''')
                        g.write("</div>\n")
                        g.write("</article>\n")
            g.write("</section>\n")
        g.write("</body>\n")    
        g.write("</html>")

traitement_caracteres()