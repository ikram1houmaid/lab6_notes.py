# Lab 6 – Gestion des notes des étudiants en Python

## Description
Ce TP consiste à développer un programme Python permettant de gérer les notes des étudiants, de calculer les moyennes, d'appliquer un bonus et de générer un rapport détaillé.

## Objectifs
- Calculer la moyenne des notes des étudiants.
- Ajouter un bonus de +1 à chaque note sans dépasser 20.
- Filtrer les notes supérieures ou égales à un seuil.
- Générer un rapport détaillé dans un fichier texte.
- Identifier les trois meilleures notes.

## Étapes réalisées

### Étape 1 : Calcul de la moyenne
- Initialiser `total = 0`.
- Parcourir la liste avec une boucle `for`.
- Calculer la moyenne en divisant le total par le nombre de notes.
- Afficher la moyenne avec deux décimales.

### Étape 2 : Ajouter un bonus
- Utiliser une *list comprehension*.
- Ajouter 1 point à chaque note.
- Utiliser `min()` pour ne pas dépasser 20.

### Étape 3 : Filtrer les notes
- Définir un seuil de validation égal à 12.
- Utiliser une *list comprehension* avec une condition.
- Conserver uniquement les notes supérieures ou égales à 12.

### Étape 4 : Générer un rapport
- Calculer la moyenne initiale et la moyenne après bonus.
- Construire un rapport avec `append()`.
- Utiliser `enumerate()` pour afficher les détails de chaque étudiant.
- Fusionner les lignes avec `join()`.
- Sauvegarder le rapport dans `rapport_notes.txt`.

### Étape 5 : Améliorations
- Tester le programme avec différentes listes de notes.
- Gérer le cas d'une liste vide.
- Afficher le Top 3 des meilleures notes avec `sorted()`.

## Notions Python utilisées
- Variables et listes.
- Boucle `for`.
- Conditions `if`.
- Fonctions `len()`, `sum()`, `min()` et `sorted()`.
- List comprehension.
- Fonction `enumerate()`.
- Méthodes `append()` et `join()`.
- Gestion des fichiers avec `open()`.

## Structure du projet

```text
lab6_notes/
│
├── lab6_notes.py
├── rapport_notes.txt
└── README.md
```

## Exécution du programme

1. Ouvrir le dossier dans VS Code.
2. Ouvrir le terminal.
3. Exécuter la commande :

```bash
python lab6_notes.py
```

## Résultat attendu
Le programme affiche :
- Le nombre d'étudiants.
- Les notes originales.
- Les notes après bonus.
- La moyenne initiale et la moyenne après bonus.
- Les notes validées.
- Les détails de chaque étudiant.
- Le Top 3 des meilleures notes.

Un fichier `rapport_notes.txt` est également généré automatiquement.

## Conclusion
Ce TP permet de pratiquer les listes, les boucles, les conditions, les compréhensions de listes et la manipulation des fichiers en Python à travers un exemple concret de gestion des notes des étudiants.
<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/d6bc868c-57a9-40cc-b5cf-48ad3962158d" />
