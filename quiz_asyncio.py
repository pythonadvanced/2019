from nbautoeval import Quiz, QuizQuestion, Option, CodeOption, MathOption, MarkdownOption
from nbautoeval import TextContent, MarkdownContent

# NOTE à propos de markdown
# dans cette première question j'avais dans un premier
# temps utilisé un bloc entre ```
# et il s'avère que ça marchouille seulement
# 
# à terme on pourrait imaginer utiliser une autre librairie 
# de markdown, je pense à celui de jupyter notebook...

questions = []

# 
questions.append(
QuizQuestion(
    question=MarkdownContent(
"""
On considère le code suivant :

***

    import asyncio

    async def foo():
        await asyncio.sleep(0.2)
        print("done")
        return 42
        
    x = foo()
"""),
    question2=TextContent("""
    On exécute ce code avec un interpréteur python;
    <br> cochez parmi les assertations suivantes 
    <br> celles qui vraies à la fin de de l'exécution
    """),
    options=[
        MarkdownOption("rien n'est affiché", correct=True),
        MarkdownOption("le programme a affiché `done`"),
        MarkdownOption("la variable `x` vaut `42`"),
        MarkdownOption("(l'objet référencé par) la variable `x` est awaitable", correct=True),
        MarkdownOption("rien ne s'exécute, à cause d'une erreur de syntaxe"),
    ],
    horizontal_layout=True,
))

#
'''
questions.append(
QuizQuestion(
    question=MarkdownContent(
"""
"""),
    question2="",
    options=[
        Option(""),
    ],
))
'''

quiz = Quiz(
    "asyncio",
    max_attempts=3,
    questions=questions,
)

