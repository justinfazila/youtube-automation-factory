# 🎬 YouTube Automation Factory

> **Content Factory** — A multi-agent system for producing monetizable, faceless YouTube content at scale.

---

## 📋 Overview

This repository contains the strategic blueprint, scripts, assets, and data for a fully automated YouTube channel focused on **Business, AI & Business Automation / Financial Productivity** — a high-CPM niche ($15-45 CPM).

### Monetization Targets
- **YPP Eligibility**: 1,000 subscribers + 4,000 watch hours (long-form) OR 10M Shorts views
- **Primary Revenue**: YouTube AdSense
- **Secondary**: Affiliate marketing, digital products, sponsorships

---

## 🏗️ Repository Structure

```
youtube-automation-factory/
├── scripts/                    # Video scripts in Markdown
│   ├── YOUTUBE_MONETIZATION_BLUEPRINT.md   # Strategic master plan
│   ├── VIDEO1_SCRIPT.md                    # First video script (10 min)
│   └── VISUAL_STRATEGY_AND_PUBLICATION.md  # Visual & publication workflow
├── assets/                     # Visual assets (gitignored large files)
│   ├── LOGO_PLACEHOLDER.md     # Brand guidelines & specs
│   ├── logo.svg                # Vector logo (to be created)
│   ├── banner-2560x1440.png    # Channel banner (to be created)
│   └── thumbnails/             # Video thumbnails (to be created)
├── data/                       # Structured data (JSON)
│   ├── themes.json             # Content themes & video ideas
│   ├── keywords.json           # SEO keyword database
│   └── videos.json             # Production tracking & metadata
├── .gitignore
└── README.md                   # This file
```

---

## 🤖 Agent Team Architecture

```
┌───────────────────────────┐
│   AGENT LEAD (Orchestrator)│
└─────────────┬─────────────┘
              │
    ┌─────────┼─────────┐
    ▼         ▼         ▼
┌────────┐ ┌────────┐ ┌────────┐
│Research│ │Script  │ │Visual  │
│& SEO   │ │Writer  │ │& Canva │
└────────┘ └────────┘ └────────┘
```

| Agent | Responsibility | Tools |
|-------|---------------|-------|
| **Lead** | Pipeline orchestration, GitHub, Calendar, Publication | Git, Google Calendar, YouTube API |
| **Research & SEO** | Keyword research, topic ideation, title optimization | Ahrefs/SEMrush APIs, YouTube search |
| **Scriptwriter** | Hooks, storytelling, retention structure, CTAs | Custom prompts, frameworks |
| **Visual & Canva** | Thumbnails (3 variants/video), brand assets | Canva API / `control-local-browser` |

---

## 📊 Current Status

| Metric | Status |
|--------|--------|
| **Niche Selected** | ✅ Business & AI Automation |
| **Blueprint** | ✅ Complete |
| **Video 1 Script** | ✅ Complete (10 min) |
| **Visual Strategy** | ✅ Defined |
| **Keyword Database** | ✅ 8 high-value keywords |
| **Themes Database** | ✅ 3 themes, 15+ video ideas |
| **Production Tracking** | ✅ Initialized |
| **GitHub Remote** | ⏳ Pending |
| **Thumbnails** | ⏳ Pending (Canva) |
| **Voiceover** | ⏳ Pending (ElevenLabs/Edge-TTS) |
| **Video Edit** | ⏳ Pending |

---

## 🚀 Quick Start

### Prerequisites
- Git
- Node.js 18+ (for automation scripts)
- Python 3.10+ (for data processing)
- Canva Pro account (for thumbnail automation)
- ElevenLabs API key (for voiceover)

### Clone & Setup
```bash
git clone <repository-url>
cd youtube-automation-factory
```

### Initialize GitHub Remote
```bash
git remote add origin https://github.com/<your-username>/youtube-automation-factory.git
git push -u origin master
```

---

## 📝 Script Format (Markdown)

All video scripts follow a standardized structure:

```markdown
# 🎬 SCRIPT VIDÉO X : "TITLE"

**Durée estimée** : X minutes
**Format** : Vidéo faceless avec narration IA + B-roll
**Objectif** : [Watch time / Conversion / Brand awareness]

---

## 0-30s - HOOK ULTRA-CAPTIVANT
[Voice direction + Visual cues]

---

## 30s-2m - PROMESSE & STRUCTURE
[Promise + retention hook]

---

## 2m-Xm - CORPS (X Secrets/Étapes)
### SECRET/ÉTAPE 1
[Content]

---

## Xm-Ym - CONCLUSION & CTA
[Summary + Subscribe CTA + Next video link]
```

---

## 📈 Data Files

### `data/themes.json`
Content pillars with video ideas, target CPM, competition analysis.

### `data/keywords.json`
SEO keyword database with volume, CPC, difficulty, intent, related questions.

### `data/videos.json`
Production pipeline tracking: status, scheduling, performance metrics.

---

## 🔄 Production Workflow

1. **Research** → New topics added to `themes.json` + `keywords.json`
2. **Script** → New `.md` in `scripts/` following template
3. **Visual** → 3 thumbnail variants in `assets/thumbnails/`
4. **Audio** → Voiceover generated (ElevenLabs/Edge-TTS)
5. **Edit** → Assemble in editor (CapCut/Premiere/DaVinci)
6. **Publish** → Scheduled via YouTube API + Calendar
7. **Track** → Update `videos.json` with performance data

---

## 🛡️ Monetization Compliance

- ✅ Original scripts (no reused content)
- ✅ High-quality AI voiceover (ElevenLabs v2+)
- ✅ Dynamic editing with context & B-roll
- ✅ Value-added commentary, not raw AI output
- ✅ Clear disclosure where required

---

## 📄 License

Proprietary — Internal use only for Content Factory operations.

---

## 🤝 Contributing

This is an automated production repository. Manual edits should follow the established structure. For process changes, contact the **Agent Lead**.

---

*Powered by DeepSeek Harness Agent Team* 🤖