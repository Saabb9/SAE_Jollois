import streamlit as st
import folium
import pandas as pd
from streamlit_folium import folium_static
import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from math import pi

csv_file_path = "Z:/BUT3/jollois_ville-20240412T092054Z-001/jollois_ville/data/bdd_ville.csv"

# Load the data into a DataFrame
df = pd.read_csv(csv_file_path, sep=';')

violet_shades = ['#DDA0DD', '#BA55D3',  '#D2CAEC', '#D8BFD8', '#DDA0DD', '#DA70D6', '#BA55D3', '#9932CC', '#8A2BE2', '#9400D3']
# Personnalisation du style avec CSS

plt.rcParams.update({
    'text.color': 'white',
    'axes.labelcolor': '#DA70D6',
    'axes.labelsize': 16,
    'axes.titlesize':21,
    'axes.titlecolor': '#D8BFD8',
    'axes.facecolor': '#000000',  # Noir pour le fond
    'axes.edgecolor': 'white',
    'figure.facecolor': '#000000',  # Noir pour le fond de la figure
    'figure.edgecolor': '#000000',
    'xtick.color': 'white',
    'ytick.color': 'white',
    'font.family': 'sans-serif',
    'font.sans-serif': ['Times New Roman']  # Assurez-vous que cette police est installée
})

st.markdown("""

<style>
/* Réinitialisation des polices pour toutes les balises */
body, h1, h2, h3, h4, h5, div, p, a, .st-bq, .st-br, .st-bs {
    font-family: "Times New Roman", serif;
}


h6, .h6 {
    font-family: "American Typewriter", serif;
    font-weight: normal; /* Pour s'assurer que le texte n'est pas en gras */
    color: #FFFFFF; /* Blanc cassé */
    font-size : 20px;
}
                     
h7, .h7 {
    font-family: "Geneva", serif;
    font-weight: normal; /* Pour s'assurer que le texte n'est pas en gras */
    font-size: 22px; /* Taille de la police */
    color: #FFFFFF; /* Blanc cassé */
}
/* Style pour les onglets non sélectionnés */
.stTabs .stTab {
    background-color: #6B28A5; /* Couleur violette pour les onglets */
    color: white; /* Texte en blanc pour les onglets */
    padding: 10px; /* Espace intérieur pour les onglets */
    border-radius: 10px; /* Coins arrondis pour les onglets */
    margin-right: 10px; /* Espace entre les onglets */
}

/* Style pour les onglets sélectionnés */
.stTabs .stTab.st--selected {
    background-color: #8849C7; /* Couleur violette plus foncée pour l'onglet sélectionné */
    color: white;
    border-bottom: 2px solid white; /* Bordure en bas pour l'onglet sélectionné */
}

/* Style pour les contenus des onglets */
.stTabContent {
    padding: 16px; /* Espace intérieur pour le contenu des onglets */
    border: 1px solid #6B28A5; /* Bordure autour du contenu de l'onglet */
    border-radius: 10px; /* Coins arrondis pour le contenu de l'onglet */
    margin-top: 10px; /* Espace au-dessus du contenu des onglets */
    background-color: white; /* Fond blanc pour le contenu des onglets */
}

button {
    color: white !important;
    border: 2px solid rgba(140, 40, 165, 0.5) !important;
    margin-left: 20px !important;
    margin-right: 20px !important;
    font-family: "Times New Roman", serif;
    padding: 8px;
}

.spacer {
    height: 50px;  /* Ajustez cette valeur pour créer plus ou moins d'espace */
}

.stApp {
    background-color: #000000;
}
/* Modification de la couleur de fond de l'onglet sélectionné */
.stTabs > div > div > button[aria-selected="true"] {
    background-color: #79009B;
    color: white;
    font-weight: bold;
}



</style>
""", unsafe_allow_html=True)

st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css"> """, unsafe_allow_html=True)


# En-tête avec logo dynamique et titre ajusté
col1, col2 = st.columns([1, 5])
with col1:
    st.image("image/a.png", width=150, output_format="PNG")
with col2:
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    st.image("image/3.png", width=350, output_format="PNG")


# Sélection des villes dans la barre latérale
cities = ["Paris", "Marseille", "Lyon", "Montpellier", "Strasbourg", "Toulouse", "Nice", "Bordeaux"]
city1 = st.sidebar.selectbox('Choisissez la première ville:', cities)
city2 = st.sidebar.selectbox('Choisissez la deuxième ville:', cities)

