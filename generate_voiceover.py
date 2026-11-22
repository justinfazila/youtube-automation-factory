#!/usr/bin/env python3
"""
Génération voix off Vidéo #1 - Le Bon Raccourci
Utilise Edge-TTS (gratuit, local) avec voix fr-FR-HenriNeural
"""

import edge_tts
import asyncio
import os

# Configuration voix
VOICE = "fr-FR-HenriNeural"
RATE = "-5%"
PITCH = "+2Hz"

# Texte brut nettoyé (sans balises SSML)
TEXT = """Si tu pensais que l'Intelligence Artificielle était juste pour les développeurs et les géants de la tech, tu es sur le point de découvrir une erreur colossale qui te coûte de l'argent chaque jour.

Dans les 30 prochaines secondes, je vais te révéler le premier secret qui a permis à des milliers d'entrepreneurs de doubler leur productivité sans embaucher une seule personne. Et non, ce n'est pas ChatGPT.

Bienvenue sur notre chaîne, le canal qui te montre comment dompter l'IA pour conquérir ton business. Aujourd'hui, nous allons te dévoiler 7 secrets d'IA que les entrepreneurs qui réussissent gardent jalousement pour eux.

Tu apprendras comment automatiser tes tâches chronophages, générer des revenus passifs et prendre une longueur d'avance sur la concurrence.

Reste jusqu'à la fin, car le secret numéro 7 va littéralement changer la façon dont tu travailles pour toujours.

Secret 1 : L'Automatisation Invisible des Processus. Pense "Processus" et non "Outil". La plupart des gens se demandent "Quel outil IA dois-je utiliser ?". Les pros eux se demandent "Quel est le processus chiant que je peux faire disparaître ?". Prends par exemple ta gestion des e-mails. Au lieu de passer 2 heures par jour à répondre aux mêmes questions clients, crée un agent IA qui répond automatiquement avec 95% de précision.

Secret 2 : Le Prompting Spécialisé vs Généraliste. Un prompt généraliste ne fait que te faire perdre du temps. Les entrepreneurs à succès n'utilisent pas de prompts copiés-collés trouvés sur internet. Ils créent des "Prompts Système" sur-mesure, adaptés à leur niche. Un prompt pour un avocat ne peut pas être le même que pour un coach en développement personnel. C'est le secret de la productivité.

Secret 3 : L'IA comme Générateur de Contenu de Marque. Tu ne crées pas juste du contenu, tu construis un actif. Utilise l'IA pour créer une bibliothèque de contenus evergreen : articles de blog, scripts YouTube, posts LinkedIn. Ces contenus continueront de générer du trafic pour toi pendant des années sans que tu n'aies à y toucher.

Secret 4 : La Synergie IA Automatisation. Combine l'IA avec les outils d'automatisation comme Zapier, Make ou n8n. Par exemple : Un nouveau client remplit un formulaire, l'IA génère un devis personnalisé, le devis est envoyé automatiquement par e-mail, le rappel de paiement est programmé. Tout cela sans une seule intervention humaine.

Secret 5 : La Recherche de Marché en Temps Réel. Les entrepreneurs savent que l'information est la nouvelle monnaie. Utilise l'IA pour scanner en temps réel les tendances de ton marché, analyser les avis de la concurrence sur Google et Amazon, et identifier les failles qu'ils ne voient pas.

Secret 6 : Le Testing à l'Infini. Tu n'as plus besoin de deviner ce qui fonctionne. Fais tester 100 variantes de ta page de vente par l'IA en quelques minutes. Analyse les taux de conversion potentiels, identifie les points de friction et optimise avant même de lancer ta campagne.

Secret 7, LE PLUS PUISSANT : La Création de Produits Digitaux Instantanés. Tu peux maintenant créer un produit digital complet en une après-midi. Imagine : un e-book de 100 pages, un cours vidéo avec script, un workbook interactif. Le tout généré par l'IA et personnalisé à ton audience. C'est le chemin le plus rapide vers un revenu passif.

C'est tout pour aujourd'hui. Tu viens de découvrir les 7 secrets qui séparent les entrepreneurs qui stagnent de ceux qui explosent grâce à l'IA.

Si tu veux que je t'apprenne comment mettre en place ces systèmes étape par étape, abonne-toi et active la cloche.

Clique sur la vidéo à côté pour apprendre comment automatiser ta chaîne YouTube avec l'IA en 5 étapes simples.

À demain pour un nouveau secret."""

async def main():
    # Créer le dossier de sortie
    output_dir = "assets/audio/video-1"
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, "voiceover_raw.mp3")
    
    print(f"[VOICE] Generation voix off avec {VOICE}...")
    print(f"[OUTPUT] Sortie : {output_path}")
    print(f"[CONFIG] Rate: {RATE}, Pitch: {PITCH}")
    print(f"[TEXT] Longueur texte : {len(TEXT)} caractères (~{len(TEXT)//15} mots)")
    
    communicate = edge_tts.Communicate(TEXT, VOICE, rate=RATE, pitch=PITCH)
    await communicate.save(output_path)
    
    # Vérifier le fichier généré
    if os.path.exists(output_path):
        size_mb = os.path.getsize(output_path) / (1024 * 1024)
        print(f"[SUCCESS] Voix off générée avec succès ! ({size_mb:.2f} MB)")
        print(f"[FILE] Fichier : {output_path}")
    else:
        print("[ERROR] Erreur : fichier non généré")

if __name__ == "__main__":
    asyncio.run(main())