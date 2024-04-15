import streamlit as st
import requests
from bs4 import BeautifulSoup

def extract_frontend_code(url):
    try:
        # Fetch the HTML content of the website
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')

            # Extract front-end code (HTML, CSS, JavaScript)
            front_end_code = str(soup)

            return front_end_code
        else:
            st.error(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

def main():
    st.title("Frontend Code Extractor")

    # Get URL input from the user
    url = st.text_input("Enter the URL of the website:")

    if st.button("Extract Frontend Code"):
        if url:
            frontend_code = extract_frontend_code(url)
            if frontend_code:
                # Display the extracted front-end code
                st.code(frontend_code, language='html')
        else:
            st.warning("Please enter a URL.")

if __name__ == "__main__":
    main()
