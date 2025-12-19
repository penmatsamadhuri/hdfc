import streamlit as st
import pandas as pd
from supabase import create_client


SUPABASE_URL="https://vhbkuopezvcvfbpjryro.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZoYmt1b3BlenZjdmZicGpyeXJvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYwNDA3OTYsImV4cCI6MjA4MTYxNjc5Nn0.pgEr4B-ubxw6DYc2ZO02C_boak8jgzccli0sExOdlPs"

supabase=create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("HDFC BANK(supabase)")
menu=["REGISTER","VIEW"]
choice=st.sidebar.selectbox("Menu",menu)
if choice=="REGISTER":
    name=st.text_input("Enter Name")
    age=st.number_input("AGE",min_value=18)
    account=int(st.number_input("ACCOUNT NUMBER"))
    bal=st.number_input("BALANCE",min_value=500)
    if st.button("Save"):
        supabase.table("users").insert({
            "name":name,
            "age":age,
            "account":account,
            "balance":bal}).execute()
        st.success("user added successfully")

if choice=="VIEW":
    st.subheader("View users")
    data=supabase.table("users").select("*").execute()
    df=pd.DataFrame(data.data)
    st.dataframe(df)
