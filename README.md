Projet TNAH-2021-DecameronFR
====
![f18](https://gallica.bnf.fr/iiif/ark:/12148/btv1b7100018t/f18/707,1708,1457,822/max/0/default.jpg)

Le projet vise à la consitution de vérités de terrain pour l'entraînement de modèles HTR à partir d'un manuscrit français des années 1430-1455 : le manuscrit 5070 de la Bibliothèque de l'Arsenal (reproduit sur [Gallica](https://gallica.bnf.fr/ark:/12148/btv1b7100018t/f18)). Ce manuscrit contient la traduction française du *Decameron* de Boccace par Laurent de Premierfait. Nos vérités de terrain recouvrent la description de la peste à Florence située dans le prologue de l'ouvrage.

Le passage concerné occupe les folios 2v (lettrine M) à 6v (premier pied de mouche), soit 16 colonnes, à savoir:
- [folio 2v](https://gallica.bnf.fr/view3if/ga/ark:/12148/btv1b7100018t/f18)
- [folio 3r](https://gallica.bnf.fr/view3if/ga/ark:/12148/btv1b7100018t/f19)
- [folio 3v](https://gallica.bnf.fr/view3if/ga/ark:/12148/btv1b7100018t/f20)
- [folio 4r](https://gallica.bnf.fr/view3if/ga/ark:/12148/btv1b7100018t/f21)
- [folio 4v](https://gallica.bnf.fr/view3if/ga/ark:/12148/btv1b7100018t/f22)
- [folio 5r](https://gallica.bnf.fr/view3if/ga/ark:/12148/btv1b7100018t/f23)
- [folio 5v](https://gallica.bnf.fr/view3if/ga/ark:/12148/btv1b7100018t/f24)
- [folio 6r](https://gallica.bnf.fr/view3if/ga/ark:/12148/btv1b7100018t/f25)
- [folio 6v](https://gallica.bnf.fr/view3if/ga/ark:/12148/btv1b7100018t/f26)

# Contenu du dépôt
- `css/` contient la feuille de style de `caracteres.html`
- `csv/` contient la table des caractères
- `documentsDeTravail/` contient les transcriptions utilisées pour réaliser les `veriteTerrain/` du projet
- `img/` contient des images pour l'illustration de `caracteres.html` et de `normesTranscription.md`
- `modeles/` : contient les modèles d'entraînement HTR utilisés:
    - `cremma_medieval_bicerin_decameron.mlmodel` : le modèle Cremma Mediéval 1.0.0 Bicerin entraîné
    - `cremma_medieval_bicerin.mlmodel` : le modèle Cremma Mediéval 1.0.0 Bicerin
    - `fineTunEneide2mains_best_decameron.mlmodel` : le modèle fineTunEneide entraîné
    - `fineTunEneide2mains_best.mlmodel` : le modèle fineTunEneide
- `py/` contient
    - `caracteres.py` : le script python de génération de `caracteres.html` à partir de `csv/caracteres.csv`
    - `iiifSelection.py` : le script python de génération dans un terminal de l'URL d'une zone d'intérêt dans une image IIIF
- `tutos/` contient des outils de contribution au projet :
    - `tuto-iiif.md` : pour générer l'URL d'une zone d'intérêt dans une image IIIF
    - `tutoJunicode.md` : pour installer la police de caractères Junicode
    - `tuto-segmentation.mp4` : pour segmenter un folio dans eScriptorium
    - `tuto-trasncription.tar.xz` : pour transcrire un folio dans e-Scriptorium
- `veriteTerrain/` contient les vérité de terrain du projet : fichiers `.xml` et images `.jpg`
- `caracteres.html` : table des caractères d'après le manuscrit du projet ; elle propose une liste des formes de lettres et les solutions d'encodage des cas complexes, notamment les abréviations
- `clavier-virtuel-decameron.json` : clavier virtuel à importer dans e-Scriptorium avant de commencer la transcription ; donne accès à la plupart des caractères spéciaux utilisés
- `normesTranscription.md` : description détaillée des normes de transcription employée dans le projet