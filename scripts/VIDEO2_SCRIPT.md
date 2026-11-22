# 🎬 SCRIPT VIDÉO 2 - LE BON RACCOURCI
## "Comment transcrire AUTOMATIQUEMENT tes cours/réunions en texte (Gratuit, Local, 2 min)"

**Durée estimée** : 9 minutes  
**Format** : Vidéo faceless tutoriel — Narration IA (Edge-TTS) + Capture écran démo temps réel  
**Objectif** : Watch time > 55%, CTR > 12%, Conversion lead magnet (Template Notion + Checklist)  
**Slogan appliqué** : *"Un problème, une démo, une solution"*  
**Date tournage** : Mercredi (J+3) | **Publication** : Jeudi 10h (J+4)

---

## 🎯 0-30s — HOOK (3 VARIANTES A/B TEST)

> **CHOIX FINAL DÉCIDÉ EN MONTAGE** selon thumbnail retenue.
> Toutes les 3 variantes font ≤ 25s, promettent résultat visible, ouvrent boucle.

---

### VARIANTE 1 — DOULEUR VISUELLE + PROMESSE IMMÉDIATE (Recommandée par défaut)
**[VOIX OFF — Ton empathique, rythme soutenu]**
> "3 heures de cours magistral. 2 heures de réunion Teams. Tout ça pour... quoi ? Des notes illisibles ? Une page blanche ? Regarde : *[COUPURE BRUTALE — ÉCRAN : Fichier audio 3h → Texte propre en 18 secondes]* C'est Whisper en local. Gratuit. Privé. 2 minutes config. Je te montre tout."

**[VISUEL]** : Split screen — Gauche : Lecteur audio "Cours_Eco_3h.mp3" (barre progression) — Droite : Texte qui s'écrit en temps réel (curseur clignotant) — Timer coin : 0:18 — Texte final : "✅ 47 pages générées"

---

### VARIANTE 2 — PREUVE SOCIALE + CURIOSITÉ TECHNIQUE
**[VOIX OFF — Ton expert, crédibilité]**
> "Mes étudiants m'ont demandé : 'Comment tu fais pour avoir tes notes de cours complètes avant même la fin de l'amphi ?' La réponse tient en un mot : Whisper. Mais pas la version cloud qui envoie tes données chez OpenAI. La version LOCALE. 100% gratuit. 100% privé. Fonctionne hors ligne. *[ÉCRAN : Terminal `whisper cours.mp3 --model base --language fr` → Sortie SRT]* 2 minutes. C'est parti."

**[VISUEL]** : Terminal recording — Commande tapée → Exécution → Fichier .srt ouvert dans VS Code — Surbrillance "language: fr" + segments temps codés

---

### VARIANTE 3 — CONTRE-INTUITIF + ÉCONOMIE CONCRÈTE
**[VOIX OFF — Ton provocateur, énergie]**
> "Arrête de payer Notta 22€/mois. Arrête d'uploader tes réunions chez Otter. Tu as déjà le meilleur moteur de transcription SUR ton ordinateur. Gratuit. Illimité. Et personne ne te l'a dit. *[ÉCRAN : Comparatif prix — Notta 264€/an vs Whisper 0€]* Aujourd'hui : Installation 1-clic + Raccourci clavier 'Transcrire' + Export auto Notion. Ton portefeuille va dire merci."

**[VISUEL]** : Tableau comparatif animé — Logos Notta/Otter/Whisper — Prix/an — Flèche "GRATUIT" clignotante sur Whisper — Raccourci clavier `Ctrl+Shift+T` apparaître

---

## 📋 30s-1m30 — PROBLÈME + PROMESSE + ROADMAP

**[VOIX OFF — Ton clair, structurant]**
> "Bienvenue sur **Le Bon Raccourci** — la chaîne qui te donne *un problème, une démo, une solution* en moins de 10 minutes.
>
> **Le problème** : Tu passes 5h/semaine à réécouter tes cours ou réunions pour en tirer 10 minutes d'infos utiles. C'est 260h/an. Perdues.
>
> **La promesse** : À la fin de cette vidéo, tu auras un système qui transforme **n'importe quel audio en texte structuré, recherchable, exportable en 2 minutes chrono**. Gratuit. Local. Sans compte.
>
> **Le plan** : 3 démos progressives.
> 1️⃣ **Whisper Web** — Zéro install, test immédiat dans ton navigateur.
> 2️⃣ **Whisper Local** — Installation 1-clic, puissance illimitée, 100% privé.
> 3️⃣ **Workflow Pro** — Raccourci clavier + Export auto Notion/Word + Dossier 'À transcrire' surveillé.
>
> **Bonus** : Mon template Notion 'Cours & Réunions' + Checklist installation offerts en description.
>
> C'est parti."

