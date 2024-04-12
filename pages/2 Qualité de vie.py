import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

csv_file_path = "Z:/BUT3/jollois_ville-20240412T092054Z-001/jollois_ville/data/bdd_ville.csv"
df = pd.read_csv(csv_file_path, sep=';')

violet_shades = ['#DDA0DD', '#BA55D3',  '#D2CAEC', '#D8BFD8', '#DDA0DD', '#DA70D6', '#BA55D3', '#9932CC', '#8A2BE2', '#9400D3']

# Configuration de style et des onglets
st.markdown("""
<style>
/* Base styles */
body, h1, h2, h3, h4, h5, div, p, a, .st-bq, .st-br, .st-bs { font-family: "Times New Roman", serif; }
h6, .h6 { font-family: "American Typewriter", serif; font-weight: normal; font-size: 24px; color: #F5F5F5; }
h7, .h7 { font-family: "Geneva", serif; font-weight: normal; font-size: 22px; color: #F5F5F5; }
/* Tabs and buttons styling */
.stTabs .stTab { background-color: #6B28A5; color: white; padding: 10px; border-radius: 10px; margin-right: 10px; }
.stTabs .stTab.st--selected { background-color: #8849C7; color: white; border-bottom: 2px solid white; }
.stTabContent { padding: 16px; border: 1px solid #6B28A5; border-radius: 10px; margin-top: 10px; background-color: white; }
button { color: white !important; border: 2px solid rgba(140, 40, 165, 0.5) !important; margin-left: 20px; margin-right: 20px; padding: 50px 70px; }
.spacer { height: 50px; }
.stApp { background-color: #000000; }
.stTabs > div > div > button[aria-selected="true"] { background-color: #79009B; color: white; font-weight: bold; }
</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
""", unsafe_allow_html=True)

# Header with logo and title
col1, col2 = st.columns([1, 5])
with col1:
    st.image("image/a.png", width=150, output_format="PNG")
with col2:
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    st.image("image/3.png", width=350, output_format="PNG")

# City selection sidebar
cities = ["Paris", "Marseille", "Lyon", "Montpellier", "Strasbourg", "Toulouse", "Nice", "Bordeaux"]
city1 = st.sidebar.selectbox('Choisissez la première ville:', cities)
city2 = st.sidebar.selectbox('Choisissez la deuxième ville:', cities)

# Tabs for different categories
tab1, tab2, tab3 = st.tabs(["Loisirs", "Climat", "Services et sécurité"])

with tab1:
    # Adjust figure size per visualization requirements
    fig, axs = plt.subplots(2, 2, figsize=(18, 14))
    selected_cities_df = df[df['Ville'].isin([city1, city2])]
    # Bar charts for leisure activities
    sns.barplot(x="Nb de Musees", y="Ville", data=df[df['Ville'].isin([city1, city2])], ax=axs[0, 0], palette=violet_shades)
    axs[0, 0].set_title("Nombre de musées par ville")
    sns.barplot(x="Nb de Cinemas", y="Ville", data=df[df['Ville'].isin([city1, city2])], ax=axs[0, 1], palette=violet_shades)
    axs[0, 1].set_title("Nombre de cinémas par ville")
    sns.barplot(x="Nb biblotheque", y="Ville", data=df[df['Ville'].isin([city1, city2])], ax=axs[1, 0], palette=violet_shades)
    axs[1, 0].set_title("Nombre de bibliothèques par ville")
    sns.lineplot(x="Ville", y="Nb de Restaurants", data=df[df['Ville'].isin([city1, city2])], ax=axs[1, 1], marker='o', palette=violet_shades)
    axs[1, 1].set_title("Nombre de restaurants par ville")
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("---")


    selected_cities_df['Total_loisirs'] = selected_cities_df['Nb de Musees'] + selected_cities_df['Nb de Cinemas'] + selected_cities_df['Nb biblotheque'] + selected_cities_df['Nb de Restaurants']
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.pie(selected_cities_df['Total_loisirs'], labels=selected_cities_df['Ville'], autopct='%1.1f%%', startangle=140, colors=violet_shades)
    ax.set_title("Répartition des loisirs")
    ax.axis('equal')
    st.pyplot(fig)

