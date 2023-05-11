import streamlit as st
import openai
import json

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

# Create a text input for the character backstory
st.header("Character Description")
description_prompt = "Describe your character. What's their personality like? What kind of race and background do you imagine for them?"
description = st.text_area("Description", max_chars=2048)

# Create a button to generate the character
if st.button("Create Character"):
    # Generate the D&D character using OpenAI's GPT-3 API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"A D&D player wants to create a new character. "
                f"The character has the following attributes: Strength {strength}, Dexterity {dexterity}, Constitution {constitution}, Intelligence {intelligence}, Wisdom {wisdom}, Charisma {charisma}. "
                f"The player describes the character as: '{description}'. "
                f"Please generate a detailed backstory roughly 3 paragraphs in length. Include the character's name, race, and sex. It should detail the character's origin, motivation, personal conflicts they've overcome in the past, how their personality has developed over time, their relationship with a significant person in their life, quirks, traits, and if they harbor any secrets."),
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the character information from the API response
    character_info = response.choices[0].text.strip()
    st.subheader("Your Character:")
    st.write(character_info)
