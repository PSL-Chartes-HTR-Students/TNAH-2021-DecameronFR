Normes de transcription : liste de points d'attention
====

# Mise en page
## Paragraphes
Les paragraphes sont soigneusement marqués dans le manuscrit par l’alternance des **pieds de mouche ¶** rouges et bleus. Discuté dans l'[issue 13](https://github.com/kristinkonstantinova/TNAH-2021-DecameronFR/issues/13), nous pourrions opter pour une simple transcription avec le caractère MUFI PILCROW SIGN (si choisi, reprendre l'argumentation).

# Emploi de caractères spéciaux
- Le projet CREMMA Médiéval (désormais CM) propose une [table des caractères](https://github.com/HTR-United/cremma-medieval/blob/main/table.csv)
- Le « Manuel d’encodage BFM-Manuscrits » de la *Base de Français Médiéval* (désormais BFM) en ligne [ici](http://bfm.ens-lyon.fr/spip.php?article282) propose lui aussi un choix d'entités MUFI pour les besoins de l'encodage des textes médiévaux (voir p. 35 et suivantes).

# Règles de transcription
Les lettres *i* et *u* doivent être transcrites telles quelles.

En position initiale, *i* et *j* suivent le même *ductus*. **Le retrouve-t-on avec valeur de *j* en milieu de mot ?** traité dans [ce commentaire](https://github.com/kristinkonstantinova/TNAH-2021-DecameronFR/issues/11#issuecomment-981391510).

En position initiale, *v* prend une forme particulière, mais sa valeur peut être aussi bien *u* que *v*. **Ajouter un exemple avec l'article *une***

## Majuscules et minuscules
Les noms propres ne prennent pas de majuscule dans le manuscrit (*florence*, f2vb) :
![florence, f2vb](https://gallica.bnf.fr/iiif/ark:/12148/btv1b7100018t/f18/2266,3351,995,103/max/0/default.jpg)

Les majuscules sont employées en début de phrase (après une coupure forte, en début de paragraphe), et parfois après une coupure faible (cf. *infra* Ponctuation) :
> vous ay promise auant temps, **E**t se par auenture je uous eusse dites (f2vb)

![exemple](https://gallica.bnf.fr/iiif/ark:/12148/btv1b7100018t/f18/2232,1452,1210,227/max/0/default.jpg)

Il est sans doute judicieux de respecter l'emploi des majuscules et des minuscules dans le manuscrit.

## Allographes
Faut-il distinguer *s* long et *s* rond, par exemple ? **Ils ne sont pas distingués dans CM**. Il s'agit d'entraîner l'algorithme à la reconnaissance des caractères, quelle que soit leur forme graphique.

## Abréviations
Les abréviations ne doivent pas être résolues. On fera appel à des **caractères spéciaux MUFI** pour noter les signes d'abréviation.

## Accentuation
En l'absence d'accentuation dans le manuscrit, il n'est sans doute pas pertinent d'employer des caractères accentués dans la transcription. Les règles arbitraires d’accentuation des textes médiévaux ne seraient donc pas appliquées. C'est le choix fait pour le CM (par exemple, pas d'accent aigu sur le *e* final prononcé *é*).

## Lettres pointées
Les *i* et les *y* sont parfois pointés dans le manuscrit, mais pas systématiquement. 
- *Comprinse* avec *i* pointé :

    ![comprinse, f2vb](https://gallica.bnf.fr/iiif/ark:/12148/btv1b7100018t/f18/2814,1226,367,124/max/0/default.jpg)

- *Sentier* avec *i* non pointé :

    ![sentier, f2vb](https://gallica.bnf.fr/iiif/ark:/12148/btv1b7100018t/f18/2402,1972,262,120/max/0/default.jpg)

Comme le pointage est un élément graphique très petit, en tenir compte nous expose peut-être à un faible taux de succès de la reconnaissance automatisée. En outre, en l'absence de règle évidente suivie par le copiste, il est sans doute préférable de modernier la transcription des *i* en utilisant partout le caractère moderne pointé (les *i* non pointés du ms. BNF fr. 844 ont été transcrits par *i* dans CM).

Ne tenant pas compte du pointage du *i*, il est peut-être cohérent de ne pas tenir compte de celui du *y* (le *y* pointé correspondrait à l'entité MUFI `&ydot;`)

## Séparation des mots
La séparation des mots a été globalement établie avec précision par le scribe : on rédécoupera donc les mots là où l'algorithme n'y parvient pas. En revanche, il serait préférable de suivre également l'usage graphique du manuscrit en ne découpant pas les articles ou prépositions élidés devant un mot, et en ne restituant pas d'apostrophe.

On transcrira donc *louuraige* et non *l'ouuraige* :

![louuvraige, f2vb](https://gallica.bnf.fr/iiif/ark:/12148/btv1b7100018t/f18/2286,3676,371,103/max/0/default.jpg)

Et encore, *quilz nentrassent* et non *qu'ilz n'entrassent* :

![quilz nentrassent, f3ra](https://gallica.bnf.fr/iiif/ark:/12148/btv1b7100018t/f19/585,1843,755,140/max/0/default.jpg)


## Ponctuation
Le texte du témoin manuscrit a été soigneusement ponctué. On fera appel à des **caractères spéciaux MUFI** pour noter ces signes.
- Pose forte : MUFI MIDDLE DOT
    + CM : POINT MEDIAN, pas d'info MUFI ; mais *.* normal par exemple pour bnf_fr_412_wauchier
- Pose faible : pas encodé dans MsRoi ni Wauchier CM
- Trait de suite : pas encodé dans MsRoi ni Wauchier CM