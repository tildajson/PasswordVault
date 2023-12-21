import streamlit as st
import ipapi

st.set_page_config(page_title="IP Lookup")

st.markdown("# IP Lookup")
st.sidebar.header("IP Lookup")
st.write("### Enter the IP address you want to identify")

enter_ip = st.text_input("Enter IP Address")

if st.button("Search"):
    data = ipapi.location(ip=enter_ip, output="json")
    try:
        with st.container(border=True):
            st.write("City: ", data["city"])
            st.write("Region: ", data["region"])
            st.write("Country: ", data["country_name"])
            st.write("Postal Code: ", str(data["postal"]))
            st.write("Latitude: ", str(data["latitude"]))
            st.write("Longitude: ", str(data["longitude"]))
            st.write("Service Provider: ", data["org"])
    except:
        st.error("Cannot find the given IP address.")
