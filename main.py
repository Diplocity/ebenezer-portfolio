import streamlit as st

# Set up page configuration
st.set_page_config(
    page_title="Ebenezer Edem's Portfolio",
    page_icon="🌟",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Navigate to:", ["Home", "About Me", "Skills", "Projects", "Contact"])

# Home Page
if page == "Home":
    st.title("🌟 Welcome to My Portfolio!")

    # Welcome message
    st.write("""
    Hi there! I'm **Ebenezer Edem Zuh**, a passionate developer and data analyst. I enjoy solving problems, building interactive applications, and using technology to create real value. Feel free to reach out if you'd like to connect or learn more about what I do!
    """)

    # Profile Picture below the welcome message
    st.image("profile.jpg", width=150)  # Replace with your profile picture file

    st.write("""
   I am an experienced developer with a strong background in data analysis, machine learning and web development.I have had the opportunity to work on a variety of projects that involve real-time data analysis, building recommendation systems, and creating dynamic dashboards. My passion for solving complex problems through innovative solutions has driven me to continuously expand my skill set and tackle new challenges. I invite you to explore my portfolio to gain a deeper understanding of the projects I have worked on and the expertise I bring to every project I undertake.
    """)

# About Me Page
elif page == "About Me":
    st.title("About Me")
    st.image("profile.jpg", width=150)  # Replace with your profile picture file
    st.write("""
    I am a passionate professional with a strong background in data science, web development and programming. I specialize in creating intuitive solutions to complex problems using technology, with experience in real-time data analysis, recommendation systems, and dynamic dashboards. I am currently expanding my expertise in full-stack web development and data analytics.

With skills in Python, Flask, Streamlit and database management (MySQL, SQLite), I focus on building scalable applications and integrating APIs for real-time functionality. I am committed to continuous learning and eager to contribute to impactful projects that challenge my skills and knowledge. Feel free to explore my portfolio to learn more about my work.
    """)

# Skills Page
elif page == "Skills":
    st.title("Skills")
    st.write("Here are some of the technical skills and tools I use:")

    # Using expanders for different categories of skills
    with st.expander("Programming Languages"):
        st.write("- Python")
        st.write("- JavaScript")
        st.write("- SQL")
        st.write("- C++")
        st.write("- Java")

    with st.expander("Frameworks & Tools"):
        st.write("- Streamlit")
        st.write("- Flask")
        st.write("- Dash")
        st.write("- Vue.js")

    with st.expander("Data Science"):
        st.write("- Pandas")
        st.write("- NumPy")
        st.write("- Scikit-learn")
        st.write("- Matplotlib")

    with st.expander("Web Development"):
        st.write("- HTML")
        st.write("- CSS")
        st.write("- JavaScript")
        st.write("- Flask")

# Projects Page
elif page == "Projects":
    st.title("Projects")

    # Using expanders to showcase projects
    with st.expander("Project 1: Movie Recommendation System"):
        st.markdown("""
        **[Movie Recommendation System](https://movieexplorer.streamlit.app/)**  
        A recommendation engine that suggests movies based on user preferences using collaborative filtering 
        and content-based filtering techniques.  
        **Technologies used**: Python, Pandas, Scikit-Learn  
        **Features**:
        - Collaborative filtering for recommendations
        - Content-based filtering for personalized suggestions
        - Real-time user interaction
        """)

    with st.expander("Project 2: Real-Time Stock Price Dashboard"):
        st.markdown("""
        **[Real-Time Stock Price Dashboard](https://stock-0sj0.onrender.com/)**  
        An interactive dashboard for tracking stock prices using Streamlit. It allows users to view real-time data 
        and visualize price trends.  
        **Technologies used**: Python, Streamlit, Finnhub API  
        **Features**:
        - Real-time stock data visualization
        - Ability to select different time intervals
        - Displaying weekly high stock prices
        """)

    with st.expander("Project 3: Real-Time Weather Dashboard"):
        st.markdown("""
        **[Real-Time Weather Dashboard](https://real-time-weather-vph6.onrender.com)**  
        A real-time weather app that displays weather information for selected cities worldwide, including temperature, 
        humidity, and other details.  
        **Technologies used**: Python, Streamlit, Weather API  
        **Features**:
        - Real-time weather data
        - City-wise selection
        - Comprehensive weather insights
        """)

# Contact Page
elif page == "Contact":
    st.title("Contact Me")
    st.markdown("""
    ### Let’s Connect! 🤝  
    I’d love to hear from you—whether you have a project in mind, a question, or just want to say hi!  
    """)
    st.write("📧 [Email Me](mailto:trugoy64@gmail.com)")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/edem360/)")
    st.write("🐙 [GitHub](https://github.com/Diplocity)")

    # WhatsApp link with visible number
    st.write("📱 [Click to WhatsApp Me](https://wa.me/4915733302744) or contact me directly at **+49 157 33302744**")

    st.subheader("Send a Message")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.success("Thank you! Your message has been received.")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("© 2024 Ebenezer Edem Zuh | Built with ❤️ using Streamlit")
