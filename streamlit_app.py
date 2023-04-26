import streamlit as st

# Set page title and layout
st.set_page_config(page_title="D&D Character Creator", layout="wide")

# Point buy cost table
point_buy_cost = {
    8: 0,
    9: 1,
    10: 2,
    11: 3,
    12: 4,
    13: 5,
    14: 7,
    15: 9
}

# Character creation form
st.title("D&D Character Creator")

with st.form("character_form"):
    st.header("Personal Information")
    character_name = st.text_input("Character Name")
    player_name = st.text_input("Player Name")

    st.header("Attributes")
    total_points = st.selectbox("Total Points", (27, 30, 33, 36))
    remaining_points = total_points

    strength = st.number_input("Strength", min_value=8, max_value=15, value=8)
    remaining_points -= point_buy_cost[strength]

    dexterity = st.number_input("Dexterity", min_value=8, max_value=15, value=8, key="dexterity_input")
    remaining_points -= point_buy_cost[dexterity]

    constitution = st.number_input("Constitution", min_value=8, max_value=15, value=8, key="constitution_input")
    remaining_points -= point_buy_cost[constitution]

    intelligence = st.number_input("Intelligence", min_value=8, max_value=15, value=8, key="intelligence_input")
    remaining_points -= point_buy_cost[intelligence]

    wisdom = st.number_input("Wisdom", min_value=8, max_value=15, value=8, key="wisdom_input")
    remaining_points -= point_buy_cost[wisdom]

    charisma = st.number_input("Charisma", min_value=8, max_value=15, value=8, key="charisma_input")
    remaining_points -= point_buy_cost[charisma]

    st.info(f"Remaining Points: {remaining_points}")

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
    st.write("
