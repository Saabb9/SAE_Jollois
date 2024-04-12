import streamlit as st
import pandas as pd




csv_file_path = "Z:/BUT3/jollois_ville-20240412T092054Z-001/jollois_ville/data/bdd_ville.csv"

# Load the data into a DataFrame
df = pd.read_csv(csv_file_path, sep=';')

# Personnalisation du style avec CSS pour le logo et le titre
st.markdown("""
<style>
.title {
    text-align: center;
    color: white;
    border: 2px solid #6B28A5; /* Couleur violette pour la bordure */
    padding: 5px; /* Réduit le padding pour un encadrement plus proche du texte */
    border-radius: 5px; /* Coins légèrement arrondis */
    display: inline-block; /* Limite la largeur de la bordure au contenu du texte */
    margin-bottom: 20px; /* Ajoute un espace après le titre */     
}

/* Styles supplémentaires pour l'apparence générale */
body, h1, h2, h3, h4, h5, h6, .logo-title {
    font-family: "Times New Roman", serif;
    color: white;
}
h1 {
    font-size: 48px !important;
    font-weight: bold;
}
h2, h3 {
    font-size: 28px;
}
h4, h5, h6 {
    font-size: 20px;
}
.stApp {
    background-color: #000000;
}
.spacer {
    height: 50px; /* Ajustez cette valeur pour créer plus ou moins d'espace */
}
.stMarkdown {
    color: white; /* Couleur du texte blanc pour tous les textes générés par Streamlit */
}
</style>
""", unsafe_allow_html=True)



# Liste des variables pour le classement top 3
variables_classement = [
   "Superficie",
   "Proprietaire",
   "Salaire Moyen",
   "Taux de Chomage",
   "Prix Moyen Logement par metre",
   "Nb Creche",
   "Nb Maternelle",
   "Nb college",
   "Nb lycee",
   "Nb d'Universites",
   "Nb de Restaurants",
   "Prix Mensuel Transport",
   "Nb d'Aeroports",
   "Temperature Automne",
   "Temperature Hiver",
   "Temperature Printemps",
   "Temperature Ete",
   "Nb heure soleil",
   "Prix carburant",
   "Nb d'hopitaux",
   "Nb de crime et delit pour 100 000 habitants"
]


# Fonction pour le classement top 3
def top3_classement(variable):
   if variable in ["Taux de Chomage", "Prix Moyen Logement par metre", "Nb de crime et delit pour 100 000 habitants"]:
       df_sorted = df.sort_values(by=variable, ascending=True)
   else:
       df_sorted = df.sort_values(by=variable, ascending=False)
   top3 = df_sorted.head(3)
   return top3


# Page Classement top 3
def classement_top3():
  
   # Sélection de la variable pour le classement top 3
   variable_classement = st.selectbox("Choisissez la variable pour le classement top 3 :", variables_classement)


   # Générer le classement top 3
   top3 = top3_classement(variable_classement)


   # Afficher le classement top 3 dans une table
   st.write(f"Classement Top 3 pour la variable '{variable_classement}' (du plus petit au plus grand) :")
   st.write(top3)



# En-tête avec logo dynamique et titre ajusté
col1, col2 = st.columns([1, 5])
with col1:
    st.image("image/a.png", width=150, output_format="PNG")
with col2:
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    st.image("image/3.png", width=350, output_format="PNG")



st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<h2 class="title" style="text-align: center;">Classement Top 3</h2>', unsafe_allow_html=True)


#  paragraphe d'introduction
st.markdown("""
Dans cette page, vous aurez l'occasion de découvrir les trois meilleures villes en fonction du facteur que vous choisirez. Sélectionnez simplement le critère qui vous intéresse dans la liste déroulante ci-dessous et laissez-nous vous montrer les trois premières villes en fonction de ce facteur. Que vous soyez à la recherche de la ville avec le plus bas taux de chômage, le prix moyen du logement le plus bas par mètre carré ou tout autre critère, vous trouverez ici les trois meilleures options pour vous.
""")


# Exécuter la page Classement top 3
if __name__ == "__main__":
   classement_top3()


