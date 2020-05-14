# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     formats: py:percent
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   notebookname: git layout & interactive notebooks
#   version: '1.0'
# ---

# %% [markdown]
# # cours ***Python avancé*** - 15 Mai 2020

# %% [markdown]
# Aujourd'hui nous abordons deux sujets qui n'ont rien à voir entre eux, mais qui peuvent tous les deux vous être utiles pour les projets :
#
# 1. bonnes pratiques pour organiser votre repo git
# 1. notebooks interactifs, pour des visualisations plus expressives
#
# Pour ce cours qui est au total de 3h, je vous recommande  
# de consacrer **au maximum** de l'ordre de 30' à 45' sur le premier sujet.
#
# *** 
#
# <span style="background-color: red; padding: 10px;">
# Notez bien les éléments que vous avez à rendre :
# </span>
#
# * un quiz, consacré essentiellement à la première partie,
# * pour la seconde partie, on vous demande d'envoyer à votre enseignant votre solution pour **au moins un des deux exercices** proposés (Taylor ou coronavirus)

# %% [markdown]
# # partie cours

# %% [markdown]
# ## bonnes pratiques pour l'organisation de votre repo git

# %% [markdown]
# Pour aborder ce sujet, le contenu principal est extrait du MOOC Python3, que je vous invite à le lire directement sur nbhosting :
#
#  * https://nbhosting.inria.fr/auditor/notebook/python3-s2:mooc/w6/w6-s9-c1-organisation-sources
#  
# Normalement ce notebook est suffisant pour répondre au quiz; si vous voulez approfondir et voir des aspects, on va dire, plus théoriques, vous pouvez parcourir également :
#
#   * https://nbhosting.inria.fr/auditor/notebook/python3-s2:mooc/w5/w5-s6-c2-modules-et-chemins
#   * https://nbhosting.inria.fr/auditor/notebook/python3-s2:mooc/w5/w5-s7-c3-packages
#   * https://nbhosting.inria.fr/auditor/notebook/python3-s2:mooc/w5/w5-s7-c4-import-advanced
#
# dans lesquels on explique plus en détail les différents mécanismes mis en oeuvre dans le système de chargement des modules et des packages en Python.
#
# **Consignes** :
#
# * au minimum vous devez répondre au quiz ci-dessous;
# * si votre **projet informatique est en Python**, il sera impératif que vous suiviez ces bonnes pratiques pour le rendu.

# %% [markdown]
#
# ## cours sur dataviz et notebooks interactifs

# %% [markdown]
# Mêmes modalités, on va s'appuyer sur des contenus du MOOC Python3, je vous invite à étudier ces éléments :
#
# #### dataviz en Python
#
# * https://nbhosting.inria.fr/auditor/notebook/python3-s2:mooc/w7/w7-s10-c3-notebooks-interactifs
# * https://nbhosting.inria.fr/auditor/notebook/python3-s2:mooc/w7/w7-s10-c4-animations-matplotlib
# * https://nbhosting.inria.fr/auditor/notebook/python3-s2:mooc/w7/w7-s10-c5-bokeh-et-al
# * https://nbhosting.inria.fr/auditor/notebook/python3-s2:mooc/w7/w7-s10-c6-fourier-k3d
#
# #### exercices :
#
# * https://nbhosting.inria.fr/auditor/notebook/python3-s2:mooc/w7/w7-s10-x1-taylor
# * https://nbhosting.inria.fr/auditor/notebook/python3-s2:mooc/w7/w7-s10-x2-coronavirus
#
# **Consignes**
#
# * faites passer à votre enseignant votre travail pour au moins un des deux exercices ci-dessus; pour les élèves rapides, n'hésitez pas à les traiter tous les deux.
#

# %% [markdown]
# # le quiz d'aujourd'hui

# %% [markdown]
# Évaluez la cellule suivante pour voir le quiz, que nous vous demandons de remplir **le plus tôt possible après avoir suivi le cours**.
#
# <span style="background-color:red; padding: 10px; margin-top: 5px;">On relèvera les résultats le jour du cours à 20:00</span>

# %% [markdown]
# Rappel du mode d'emploi :
#
# * vous avez plusieurs essais pour y répondre, n'hésitez pas à revenir en arrière sur le cours en cas de besoin; vous avez le droit de faire tourner le code localement pour répondre
# * toutes les questions ont au moins une réponse valable, si vous ne cochez aucune réponse on considère que vous préférez ne pas répondre
# * le signe ♧ (c'est le cas pour toutes les questions ici) indique que plusieurs réponses sont possibles
#
#
# * le barême est indiqué pour chaque question, par exemple `4 pts / -1 pt / 0 pt`  
#   pour **bonne** réponse, **mauvaise** réponse, **pas de réponse**, respectivement
# * votre score est calculé à chaque tentative, vous obtenez comme note finale **le meilleur** de ces scores  
# * mais notez que le score est calculé comme un tout pour le quiz en entier; du coup ce n'est pas parce que vous avez répondu au moins une fois correctement à la question 1 que vous aurez les points correspondants
# * vous aurez donc une note même si vous n'utilisez pas tous vos essais  
#   il se peut que votre note soit supérieure au score final affiché, qui correspond à la dernière tentative

# %% [markdown]
# <span style="background-color:red; padding: 10px; margin-top: 5px;">
# N'oubliez pas de traiter aussi au moins un des deux exercices (Taylor et coronavirus) consacrés à la deuxième partie.</span>

# %%
from nbautoeval import run_yaml_quiz

# %%
# xxx REMOVE ME
# juste pour remettre les compteurs à zéro pendant qu'on relit

from nbautoeval.storage import storage_clear
storage_clear("repo-structure-and-dataviz")
# xxx REMOVE ME

# %% scrolled=false
run_yaml_quiz("quiz-extra2", "quiz-all")
