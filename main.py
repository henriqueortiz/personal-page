import streamlit as st

def main():
    # Custom CSS for styling
    custom_css = """
    <style>
    /* This styles the sidebar */
    .css-1d391kg { 
        background-color: #f0f2f6;  # Change the background color
        color: #f63366;  # Change the text color
        font-size: 16px;  # Change the font size
    }
    /* This styles the radio items in the sidebar */
    label.css-11gv8vo {
        font-size: 16px;
        color: #333;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    st.sidebar.title("Navigation")
    menu = ["Home", "About", "Skills", "Experience", "Projects", "Contact"]
    choice = st.sidebar.radio("Go to", menu)

    if choice == "Home":
        st.subheader("Home")
        st.write("Welcome to my personal page!")
        st.image("./foto.jpg", caption="Senior Data Engineer")
    
    elif choice == "About":
        st.subheader("About Me")
        st.write("Hello! I’m Henrique Ortiz, a Senior Data Engineer with 7 years of experience in building scalable solutions. I specialize in developing robust data warehouses and data lakes.")
    
    elif choice == "Skills":
        st.subheader("Skills")
        st.write("""
        **General:** Python, Git, Linux, SQL, Bash, Docker  
        **Visualization Tools:** Tableau, Power BI, Looker Studio, SAP Business Objects  
        **Google Cloud:** CloudRun, CloudFunctions, CloudStorage, Dataproc, BigQuery  
        **Pipeline Orchestration:** Apache Airflow, Apache Beam, Pentaho Data Integration
        """)
    
    elif choice == "Experience":
        st.subheader("Experience")
        st.write("""
        - Developed and implemented comprehensive data warehouse solutions to manage large-scale data across multiple platforms.
        - Designed and optimized data lakes, enhancing data availability and accessibility for business intelligence tools.
        """)
    
    elif choice == "Projects":
        st.subheader("Projects")
        st.write("Here, I would detail some of the key projects I've worked on, focusing on challenges faced and solutions provided.")

    elif choice == "Contact":
        st.subheader("Contact Me")
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message")
            submit_button = st.form_submit_button("Submit")
            if submit_button:
                st.write("Thanks for your message, ", name, "! I will get back to you soon.")

if __name__ == "__main__":
    main()
