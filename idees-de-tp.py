# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.1.7
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # idées de TP pour la suite
#
# très informellement, je souhaite prendre quelques notes sur des sujets possibles en décembre

# %% [markdown] {"slideshow": {"slide_type": ""}}
# # calculette infixe
#
# idée proposée par Aurélien Noce
#
# * éventuellement multiforme  
#   * depuis une chaine
#   * depuis la ligne de commande
#   * depuis un fichier
#   
# * premier temps: les tokens sont tous séparés par des espaces, on fait expr.split() et basta
#
# * second temps: on définit les tokens du langage à base d'expressions régulières
#
# * troisième temps: on introduit des opérateurs unaires; (ternaires ? genre `a ? b : c`)
#
# * on ajoute les variables sous la forme d'un dictionnaire

# %%
from operator import add, mul, sub, floordiv

from collections import namedtuple

Operator = namedtuple('Operator', ['function', 'precedence'])

supported = {
    '(':  Operator(None, 0),
    '+' : Operator(add, 1),
    '-':  Operator(sub, 1),
    '*':  Operator(mul, 2),
    '/':  Operator(floordiv, 2),
}


def infix_eval(expr):
    val_stack = []
    op_stack = []
    for token in expr.split():
        # a litteral value
        try:
            operand = int(token)
            val_stack.append(operand)
            continue
        except ValueError:
            pass
        # something else
        if token == '(':
            op_stack.append(token)
        elif token == ')':
            while op_stack[-1] != '(':
                function = supported[op_stack.pop()].function
                right, left = val_stack.pop(), val_stack.pop()
                val_stack.append(function(left, right))
            # this now is a '('
            op_stack.pop()
        elif token in supported:
            while (op_stack and 
                      supported[op_stack[-1]].precedence 
                      >= supported[token].precedence):
                function = supported[op_stack.pop()].function
                right, left = val_stack.pop(), val_stack.pop()
                val_stack.append(function(left, right))
            op_stack.append(token)
    while op_stack:
        op = op_stack.pop()
        function = supported[op].function
        right, left = val_stack.pop(), val_stack.pop()
        val_stack.append(function(left, right))
    assert len(val_stack) == 1
    assert not op_stack
    return val_stack[0]


# %% {"cell_style": "split"}
infix_eval("10 + 30")

# %% {"cell_style": "split"}
infix_eval("10 + 20 + 30")

# %% {"cell_style": "split"}
# should be 150
infix_eval("( 3 + 2 ) * ( 10 + 20 )")

# %% {"cell_style": "split"}
# should be 43
infix_eval("3 + 2 * 10 + 20")

# %% [markdown]
# # distance dans les ADN
#
# * leur faire implémenter l'algorithme de Needleman and Wunsch
#
# https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm
#
# bon je trouve que la page wikipedia a tendance à présenter les choses sous une forme plus compliquée que nécessaire

# %% [markdown]
# # bases de données
#
# vu dans les notebooks de Laurent Signac à ENSIP/Poitiers
# <https://nbhosting.inria.fr/auditor/notebook/ensip:generic/diueil/1_2_2_Traitement_donnees_table-sujet>
#
# * exo sur une simulation de bdd en mémoire
# * une table = une liste de dictionnaires
# * sujet = modéliser les requêtes SQL (join, WHERE, ...) sous forme de fonctions Python
# * sans doute améliorable en utilisant des itérateurs et générateurs pour les diverses opérations de combinaison

# %%
from typing import List, Dict, Iterator, Callable
import itertools


Line = Dict
Table = Iterator[Line]


def select(table: Table, colonnes: List[str]) -> Iterator[Line]:
    for line in table:
        projected_line = {}
        for colonne in colonnes:
            projected_line[colonne] = line[colonne]
        yield projected_line


def product(tableA: Table, tableB: Table) -> Iterator[Line]:
    for lineA, lineB in itertools.product(tableA, tableB):
        yield {**lineA, **lineB}


def filter(table: Table, function: Callable[[Line], bool]) -> Iterator[Line]:
    for line in table:
        if function(line):
            yield line


def join(tableA: Table, colA: str, tableB: Table, colB: str):
    return filter(product(tableA, tableB), lambda line: line[colA] == line[colB])


# %%
t1 = [{'nom': 'Dupont', 'prenom': 'Jean', 'person_id': 1}, {'nom': 'Durand', 'prenom': 'Jeanne', 'person_id': 2}]
t2 = [{'nom2': 'Smith', 'prenom2': 'John', 'person2_id': 1}, {'nom2': 'Durand', 'prenom2': 'Jeanne', 'person2_id': 2}]

for flat in select(product(t1, t2), ['nom', 'nom2']):
    print(flat)


# %% [markdown]
# ****

# %% [markdown]
# ***NOTE***
#
# ce notebook est le premier de ceux qui utilisent un **workflow basé sur jupytext**
#
# en pratique ça signifie que
# * dans mon repo de travail je sauve automatiquement un `.ipynb` **ET** un `.py` 
# * je ne mets **sous git QUE le `.py`** 
#
# mon objectif est de vérifier que nbhosting fonctionne correctement avec de tels notebooks  
# **update**: ça ne fonctionne pas en l'état sous nbhosting; 
# mais j'hésite à faire la correction pour la raison suivante. 
#
#
#
# les avantages :
# * `git diff` plus facile (pas besoin de nbdime en fait)
# * `git commit` plus facile (pas besoin de nbstripout non plus)
# * `git pull` plus facile (jupytext est configuré pour **ne pas sauver certains détails** comme notamment le niveau de version de Python qui n'arrête pas de changer entre moi et les différentes images sur nbhosting)
#
# à suivre sur la durée donc
