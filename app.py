from flask import Flask, render_template

app = Flask(__name__)

HUB_CONFIG = {
    "brand_name": "Octix",
    "hub_name": "Omni",
    "tagline": "Écosystème applicatif & plateforme de services",
}

UNIVERSES = [
    {
        "name": "Axiom",
        "logo": "axiom.png",
        "maps_to": "jeux",
        "role": "Stratégie & logique",
        "description": "Jeux de bluff, déduction, calcul et anticipation.",
        "color": "#38bdf8",
    },
    {
        "name": "Octix",
        "logo": "octix.png",
        "maps_to": None,
        "role": "Le cœur du système",
        "description": "La plateforme qui relie et fait tourner tous les univers.",
        "color": "#22d3ee",
    },
    {
        "name": "Omnia",
        "logo": "omnia.png",
        "maps_to": "outils",
        "role": "Apprendre & progresser",
        "description": "Des espaces de cours et d’entraînement pour avancer pas à pas.",
        "color": "#fb7185",
    },
    {
        "name": "Opsiom",
        "logo": "opsiom.png",
        "maps_to": "IA",
        "role": "Recherche en IA",
        "description": "Des outils intelligents conçus pour enrichir chaque expérience.",
        "color": "#c084fc",
    },
]

SERVICES = [
    {"name": "Intrigues & Couronnes", "category": "jeux", "url": "https://intrigues-et-couronnesv2-yvb0.onrender.com", "description": "Jeu de stratégie politique et de bluff à la Cour.", "icon": "crown", "supports_qr": True, "auto_wake": True},
    {"name": "Loup Garou", "category": "jeux", "url": "https://juloeco-wolfpro.hf.space", "description": "Jeu d’ambiance et de déduction multijoueur.", "icon": "moon", "supports_qr": True, "auto_wake": True},
    {"name": "Entreprise simulation", "category": "jeux", "url": "https://entreprise-mu-eight.vercel.app/", "description": "Une simulation d’entreprise de haute qualité.", "icon": "building-2", "supports_qr": True, "auto_wake": False},
    {"name": "Undercover Dessin", "category": "jeux", "url": "https://undercover-dessin.onrender.com", "description": "Jeu de dessin, d’indices et de rôle caché.", "icon": "palette", "supports_qr": True, "auto_wake": False},
    {"name": "Quiz Room", "category": "jeux", "url": "https://juloeco-quiz-room.hf.space", "description": "Arène de quiz dynamique en ligne.", "icon": "circle-help", "supports_qr": True, "auto_wake": False},
    {"name": "Jeux Multijoueurs Tactiles", "category": "jeux", "url": "https://multijoueursv2.onrender.com", "description": "Plateforme de mini-jeux tactiles en réseau local/web.", "icon": "smartphone", "supports_qr": True, "auto_wake": False},
    {"name": "Jeu de Trading", "category": "jeux", "url": "https://trading-tfxt.onrender.com", "description": "Simulation et jeu de marchés financiers.", "icon": "chart-no-axes-combined", "supports_qr": True, "auto_wake": False},
    {"name": "LearnCode", "category": "education", "url": "https://learncode-io6e.onrender.com", "description": "Plateforme interactive d’apprentissage de la programmation.", "icon": "code-2", "supports_qr": True, "auto_wake": False},
    {"name": "Classroom", "category": "education", "url": "https://classroom-ejxx.onrender.com", "description": "Gestionnaire d’espace de cours et de classe.", "icon": "book-open", "supports_qr": True, "auto_wake": False},
    {"name": "Liste de Courses", "category": "outils", "url": "https://listedecourse.pythonanywhere.com", "description": "Gestionnaire de repas de saison et listes automatisées.", "icon": "shopping-basket", "supports_qr": True, "auto_wake": False},
    {"name": "Chatting App", "category": "outils", "url": "https://chatting-u91z.onrender.com", "description": "Messagerie instantanée et salon de discussion.", "icon": "message-circle", "supports_qr": True, "auto_wake": False},
    {"name": "Opsiom — ASCII", "category": "IA", "url": "https://juloeco.github.io/ASCII-generator/", "description": "Convertisseur d’images et de texte en caractères ASCII.", "icon": "scan-text", "supports_qr": True, "auto_wake": False},
    {"name": "Opsiom — AI", "category": "IA", "url": "https://opsiom-frontend.onrender.com/", "description": "Assistant IA pour explorer, créer et réfléchir autrement.", "icon": "sparkles", "supports_qr": True, "auto_wake": False},
]

@app.route('/')
def index():
    universe_by_name = {universe["name"]: universe for universe in UNIVERSES}
    intro_order = ["Axiom", "Omnia", "Opsiom", "Octix"]
    presentation_order = ["Octix", "Opsiom", "Omnia", "Axiom"]
    return render_template(
        "index.html",
        config=HUB_CONFIG,
        services=SERVICES,
        universes=[universe_by_name[name] for name in presentation_order],
        intro_universes=[universe_by_name[name] for name in intro_order],
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
