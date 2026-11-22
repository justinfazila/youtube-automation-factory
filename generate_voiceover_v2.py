import asyncio
import edge_tts
import os

TEXT_V2 = """
3 heures de cours magistral. 2 heures de reunion Teams. Tout ça pour des notes illisibles ou une page blanche ?
Regarde : Fichier audio de 3 heures converti en texte propre en 18 secondes.
C'est Whisper en local. Gratuit. Prive. 2 minutes de configuration. Je te montre tout.

Bienvenue sur Le Bon Raccourci, la chaîne qui te donne un problème, une démo, une solution en moins de 10 minutes.
Le problème : Tu passes 5 heures par semaine à réécouter tes cours ou réunions pour en tirer 10 minutes d'infos utiles. C'est 260 heures par an perdues.
La promesse : À la fin de cette vidéo, tu auras un système qui transforme n'importe quel audio en texte structuré, recherchable, exportable en 2 minutes chrono. Gratuit, local et sans compte.

Au programme aujourd'hui, 3 démos progressives :
Premièrement, Whisper Web : Zéro installation, test immédiat dans ton navigateur.
Deuxièmement, Whisper Local : Installation 1-clic, puissance illimitée et 100% privé.
Troisièmement, le Workflow Pro : Raccourci clavier, export automatique vers Notion et Word, avec un dossier surveillé.

Et en bonus : Mon template Notion Cours et Réunions et la checklist d'installation sont offerts en description. C'est parti.

Démo 1 : Whisper Web. Si tu veux tester tout de suite sans rien installer, direction Hugging Face avec Whisper Web. Tu glisses ton fichier audio, tu choisis le modèle, et en quelques secondes le texte apparaît. C'est parfait pour un besoin ponctuel.

Démo 2 : Whisper Local. Pour aller plus loin et garder 100% de tes données privées sur ton PC, on installe Whisper en local. Une simple ligne de commande et ton ordinateur devient une usine à transcription automatique ultra rapide.

Démo 3 : Workflow Pro et Automatisation. Maintenant, on connecte Whisper à un raccourci clavier et un dossier surveillé. Dès que tu déposes un enregistrement audio, Whisper le transcrit automatiquement et l'envoie dans ton espace Notion avec un résumé structuré.

En résumé, tu as maintenant le bon raccourci pour ne plus jamais perdre de temps à prendre des notes à la main.
Télécharge la checklist et le template Notion en description, abonne-toi et active la cloche pour le prochain raccourci !
"""

async def generate():
    os.makedirs("assets/audio/video-2", exist_ok=True)
    output_file = os.path.join("assets", "audio", "video-2", "voiceover_raw.mp3")
    print("[VOICE] Generation voix off Vidéo #2 avec fr-FR-HenriNeural...")
    
    communicate = edge_tts.Communicate(
        text=TEXT_V2,
        voice="fr-FR-HenriNeural",
        rate="-5%",
        pitch="+2Hz"
    )
    
    await communicate.save(output_file)
    size_mb = os.path.getsize(output_file) / (1024 * 1024)
    print(f"[SUCCESS] Voix off Vidéo #2 générée avec succès ! ({size_mb:.2f} MB)")
    print(f"[FILE] Fichier : {output_file}")

if __name__ == "__main__":
    asyncio.run(generate())
