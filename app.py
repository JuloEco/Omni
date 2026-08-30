from flask import Flask, render_template

app = Flask(__name__)

# Configuration de l'entreprise et du Hub
HUB_CONFIG = {
    "brand_name": "Octix",
    "hub_name": "Omni",
    "tagline": "Écosystème Applicatif & Plateforme de Services"
}

# Les quatre univers de marque d'Octix. "octix" est le cœur transversal ;
# les trois autres correspondent chacun à une catégorie de SERVICES.
UNIVERSES = [
    {
        "name": "Axiom",
        "logo": "axiom.png",
        "maps_to": "jeux",
        "role": "Stratégie & logique",
        "description": "Les jeux qui demandent de réfléchir avant d'agir : bluff, déduction, calcul, anticipation.",
        "color": "#3b82a6"
    },
    {
        "name": "Octix",
        "logo": "octix.png",
        "maps_to": None,
        "role": "Le cœur du système",
        "description": "La plateforme elle-même : ce qui relie et fait tourner tous les autres univers, ici réunis.",
        "color": "#22b8c8"
    },
    {
        "name": "Omnia",
        "logo": "omnia.png",
        "maps_to": "outils",
        "role": "L'apprentissage du code",
        "description": "Les espaces de cours et d'entraînement, pensés pour progresser pas à pas.",
        "color": "#d9502f"
    },
    {
        "name": "Opsiom",
        "logo": "opsiom.png",
        "maps_to": "education",
        "role": "Recherche en IA",
        "description": "Modèles d'IA, pour une expérience de qualité.",
        "color": "#9d5fc4"
    }
]

# Liste des services (Sans les URLs Railway)
SERVICES = [
    # --- JEUX MULTIJOUEURS & STRATÉGIE ---
    {
        "name": "Intrigues & Couronnes",
        "category": "jeux",
        "url": "https://intrigues-et-couronnes.onrender.com",
        "description": "Jeu de stratégie politique et de bluff à la Cour.",
        "icon": "👑",
        "supports_qr": True,
        "auto_wake": True
    },
    {
        "name": "Loup Garou",
        "category": "jeux",
        "url": "https://juloeco-wolfpro.hf.space",
        "description": "Jeu d'ambiance et de déduction multijoueur.",
        "icon": "🐺",
        "supports_qr": True,
        "auto_wake": True
    },
    {
        "name": "Undercover Dessin",
        "category": "jeux",
        "url": "https://undercover-dessin.onrender.com",
        "description": "Jeu de dessin, d'indices et de rôle caché.",
        "icon": "🎨",
        "supports_qr": True,
        "auto_wake": False
    },
    {
        "name": "Quiz Room",
        "category": "jeux",
        "url": "https://juloeco-quiz-room.hf.space",
        "description": "Arène de quiz dynamique en ligne.",
        "icon": "❓",
        "supports_qr": True,
        "auto_wake": False
    },
    {
        "name": "Jeux Multijoueurs Tactiles",
        "category": "jeux",
        "url": "https://multijoueursv2.onrender.com",
        "description": "Plateforme de mini-jeux tactiles en réseau local/web.",
        "icon": "📱",
        "supports_qr": True,
        "auto_wake": False
    },
    {
        "name": "Jeu de Trading",
        "category": "jeux",
        "url": "https://trading-tfxt.onrender.com",
        "description": "Simulation et jeu de marchés financiers.",
        "icon": "📈",
        "supports_qr": False,
        "auto_wake": False
    },

    # --- ÉDUCATION & APPRENTISSAGE ---
    {
        "name": "LearnCode",
        "category": "education",
        "url": "https://learncode-n2qy.onrender.com",
        "description": "Plateforme interactive d'apprentissage de la programmation.",
        "icon": "💻",
        "supports_qr": False,
        "auto_wake": False
    },
    {
        "name": "Classroom",
        "category": "education",
        "url": "https://classroom-ejxx.onrender.com",
        "description": "Gestionnaire d'espace de cours et de classe.",
        "icon": "📚",
        "supports_qr": False,
        "auto_wake": True
    },

    # --- UTILITAIRES & PRODUCTIVITÉ ---
    {
        "name": "Liste de Courses",
        "category": "outils",
        "url": "https://listedecourse.pythonanywhere.com",
        "description": "Gestionnaire de repas de saison et listes automatisées.",
        "icon": "🛒",
        "supports_qr": True,
        "auto_wake": False
    },
    {
        "name": "Chatting App",
        "category": "outils",
        "url": "https://chatting-u91z.onrender.com",
        "description": "Messagerie instantanée et salon de discussion.",
        "icon": "💬",
        "supports_qr": False,
        "auto_wake": False
    }
]

@app.route('/')
def index():
    universe_by_name = {u["name"]: u for u in UNIVERSES}
    intro_order = ["Axiom", "Omnia", "Opsiom", "Octix"]
    presentation_order = ["Octix", "Opsiom", "Omnia", "Axiom"]
    return render_template(
        'index.html',
        config=HUB_CONFIG,
        services=SERVICES,
        universes=[universe_by_name[name] for name in presentation_order],
        intro_universes=[universe_by_name[name] for name in intro_order]
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