# Tabulation pour Démographie
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Démographie", "Coût de la vie", "Logement", "Emploi", "Éducation", "Transports"])

##############################################3
# Fonction pour afficher une carte basée sur le nom de la ville
def display_city_map(city_name):
    
    if city_name == "Paris":
        geojson_path = r"Z:\BUT3\jollois_ville-20240412T092054Z-001\jollois_ville\geo\departement-75-paris.geojson"
        center_location = [48.8566, 2.3522]
        zoom_start = 10
    elif city_name == "Marseille":
        geojson_path = r"Z:\BUT3\jollois_ville-20240412T092054Z-001\jollois_ville\geo\departement-13-bouches-du-rhone.geojson"
        center_location = [43.2965, 5.3698]
        zoom_start=7.3
    elif city_name == "Lyon":
        geojson_path = r"Z:\BUT3\jollois_ville-20240412T092054Z-001\jollois_ville\geo\departement-69-rhone.geojson"
        center_location = [45.75, 4.85]
        zoom_start=7
    elif city_name == "Montpelier":
        geojson_path = r"Z:\BUT3\jollois_ville-20240412T092054Z-001\jollois_ville\geo\departement-34-herault.geojson"
        center_location = [43.6, 3.8833]
        zoom_start=8
    elif city_name == "Strasbourg":
        geojson_path =  r"Z:\BUT3\jollois_ville-20240412T092054Z-001\jollois_ville\geo\departement-67-bas-rhin.geojson"
        center_location = [48.5833, 7.75]
        zoom_start=8
    elif city_name == "Toulouse":
        zoom_start=8
        geojson_path =  r"Z:\BUT3\jollois_ville-20240412T092054Z-001\jollois_ville\geo\departement-31-haute-garonne.geojson"
        center_location = [43.6, 1.43333]
        zoom_start = 7
    elif city_name == "Nice":
        geojson_path =  r"Z:\BUT3\jollois_ville-20240412T092054Z-001\jollois_ville\geo\departement-06-alpes-maritimes.geojson"
        center_location = [43.7, 7.25]
        zoom_start=7
    elif city_name == "Bordeaux":
        geojson_path =  r"Z:\BUT3\jollois_ville-20240412T092054Z-001\jollois_ville\geo\departement-33-gironde.geojson"
        center_location = [44.8333, -0.5667]
        zoom_start= 7
    else:
        return  

    # Création et affichage de la carte
    map_ = folium.Map(location=center_location, zoom_start=zoom_start, tiles='CartoDB dark_matter')
    folium.GeoJson(
        geojson_path,
        name='geojson',
        style_function=lambda x: {
            'fillColor': 'violet',
            'color': 'purple',
            'weight': 4.0,
            'fillOpacity': 0.2
        }
    ).add_to(map_)
    folium_static(map_, width=330, height=250)