**[VISUEL]** : Animation logo chaîne — Titre vidéo en surimpression — Roadmap visuelle 3 étapes (icônes : 🌐 💻 ⚡) — Timer "9:00" décompte

---

## 🌐 1m30-3m30 — DÉMO 1 : WHISPER WEB (ZÉRO INSTALL, TEST IMMÉDIAT)

**[VOIX OFF]**
> "Première démo : **Whisper Web**. Tu as 30 secondes ? Va sur `huggingface.co/spaces/openai/whisper`. C'est le modèle officiel OpenAI, hébergé gratuitement. Zero config."

**[ACTION ÉCRAN — Temps réel]**
1. Navigateur → `huggingface.co/spaces/openai/whisper`
2. Page charge — Modèle "large-v3" sélectionné par défaut
3. **Glisser-déposer** : Fichier `Réunion_Equipe_45min.wav` (préparé)
4. Bouton "Submit" → Barre progression
5. **Résultat** : Texte complet avec timestamps — Copier-coller direct

**[VOIX OFF]**
> "45 minutes transcrites en 1m12. Précision : 94% sur du français clair. **Mais...** 3 limites : Fichier max 25 Mo. Pas de confidentialité (upload cloud). Pas d'automatisation. C'est pour ça qu'on passe au niveau supérieur."

**[VISUEL]** : Callout animé "⚠️ LIMITES" — 3 points — Flèche vers "Démo 2"

---

## 💻 3m30-6m — DÉMO 2 : WHISPER LOCAL (INSTALL 1-CLIC, PUISSANCE ILLIMITÉE, 100% PRIVÉ)

**[VOIX OFF — Ton "c'est ici que ça devient intéressant"]**
> "Maintenant, **la vraie solution**. Whisper en local sur TA machine. Gratuit. Illimité. Tes données ne sortent jamais. Voici l'installation la plus simple qui existe."

### ÉTAPE 1 — INSTALLATION (Windows / Mac / Linux unifié)

**[ACTION ÉCRAN]**
> **Windows** : PowerShell Admin → `irm get.scoop.sh | iex` → `scoop install whisper` ✅
> **Mac** : Terminal → `brew install whisper` ✅
> **Linux** : `pip install -U openai-whisper` ✅
> *(Afficher les 3 en parallèle — Split screen 3 terminaux)*

**[VOIX OFF]**
> "30 secondes. C'est tout. Scoop/Homebrew/pip gèrent les dépendances Python, FFmpeg, le modèle. Tu n'as **rien** à configurer."

### ÉTAPE 2 — PREMIÈRE TRANSCRIPTION

**[ACTION ÉCRAN]**
```bash
whisper "Cours_Droit_2h.mp3" --model base --language fr --output_format txt srt vtt
```

**[VOIX OFF]**
> "`--model base` : Le sweet spot vitesse/précision (74 Mo, ~2x temps réel). `--language fr` : Force le français, évite la détection auto. `--output_format` : Sortie triple — `.txt` pour lire, `.srt` pour sous-titres, `.vtt` pour navigateur."

**[ACTION ÉCRAN — Temps réel accéléré 4x]**
- Barre progression Whisper
- "Transcribing: 100% | 2h audio → 3m45s traitement"
- Fichiers générés : `Cours_Droit_2h.txt` (187 KB), `.srt`, `.vtt`

**[VOIX OFF]**
> "2h de cours → 47 pages de texte propre en **3 minutes 45**. Sur un laptop classique (i5, 16 Go RAM, pas de GPU). Précision : 97%. Les noms propres, termes techniques, tout est là."

### ÉTAPE 3 — MODÈLES : LEQUEL CHOISIR ?

**[VISUEL — Tableau comparatif animé]**

