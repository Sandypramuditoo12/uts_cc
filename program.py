import streamlit as st

# Judul aplikasi
st.title("💸 Kalkulator Diskon Online")

# Deskripsi
st.write("""
Masukkan harga dan diskon untuk menghitung total harga setelah potongan.
""")

# Input harga dan diskon
harga_asli = st.number_input("Masukkan harga asli (Rp)", min_value=0.0, step=1000.0)
diskon = st.slider("Masukkan diskon (%)", min_value=0, max_value=100, value=10)

# Tombol hitung
if st.button("Hitung Harga Setelah Diskon"):
    harga_diskon = harga_asli * (1 - diskon / 100)
    st.success(f"Harga setelah diskon {diskon}% adalah **Rp {harga_diskon:,.0f}**")

    # Tambahan informasi
    st.info(f"Potongan harga: Rp {harga_asli - harga_diskon:,.0f}")

# Footer
st.caption("Dibuat dengan ❤️ menggunakan Streamlit")
