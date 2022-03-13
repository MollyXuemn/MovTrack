
**User story** :information_desk_person:
	
1.1 (1er sprint -> 17/3/22)</br>


**En tant que**

Gestionnaire de donnée </br>


**Je veux**

Administrer une base de données de LifeMomentSequence. La BDD contient la liste des différentes LifeMomentSequence et les métadonnées associées suivantes :  

 - début / fin 

 - identifiant_capteur 

 - identifiant_individu 

 - liste_de_tags (vide au départ) 

 - le CSV de Skeleton associé (directement dans la base ou sous la forme d’un chemin vers un fichier stocké quelque part) </br>
 

**Afin que** :trollface:

Stocker les données posturales sous une forme interrogeable. 

Le BBD en format:
```json
{
   "camera_id" : 
   "individual_id" :
   "liste_de_tags": -t immobile
}
```
