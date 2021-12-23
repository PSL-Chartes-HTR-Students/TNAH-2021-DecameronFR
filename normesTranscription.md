Normes de transcription : liste de points d'attention
====

# Mise en page
## Paragraphes
Les paragraphes sont soigneusement marqués dans le manuscrit par l’alternance des **pieds de mouche ¶** rouges et bleus. Discuté dans l'[issue 13](https://github.com/kristinkonstantinova/TNAH-2021-DecameronFR/issues/13), nous pourrions opter pour une simple transcription avec le caractère MUFI PILCROW SIGN (si choisi, reprendre l'argumentation).
- Approuvé par [Victor](https://github.com/kristinkonstantinova/TNAH-2021-DecameronFR/issues/11#issuecomment-977986556)

## Annotations
Voir issue #21

# Emploi de caractères spéciaux
- Le projet CREMMA Médiéval (désormais CM) propose une [table des caractères](https://github.com/HTR-United/cremma-medieval/blob/main/table.csv)
- Le « Manuel d’encodage BFM-Manuscrits » de la *Base de Français Médiéval* (désormais BFM) en ligne [ici](http://bfm.ens-lyon.fr/spip.php?article282) propose lui aussi un choix d'entités MUFI pour les besoins de l'encodage des textes médiévaux (voir p. 35 et suivantes).

# Règles de transcription
Les lettres *i* et *u* doivent être transcrites telles quelles.

En position initiale, *i* et *j* suivent le même *ductus*. **Le retrouve-t-on avec valeur de *j* en milieu de mot ?** traité dans [ce commentaire](https://github.com/kristinkonstantinova/TNAH-2021-DecameronFR/issues/11#issuecomment-981391510), non ! dans [ce commentaire](https://github.com/kristinkonstantinova/TNAH-2021-DecameronFR/issues/11#issuecomment-991728058), Victor a montré que *tousjours* est écrit avec le caractère *i*.

En position initiale, *v* prend une forme particulière, mais sa valeur peut être aussi bien *u* que *v*. **Ajouter un exemple avec l'article *une***
Traitement dans Cremma (university_of_pennsylvania_660_pelerinage_mademoiselle_sapience, no. 0) [Pelerinage de mademoiselle Sapience](https://github.com/HTR-United/cremma-medieval/tree/main/university_of_pennsylvania_660_pelerinage_mademoiselle_sapience)
> et vit en une ꝑtie ung lieu gaste aussi cõe une

## Majuscules et minuscules
Les noms propres ne prennent pas de majuscule dans le manuscrit (*florence*, f2vb) :
![florence, f2vb](https://gallica.bnf.fr/iiif/ark:/12148/btv1b7100018t/f18/2266,3351,995,103/max/0/default.jpg)

Les majuscules sont employées en début de phrase (après une coupure forte, en début de paragraphe), et parfois après une coupure faible (cf. *infra* Ponctuation) :
> vous ay promise auant temps, **E**t se par auenture je uous eusse dites (f2vb)

![exemple](https://gallica.bnf.fr/iiif/ark:/12148/btv1b7100018t/f18/2232,1452,1210,227/max/0/default.jpg)

Point développé dans [ce commentaire](https://github.com/kristinkonstantinova/TNAH-2021-DecameronFR/issues/11#issuecomment-981415832) : il s'agirait de transcrire en maj. le E dans le cas du et initial ayant cette valeur syntaxique.

## Allographes
Faut-il distinguer *s* long et *s* rond, par exemple ? **Ils ne sont pas distingués dans CM**. Il s'agit d'entraîner l'algorithme à la reconnaissance des caractères, quelle que soit leur forme graphique.

Voir issue #17.

## Abréviations
Les abréviations ne doivent pas être résolues. On fera appel à des **caractères spéciaux MUFI** pour noter les signes d'abréviation.

Pour les abréviations n'ayant pas de caractère dédié :
- Pour le *-oient* utiliser **'**

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
Le texte du témoin manuscrit a été soigneusement ponctué. On fera appel à des caractères conventionnels et à des **caractères spéciaux MUFI** pour noter ces signes.
- Pause forte : MUFI MIDDLE DOT
    + CM : POINT MEDIAN, pas d'info MUFI ; mais *.* normal par exemple pour bnf_fr_412_wauchier
- Punctus elevatus, ancêtre du point virgule (MUFI `&punctelev;`, encodé &#F161;) a été transcrit dans Cremma-Medieval par un simple point virgule moderne (cf. table). 
- Pause faible : pas encodé dans MsRoi ni Wauchier CM
- Trait de suite : pas encodé dans MsRoi ni Wauchier CM

La ponctuation n'est pas systématiquement présente avant la conjonction *Et* dotée d'une majuscule, celle-ci ayant une forte valeur syntaxique.

## Corrections
En discussion dans l'issue #11, à partir de ce [commentaire](https://github.com/kristinkonstantinova/TNAH-2021-DecameronFR/issues/11#issuecomment-998959561).

Nous avons deux possibilités :
- La plus simple : ne pas en tenir compte !
- Un peu plus complexe : utiliser des caractères exponctués (les exponctuations sont bien visibles dans le ms.)
    - pour ẹ 1EB9 LATIN SMALL LETTER E WITH DOT BELOW 
    - pour  E466 LATIN SMALL LETTER C WITH DOT BELOW (nécessite la police Junicode)

Zoé propose de ne pas les signaler [ici](https://github.com/kristinkonstantinova/TNAH-2021-DecameronFR/issues/11#issuecomment-1000196675).

## Nombres
Les nombres ont été écrits suivis d'un point médians :

![3ou4](https://gallica.bnf.fr/iiif/ark:/12148/btv1b7100018t/f24/3147,1106,410,161/max/0/default.jpg)

On les a transcrits de même :
> iii· ou iiii·