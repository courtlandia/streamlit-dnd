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
    
    # Create a dictionary to hold attribute values and their respective point buy costs
    attributes = {
        "Strength": {"value": 8, "cost": point_buy_cost[8]},
        "Dexterity": {"value": 8, "cost": point_buy_cost[8]},
        "Constitution": {"value": 8, "cost": point_buy_cost[8]},
        "Intelligence": {"value": 8, "cost": point_buy_cost[8]},
        "Wisdom": {"value": 8, "cost": point_buy_cost[8]},
        "Charisma": {"value": 8, "cost": point_buy_cost[8]}
    }

    for attribute in attributes:
        attributes[attribute]["value"] = st.number_input(attribute, min_value=8, max_value=15,
                                                        value=attributes[attribute]["value"],
                                                        key=f"{attribute.lower()}_input")

    remaining_points = total_points - sum(attributes[attribute]["cost"] for attribute in attributes)
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
    for attribute in attributes:
        st.write(f"{attribute}: {attributes[attribute]['value']}")
