import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")


st.header("The Best Company")
st.write("""Systems analysts work to optimize user experience with programs.
          These professionals advise employers and clients on which software 
          they may need, implement the software, and liaise with users to ensure
          the programs function properly.
          Systems analysts work to optimize user experience with programs.
          These professionals advise employers and clients on which software 
          they may need, implement the software, and liaise with users to ensure
          the programs function properly.
          Systems analysts work to optimize user experience with programs.
          These professionals advise employers and clients on which software 
          they may need, implement the software, and liaise with users to ensure
          the programs function properly.""")

st.subheader("Our Team")

data = pd.read_csv("data (1).csv")

col1,  col2, col3 = st.columns(3)
with col1:
    for index, row in data[:4].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images/" + (row["image"]))

with col2:
    for index, row in data[4:8].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images/" + (row["image"]))

with col3:
    for index, row in data[8:].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images/" + (row["image"]))

