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
#   notebookname: programmation asynchrone
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
#   version: '1.0'
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
# Enregistrez-vous pour le cours [qui s'appelle "**Python3 : des fondamentaux aux concepts avancés du langage**"](https://www.fun-mooc.fr/courses/course-v1:UCA+107001+session02/about)
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
# ## rappel à propos de `asyncio.run()`

# %% [markdown]
# C'est expliqué dans un complément du cours, mais juste pour insister sur ce point :
#
#
# À l'époque du tournage des vidéos, on a utilisé Python-3.6 et on a dû utiliser cette construction un peu lourde :
#
# ```python
# # nécessaire en Python-3.6
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(unecoroutine())
# ```
#
# Avec le Python d'aujourd'hui - disons Python-3.7 - on peut remplacer cela par un idiome plus léger :
#
# ```python
# # suffisant en Python-3.7
#
# asyncio.run(unecoroutine())
# ```

# %% [markdown]
# Et notez aussi, si vous travaillez dans un notebook, que vous pouvez alors faire tout simplement comme ceci (mais attention ça ne marche que dans le notebook, ou dans `ipython`) :

# %%
# définissons une coroutine 
import asyncio

async def unecoroutine():
    await asyncio.sleep(0.5)
    print("après un petit délai")

# %%
# dans IPython c'est encore plus simple maintenant 

await unecoroutine()

# %% [markdown]
# ## un petit quiz

# %% [markdown]
# Évaluez la cellule suivante pour voir le quiz, que nous vous demandons de remplir **le plus tôt possible après avoir suivi le cours**.
#
# <span style="background-color:red; padding: 5px; margin-top: 5px;">On relèvera les résultats le lundi 27 dans la matinée</span>

# %% [markdown]
# Mode d'emploi :
#
# * toutes les questions ont au moins une réponse valable, si vous ne cochez aucune réponse on considère que vous préférez ne pas répondre
# * le signe ♧ (c'est le cas pour toutes les questions ici) indique que plusieurs réponses sont possibles
# * le barême est indiqué pour chaque question; par exemple `3 pt / -1 pt / 0 pt` signifie
#   * 3 points pour une bonne réponse
#   * -1 point en cas de réponse fausse
#   * 0 point si vous ne répondez pas du tout (à nouveau : si vous ne cochez aucune option)
# * vous avez plusieurs essais pour y répondre, n'hésitez pas à revenir sur les vidéos en cas de besoin); bien entendu, il n'y a pas d'effet cumulatif, le résultat final correspond exactement à votre dernier essai : si vous répondez correctement à la première tentative à la question 1, mais qu'ensuite vous changez d'avis, vous perdez ces points.

# %%
from quiz_asyncio import quiz

quiz.widget()

# %% [markdown]
# ## pour les rapides

# %% [markdown]
# Si vous avez terminé de suivre le cours sur le MOOC, que vous avez répondu au quiz, et que vous voulez approfondir, voici quelques idées pour poursuivre la découverte

# %% [markdown]
# ### exo -  niveau facile
#
# modifiez `async_http.py` pour que le programme affiche un 'tick' à une certaine fréquence, par exemple toutes les 100ms

# %% [markdown]
# ### exo - niveau intermédiaire
#
# dans `game.py`, on veut limiter le nombre de sous-processus  
# modifiez `game.py` pour garantir que, quel que soit la vitesse à laquelle on crée des sous-process au clavier, on ne conserve en tout qu'au maximum, disons 4, sous-processus

# %% [markdown]
# ### exo - niveau avancé
#
# récrivez un web scraper, qui dans l'esprit de `async_http.py` va chercher autant qu'il peut des pages en parallèle;
# sauf que cette fois-ci, on veut quelque chose qui fonctionne par fermeture transitive;
# c'est à dire que je donne une ou plusieurs pages en entrée, on lit les résultats au fur et à mesure, et chaque fois qu'on trouve un lien HTML vers une autre page, on ajoute cette autre page à la liste des pages qu'on veut aller chercher.
#
# Pour éviter que ça ne parte en vrille, je vous conseille dans un premier temps de vous donner des hypothèse simplificatrices :
#
# * on part de exactement une page
# * on se restreint aux pages qui sont dans le même domaine - le même site quoi..
#
# cela permet en principe d'*aspirer* entièrement les petits sites statiques; si vous n'avez pas d'exemple sous la main vous pouvez vous entrainer avec <https://r2lab.inria.fr/> qui entre dans cette catégorie avec un nombre de pages raisonnable pour le sujet (quelques dizaines en tout)
#
# **Hints** 
#
# * pour trouver les hyperliens; souvenez-vous du cours HTML, un hyperlien ça se présente sous ce genre de forme  
#   `<a href="http://un.autre.endroit/">`  
#   on pourrait penser utiliser des expressions régulières mais je ne vous conseille pas trop, il y a énormément de variantes possibles : ça peut être des quotes doubles ou simples, il peut y avoir d'autres attributs que le `href` dans le tag `<a>` et dans n'importe quel ordre…  
#   pour faire ces traitements-là je vous conseille la librairie `beautifulsoup4` - voyez plus bas
#   
#   https://stackoverflow.com/questions/3075550/how-can-i-get-href-links-from-html-using-python
#   
# * c'est quoi cette histoire de domaine ?  
#   en partant de la page d'accueil d'un site, on veut souvent se concentrer sur ce site-là, et éviter de se perdre à aspirer tous les autres sites référencés à partir de là  

# %% [markdown]
# Voici un brouillon qui vous indique comment trouver les hyperliens dans une page :

# %%
# celle-ci vous commencez à la connaitre
import requests

# %%
# pour installer beautifulsoup4 comme si on était dans un terminal
# ! pip install beautifulsoup4

# %%
# dans le notebook, il se peut que vous ayez besoin de remédarrer 
# votre kernel après l'installation

# %%
# ça n'est pas habituel - heureusement d'ailleurs 
# mais cette librairie s'importe sous un autre nom que celui connu de pip
from bs4 import BeautifulSoup

# %%
# je vais chercher la page d'accueil
# notez bien, ici de manière séquentielle / synchrone
# je m'intéresse juste au traitement du HTML

html_page = requests.get("https://r2lab.inria.fr").text
print(f"le HTML de la page d'accueil contient {len(html_page)} caractères")

# %%
# pour trouver les liens
soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
    print(link.get('href'))

# %% [markdown]
# Comment ça se lit ? eh bien comme vous le devinez :
# . si l'url contient un nom de machine (comme https://r2labapi.inria.fr/) c'est l'url du lien
# . si elle commence par un `/`, c'est le chemin par rapport au domaine courant
# . si elle commence par autre chose, c'est le chemin par rapport au répertoire courant
#
# donc ici `/overview.md` et `news.md` se récrivent toutes les deux en `https://r2lab.inria.fr/overview.md` et `https://r2lab.inria.fr/news.md`
#
# mais si trouve ce HTML dans la page disons `https://r2lab.inria.fr/un/chemin/unepage.md`, alors `/overview.md` et `news.md` se récrivent en `https://r2lab.inria.fr/overview.md` et `https://r2lab.inria.fr/un/chemin/news.md` parce que le second est relatif au chemin courant.
