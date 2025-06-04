import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

st.set_page_config(page_title="UPI QR Generator", page_icon="💸")
st.title("💸 UPI Payment QR Code Generator")

# Static details
upi_id = "v.gugan16@okaxis"
name = "v.gugan"
note = "Payment to Gugan"

with st.form("upi_form"):
    amount = st.text_input("Enter Amount (INR)", "100")
    submitted = st.form_submit_button("Generate QR")

if submitted:
    upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR&tn={note}"
    st.markdown(f"✅ **Generated UPI Link:** `{upi_link}`")

    # Generate QR code
    qr = qrcode.make(upi_link)
    buf = BytesIO()
    qr.save(buf)
    buf.seek(0)

    st.image(Image.open(buf), caption="📱 Scan this QR with Google Pay / PhonePe", use_column_width=False)
    st.download_button("📥 Download QR Code", data=buf, file_name="gpay_qr.png", mime="image/png")