def create_side_by_side_pie_charts(sizes1, sizes2, labels, title1, title2, colors):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3))  # Deux graphiques dans une ligne
    ax1.pie(sizes1, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    ax1.set_title(title1)
    ax2.pie(sizes2, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    ax2.set_title(title2)
    plt.tight_layout()
    return fig

# Collecte des données pour City 1 et City 2
sizes_musees = [df[df['Ville'] == city1]["Nb de Musees"].values[0], df[df['Ville'] == city2]["Nb de Musees"].values[0]]
sizes_hopitaux = [df[df['Ville'] == city1]["Nb d'hopitaux"].values[0], df[df['Ville'] == city2]["Nb d'hopitaux"].values[0]]
labels = [city1, city2]
colors = ['#9467bd', '#c5b0d5']  # Deux teintes de violet


fig = create_side_by_side_pie_charts(sizes_musees, sizes_hopitaux, labels, 'Musées', 'Hôpitaux', colors)

def plot_cost_comparison_and_description(df, subject, city1, city2):
    cost_city1 = df.loc[df['Ville'] == city1, subject].values[0]
    cost_city2 = df.loc[df['Ville'] == city2, subject].values[0]
    
    if cost_city1 > cost_city2:
        difference = (cost_city1 - cost_city2) / cost_city2 * 100
        description = f"Le coût de {subject} est <b>{difference:.2f}%</b> plus élevé à {city1} qu'à {city2}."
    elif cost_city2 > cost_city1:
        difference = (cost_city2 - cost_city1) / cost_city1 * 100
        description = f"Le coût de {subject} est <b>{difference:.2f}%</b> plus élevé à {city2} qu'à {city1}."
    else:
        description = f"Le coût de {subject} est identique à {city1} et {city2}."
    
    fig, ax = plt.subplots(figsize=(4, 3))  # Taille du graphique
    bars = ax.bar([city1, city2], [cost_city1, cost_city2], color=['#9467bd', '#c5b0d5'])
    ax.set_title(f'Coût de {subject}', fontname="Comic Sans MS", fontsize=12)  # Titre du graphique avec une police définie
    ax.set_ylabel('Coût', fontname="Comic Sans MS", fontsize=10)  # Etiquette Y
    ax.tick_params(axis='both', which='major', labelsize=8)  # Taille des ticks
    
    col1, col2 = st.columns([3, 2])  # Ajustement des colonnes
    with col1:
        st.pyplot(fig)
    with col2:
        # Stylisation de la description avec CSS pour une belle écriture et alignement au milieu
        st.markdown(f"<p style='text-align: center; font-family:Comic Sans MS; font-size:14px;'>{description}</p>", unsafe_allow_html=True)


##############################################""""""

with tab1:

    # Affichage des cartes
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### {city1}")
        display_city_map(city1)
    with col2:
        st.markdown(f"### {city2}")
        display_city_map(city2)

    # Séparateur
    st.markdown("<hr>", unsafe_allow_html=True)

    # Affichage de la superficie
    st.markdown(f"<h3 style='text-align: center; color: white;'>Superficie</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        population_city1 = df[df['Ville'] == city1]['Demographie'].values[0]
        superficie_city1 = df[df['Ville'] == city1]['Superficie'].values[0]
        st.markdown(f"<h6 style='text-align: center;'><i class='fas fa-map-marked-alt' style='color: violet; font-size: 24px;'></i> {superficie_city1} km²</h6>", unsafe_allow_html=True)
    with col2:
        population_city2 = df[df['Ville'] == city2]['Demographie'].values[0]
        superficie_city2 = df[df['Ville'] == city2]['Superficie'].values[0]
        st.markdown(f"<h6 style='text-align: center;'><i class='fas fa-map-marked-alt' style='color: violet; font-size: 24px;'></i> {superficie_city2} km²</h6>", unsafe_allow_html=True)

    # Séparateur
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center; color: white;'>Population</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<h6 style='text-align: center;'><i class='fas fa-users' style='color: violet; font-size: 24px;'></i> {population_city1} habitants</h6>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<h6 style='text-align: center;'><i class='fas fa-users' style='color: violet; font-size: 24px;'></i> {population_city2} habitants</h6>", unsafe_allow_html=True)
################################################

###############################################

with tab2:
    subjects = [
        "Cout Moyen d'un panier de course", 
        "Prix Ticket Transport", 
        "Prix Mensuel Transport", 
        "Prix carburant"

    ]
    for subject in subjects:
        plot_cost_comparison_and_description(df, subject, city1, city2)


################################################

# Fonction pour créer un graphique en anneau
def create_donut_chart(city_name, ax):
    city_data = df[df['Ville'] == city_name].iloc[0]
    maison = city_data['Type habitat Maison']
    appartement = city_data['Type habitat appart']
    
    sizes = [maison, appartement]
    colors = ['#BB92DF', '#79009B']  # violet pour appartement, beige pour maison
    labels = ['Maisons', 'Appartements']
    ax.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
    
    # Dessinez un cercle au centre pour transformer en donut chart
    centre_circle = plt.Circle((0,0),0.70,fc='black')
    ax.add_artist(centre_circle)

    # Égaliser l'aspect ratio pour que le pie chart soit rond
    ax.axis('equal')  
    ax.set_title(f"Type d'habitat pour {city_name}", color='white', fontsize=14)

def create_bar_chart(data, title, ax, color):
    ax.bar(data.keys(), data.values(), color=color)
    ax.set_title(title, color='white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')


with tab3 : 
    # Sous-titre pour la section Type d'habitat
    st.markdown("<h2 style='text-align: center; color: white;'>Type d'habitat</h2>", unsafe_allow_html=True)
    
    # Création des colonnes pour les graphiques des deux villes
    col1, col2 = st.columns(2)
    
    with col1:
        # Titre pour la ville 1 et son graphique
        st.markdown(f"<h3 style='text-align: center; color: white;'>{city1}</h3>", unsafe_allow_html=True)
        fig, ax = plt.subplots()
        create_donut_chart(city1, ax)
        st.pyplot(fig)
    
    with col2:
        # Titre pour la ville 2 et son graphique
        st.markdown(f"<h3 style='text-align: center; color: white;'>{city2}</h3>", unsafe_allow_html=True)
        fig, ax = plt.subplots()
        create_donut_chart(city2, ax)
        st.pyplot(fig)

    proprietaires_city1 = df[df['Ville'] == city1]['Proprietaire'].values[0]
    locataires_city1 = df[df['Ville'] == city1]['Locataire'].values[0]
    proprietaires_city2 = df[df['Ville'] == city2]['Proprietaire'].values[0]
    locataires_city2 = df[df['Ville'] == city2]['Locataire'].values[0]

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<h3 style='text-align: center; color: white;'>{city1}</h3>", unsafe_allow_html=True)
        st.metric("Propriétaires", f"{proprietaires_city1}")
        st.metric("Locataires", f"{locataires_city1}")

    with col2:
        st.markdown(f"<h3 style='text-align: center; color: white;'>{city2}</h3>", unsafe_allow_html=True)
        st.metric("Propriétaires", f"{proprietaires_city2}")
        st.metric("Locataires", f"{locataires_city2}")

    st.markdown("<hr>", unsafe_allow_html=True)

    # Ajout des graphiques pour les prix moyens
    st.markdown("<h2 style='text-align: center; color: white;'>Prix Moyens</h2>", unsafe_allow_html=True)
    
    # Données de prix moyens
    prix_moyen_data_city1 = {
        'Maison/m²': df[df['Ville'] == city1]['Prix Moyen Maison par metre'].values[0],
        'Logement/m²': df[df['Ville'] == city1]['Prix Moyen Logement par metre'].values[0],
        'Logement F2': df[df['Ville'] == city1]['Prix Moyen Logement F2'].values[0],
        'Logement F4': df[df['Ville'] == city1]['Prix Moyen Logement F4'].values[0]
    }
    prix_moyen_data_city2 = {
        'Maison/m²': df[df['Ville'] == city2]['Prix Moyen Maison par metre'].values[0],
        'Logement/m²': df[df['Ville'] == city2]['Prix Moyen Logement par metre'].values[0],
        'Logement F2': df[df['Ville'] == city2]['Prix Moyen Logement F2'].values[0],
        'Logement F4': df[df['Ville'] == city2]['Prix Moyen Logement F4'].values[0]
    }

    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots()
        create_bar_chart(prix_moyen_data_city1, f"Prix Moyens à {city1}", ax, '#BB92DF')
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots()
        create_bar_chart(prix_moyen_data_city2, f"Prix Moyens à {city2}", ax, '#79009B')
        st.pyplot(fig)


###############################################
with tab4:
    salaire_moyen = [df[df['Ville'] == city1]['Salaire Moyen'].values[0], df[df['Ville'] == city2]['Salaire Moyen'].values[0]]
    taux_chomage = [df[df['Ville'] == city1]['Taux de Chomage'].values[0], df[df['Ville'] == city2]['Taux de Chomage'].values[0]]
    labels = [city1, city2]
    colors = ['#9467bd', '#c5b0d5']  # Couleurs pour les diagrammes

    # Création des camemberts
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.pie(salaire_moyen, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops=dict(width=0.4), pctdistance=0.85)
    ax1.set_title('Salaire Moyen')
    ax2.pie(taux_chomage, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops=dict(width=0.4), pctdistance=0.85)
    ax2.set_title('Taux de Chômage')

    plt.tight_layout()
    st.pyplot(fig)

    # Phrases descriptives
    st.markdown(f"**Salaire Moyen :** À *{city1}*, le salaire moyen est de **{salaire_moyen[0]}€**. À *{city2}*, il est de **{salaire_moyen[1]}€**.", unsafe_allow_html=True)
    st.markdown(f"**Taux de Chômage :** À *{city1}*, le taux de chômage est de **{taux_chomage[0]}%**. À *{city2}*, il est de **{taux_chomage[1]}%**.", unsafe_allow_html=True)

###############################################


nb_creche_city1 = df[df['Ville'] == city1]['Nb Creche'].values[0]
nb_maternelle_city1 = df[df['Ville'] == city1]['Nb Maternelle'].values[0]
nb_college_city1 = df[df['Ville'] == city1]['Nb college'].values[0]
nb_lycee_city1 = df[df['Ville'] == city1]['Nb lycee'].values[0]
nb_universites_city1 = df[df['Ville'] == city1]["Nb d'Universites"].values[0]

nb_creche_city2 = df[df['Ville'] == city2]['Nb Creche'].values[0]
nb_maternelle_city2 = df[df['Ville'] == city2]['Nb Maternelle'].values[0]
nb_college_city2 = df[df['Ville'] == city2]['Nb college'].values[0]
nb_lycee_city2 = df[df['Ville'] == city2]['Nb lycee'].values[0]
nb_universites_city2 = df[df['Ville'] == city2]["Nb d'Universites"].values[0]

###############################################
with tab5:
    education_data = {
        'Ville': [city1, city2],
        'Nombre de Crèches': [nb_creche_city1, nb_creche_city2],
        'Nombre de Maternelles': [nb_maternelle_city1, nb_maternelle_city2],
        'Nombre de Collèges': [nb_college_city1, nb_college_city2],
        'Nombre de Lycées': [nb_lycee_city1, nb_lycee_city2],
        "Nombre d'Universités": [nb_universites_city1, nb_universites_city2]
    }

    # Créer un DataFrame à partir du dictionnaire
    education_df = pd.DataFrame(education_data)

    # Afficher le DataFrame dans un tableau
    st.write(education_df)

    st.markdown("---")
    total_ecoles_city1 = nb_creche_city1 + nb_maternelle_city1 + nb_college_city1 + nb_lycee_city1 + nb_universites_city1
    total_ecoles_city2 = nb_creche_city2 + nb_maternelle_city2 + nb_college_city2 + nb_lycee_city2 + nb_universites_city2

    # Création d'une liste des totaux pour les deux villes
    totaux = [total_ecoles_city1, total_ecoles_city2]

    # Noms des villes
    villes = [city1, city2]

    # Création du camembert
    plt.figure(figsize=(6, 4))
    plt.pie(totaux, labels=villes, autopct='%1.1f%%', startangle=140, colors=violet_shades)
    plt.title('Proportion de la scolarité dans les deux villes')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(plt)


###############################################

###############################################
with tab6:
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center; color: white;'>Transports</h3>", unsafe_allow_html=True)
    
    # Données pré-définies
    villes = ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Strasbourg", "Bordeaux"]
    stations_metro = [303, 29, 40, 37, 3, 6, 28]  # Nombre de stations de métro dans chaque ville
    arrets_bus = [12368, 942, 1456, 787, 270, 242, 1034]  # Nombre d'arrêts de bus dans chaque ville

    # Filtrer les données pour les villes sélectionnées
    selected_indices = [villes.index(city1), villes.index(city2)]
    selected_cities = [villes[i] for i in selected_indices]
    selected_metro = [stations_metro[i] for i in selected_indices]
    selected_bus = [arrets_bus[i] for i in selected_indices]

    # Création des graphiques
    plt.figure(figsize=(12, 6))  # Augmentez la largeur de la figure pour éviter la superposition des noms de villes

    # Histogramme pour le nombre de stations de métro
    plt.subplot(1, 2, 1)
    plt.barh(selected_cities, selected_metro, color=violet_shades)  # Utilisez barh pour les barres horizontales
    plt.title('Nombre de stations de métro dans chaque ville')
    plt.xlabel('Nombre de stations')
    plt.ylabel('Villes')

    # Diagramme en barres pour le nombre d'arrêts de bus
    plt.subplot(1, 2, 2)
    plt.barh(selected_cities, selected_bus, color=violet_shades)  # Utilisez barh pour les barres horizontales
    plt.title('Nombre d\'arrêts de bus dans chaque ville')
    plt.xlabel('Nombre d\'arrêts')
    plt.ylabel('Villes')

    # Affichage des graphiques
    plt.tight_layout()
    st.pyplot(plt)

###############################################