with tab2:
    # Radar chart for climate comparison
    fig, ax = plt.subplots(subplot_kw=dict(polar=True), figsize=(6, 6))
    ax.set_facecolor('black')
    data = df[df['Ville'].isin([city1, city2])][["Temperature Automne", "Temperature Hiver", "Temperature Printemps", "Temperature Ete"]].values
    labels = ["Automne", "Hiver", "Printemps", "Été"]
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    plt.xticks(angles[:-1], labels, color='white', size=12)
    ax.set_rlabel_position(0)
    plt.yticks([10, 20, 30], ["10", "20", "30"], color="white", size=9)
    plt.ylim(0, 40)
    for idx, d in enumerate(data):
        line = np.concatenate((d, [d[0]]))
        ax.plot(angles, line, linewidth=2, linestyle='solid', label=cities[idx], color=violet_shades[idx])
        ax.fill(angles, line, color=violet_shades[idx], alpha=0.25)
    plt.title("Comparaison des températures", size=15, color='white', y=1.1)
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2))
    st.pyplot(fig)
    
    st.markdown("---")


    def create_donut_chart(data, labels, colors, ax, title):
        wedges, texts, autotexts = ax.pie(data, autopct='%1.1f%%', startangle=90, colors=colors,
                                        wedgeprops=dict(width=0.4, edgecolor='w'))
        ax.set_title(title, color='white', fontsize=35)
        plt.setp(texts, color='white')
        plt.setp(autotexts, size=20, weight="bold")

    # Supposons que 'df', 'city1', et 'city2' soient déjà définis et importés comme dans votre script initial
    # Données pour les diagrammes en anneaux
    hours_data = [df[df['Ville'] == city1]['Nb heure soleil'].values[0], df[df['Ville'] == city2]['Nb heure soleil'].values[0]]
    rain_data = [df[df['Ville'] == city1]['Jour de pluie'].values[0], df[df['Ville'] == city2]['Jour de pluie'].values[0]]
    frost_data = [df[df['Ville'] == city1]['Jour de gel'].values[0], df[df['Ville'] == city2]['Jour de gel'].values[0]]

    # Sélection de couleurs dans la palette violet_shades pour chaque ville
    colors = [violet_shades[1], violet_shades[5]]  # Assurez-vous que cette palette a suffisamment de couleurs

    # Création et affichage des diagrammes en anneaux
    figu, axs = plt.subplots(1, 3, figsize=(25,10))
    create_donut_chart(hours_data, [city1, city2], colors, axs[0], 'Heures de soleil')
    create_donut_chart(rain_data, [city1, city2], colors, axs[1], 'Jours de pluie')
    create_donut_chart(frost_data, [city1, city2], colors, axs[2], 'Jours de gel')
    st.pyplot(figu)


with tab3:
    selected_cities_df = df[df['Ville'].isin([city1, city2])]

    # Calculate 'Total' column for health services
    selected_cities_df['Total'] = selected_cities_df["Nb d'hopitaux"] + selected_cities_df["Nb d'Aeroports"]

    # Security and services data visualization
    fig, axs = plt.subplots(1, 3, figsize=(18, 6), constrained_layout=True)
    sns.barplot(x="Nb d'Aeroports", y="Ville", data=selected_cities_df, ax=axs[0], palette=violet_shades)
    axs[0].set_title("Nombre d'aéroports par ville")
    sns.barplot(x="Nb d'hopitaux", y="Ville", data=selected_cities_df, ax=axs[1], palette=violet_shades)
    axs[1].set_title("Nombre d'hôpitaux par ville")
    sns.barplot(x="Nb de crime et delit pour 100 000 habitants", y="Ville", data=selected_cities_df, ax=axs[2], palette=violet_shades)
    axs[2].set_title("Nombre de crimes et délits pour 100 000 habitants")
    st.pyplot(fig)

    st.markdown("---")

    plt.figure(figsize=(8, 6))
    plt.pie(selected_cities_df['Total'], labels=selected_cities_df['Ville'], autopct='%1.1f%%', startangle=140, colors=violet_shades)
    plt.title("Service de santé")
    plt.axis('equal')  # Assure que le camembert est un cercle

    # Affichage du graphique en camembert
    st.pyplot(plt)