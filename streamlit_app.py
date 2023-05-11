import streamlit as st
import openai

st.set_page_config(page_title="D&D Character Generator", layout="wide")

# OpenAI API authentication
openai.api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")

# Create a title and subheader
st.title("D&D Character Generator")
st.subheader("Create your own D&D character using natural language!")

# Create number inputs for each attribute
st.header("Attributes")
strength = st.number_input("Strength", min_value=8, max_value=15, value=8, key="strength_input")
dexterity = st.number_input("Dexterity", min_value=8, max_value=15, value=8, key="dexterity_input")
constitution = st.number_input("Constitution", min_value=8, max_value=15, value=8, key="constitution_input")
intelligence = st.number_input("Intelligence", min_value=8, max_value=15, value=8, key="intelligence_input")
wisdom = st.number_input("Wisdom", min_value=8, max_value=15, value=8, key="wisdom_input")
charisma = st.number_input("Charisma", min_value=8, max_value=15, value=8, key="charisma_input")

# Calculate remaining points
point_buy_cost = {8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9}
remaining_points = 27 - point_buy_cost[strength] - point_buy_cost[dexterity] - point_buy_cost[constitution] - point_buy_cost[intelligence] - point_buy_cost[wisdom] - point_buy_cost[charisma]
st.write("Remaining points:", remaining_points)

# Create select box inputs for race, class, sex, and campaign setting
st.header("Character Details")
race = st.selectbox("Race", ["Human", "Elf", "Dwarf", "Halfling", "Gnome", "Half-Elf", "Half-Orc", "Tiefling", "Dragonborn"])
character_class = st.selectbox("Class", ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"])
sex = st.selectbox("Sex", ["Male", "Female", "Other"])
campaign_setting = st.selectbox("Campaign Setting", ["Eberron", "Forgotten Realms", "Ravenloft", "Dark Sun", "Spelljammer"])

# Create a text input for the character backstory
st.header("Character Description")
description_prompt = "Describe your character. What's their personality like? What kind of background do you imagine for them?"
description = st.text_area("Description", max_chars=2048)

# Create a button to generate the character
if st.button("Create Character"):
    # Generate the D&D character using OpenAI's GPT-3 API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"A D&D player wants to create a new character in the {campaign_setting} setting. "
                f"The character is a {sex} {race} {character_class} with the following attributes: Strength {strength}, Dexterity {dexterity}, Constitution {constitution}, Intelligence {intelligence}, Wisdom {wisdom}, Charisma {charisma}. "
                f"The player described the character as follows: '{description}'. Based on this information, please generate a compelling backstory for this character that is 5 paragraphs long."),
        max_tokens=2048,
        temperature=0.6,
    )

    # Extract the character information from the API response
    character_info = response.choices[0].text.strip()

    # Display the character backstory to the user
    st.subheader("Your Character's Backstory:")
    st.write(character_info)
