import click


@click.command()
@click.argument('adresse')
@click.argument('ark')
@click.argument('image', type=str)
@click.argument('x', type=int)
@click.argument('y', type=int)
@click.argument('w', type=int)
@click.argument('h', type=int)
def selectiiif(adresse, ark, image, x, y, w, h):
    """ Cette fonction imprime l'URL d'une sélection d'image 3IF en prenant comme argument :
    - L'URL du site hébergeant l'image
    - Le numéro ark de l'objet
    - Le nom du fichier image
    - Les coordonnées de la sélection
    
    :param adresse: URL du site hébergeant l'image
    :param ark: numéro ark de l'objet
    :param image: numéro de l'image
    :param x: Position du coin sup. gauche de la sélection sur l'axe horizontal en pixels
    :param y: Position du coin sup. gauche de la sélection sur l'axe vertical (en pixels)
    :param w: "Width" largeur de la sélection (en pixels)
    :param h: "Height" Hauteur de la sélection (en pixels)
    :return: None
    """
    
    if adresse == "gallica":
        adresse = "https://gallica.bnf.fr"
    if ark == "decars":
        ark = "ark:/12148/btv1b7100018t"
    
    print(f"{adresse}/iiif/{ark}/{image}/{x},{y},{w},{h}/max/0/default.jpg")


selectiiif()
