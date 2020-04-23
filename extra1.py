# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     formats: py:percent
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.3.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   notebookname: "tutorat sujet \xE9valuation"
#   toc:
#     base_numbering: 1
#     nav_menu: {}
#     number_sections: true
#     sideBar: true
#     skip_h1_title: false
#     title_cell: Table of Contents
#     title_sidebar: Contents
#     toc_cell: false
#     toc_position: {}
#     toc_section_display: true
#     toc_window_display: false
# ---

# %% [markdown]
# # cours ***Python avancé*** - 24 Avril 2020

# %% [markdown]
# Le thème du jour :
#
# > programmation asynchrone avec les coroutines : `async`, `await` et `asyncio`

# %% [markdown]
# ## inscrivez-vous sur `fun-mooc.fr`

# %% [markdown]
# La charpente du cours d'aujourd'hui, cela tombe bien avec le confinement, est **[extraite d'un MOOC](https://www.fun-mooc.fr/courses/course-v1:UCA+107001+session02/about)** en ligne sur [le site de **France Université Numérique**](https://www.fun-mooc.fr/).
#
# Aussi nous allons vous demander de vous inscrire sur cette plateforme qui est entièrement publique et gratuite.
#
# Enregistrez-vous pour le cours [qui s'appelle "**Python3: des fondamentaux aux concepts avancés du langage**"](https://www.fun-mooc.fr/courses/course-v1:UCA+107001+session02/about)
#

# %% [markdown]
# ## le sujet d'aujourd'hui : la semaine nº8

# %% [markdown]
# Nous vous invitons à suivre **la semaine nº8** intitulée "Programmation asynchrone - asyncio".  
# Pour la trouver, une fois inscrit allez dans l'onglet *Cours* et naviguez dans le contenu comme indiqué ci-dessous.  
# Le cours de cette semaine 8 contient 9 sections (flêche 3) et chacune contient une vidéo, et éventuellement des notebooks de complément (flêche 4).
#
# <img src="mooc.png" width="400px">

# %% [markdown]
# ## un petit quiz

# %% [markdown]
# Évaluez la cellule suivante pour voir le quiz, que nous vous demandons de remplir le plus tôt possible après avoir suivi le cours.
#
# Mode d'emploi :
#
# * toutes les questions ont au moins une réponse valable, si vous ne cochez aucune réponse on considère que vous préférez ne pas répondre
# * le barême est indiqué pour chaque question; par exemple `3 pt / -1 pt / 0 pt` signifie
#   * 3 points pour une bonne réponse
#   * -1 point en cas de réponse fausse
#   * 0 point si vous ne répondez pas du tout
# * les questions avec un ♧ indiquent que plusieurs réponses sont possibles; dit autrement, lorsque la question n'a pas de ♧, le fait de cliquer une réponse va dévalider les autres
# * vous avez plusieurs essais pour y répondre, n'hésitez pas à revenir sur les vidéos en cas de besoin)

# %%
from quiz_asyncio import quiz
quiz.widget()
