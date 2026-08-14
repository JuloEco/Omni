from flask import Flask, render_template

app = Flask(__name__)

# Configuration de l'entreprise et du Hub
HUB_CONFIG = {
    "brand_name": "Opix",
    "hub_name": "Omni",
    "tagline": "Écosystème Applicatif & Plateforme de Services"
}

# Liste des services (Sans les URLs Railway)
SERVICES = [
    # --- JEUX MULTIJOUEURS & STRATÉGIE ---
    {
        "name": "Intrigues & Couronnes",
        "category": "jeux",
        "url": "https://intrigues-et-couronnes.onrender.com",
        "description": "Jeu de stratégie politique et de bluff à la Cour.",
        "icon": "👑",
        "supports_qr": True
    },
    {
        "name": "Loup Garou",
        "category": "jeux",
        "url": "https://juloeco-wolfpro.hf.space",
        "description": "Jeu d'ambiance et de déduction multijoueur.",
        "icon": "🐺",
        "supports_qr": True
    },
    {
        "name": "Undercover Dessin",
        "category": "jeux",
        "url": "https://undercover-dessin.onrender.com",
        "description": "Jeu de dessin, d'indices et de rôle caché.",
        "icon": "🎨",
        "supports_qr": True
    },
    {
        "name": "Quiz Room",
        "category": "jeux",
        "url": "https://juloeco-quiz-room.hf.space",
        "description": "Arène de quiz dynamique en ligne.",
        "icon": "❓",
        "supports_qr": True
    },
    {
        "name": "Jeux Multijoueurs Tactiles",
        "category": "jeux",
        "url": "https://multijoueursv2.onrender.com",
        "description": "Plateforme de mini-jeux tactiles en réseau local/web.",
        "icon": "📱",
        "supports_qr": True
    },
    {
        "name": "Jeu de Trading",
        "category": "jeux",
        "url": "https://trading-tfxt.onrender.com",
        "description": "Simulation et jeu de marchés financiers.",
        "icon": "📈",
        "supports_qr": False
    },

    # --- ÉDUCATION & APPRENTISSAGE ---
    {
        "name": "LearnCode",
        "category": "education",
        "url": "https://juloeco-learncode.hf.space",
        "description": "Plateforme interactive d'apprentissage de la programmation.",
        "icon": "💻",
        "supports_qr": False
    },
    {
        "name": "Classroom",
        "category": "education",
        "url": "https://classroom-ejxx.onrender.com",
        "description": "Gestionnaire d'espace de cours et de classe.",
        "icon": "📚",
        "supports_qr": False
    },

    # --- UTILITAIRES & PRODUCTIVITÉ ---
    {
        "name": "Liste de Courses",
        "category": "outils",
        "url": "https://listedecourse.pythonanywhere.com",
        "description": "Gestionnaire de repas de saison et listes automatisées.",
        "icon": "🛒",
        "supports_qr": True
    },
    {
        "name": "Chatting App",
        "category": "outils",
        "url": "https://chatting-u91z.onrender.com",
        "description": "Messagerie instantanée et salon de discussion.",
        "icon": "💬",
        "supports_qr": False
    }
]

@app.route('/')
def index():
    return render_template('index.html', config=HUB_CONFIG, services=SERVICES)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)