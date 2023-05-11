import streamlit as st
import openai

st.set_page_config(page_title="D&D Character Generator", layout="wide")

# OpenAI API authentication
openai.api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")
# Allow users to select the temperature parameter
temperature = st.sidebar.selectbox(
    'Select the creativity level for the character backstory (closer to 0 = predictable, closer to 1 = creative:',
    [0.2, 0.4, 0.6, 0.8, 1.0],
    index=2
)

# Create a title and subheader
st.title("D&D Character Background Generator")
st.subheader("Too lazy to write a backstory for your D&D character? This app is for you!")
st.write("In the sidebar, enter your OpenAI API key, select how creative you want your backstory to be, fill in your character information and click 'Create character'. Then add any additional description of your character below, and click 'Create backstory'"

# Create form inputs for character details n the sidebar
background_options = ['Acolyte', 'Criminal', 'Guild Artisan', 'Hermit', 'Noble', 'Outlander', 'Sage', 'Soldier']
alignment_options = ['Lawful Good', 'Neutral Good', 'Chaotic Good', 'Lawful Neutral', 'True Neutral', 'Chaotic Neutral', 'Lawful Evil', 'Neutral Evil', 'Chaotic Evil']

with st.sidebar.form(key='my_form'):
    st.header("Character details")
    name = st.text_input("Name", max_chars=50)
    race = st.selectbox("Race", ["Human", "Elf", "Dwarf", "Halfling", "Gnome", "Half-Elf", "Half-Orc", "Warforged", "Goblin", "Hobgoblin", "Orc", "Bugbear"])
    character_class = st.selectbox("Class", ["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"])
    sex = st.selectbox("Sex", ["Male", "Female", "Other"])
    campaign_setting = st.selectbox("Campaign Setting", ["Eberron", "Forgotten Realms", "Ravenloft", "Dark Sun", "Spelljammer"])
    background = st.selectbox('Select the character\'s background:', background_options)
    alignment = st.selectbox('Select the character\'s alignment:', alignment_options)
    
    # Create number inputs for each attribute
    st.header("Character attributes")
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

    # When the user is done, they press the "Submit" button to process their inputs
    submit_button = st.form_submit_button(label='Create Character')

# Create a text input for the character backstory
st.header("Character Description")
description_prompt = "Describe your character. What's their personality like? What kind of background do you imagine for them?"
description = st.text_area("Description", max_chars=2048)

# Create a button to generate the character
if st.button("Create Backstory"):
    # Generate the D&D character using OpenAI's GPT-3 API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"A D&D player wants to create a new character named {name} in the {campaign_setting} setting with a {background.lower()} background and {alignment.lower()} alignment. "
                f"The character is a {sex} {race} {character_class} with the following attributes: Strength {strength}, Dexterity {dexterity}, Constitution {constitution}, Intelligence {intelligence}, Wisdom {wisdom}, Charisma {charisma}. "
                f"The player described the character as follows: '{description}'. Based on this information, please generate a compelling backstory for this character that is 10 paragraphs long and does not include any killing."),
        max_tokens=2048,
        temperature=temperature,
    )

    # Extract the character information from the API response
    character_info = response.choices[0].text.strip()

    # Display the character backstory to the user
    st.subheader("Your Character's Backstory:")
    st.write(character_info)