| Modèle | Taille | Vitesse (CPU) | Précision FR | Usage Recommandé |
|--------|--------|---------------|--------------|------------------|
| `tiny` | 39 Mo | ~6x temps réel | 88% | Test rapide, mobile |
| `base` | 74 Mo | ~2.5x temps réel | **97%** | **⭐ DAILY DRIVER** |
| `small` | 244 Mo | ~1.2x temps réel | 98% | Qualité max, patience |
| `medium` | 769 Mo | ~0.6x temps réel | 99% | Pro, GPU requis |
| `large-v3` | 1550 Mo | ~0.3x temps réel | 99.5% | Archive, production |

**[VOIX OFF]**
> "Mon conseil : **`base` pour 95% des cas**. `small` si tu as du temps et veux la quasi-perfection. Les gros modèles ? Inutiles sauf usage pro intensif."

---

## ⚡ 6m-8m — DÉMO 3 : WORKFLOW PRO (RACCOURCI CLAVIER + EXPORT AUTO NOTION + DOSSIER SURVEILLÉ)

**[VOIX OFF — Ton "voici le raccourci qui change tout"]**
> "Tu ne veux pas taper des commandes à vie. Tu veux : **Fichier audio → Raccourci → Texte dans Notion**. C'est parti."

### 3.1 — SCRIPT POWERSHELL / BASH "TRANSCRIBE" (1 fichier, partout)

**[ACTION ÉCRAN — VS Code ouvert]**
```powershell
# transcribe.ps1 — Place dans ~/Scripts/ + Ajoute au PATH
param([string]$AudioPath, [string]$Model="base", [string]$Lang="fr")
$OutputDir = Split-Path $AudioPath
$FileName = [System.IO.Path]::GetFileNameWithoutExtension($AudioPath)
whisper $AudioPath --model $Model --language $Lang --output_format txt srt --output_dir $OutputDir
# Notification Windows
New-BurntToastNotification -Text "Transcription terminée", "$FileName prêt dans $OutputDir"
```

**[VOIX OFF]**
> "Ce script : Prend n'importe quel audio → Sortie `.txt` + `.srt` dans le MÊME dossier → Notification Windows. Place-le dans `~/Scripts`, ajoute au PATH. Fini la ligne de commande."

### 3.2 — RACCOURCI CLAVIER GLOBAL (AUTOKEY / POWERSHELL / AUTOMATOR)

**[ACTION ÉCRAN — Configuration]**
> **Windows (AutoHotkey)** : `Ctrl+Shift+T` → Sélection fichier explorateur → Lance `transcribe.ps1`
> **Mac (Automator/Shortcuts)** : `Cmd+Shift+T` → Quick Action → Fichiers sélectionnés → Run Shell Script
> **Linux (AutoKey)** : `Ctrl+Shift+T` → Même logique

**[VOIX OFF]**
> "Un raccourci. **N'importe quel fichier audio sélectionné dans l'explorateur**. `Ctrl+Shift+T`. Tu reviens 2 minutes plus tard : le texte est à côté."

### 3.3 — EXPORT AUTO VERS NOTION (LA KILLER FEATURE)

**[ACTION ÉCRAN — Notion API + Script Python minimal]**
```python
# notion_export.py — Ajouté au script transcribe.ps1
from notion_client import Client
import os, sys

notion = Client(auth=os.getenv("NOTION_TOKEN"))
database_id = os.getenv("NOTION_DB_ID")  # Ta DB "Cours & Réunions"

def push_to_notion(txt_path, srt_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        content = f.read()
    title = os.path.basename(txt_path).replace('.txt', '')
    notion.pages.create(parent={"database_id": database_id}, properties={
        "Titre": {"title": [{"text": {"content": title}}]},
        "Date": {"date": {"start": datetime.now().isoformat()}},
        "Fichier Source": {"files": [{"name": os.path.basename(txt_path), "external": {"url": f"file://{txt_path}"}}]},
        "Contenu": {"rich_text": [{"text": {"content": content[:2000]}}]}  # Notion limite 2000 chars
    })
```

**[VISUEL — DÉMO EN TEMPS RÉEL]**
1. Explorateur : `Réunion_Client_30min.mp3` sélectionné
2. `Ctrl+Shift+T` pressé
3. Notification "Transcription démarrée..."
4. 45s plus tard → Notification "✅ Prêt dans Notion"
5. **Basculer Notion** : Nouvelle page "Réunion_Client_30min" créée — Contenu + Lien fichier + Date auto

