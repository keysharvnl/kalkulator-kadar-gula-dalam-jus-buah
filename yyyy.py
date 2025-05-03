import streamlit as st
import pandas as pd

# Menampilkan slide untuk pendahuluan
st.markdown(
    """
    <div style='background-color: #f0f0f0; padding: 20px; border-radius: 10px;'>
        <h2 style='color: #333333; text-align:center;'>Selamat Datang di Aplikasi Menghitung Kadar Gula Dalam Jus Buah</h2>
        <p style='color: #333333; text-align:justify;'>Aplikasi ini dirancang untuk membantu Anda menghitung jumlah kadar gula dalam berbagai jenis buah sebanyak 250mL. . 
        Pilih jus buah yang anda ingin ketahui kadar gulanya dan aplikasi kami akan memberikan informasi tentang jumlah kadar gulanya.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Informasi tambahan tentang manfaat kesehatan, cara memilih buah yang baik, dan resep
informasi_tambahan = {
    'apel': {
        'manfaat': "Apel mengandung serat yang baik untuk pencernaan dan antioksidan yang dapat membantu menjaga kesehatan jantung.",
        'cara_memilih': "Pilih apel yang berwarna cerah, beratnya padat, dan tanpa memar. Hindari apel yang terlalu lembek.",
        
    },
    'pisang': {
        'manfaat': "Pisang kaya akan kalium yang baik untuk kesehatan jantung dan membantu menjaga tekanan darah.",
        'cara_memilih': "Pilih pisang yang kulitnya tidak terlalu berwarna hijau dan tidak terlalu berwarna cokelat. Pilih yang masih dalam kondisi sedikit kehijauan.",
        
    },
    'jeruk': {
        'manfaat': "Jeruk kaya akan vitamin C yang baik untuk sistem kekebalan tubuh dan mengandung antioksidan untuk kesehatan kulit.",
        'cara_memilih': "Pilih jeruk yang beratnya padat dan berwarna cerah. Hindari jeruk yang terlalu lembek atau memiliki bintik-bintik coklat.",
        
    },
    'pir': {
        'manfaat': "Pir mengandung serat yang baik untuk pencernaan dan mengandung antioksidan yang membantu menjaga kesehatan tubuh.",
        'cara_memilih': "Pilih pir yang berwarna cerah dan padat. Hindari pir yang terlalu lembek atau memiliki bintik-bintik coklat.",
        
    },
    'strawberry': {
        'manfaat': "Stroberi kaya akan vitamin C dan antioksidan yang baik untuk kesehatan jantung dan kulit.",
        'cara_memilih': "Pilih stroberi yang berwarna cerah, tanpa noda hitam, dan berukuran sedang.",
        
    },
    'semangka': {
        'manfaat': "Semangka mengandung air yang tinggi, membantu menjaga hidrasi tubuh, dan mengandung antioksidan untuk kesehatan kulit.",
        'cara_memilih': "Pilih semangka yang beratnya padat dan memiliki bintik kuning di bagian bawahnya.",
        
    },
    'mangga': {
        'manfaat': "Mangga mengandung vitamin A dan C yang baik untuk kesehatan mata dan sistem kekebalan tubuh.",
        'cara_memilih': "Pilih mangga yang berwarna cerah, beratnya padat, dan sedikit memberi aroma di pangkalnya.",
        
    },
    'alpukat': {
        'manfaat': "Alpukat kaya akan lemak sehat, serat, dan vitamin K. Baik untuk kesehatan jantung dan otak.",
        'cara_memilih': "Pilih alpukat yang memberi sedikit tekanan ketika ditekan dan beratnya terasa padat.",

        
    },
    'kiwi': {
        'manfaat': "Kiwi kaya akan vitamin C dan serat yang baik untuk pencernaan.",
        'cara_memilih': "Pilih kiwi yang memberi sedikit tekanan ketika ditekan, hindari yang terlalu lembek.",

    },
    'melon': {
        'manfaat': "Melon dpaat meningkatkan hidrasi, kaya vitamin C, dan mendukung kesehatan mata.",
        'cara_memilih': "perhatikan aroma, permukaan yang halus, berat yang seimbang, dan warna yang cerah.",
    },
    'buah naga': {
        'manfaat': "Buah Naga  dapat meningkatkan sistem kekebalan tubuh, menjaga kesehatan kulit, dan membantu pencernaan.",
        'cara_memilih': "pilih yang memiliki warna cerah, sisik yang sedikit layu, dan hindari yang memiliki noda atau kecokelatan pada ujung sisiknya."
    },
    'sirsak': {
        'manfaat': "meningkatkan daya tahan tubuh, meredakan peradangan, dan melancarkan pencernaan.",
        'cara_memilih' : "  pilih yang kulitnya agak lunak, berwarna cerah, dan memiliki duri yang jarang serta lunak.",
        
    }  
}    
# Tambahkan tautan ke informasi tambahan untuk buah yang dipilih
st.sidebar.title('Informasi Tambahan')
buah_info = st.sidebar.selectbox('Pilih Jus Buah', list(informasi_tambahan.keys()), format_func=lambda x: x.capitalize())

# Tambahkan fitur interaktif untuk membuka atau menutup informasi tambahan
if buah_info:
    if st.sidebar.checkbox('Tampilkan Informasi Tambahan'):
        st.sidebar.subheader('Manfaat Kesehatan:')
        st.sidebar.write(informasi_tambahan[buah_info]['manfaat'])

        st.sidebar.subheader('Cara Memilih Buah yang Baik:')
        st.sidebar.write(informasi_tambahan[buah_info]['cara_memilih'])


# Melanjutkan dengan kode aplikasi Streamlit Anda seperti biasa
kadar gula_buah = {
    'Jus apel': {
        'kadar gula': 24, 
        'vitamin': {'Vitamin A': '3%', 'Vitamin C': '14%'},
        
    },
    'pisang': {
        'kadar gula': 24,
        'vitamin': {'Vitamin B6': '20%', 'Vitamin C': '14%'},
        
    },
    'jeruk': {
        'kadar gula': 21,
        'vitamin': {'Vitamin C': '90%'},
        
    },
    'pir': {
        'kadar gula': 12,
        'vitamin': {'Vitamin C': '7%'},
        
    },
    'strawberry': {
        'kadar gula': 13,
        'vitamin': {'Vitamin C': '98%'},
        
    },
    'semangka': {
        'kadar gula': 9,
        'vitamin': {'Vitamin A': '11%', 'Vitamin C': '13%'},
        
    },
    'mangga': {
        'kadar gula': 30,
        'vitamin': {'Vitamin A': '25%', 'Vitamin C': '76%'},
       
    },
    'alpukat': {
        'kadar gula': 2,
        'vitamin': {'Vitamin K': '26%', 'Vitamin E': '14%'},
   
    },
    'kiwi': {
        'kadar gula': 20,
        'vitamin': {'Vitamin C': '112%', 'Vitamin K': '38%'},
   
    },
    'melon': {
        'kadar gula': 12,
        'vitamin': {'Vitamin A': '12%', 'Vitamin C': '61%'},
        
    },
    
    'buah naga': {
        'kadar gula': 15,
        'vitamin': {'Vitamin C': '9%', 'Vitamin B3': '8%'},
    
    },
    'sirsak': {
        'kadar gula': 11,7,
        'vitamin': {'Vitamin C': '24%', 'Vitamin B6': '5%'},
     
    
    }
}    

# Sekarang lanjutkan dengan kode aplikasi Streamlit Anda seperti biasa

st.title('Menghitung Kadar Gula dalam Jus Buah')
st.write("Selamat datang di aplikasi menghitung kadar gula dalam jus buah. Pilih buah favorit Anda , lalu kami akan memberi tahu Anda jumlah kadar gula yang terkandung.")
buah = st.selectbox('Pilih Buah', list(kadar gula_buah.keys()), format_func=lambda x: x.capitalize())



if st.button('Hitung Kadar Gula'):
    kadar gula_total = (kadar gula_buah[buah]['kadar gula'] / 250) 
    st.write(f"Jumlah kadar gula dalam 250mL jus buah adalah: {kadar gula_total} gram")
    st.write("Kandungan Vitamin:")
    for vitamin, nilai in kadar gula_buah[buah]['vitamin'].items():
        st.write(f"- {vitamin}: {nilai}")
