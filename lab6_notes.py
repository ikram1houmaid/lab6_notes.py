
notes = [14, 10, 18, 9, 16, 19, 11, 13]

# Vérifier si la liste est vide
if not notes:
    print("Aucune note à traiter.")

else:
    # ==========================================
    # Étape 1 : Calculer la moyenne
    # ==========================================

    total = 0
    nb_notes = len(notes)

    for note in notes:
        total += note

    moyenne = total / nb_notes

    print("Moyenne :", f"{moyenne:.2f}")

    # ==========================================
    # Étape 2 : Ajouter un bonus de +1
    # ==========================================

    notes_bonus = [min(note + 1, 20) for note in notes]

    print("Notes après bonus :", notes_bonus)

    # ==========================================
    # Étape 3 : Filtrer les notes validées
    # ==========================================

    seuil = 12

    notes_valides = [note for note in notes if note >= seuil]

    print(f"Notes >= {seuil} :", notes_valides)

    # ==========================================
    # Étape 4 : Générer un rapport texte
    # ==========================================

    moyenne_initiale = sum(notes) / nb_notes
    moyenne_bonus = sum(notes_bonus) / len(notes_bonus)

    lignes = []

    lignes.append("=== Rapport des notes ===")
    lignes.append(f"Nombre d'étudiants : {nb_notes}")
    lignes.append(f"Notes originales : {notes}")
    lignes.append(f"Notes après bonus : {notes_bonus}")
    lignes.append(f"Moyenne initiale : {moyenne_initiale:.2f}")
    lignes.append(f"Moyenne après bonus : {moyenne_bonus:.2f}")
    lignes.append(
        f"Notes >= {seuil} : {notes_valides} "
        f"(soit {len(notes_valides)} étudiants)"
    )

    lignes.append("Détails par étudiant :")

    for index, note in enumerate(notes, start=1):
        bonus = notes_bonus[index - 1]

        lignes.append(
            f"Étudiant {index:02d} — "
            f"note {note:>5.2f} → bonus {bonus:>5.2f}"
        )

    # Fusionner les lignes
    rapport = "\n".join(lignes)

    # Afficher le rapport
    print("\n" + rapport)

    # Sauvegarder dans un fichier texte
    with open("rapport_notes.txt", "w", encoding="utf-8") as f:
        f.write(rapport)

    print("\nRapport sauvegardé dans rapport_notes.txt")

    # ==========================================
    # Étape 5 : Aller plus loin
    # ==========================================

    # Top 3 des meilleures notes
    top3 = sorted(notes, reverse=True)[:3]

    print("\nTop 3 des meilleures notes :", top3)
