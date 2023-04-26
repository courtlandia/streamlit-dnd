import streamlit as st

# Set page title and layout
st.set_page_config(page_title="D&D Character Creator", layout="wide")

# Character creation form
st.title("D&D Character Creator")

with st.form("character_form"):
    st.header("Personal Information")
    character_name = st.text_input("Character Name")
    player_name = st.text_input("Player Name")

    st.header("Attributes")
    strength = st.number_input("Strength", min_value=1, max_value=20, value=10)
    dexterity = st.number_input("Dexterity", min_value=1, max_value=20, value=10)
    constitution = st.number_input("Constitution", min_value=1, max_value=20, value=10)
    intelligence = st.number_input("Intelligence", min_value=1, max_value=20, value=10)
    wisdom = st.number_input("Wisdom", min_value=1, max_value=20, value=10)
    charisma = st.number_input("Charisma", min_value=1, max_value=20, value=10)

    st.header("Class")
    character_class = st.selectbox("Choose Class", ("Barbarian", "Bard", "Cleric", "Druid",
                                                     "Fighter", "Monk", "Paladin", "Ranger",
                                                     "Rogue", "Sorcerer", "Warlock", "Wizard"))

    st.header("Race")
    character_race = st.selectbox("Choose Race", ("Human", "Elf", "Dwarf", "Halfling",
                                                  "Dragonborn", "Gnome", "Half-Elf", "Half-Orc",
                                                  "Tiefling"))

    st.header("Background")
    character_background = st.selectbox("Choose Background", ("Acolyte", "Charlatan", "Criminal",
                                                              "Entertainer", "Folk Hero", "Guild Artisan",
                                                              "Hermit", "Noble", "Outlander", "Sage",
                                                              "Sailor", "Soldier", "Urchin"))

    submit_button = st.form_submit_button("Create Character")

# Character creation result
if submit_button:
    st.success("Character Created!")
    st.write("Character Name:", character_name)
    st.write("Player Name:", player_name)
    st.write("Class:", character_class)
    st.write("Race:", character_race)
    st.write("Background:", character_background)
    st.write("Attributes:")
    st.write("Strength:", strength)
    st.write("Dexterity:", dexterity)
    st.write("Constitution:", constitution)
    st.write("Intelligence:", intelligence)
    st.write("Wisdom:", wisdom)
    st.write("Charisma:", charisma)
