import streamlit as st
from PIL import Image

# Load profile picture
profile_pic = Image.open("profile.png")

# Page config
st.set_page_config(page_title="My Portfolio", page_icon="📁", layout="wide")

# Sidebar
with st.sidebar:
    st.image(profile_pic, width=150)
    st.title("Otieno James Odongo")
    st.write("📧 jamesodongo1290@gmail.com")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/james-otieno-90a951253?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")
    st.write("💻 [GitHub](https://github.com/jamesodongoo)")
    st.write("📄 [Resume](https://drive.google.com/file/d/1pwUPcwMEP24roNP9fE5Ehp_9G4UdVd0k/view?usp=sharing)") 

# Main page
st.title("👋 Welcome to My Portfolio")

st.header("🧑‍💻 About")
st.write("""
Hi there! I'm a data enthusiast with a passion for transforming raw information into meaningful insights that solve real-world problems. 

I currently work as a Data Analytics and Machine Learning Trainer at Adaptive Management and Research Consultants (AMREC) in Nairobi, where I mentor students on how to apply statistical and programming skills in health research. My academic background is in Biostatistics (B.Sc.) from Jomo Kenyatta University of Agriculture and Technology, where I developed a strong foundation in data science, epidemiological analysis, and statistical modeling. 

Beyond the classroom, I’ve led and contributed to innovative projects from mapping neonatal mortality in Kenya to building intelligent AI-driven systems and chatbots. My work blends technical skills in Python, R, Stata, and Streamlit with a deep curiosity for solving meaningful challenges through research and technology. 

🏅 I’ve earned recognition through participation in hackathons, professional certification from KEMRI, and leadership roles within academic associations. I’m also fluent in both English and Swahili. 

Currently, I’m exploring how AI tools and automation can shape the future of research, data systems, and decision-making in Africa and beyond 

🤝 I'm open to collaborations on data and AI projects.

""")

st.header("📂 Projects")

projects = {
    "Prediction of Neonatal Mortality": "The project used Machine Learning to predict the neonatal mortality rate in Kenya using 2022 KDHS data",
    "Victoria Pride Chatbot": "A chatbot for Victoria Pride.",
    "Real Estate Value Tracker": "Built a web based application that used mock data to show how real estate agents can track the house prices over time.",
    "Real-time Object Detection": "Used YOLOv8 and Streamlit to detect and count vehicles in real-time traffic videos."
}

for project, description in projects.items():
    st.subheader(f"🔹 {project}")
    st.write(description)

st.header("📬 Contact Me")
st.write("Feel free to reach out via email or LinkedIn!")