**[VOIX OFF]**
> "C'est **ça** le bon raccourci. Zéro friction. Ton cerveau reste sur la réflexion, pas l'admin."

### 3.4 — DOSSIER "À TRANSCRIRE" SURVEILLÉ (AUTOMATION TOTALE)

**[ACTION ÉCRAN — PowerShell FileSystemWatcher]**
```powershell
# watch_transcribe.ps1 — Lance au démarrage Windows (Registre Run)
$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = "$env:USERPROFILE\OneDrive\A_Transcrire"
$watcher.Filter = "*.mp3;*.wav;*.m4a;*.ogg"
$watcher.IncludeSubdirectories = $true
$watcher.EnableRaisingEvents = $true

Register-ObjectEvent -InputObject $watcher -EventName Created -Action {
    $file = $Event.SourceEventArgs.FullPath
    & "$env:USERPROFILE\Scripts\transcribe.ps1" -AudioPath $file
    Move-Item $file "$env:USERPROFILE\OneDrive\Transcrits\" -Force
} | Out-Null
```

**[VOIX OFF]**
> "Tu déposes ton enregistrement dans le dossier `A_Transcrire` (synchro OneDrive/Google Drive depuis ton téléphone). **C'est tout.** Le script tourne en fond, transcrit, range dans `Transcrits`, pousse dans Notion. Tu retrouves tes notes sur ton laptop avant même d'être rentré chez toi."

---

## 🎁 8m-8m45 — BONUS : TEMPLATE NOTION "COURS & RÉUNIONS" (LEAD MAGNET)

**[VOIX OFF — Ton valeur, générosité]**
> "Parce que le texte brut c'est bien, mais le texte **structuré** c'est mieux. J'ai construit le template Notion que j'utilise tous les jours. Il est à toi. Gratuit. Lien en description."

**[VISUEL — Capture Notion template]**
- **Database "Cours & Réunions"** : Titre, Date, Type (Cours/Réunion/Conf), Statut, Tags, Fichier Source, Contenu, Actions, Résumé IA
- **Vues** : Par date (Calendrier), Par type (Board), À traiter (Liste), Par tag (Gallery)
- **Bouton "🤖 Résumer avec IA"** : Appelle API OpenAI/Gemini via Make → Remplit "Résumé IA" + "Actions"
- **Page type** : En-tête méta — Contenu brut (toggle) — Résumé IA — Actions (checkbox) — Liens liés

**[VOIX OFF]**
> "Duplicate. Connecte ton intégration Make (template fourni). Chaque transcription qui arrive = Page créée + Résumé auto + Actions extraites. C'est ton **Second Brain** pour l'audio."

---

## 📢 8m45-9m — CONCLUSION + CTA + TEASER VIDÉO 3

**[VOIX OFF — Ton chaleureux, directif]**
> "Récapitulons. **Problème** : 5h/sem perdues à réécouter. **Solution** : Whisper Local + Raccourci `Ctrl+Shift+T` + Export Notion auto. **Résultat** : 2 minutes config → Gain 260h/an. Gratuit. Privé. Pour toujours.
>
> **Ton action maintenant** :
> 1. **Clique le lien en description** → Récupère la Checklist Installation + Template Notion + Scripts prêts à l'emploi.
> 2. **Teste Whisper Web** en 30 secondes (lien direct).
> 3. **Installe la version locale** — Tu verras, c'est addictif.
>
> **Question pour toi** : Quelle est la tâche audio qui te bouffe le plus de temps ? Cours ? Réunions ? Mémos vocaux ? Dis-le en commentaire, je lis tout et ça inspire la prochaine vidéo.
>
> **Jeudi prochain** : *"Comment RÉSUMER n'importe quel PDF, vidéo ou article en 1 clic (IA locale, gratuit)"* — La suite logique. Tu prends le texte, tu en tires l'essence. Abonne-toi, active la cloche, ne la rate pas.
>
> C'était **Le Bon Raccourci**. Un problème. Une démo. Une solution. À jeudi."

