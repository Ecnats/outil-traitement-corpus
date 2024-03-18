# outil-traitement-corpus

Tâche à réaliser : Summarization

Corpus : https://huggingface.co/datasets/cnn_dailymail 

type de prédiction :
permet de faire une synthèse extractive et abstraite de plus de 300 000 documents

à quel modèle il a servi : 
la summarization a servi pour le modèle de pré-traitement BART (sur de grands textes) 
https://huggingface.co/facebook/bart-large-cnn
https://huggingface.co/sshleifer/distilbart-cnn-12-6


choses à apprendre :
La première version de cette tâche servait était déstinée à  développer pour la lecture et la compréhension automatiques et donner une réponse aux 
questions abstraites.
La métrique ROUGE, or Recall-Oriented Understudy for Gisting Evaluation, permet de mesurer l'efficacité. 
Pour l'anglais des Etats-Unis et du Royaume-Unis, le code BCP (étiquette d'identification de langue) sont différents. IL y a au moins ces 2 
variétes. Pas d'autres informations sur d'éventuels autres anglais.
Pour la structure des données : placé dans un dictionnaire, il y a un élément id (string contenant le format SHA1 qui corespond à l'url de l'article,
un élément article (chaine de caractères) et un élément mots clés/points forts (chaine de caractères qui contient les points fort de l'article).  
Source utilisé : articles de presse CNN/Daily Mail
Limitation rencontrée: grâce à l'étude de Chen&Al on apprend qu'ils ont rencontrés 100 cas aléatoires considérés comme étant difficiles, pour 
répondre de façon correct à des questions du à des erreurs d'ambiguité et de co-référence (concernant la version 1 de la tâche, qui était de faire 
 de la compréhension automatique et de donner une réponse à des questions.)

IL y a une sous tâche qui sert à la récapitulation, à la réalisation de résumé de nouveaux articles. 
Cette tâche est utilisée dans train, validation et test. 
