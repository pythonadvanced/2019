# travers fréquents

## needleman & wunsch

### la taille de la matrice

un nombre surprenant d'entre vous a alloué une matrice trop petite !

si les deux chaines font par exemple 3 et 5 de long, il faut allouer une matrice
de taille (4 x 6); le coin (0, 0) vaut 0 et il représente la distance entre '' et '';
les points (i, 0) correspondent à la distance entre une sous-chaine de longueur i et '',
transformation qui se fait en i insertions.

c'est une erreur assez lourde, vous n'avez dans ce cas aucune chance d'obtenir des
résultats corrects, évidemment

### le parcours de la matrice

tout le monde a rempli la matrice en commençant par les deux bords i==0 et j==0; ça
fonctionne bien et c'est adapté à l'énoncé; je voulais juste signaler que lorsque les
coûts, notamment les coûts d'insertion, ne sont pas uniformes, cette approche devient un
peu lourde; tout ça pour expliquer pourquoi le corrigé procède différemment et parcourt la
matrice en diagonale.

### non-déterminisme

clairement même si la distance a une valeur déterminée pour les deux chaines, il peut y
avoir plusieurs façons de calculer le rapport
(et en pratique en fait c'est très fréquemment le cas)

c'est lié au fait que le minimum qu'on calcule pour M[i, j] peut être atteint
par deux (ou même trois) des trois valeurs que l'on utilise dans le minimum

la grosse majorité d'entre vous a choisi de privilégier la voie 'diagonale'; c'est à dire
que si le minimum provient du coût induit de [i-1, j-1] on fait remonter le rapport par ce
chemin-là

### `bundle.py`

ce code est assez simple, j'avais un peu pimenté en vous demandant d'accepter des
entrées dont le nombre de lignes n'est pas pair

presque tout le monde du coup m'a écrit un code qui lit tout le fichier, pour calculer sa
taille, et traiter le cas des lignes impaires; 

ça marche, mais franchement c'est vilain ! c'est important, quand on peut, d'éviter de
charger comme ça **tout le fichier** en mémoire: il faut autant que possible utiliser le
fichier comme itérateur et traiter les lignes à la volée

reportez-vous au corrigé

## huffman

beaucoup moins de soucis avec cet algorithme, qui a été majoritairement réussi

par contre certains ont été amenés à créer une structure d'arbre super compliquée, pour le
parcours permettant d'affecter les codes, j'invite ceux-là à lire le corrigé
