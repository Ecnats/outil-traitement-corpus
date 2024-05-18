# outil-traitement-corpus
constance tauliaut 

Tâche à réaliser : Summarization

Corpus : https://huggingface.co/datasets/cnn_dailymail 

type de prédiction :
permet de faire une synthèse extractive et abstraite de plus de 300 000 documents

à quel modèle il a servi : 
la summarization a servi pour le modèle de pré-traitement BART (sur de grands textes) 
https://huggingface.co/facebook/bart-large-cnn
https://huggingface.co/sshleifer/distilbart-cnn-12-6


choses à apprendre :
La première version de cette tâche servait était déstinée à  développer pour la lecture et la compréhension automatiques et donner une réponse aux questions abstraites.
La métrique ROUGE, or Recall-Oriented Understudy for Gisting Evaluation, permet de mesurer l'efficacité. 
Pour l'anglais des Etats-Unis et du Royaume-Unis, le code BCP (étiquette d'identification de langue) sont différents. Il y a au moins ces 2 variétes. Pas d'autres informations sur d'éventuels autres anglais.
Pour la structure des données : placé dans un dictionnaire, il y a un élément id (string contenant le format SHA1 qui corespond à l'url de l'article, un élément article (chaine de caractères) et un élément mots clés/points forts (chaine de caractères qui contient les points fort de l'article).  
Source utilisé : articles de presse CNN/Daily Mail
Limitation rencontrée: grâce à l'étude de Chen&Al on apprend qu'ils ont rencontrés 100 cas aléatoires considérés comme étant difficiles, pour répondre de façon correct à des questions du à des erreurs d'ambiguité et de co-référence (concernant la version 1 de la tâche, qui était de faire de la compréhension automatique et de donner une réponse à des questions.)

Il y a une sous tâche qui sert à la récapitulation, à la réalisation de résumé de nouveaux articles. 
Cette tâche est utilisée dans train, validation et test. 


## création de mes données
J'ai scrappé mes données sur le site https://www.iletaitunehistoire.com/genres/contes-et-legendes. Elles ont été enregistrés dans un fichier csv sur lequel j'ai appliqué une analyse morphosyntaxique en utilisant le modèle spaCy. 

## visualisation des données
Le script visualise_data.ipynb a pour but de montrer comment on peut exploiter les données. Avec ce script nous récupérons divers graphiques pour voir la taille des documents, la distributions des parties du discours (POS), la répartitions des histoires dans les différentes catégories de sentiment. Et on peut également avoir des nuages de mot, pour constater les termes qui sont les plus souvents utiliser dans les histoires et les résumés du corpus. 

## métrique
Le script metrique.ipynb permet de calculer les métriques ROUGE (Recall-Oriented Understudy for Gisting Evaluation) qui servent à évaluer les résumés automatique. Les scores ROUGE sont calculés une fois avec prétraitement (sans stopword,s, sans ponctuations, lemmatiser et stemmer) et sans prétraitement, afin de constater si les résultats sont meilleurs. Malheureusement, les résultats ne sont pas très concluants car les résumés des contes de mon corpus sont trop petits. Ce script tente également de calculer la corrélation de Spearman et de Pearson. 

## points d'amélioration
Le corpus que j'ai choisis ne contient pas assez de données, du moins en ce qui concerne les résumés. En effet, je ne peux pas réellement utiliser les analyses réalisées sur les données des résumés car il y en a trop peu. Les chiffres obtenus ne suffisent pas, pour avoir des informations intéressantes. 
Des résumés sur des romans ou des articles de presses, auraient été plus interessant à examiner. Et avoir une centaine d'éléments. 

