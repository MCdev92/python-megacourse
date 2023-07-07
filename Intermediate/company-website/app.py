import streamlit as st
import pandas

# Set webpage layout to wide
st.set_page_config(layout="wide")

# Add a header and some other text
st.title("Mc Techologies Inc.")
st.info(""" Welcome to MC Technology, a premier technology staffing firm dedicated
to delivering exceptional talent solutions for the modern digital landscape.
At MC Technology, we recognize that technology is the driving force behind businesses
today. As a trusted partner, we specialize in connecting enterprises with 
highly skilled professionals who possess the expertise, innovation, and strategic
mindset to propel businesses forward. """)
st.subheader("Our Team")

# prepare the columns
col1, col2, col3 = st.columns(3)

# Make a dataframe with the company members
df = pandas.read_csv("data.csv")

# Add content to the first column
with col1:
    # Iterate over only the first four rows
    for index, row in df[:4].iterrows():
        # Add member's first and last names
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])

with col2:
     # Iterate over rows 4 to 7
    for index, row in df[4:8].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])
        
with col3:
    # Iterate over rows 4 to 7
    for index, row in df[8:].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])