**[FIN D'ÉCRAN — 5 secondes]**
- Logo animé chaîne
- **3 éléments cliquables** :
  1. 📥 "Checklist + Template Notion GRATUIT" (Lien description)
  2. ▶️ "VIDÉO 3 : Résumer PDF/Video IA" (Pré-chargée)
  3. 🔔 "S'abonner" (Bouton natif YT)

---

## 📝 MÉTADONNÉES UPLOAD (PRÊTES POUR COPIER-COLLER)

### TITRE (Choix final selon thumbnail)
> **Principal** : Comment transcrire AUTOMATIQUEMENT tes cours/réunions en texte (Gratuit, Local, 2 min)
> **A/B 1** : Whisper Local GRATUIT : Transcrire audio en texte en 2 min (Install 1-clic, Privé)
> **A/B 2** : Arrête de payer Notta/Otter : La meilleure transcription est DÉJÀ sur ton PC (Gratuit)
> **A/B 3** : Le raccourci clavier qui transcrit TOUT automatiquement vers Notion (Whisper + AutoHotkey)

### DESCRIPTION (3 premières lignes = Hook + Lead Magnet + Lien)
> **3h de cours → Texte propre en 2 min. Gratuit. Local. Sans compte.**
>
> 🎁 **GRATUIT** : Checklist Installation + Template Notion "Cours & Réunions" + Scripts Auto → [LIEN GUMROAD/GDRIVE]
>
> Dans cette vidéo : 3 démos progressives pour ne plus JAMAIS réécouter un enregistrement.
>
> **CHAPITRES :**
> 0:00 - Hook : 3h audio → texte en 18s
> 0:30 - Problème + Roadmap
> 1:30 - Démo 1 : Whisper Web (Zero install)
> 3:30 - Démo 2 : Whisper Local (Install 1-clic, Illimité, Privé)
> 6:00 - Démo 3 : Workflow Pro (Raccourci + Export Notion + Dossier surveillé)
> 8:00 - Bonus : Template Notion Second Brain
> 8:45 - CTA + Teaser Vidéo 3
>
> **OUTILS & LIENS :**
> • Whisper Web : huggingface.co/spaces/openai/whisper
> • Scoop (Win) : scoop.sh | Homebrew (Mac) : brew.sh
> • AutoHotkey : autohotkey.com | Shortcuts (Mac) : support.apple.com/guide/shortcuts
> • Notion API : developers.notion.com
> • Mon template Make (Résumé IA) : [LIEN]
>
> **AFFILIATION (Soutiens la chaîne) :**
> 📝 Notion (50% commission) : notion.so/?r=...
> 🎙️ Otter.ai (20% récurrent) : otter.ai/?ref=...
> 📱 Notta (30% récurrent) : notta.ai/?ref=...
> ⚡ Raycast Pro (Pro) : raycast.com/?ref=...
>
> **CONNECTE :**
> 📧 Newsletter "Le Raccourci Hebdo" : [LIEN]
> 🐦 Twitter/X : @LeBonRaccourci
> 💼 LinkedIn : [LIEN]
>
> #transcription #whisper #productivite #etudiants #automatisation #lebonraccourci

### TAGS (15 — Ordre priorité décroissante)
1. transcription audio texte gratuit
2. whisper ia local gratuit
3. transcrire reunion automatique
4. convertir audio en texte
5. productivite etudiants
6. automatisation taches repetitives
7. whisper openai tutoriel
8. prise de notes ia
9. gain de temps etudes
10. outils gratuits pc
11. le bon raccourci
12. speech to text francais
13. exporter audio vers notion
14. raccourci clavier productivite
15. second brain notion

### HASHTAGS (3 max)
#TranscriptionIA #ProductiviteEtudiants #LeBonRaccourci

### CARTE DE FIN (End Screen - 20s)
- **Vidéo 1** : "7 SECRETS D'IA QUE LES ENTREPRENEURS NE TE DISENT PAS" (Chaîne mère)
- **S'abonner** : Bouton natif + "Rejoins 1000+ raccourcisseurs"
- **Playlist** : "Astuces PC/Mobile/IA - La Série Complète"

### COMMENTAIRE ÉPINGLÉ
> 🎁 **RESSOURCES GRATUITES** → Checklist + Template Notion + Scripts : [LIEN]
>
> ⏱ **TIMESTAMPS** :
> 1:30 Whisper Web | 3:30 Whisper Local Install | 6:00 Workflow Pro (Raccourci + Notion)
>
> ❓ **QUESTION** : Quelle audio tu veux transcrire en premier ? Cours ? Réunions ? Mémos vocaux ? 👇
>
> 🔔 **PAS LOUper LA SUITE** : Jeudi → "Résumer PDF/Video IA en 1 clic" — Abonne-toi !

---

## 🎙️ SSML POUR EDGE-TTS (VOIX : `fr-FR-HenriNeural` — Ton tutoriel, rythme 1.05, pitch +2%)

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="fr-FR">
  <voice name="fr-FR-HenriNeural">
    <mstts:express-as style="chat" styledegree="1.2">
      <prosody rate="1.05" pitch="+2%">
        <!-- HOOK VARIANTE 1 -->
        Si tu pensais que transcrire 3 heures de cours prenait 3 heures... tu vas halluciner.
        <break time="300ms"/>
        Regarde : fichier audio 3 heures... texte propre en 18 secondes.
        <break time="400ms"/>
        C'est Whisper en local. Gratuit. Privé. 2 minutes config.
        <break time="500ms"/>
        Je te montre tout.
      </prosody>
    </mstts:express-as>
    
    <mstts:express-as style="chat" styledegree="1.0">
      <prosody rate="1.0" pitch="0%">
        <!-- INTRO -->
        Bienvenue sur Le Bon Raccourci — la chaîne qui te donne un problème, une démo, une solution en moins de 10 minutes.
        <break time="400ms"/>
        Le problème : tu passes 5 heures par semaine à réécouter tes cours ou réunions pour en tirer 10 minutes d'infos utiles.
        <break time="300ms"/>
        C'est 260 heures par an. Perdues.
        <break time="500ms"/>
        La promesse : à la fin de cette vidéo, tu auras un système qui transforme n'importe quel audio en texte structuré, recherchable, exportable en 2 minutes chrono.
        <break time="300ms"/>
        Gratuit. Local. Sans compte.
      </prosody>
    </mstts:express-as>
    
    <!-- ... SUITE DU SCRIPT AVEC BALISES <break/> STRATÉGIQUES ... -->
    <!-- Chaque transition de démo = break 800ms -->
    <!-- Chaque commande technique = break 1200ms + emphasis -->
    <!-- Chaque "killer feature" = styledegree 1.3 + pitch +5% -->
  </voice>
</speak>
```

> **Note TTS** : Générer en 3 segments (Hook, Corps, CTA) pour contrôle qualité. Assembler au montage.

---

## ✅ CHECKLIST PRÉ-TOURNAGE (VALIDATION ENGINEER)

- [ ] Fichiers audio test prêts : `Cours_Eco_3h.mp3`, `Réunion_Equipe_45min.wav`, `Cours_Droit_2h.mp3`, `Réunion_Client_30min.mp3`
- [ ] Whisper Web accessible (test HF Spaces)
- [ ] Scoop/Homebrew/pip fonctionnels sur machine tournage
- [ ] Modèles `tiny`, `base`, `small` pré-téléchargés (`whisper --model base --download_only`)
- [ ] Scripts `transcribe.ps1`, `notion_export.py`, `watch_transcribe.ps1` testés et fonctionnels
- [ ] AutoHotkey / Shortcuts / AutoKey configurés raccourci `Ctrl+Shift+T`
- [ ] Notion Integration + Database "Cours & Réunions" créés + Token/Database ID dans `.env`
- [ ] Template Notion "Cours & Réunions" dupliqué + Bouton Make "Résumer IA" opérationnel
- [ ] Dossiers `A_Transcrire` / `Transcrits` créés sur OneDrive/Google Drive
- [ ] OBS Studio configuré : Capture fenêtre unique (Terminal/Navigateur/VS Code/Notion) + Audio système
- [ ] Thumbnail concepts (3) reçus du Designer — Choix final validé

---

## 📊 MÉTRIQUES SUCCÈS CIBLE (J+7)

| KPI | Objectif | Alerte Si |
|-----|----------|-----------|
| **CTR** | > 12% | < 9% |
| **AVD** | > 55% | < 48% |
| **Rétention 30s** | > 90% | < 82% |
| **Rétention 50%** | > 70% | < 60% |
| **Cliques Description** | > 8% | < 4% |
| **Téléchargements Lead Magnet** | > 150 | < 50 |
| **Commentaires** | > 40 | < 15 |
| **Partages** | > 25 | < 8 |

---

*Script verrouillé — Prêt pour tournage Mercredi (J+3)*
*Version 1.0 — Validé par Lead — Aligné VIDEO2_RESEARCH.md + Slogan chaîne*