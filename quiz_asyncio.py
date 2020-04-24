from nbautoeval import Quiz, QuizQuestion, Option, CodeOption, MathOption, MarkdownOption
from nbautoeval import TextContent, MarkdownContent

# NOTE à propos de markdown
# dans cette première question j'avais dans un premier
# temps utilisé un bloc entre ```
# et il s'avère que ça marchouille seulement
# 
# à terme on pourrait imaginer utiliser une autre librairie 
# de markdown, je pense à celui de jupyter notebook...

# common score
SCORE = 4

questions = []


#
questions.append(
QuizQuestion(
    score=SCORE,
    question=MarkdownContent(
"""
On a besoin d'écrire un programme très gourmand en calcul; 
le problème se découpe bien en morceaux indépendant les uns des autres;
on veut absolument utiliser Python pour écrire ce programme;
on dispose d'une machine avec 64 processeurs, et on essaie de se débrouiller
pour les utiliser au mieux.
<br>Cochez les options qui sont raisonnables dans ce contexte :
"""),
#    question2="",
    options=[
        MarkdownOption("""
on crée autant de processus que 
de morceaux, en assemblant les résultats à la fin
""", correct=True),
        MarkdownOption("""
on crée autant de threads que 
de morceaux, en assemblant les résultats à la fin
"""),
        MarkdownOption("""
on crée autant de coroutines que de morceaux, on synchronise les résultats 
grâce à `asyncio.gather` et ainsi on peut assembler les résultats
"""),
    ],
))


#
questions.append(
QuizQuestion(
    score=SCORE,
        question=MarkdownContent(
"""
Indiquer, parmi les opérations suivantes, 
celles qui sont susceptibles d'induire un délai sensible dans du code synchrone,
et que vous pourriez avoir intérêt à gérer de manière asynchrone pour 
rendre votre application plus efficace ou plus réactive :
"""),
    question2="",
    options=[
        MarkdownOption("accès réseau", correct=True),
        MarkdownOption("attente d'événements liés à des sous-process", correct=True),
        MarkdownOption("temporisation/attente volontaire", correct=True),
        MarkdownOption("accès au disque dur ou base de données", correct=True),
        MarkdownOption("accès à la mémoire vive"),
        MarkdownOption("accès au terminal", correct=True),
    ],
))


# 
questions.append(
QuizQuestion(
    score=SCORE,
    question=MarkdownContent(
"""
On considère le code suivant :

***

    import asyncio

    async def foo():
        await asyncio.sleep(0.1)
        return 42

    async def bar():
        await asyncio.sleep(0.05)
        return 58

    async def both():
        return await asyncio.gather(foo(), bar())

    results = asyncio.run(both())
    print(results[0])
"""),
    question2=TextContent("""
    On exécute ce code dans un interpréteur python;
    <br> cochez parmi les assertations suivantes 
    <br> celles qui sont vraies à la fin de de l'exécution
    """),
    options=[
        MarkdownOption("le programme affiche `42`", correct=True),
        MarkdownOption("le programme dure 100ms", correct=True),
        MarkdownOption("le programme affiche `58`"),
        MarkdownOption("le programme dure 150ms"),
        MarkdownOption("le programme dure 50ms"),
        MarkdownOption("rien ne s'exécute, à cause d'une erreur"),
    ],
    horizontal_layout=True,
))


# 
questions.append(
QuizQuestion(
    score=SCORE,
    question=MarkdownContent(
"""
On considère le code suivant :

***

    import asyncio

    async def foo():
        await asyncio.sleep(0.1)
        return 42

    async def bar():
        await asyncio.sleep(0.05)
        return 58

    async def one():
        return await asyncio.wait(
            [foo(), bar()],
            return_when=asyncio.FIRST_COMPLETED)

    done, pending = asyncio.run(one())

    one_done = done.pop()
    print(one_done.result())
"""),
    question2=TextContent("""
    On exécute ce code dans un interpréteur python;
    <br> cochez parmi les assertations suivantes 
    <br> celles qui sont vraies à la fin de de l'exécution
    """),
    options=[
        MarkdownOption("le programme affiche `42`"),
        MarkdownOption("le programme dure 100ms"),
        MarkdownOption("le programme affiche `58`", correct=True),
        MarkdownOption("le programme dure 150ms"),
        MarkdownOption("le programme dure 50ms", correct=True),
        MarkdownOption("rien ne s'exécute, à cause d'une erreur"),
    ],
    horizontal_layout=True,
))

