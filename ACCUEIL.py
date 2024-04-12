import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import time

# Configuration de la page
st.set_page_config(page_title="CityCompare", layout="wide", page_icon=":cityscape:")

# Personnalisation du style avec CSS pour le logo et le titre
st.markdown("""
<style>
body {
    font-family: "Times New Roman", serif;
}
h1, h2, h3, h4, h5, h6, .logo-title {
    font-family: "Times New Roman", serif;
    color: white;
}
h1 {
    font-size: 48px !important;
    font-weight: bold;
}
            
h2 {
    font-size: 28px;
}
h3 {
    font-size: 24px;
}
h4, h5, h6 {
    font-size: 20px;
}
.logo-title {
    padding-top: 60px;
    font-size: 40px;
    font-weight: bold;
}
.stApp {
    background-color: #000000;
}
.spacer {
    height: 50px;  /* Ajustez cette valeur pour créer plus ou moins d'espace */
}
.stMarkdown {
    color: white; /* Couleur du texte blanc pour tous les textes générés par Streamlit */
}
</style>
""", unsafe_allow_html=True)

# En-tête avec logo dynamique et titre ajusté
# En-tête avec logo dynamique et titre ajusté
col1, col2 = st.columns([1, 5])
with col1:
    st.image("image/a.png", width=150, output_format="PNG")
with col2:
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    st.image("image/3.png", width=350, output_format="PNG")




# Introduction
st.markdown("### Découvrez votre ville idéale")
st.markdown("""
Vous êtes sur le point de prendre une décision importante : choisir entre les villes les plus emblématiques de France.
Bienvenue sur **CityCompare**, votre outil pour comparer les plus grandes villes de France afin de faciliter votre prise de décision pour votre futur déménagement.
Que vous envisagiez de changer de ville pour des raisons personnelles, professionnelles ou simplement pour découvrir de nouveaux horizons, notre application est là pour vous aider à prendre la meilleure décision.
""", unsafe_allow_html=True)

st.markdown("***")

# Création des colonnes pour les images et la section "À propos"
left_column, right_column = st.columns([2, 2])

with left_column:
    st.markdown('<h2><span style="color:#6B28A5;">&#x2139;</span> À propos de CityCompare</h2>', unsafe_allow_html=True)
    st.write("""
    CityCompare est conçu pour fournir une comparaison complète et objective des grandes villes françaises. Notre plateforme met en lumière :
    - Le coût de la vie
    - La qualité de la vie
    - Les attractions touristiques
    - Les opportunités d'emploi
    - Et bien plus encore
    """)

with right_column:
    st.markdown('<h2><span style="color:#6B28A5;">🏙</span> Explorez les Villes</h2>', unsafe_allow_html=True)

    image_container = st.empty()

    cities = ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Strasbourg", "Bordeaux"]
    images = ["paris.jpeg", "marseille.jpeg", "lyon.jpeg", "toulouse.jpeg", "nice.jpeg", "strasbourg.jpeg", "bordeaux.jpeg"]  # Assurez-vous que ces chemins sont corrects

    # Boucle à commenter ou à ajuster pour ne pas bloquer l'exécution du script
    for city, image_path in zip(cities, images):
         image = Image.open(f"image/{image_path}")
         draw = ImageDraw.Draw(image)
         font = ImageFont.load_default()  # Cette ligne pourrait nécessiter une adaptation pour ajuster la taille
         draw.text((15, 12), city, fill="white", font=font)
         image_container.image(image, width=450)  # Taille réduite de l'image
         time.sleep(2)  # Délai avant de passer à l'image suivante

# Pied de page
st.markdown("***")
st.markdown(" #### N'hésitez pas à explorer notre application pour trouver votre ville idéale. Bonne exploration avec **CityCompare** !", unsafe_allow_html=True)
