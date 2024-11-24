PREAMBLE = """En tant que spécialiste expérimenté en résolution de problèmes, résolvez étape par étape les questions Mathématiques suivantes."""

# The default gsm8k prompt from the CoT paper
# https://arxiv.org/pdf/2201.11903.pdf page 35.

PROMPT = """Question : Dans le bosquet, il y a 15 arbres. Aujourd'hui, les travailleurs vont planter des arbres dans le bosquet. Après qu'ils auront fini, il y aura 21 arbres. Combien d'arbres les travailleurs ont-ils plantés aujourd'hui ?
Réponse : Commençons avec 15 arbres. Plus tard, nous aurons 21 arbres. La différence doit être le nombre d'arbres qu'ils ont plantés. Ainsi, ils ont dû planter 21 - 15 = 6 arbres. La réponse est 6.

Question : Si sur le parking il y a 3 voitures et que 2 autres arrivent, combien de voitures y a-t-il sur le parking ?
Réponse : Il y a déjà 3 voitures sur le parking. En arrivent 2 autres. Maintenant, il y en a 3 + 2 = 5. La réponse est 5.

Question : Lia avait 32 chocolats et sa sœur en avait 42. Si elles en ont mangé 35, combien leur en reste-t-il en tout ?
Réponse : Lia avait 32 chocolats et la sœur de Lia en avait 42. Cela signifie qu'au début, il y avait 32 + 42 = 74 chocolats. Il en a été mangé 35. Ainsi, au total, il leur reste 74 - 35 = 39 chocolats. La réponse est 39.

Question : Sean a cinq jouets. À Noël, il a reçu deux jouets de sa mère et deux de son père. Combien de jouets a-t-il maintenant ?
Réponse : Il a 5 jouets. Il a reçu 2 jouets de sa mère, et maintenant il en a 5 + 2 = 7. Ensuite, il a reçu 2 autres jouets de son père, ce qui fait un total de 7 + 2 = 9 jouets. La réponse est 9.

Question : Olivia a 23 dollars. Elle a acheté cinq bagels à 3 dollars chacun. Combien d'argent lui reste-t-il ?
Réponse : Elle a acheté 5 bagels à 3 dollars chacun. Cela signifie qu'elle a dépensé 5 * 3 dollars = 15 dollars pour les bagels. Au début, elle avait 23 dollars, donc maintenant elle a 23 dollars - 15 dollars = 8 dollars. La réponse est 8."""

TEMPLATE = """
Вопрос: {question}
Ответ: """