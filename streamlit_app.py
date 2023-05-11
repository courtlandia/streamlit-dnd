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
st.header("Backstory")
backstory_prompt = "Write a backstory for the character. What events led them to where they are now? What are their motivations? (maximum 2048 characters)"
backstory = st.text_input("Backstory", max_chars=2048)

# Create a button to generate the character
if st.button("Create Character"):
    # Generate the D&D character using OpenAI's GPT-3 API
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=(f"Create a level 1 D&D character with the following attributes: Strength {strength}, Dexterity {dexterity}, Constitution {constitution}, Intelligence {intelligence}, Wisdom {wisdom}, Charisma {charisma}. "
                    f"{backstory_prompt} "),
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5,
        )
        print(response)

        # Extract the character information from the API response
        character_info = response.choices[0].text.strip()
        if not character_info:
            raise ValueError("Character information not found in OpenAI response.")

        character = json.loads(character_info)

        # Display the character information to the user
        st.subheader("Your Character:")
        st.write(f"Name: {character['name']}")
        st.write(f"Race: {character['race']}")
    except Exception as e:
        st.error(f"Error generating character: {e}")    
