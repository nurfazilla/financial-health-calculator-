import streamlit as st

#### Define questions and point system
questions = {
    "1. Terangkan keadaan sumber pendapatan anda?": {
        "Sumber pendapatan yang tidak menentu": 1,
        "Mempunyai sumber pendapatan yang stabil": 2,
        "Mempunyai sumber pendapatan yang stabil dan selesa": 3,
        "Mempunyai pelbagai sumber pendapatan yang stabil": 4,
        "Mempunyai pelbagai sumber pendapatan aktif dan pasif yang kukuh": 5
    },
    "2. Berdasarkan sumber pendapatan anda, bagaimanakah anda merancang perbelanjaan bulanan?": {
        "Jumlah perbelanjaan melebihi pendapatan": 1,
        "Anggaran perbelanjaan mengikut pendapatan": 2,
        "Mempunyai lebihan wang selepas perbelanjaan": 3,
        "Perbelanjaan jauh lebih rendah berbanding pendapatan": 4,
        "Satu atau dua sumber pendapatan boleh menampung perbelanjaan ": 5
    },
    "3. Berapakah jumlah simpanan anda pada masa ini?": {
        "Tidak mampu menyimpan": 1,
        "Mampu menyimpan tetapi sudah tiada simpanan": 2,
        "Mempunyai simpanan bersamaan dengan 1-6 bulan pendapatan": 3,
        "Mempunyai simpanan bersamaan dengan 6-12 bulan pendapatan": 4,
        "Mempunyai simpanan melebihi 12 bulan pendapatan": 5
    },
    "4. Adakah anda memiliki aset?": {
        "Tiada aset": 1,
        "Memiliki aset untuk kegunaan sendiri ": 2,
        "Memiliki aset untuk kegunaan sendiri dan sebahagian aset untuk pelaburan": 3,
        "Memiliki aset untuk kegunaan sendiri dan keluarga dan pelbagai aset untuk pelaburan": 4,
        "Memiliki aset untuk kegunaan sendiri dan keluarga dan pelbagai aset yang memberikan pulangan secara konsisten ": 5
    },
    "5. Adakah anda mampu untuk membayar balik hutang anda dengan pendapatan bulanan?": {
        "Pendapatan bulanan tidak mampu untuk membayar balik hutang anda": 1,
        "Pendapatan bulanan mampu untuk membayar balik hutang anda": 2,
        "Pendapatan bulanan mampu untuk membayar balik hutang dan mempunyai lebihan wang selepas pembayaran": 3,
        "Pendapatan bulanan mampu untuk membayar balik hutang dan mampu menjana pendapatan ": 4,
        "Bebas daripada hutang ": 5
    },
    "6. Adakah anda mempunyai perlindungan insurans?": {
        "Tiada perlindungan insurans": 1,
        "Mempunyai perlindungan insurans yang minimum untuk diri sendiri atau perlindungan insurans daripada majikan sahaja": 2,
        "Mempunyai perlindungan insurans yang bersamaan dengan pendapatan tahunan untuk anda dan keluarga ": 3,
        "Mempunyai perlindungan insurans yang bersamaan dengan 2 atau 3 kali pendapatan tahunan untuk anda dan keluarga ": 4,
        "Mempunyai perlindungan insurans yang melebihi 3 kali pendapatan tahunan untuk anda dan keluarga ": 5
    },  
}

#### Define result categories and their details
result_categories = {
    "Stage 1: Kewangan Tidak Stabil": {
        "range": (6, 12),
        "image": "https://raw.githubusercontent.com/nurfazilla/financial-health-calculator-/main/Stage%201.JPG"
    },
    "Stage 2: Kestabilan Kewangan": {
        "range": (13, 18),
        "image": "https://raw.githubusercontent.com/nurfazilla/financial-health-calculator-/main/Stage%202.JPG",
    },
    "Stage 3: Keselamatan Kewangan": {
        "range": (19, 24),
        "image": "https://raw.githubusercontent.com/nurfazilla/financial-health-calculator-/main/Stage%203.JPG"
    },
    "Stage 4: Kebebasan Kewangan": {
        "range": (25, 30),
        "image": "https://raw.githubusercontent.com/nurfazilla/financial-health-calculator-/main/Stage%204.JPG"
    },
    "Stage 5: Kekayaan Kewangan": {
        "range": (31, 36),
         "image": "https://raw.githubusercontent.com/nurfazilla/financial-health-calculator-/main/Stage%205.JPG"
    },
}

#### create streamlit app
def main():
    st.title("Jom Nilai Tahap Kesihatan Kewangan Anda!")

    question_number = 0
    total_points = 0

    for question, options in questions.items():
        st.write(question)
        selected_option = st.radio("Pilih satu jawapan:", [''] + list(options.keys()), key=question_number)
        if selected_option:
            total_points += options[selected_option]
        question_number += 1

    if question_number == len(questions):
        if st.button("Calculate"):
            st.write("Calculating result...")
            result_category = calculate_result_category(total_points)
            display_result(result_category)

def calculate_result_category(total_points):
    for category, details in result_categories.items():
        if details["range"][0] <= total_points <= details["range"][1]:
            return category

def display_result(result_category):
    st.subheader("Result:")
    if result_category:
        st.write(f"Berdasarkan maklum balas anda, anda berada pada kategori'{result_category}'")
        result_image = result_categories[result_category].get("image")
        if result_image:
            st.image(result_image, caption="Category Image", use_column_width=True)

if __name__ == "__main__":
    main()