quiz1 = Quiz(
    "asyncio1",
    max_attempts=4,
    questions=questions,
    max_grade=20,
    shuffle=False,
)

############################################################
questions = []

# 
questions.append(
QuizQuestion(
    score=SCORE,
    question=MarkdownContent(
"""
On considère le code suivant :

***

    import asyncio

    async def foo():
        await asyncio.sleep(1)
        print("done")
        return 42
        
    x = foo()
"""),
    question2=TextContent("""
    On exécute ce code dans un interpréteur python;
    <br> cochez parmi les assertations suivantes 
    <br> celles qui sont vraies à la fin de de l'exécution
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
questions.append(
QuizQuestion(
    score=SCORE,
    question=MarkdownContent(
"""
On considère le code suivant :

***

    import asyncio

    async def main():
        print("dans main")
        await asyncio.sleep(1)

    coro = main()
    coro.send(None)


"""),
    question2=TextContent("""
    On exécute ce code dans un interpréteur python,
    <br> cochez parmi les assertions suivantes celles qui sont vraies :
    """),
    options=[
        MarkdownOption("le programme affiche `dans main`", correct=True),
        MarkdownOption("une exception est levée car `main` n'a jamais été awaitée"),
        MarkdownOption("le programme dure quelques millisecondes", correct=True),
        MarkdownOption("le programme dure 1 s"),
    ],
    horizontal_layout=True,
))


#
questions.append(
QuizQuestion(
    score=SCORE,
    horizontal_layout=True,
    question=MarkdownContent(
"""
On considère le code suivant :

***
    class Awaitable():
        def __init__(self, message):
            self.message = message

        def __await__(self):
            factor = yield "initialisation"
            for char in self.message:
                factor = yield char*factor

    async def main(message):
        await Awaitable(message)

    message = "abcdef"
    coro = main(message)
    ret = coro.send(None)

    for i in range(1, len(message)+1):
        print(coro.send(i))

"""),
    question2=TextContent("""
    On exécute ce code dans un interpréteur python,
    <br> cochez parmi les assertions suivantes celles qui sont vraies :
    """),
    options=[
        MarkdownOption("une exception est levée car `main` n'a jamais été awaitée"),
        MarkdownOption("le programme affiche seulement `abcdef`"),
        MarkdownOption("le programme affiche une pyramide avec 1 `a`, 2 `b`, etc", correct=True),
        MarkdownOption("la variable `ret` vaut `None`"),
        MarkdownOption("la variable `ret` vaut `'initialisation'`", correct=True),
    ],
))


#
questions.append(
QuizQuestion(
    score=SCORE,
    horizontal_layout=True,
    question=MarkdownContent(
"""
On considère le code suivant :

***
    import asyncio

    TICK = 0.05

    async def c1():
        print(">>> c1")
        await asyncio.sleep(1*TICK)
        asyncio.ensure_future(c2())
        await asyncio.sleep(3*TICK)
        print("<<< c1")
        asyncio.get_event_loop().stop()

    async def c2():
        print(">>> c2")
        await asyncio.sleep(1*TICK)
        print("<<< c2")
        asyncio.get_event_loop().stop()

    asyncio.ensure_future(c1())
    try:
        print("Début")
        asyncio.get_event_loop().run_forever()
        print("Milieu")
        asyncio.get_event_loop().run_forever()
        print("Fin")
    except KeyboardInterrupt:
        print("bye")
    print("done")
"""),
    question2=TextContent("""
    On exécute ce code dans un interpréteur python,
    <br> cochez parmi les assertions suivantes celles qui sont vraies :
    """),
    options=[
        MarkdownOption("le programme s'exécute et seulement `done` s'affiche à la fin"),
        MarkdownOption("le message `<<< c1` apparaît entre `Début` et `Milieu`"),
        MarkdownOption("le message `<<< c1` apparaît entre `Milieu` et `Fin`", correct=True),
        MarkdownOption("l'utilisateur doit forcer l'arrêt du programme au clavier"),
        MarkdownOption("le message `>>> c2` n'apparaît jamais"),
        MarkdownOption("le message `<<< c2` apparaît entre `Début` et `Milieu`", correct=True),
        MarkdownOption("le message `Milieu` apparait 100ms après le début du programme", correct=True),
        MarkdownOption("le message `Milieu` apparait 200ms après le début du programme"),
    ],
))


quiz2 = Quiz(
    "asyncio2",
    max_attempts=4,
    questions=questions,
    max_grade=20,
    shuffle=False,
)
