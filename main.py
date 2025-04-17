import streamlit as st
import random
import base64

# --- Page Config ---
st.set_page_config(page_title="📝 Story Generator", layout="centered")

st.image("story.png", width=200, use_container_width=True)
# --- Optional Styling ---
st.markdown("""
    <style>
    .stApp {
        background-color: #1e1e1e;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: white;
    }
    .title {
        color: #6c5ce7;
        text-align: center;
        margin-bottom: 30px;
    }
    .score-box {
            background-color: #333333;
            border-radius: 20px;
            padding: 15px;
            margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>🪄 Interactive Story Creator</h1>", unsafe_allow_html=True)
st.markdown("Unleash your imagination. Fill in the blanks and see what kind of adventure you create! 🎨")

# --- User Inputs ---
with st.form("story_form"):
    name = st.text_input("👤 Enter a Name", value="Naomi")
    animal = st.text_input("🐾 Favorite Animal", value="Dragon")
    place = st.text_input("🗺️ A Place", value="Hydra")
    object_ = st.text_input("🎁 A Weird Object", value="Banana Phone")
    emotion = st.text_input("😲 An Emotion", value="Curious")
    power = st.text_input("🦸‍♂️ A Superpower", value="Flying")
    number = st.number_input("🔢 A Number", min_value=1, max_value=100, value=7)


    submitted = st.form_submit_button("✨ Generate Story")



# --- Story Templates ---
templates = [
    """Once upon a time in {place}, there was a brave soul named {name} who had a pet {animal}. One day, they stumbled upon a mysterious {object_} glowing under the moonlight. Feeling {emotion}, {name} activated their power of {power}, and with it, they saved {number} kittens from a burning building.""",

    """In the depths of {place}, {name} and their talking {animal} discovered a portal hidden inside a {object_}. Overcome with {emotion}, they jumped through and used their {power} to escape a time loop — but only after defeating {number} robot clowns.""",

    """There once lived a dreamer named {name}, who wandered the streets of {place} with their loyal {animal}. One rainy afternoon, they found an ancient {object_} stuck in a tree. Fueled by {emotion}, and armed with the ability to {power}, {name} challenged {number} wizards to a magical duel... and won!"""
]

# --- Generate Story ---
if submitted:
    if name and animal and place and object_ and emotion and power and number:
        story = random.choice(templates).format(
            name=name,
            animal=animal,
            place=place,
            object_=object_,
            emotion=emotion,
            power=power,
            number=int(number)
        )

        st.subheader("📖 Your Story:")
        st.write(story)

        # --- Download .txt Button ---
        story_bytes = story.encode("utf-8")
        b64 = base64.b64encode(story_bytes).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="my_story.txt">📥 Download as .txt</a>'
        st.markdown(href, unsafe_allow_html=True)
    else:
        st.warning("🚨 Please fill all fields to generate your story.")

# --- Sidebar ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3035/3035854.png", width=100)
st.sidebar.markdown("## 📜 How It Works")
st.sidebar.markdown("- Fill out the fun fields 🧠")
st.sidebar.markdown("- Click Generate ✨")
st.sidebar.markdown("- Read & Download your story 📥")
st.sidebar.markdown("---")
# 📬 Contact Section
st.sidebar.markdown("### 📬 Contact")
st.sidebar.write("📧 [Email Us](mailto:ismailahmedshahpk@gmail.com)")
st.sidebar.write("🔗 [Connect on LinkedIn](https://www.linkedin.com/in/ismail-ahmed-shah-2455b01ba/)")
st.sidebar.write("💬 [Chat on WhatsApp](https://wa.me/923322241405)")
st.sidebar.markdown("---")
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135716.png", width=90, use_container_width=True)
st.sidebar.markdown("---")
st.sidebar.markdown("<p style='text-align: center; color: grey;'>Build with ❤️ By Ismail Ahmed Shah</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")
