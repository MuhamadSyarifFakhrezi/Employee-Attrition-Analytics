## Business Understanding

Walaupun telah menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

### Permasalahan Bisnis

Untuk mencegah hal ini semakin parah, manajer departemen HR ingin meminta bantuan untuk mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, ia juga meminta untuk membuat business dashboard untuk membantunya memonitori berbagai faktor tersebut.

### Cakupan Proyek

Untuk menjawab permasalahan bisnis tersebut, pada proyek ini kita menerapkan dua metode yaitu analisis korelasi dan machine learning. Algoritma machine learning yang digunakan adalah Random Forest Classifier, dengan model yang dibuat kita terapkan function 'feature importaces' untuk mengetahui feature apa saja yang paling berpengaruh terhadap attrition.

Kita juga akan melakukan sedikit proses Exploratory Data Analysis (EDA) untuk memperoleh distribusi data dan gambaran terkait dataset yang kita gunakan.

Selain itu kita juga membuat business dashboard menggunakan Tableau untuk memberikan insight dari data yang sedang dianalisis, dan berguna untuk memonitori feature/faktor yang mempengaruhi tingginya tingkat attrition.

Kita juga membuat web app pada streamlit yang dapat digunakan untuk memprediksi attrition dari data karyawan yang diinput.

### Persiapan

Sumber data: [data.csv](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/employee/employee_data.csv)

Setup environment:
1. Buka file [notebook.ipynb](https://github.com/MuhamadSyarifFakhrezi/Employee-Attrition-Analytics/edit/main/notebook.ipnyb) pada Google Colaboratory
2. Jalankan kode berikut
   ```
   !pip install -r requirements.txt
   ```

### Run Streamlit App

```
streamlit run app.py
```
Link Streamlit App Prediction: [attrition-predictor](https://attrition-predictor.streamlit.app/)

## Business Dashboard
![muhamadsyarif-dashboard](https://github.com/user-attachments/assets/5bd2970b-e67c-463f-a77d-f4ab5865be53)
![muhamadsyarif-dashboard2](https://github.com/user-attachments/assets/ac206197-4f78-4419-9b0b-b8f7c80bf769)

Berdasarkan dashboard yang telah dibuat, berikut ini adalah beberapa insight yang diperoleh:
- Karyawan yang berumur 18-26 tahun memiliki presentase tingkat attrition yang lebih tinggi.
- gender tidak memiliki pengaruh terhadap attrition.
- Karyawan yang belum menikah memiliki tingkat attrition yang lebih tinggi dibandingkan dengan kategori lain pada status perkawinan.
- Karyawan dengan latar belakang pendidikan dibidang Technical Degree memiliki tingkat attrition tertinggi dibanding bidang lain, namun perbedaan tingkat attrition antar bidang tidak terlalu signifikan.
- Karyawan dengan pendapatan perbulan antara 1k-4k lebih memungkinkan untuk resign.
- Karyawan dengan jumlah tahun kerja kurang dari 3 tahun memiliki persentase resign lebih tinggi. *(Pada grafik ini karyawan dengan total working years 40 tahun kita abaikan karena sudah berumur kurang lebih 60 tahun, yang mana merupakan rata-rata orang berhenti bekerja)*
- Karyawan yang bekerja melebihi waktu kerja/lembur lebih mungkin untuk resign.
- Karyawan dengan tingkat level pekerjaan yang paling rendah lebih cenderung untuk resign.
- Posisi/peran pekerjaan yang memiliki tingkat presentase resign tertinggi adalah Sales Representative, perbedaannya cukup signifikan jika dibandingkan dengan peran lain.

Link dashboard yang dapat diakses: [Tableau Dashboard](https://public.tableau.com/views/HRAttritionDashboard_17148452730550/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link).

## Conclusion

Berdasarkan analisis korelasi heatmap, visualisasi, dan machine learning feature yang paling berpengaruh secara signifikan baik secara positif maupun negatif terhadap attrition karyawan adalah Age, Monthly Income, OverTime, dan Total Working Years.

Karyawan yang mengalami Over Time, karyawan yang berumur muda(18-26 tahun), yang memiliki pendapatan perbulan cenderung rendah(1k-4k), dan total tahun kerja yang relatif rendah(kurang dari 3 tahunn) merupakan karakteristik karyawan yang lebih berpotensi untuk keluar dari pekerjaannya.

Selain itu karakteristik tambahan yang juga dapat mempengaruhi kemungkinan karyawan untuk resign antara lain: karyawan yang belum menikah, karyawan dengan peran/posisi sebagai Sales Representative, dan karyawan yang memiliki level pekerjaan yang rendah.

### Recomendation Action Items

Beberapa rekomendasi aksi yang dapat dilakukan untuk memperbaiki tingkat attrition karyawan saat ini antara lain:  
- Perusahaan mungkin dapat memberikan jalan karir yang jelas kepada karyawan muda agar mereka merasa terdorong untuk tetap bertahan di perusahaan. Ini bisa meliputi program pengembangan, pelatihan, atau mentorship yang ditujukan khusus untuk mereka.
- Perusahaan dapat memantau dan mengatur jam kerja karyawan secara bijak agar tidak terjadi beban kerja yang berlebihan dan berpotensi menimbulkan atrisi.
- Tinjau kembali kebijakan kompensasi perusahaan untuk memastikan bahwa gaji yang ditawarkan kompetitif dan sesuai dengan kontribusi yang karyawan berikan.
- Tinjau kembali proses onboarding perusahaan untuk memastikan bahwa karyawan baru mendapatkan dukungan dan pembekalan yang cukup untuk berhasil dalam peran mereka.
- Perusahaan mungkin dapat mempertimbangkan program dukungan atau kasejahteraan karyawan seperti dukungan sosial, program mentoring, atau kegiatan sosial untuk memperkuat ikatan antarkaryawan.
- Perusahaan dapat mengidentifikasi posisi Sales Representative, kemudian kembangkan strategi retensi khusus untuk mempertahankan karyawan yang mengisi peran tersebut.
- Lakukan analisis untuk memahami kebutuhan dan harapan karyawan dengan tingkat level pekerjaan yang paling rendah.
