# 🧬 PCOS Diagnosis Web App using Django + ML

This project uses **Machine Learning** to diagnose **Polycystic Ovary Syndrome (PCOS)** and wraps the model in a simple **Django web application**. It allows both **patients** and **doctors** to input clinical or physical data and get a quick diagnosis based on two trained Random Forest models.

---

## 📌 Table of Contents

- [📖 About PCOS](#-about-pcos)
- [🛠️ Tech Stack](#-tech-stack)
- [📁 Project Structure](#-project-structure)
- [🔧 ML Workflow](#-ml-workflow)
- [🌐 Django Features](#-django-features)
- [📈 Model Details](#-model-details)
- [🚀 Getting Started](#-getting-started)
- [📬 Contact](#-contact)

---

## 📖 About PCOS

**Polycystic Ovary Syndrome (PCOS)** is a common hormonal disorder in women of reproductive age. Symptoms include irregular periods, excess androgen levels, and polycystic ovaries. This project uses machine learning to assist in early diagnosis.

---

## 🛠️ Tech Stack

| Layer            | Tech Used                             |
| ---------------- | ------------------------------------- |
| Machine Learning | Python, scikit-learn, pandas, seaborn |
| Web Framework    | Django 4.x                            |
| Frontend         | HTML, CSS (Bootstrap)                 |
| Model I/O        | joblib                                |

---

## 📁 Project Structure

```
pcos-diagnosis/
│
├── ML/
│   ├── PCOS_Diagnosis.ipynb        ← Full analysis & model building
│   ├── predictor_40.pkl            ← Random Forest model (all 40 features)
│   ├── predictor_23.pkl            ← Lightweight model (23 features)
│   └── dataset/                    ← Raw CSV/XLSX datasets
│
├── pcos_django/
│   ├── manage.py
│   ├── pcos_django/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── predictor/
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── templates/
│   │   │   ├── home.html
│   │   │   ├── result.html
│   │   │   └── about.html
│   │   └── static/
│   │       └── css/
│   └── models/
│       └── predictor_40.pkl
│       └── predictor_23.pkl
│
├── requirements.txt
└── README.md
```

---

## 🔧 ML Workflow

1. **Load and merge data**
2. **Clean, preprocess, and normalize**
3. **EDA** (BMI, cycles, hormonal features)
4. **Model training**
5. **Model saving with `joblib`**
6. **Model loading in Django views**

---

## 🌐 Django Features

- 🔐 **Two user levels**

  - Patient: enters general physical details
  - Doctor: inputs clinical, hormonal, and scan-based features
- 🔎 **Model switch**

  - Uses the 40-feature model for doctors and 23-feature model for patients
- 📊 **Instant Results**

  - Prediction shown with probabilities and diagnosis flag (PCOS/Non-PCOS)
- 🎨 **Frontend**

  - Responsive Bootstrap-based UI

---

## 📈 Model Details

| Model Type        | Features Used | Accuracy | File Name            |
| ----------------- | ------------- | -------- | -------------------- |
| Full Model        | 40            | High     | `predictor_40.pkl` |
| Lightweight Model | 23            | High     | `predictor_23.pkl` |

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/pcos-diagnosis.git
cd pcos-diagnosis
```

### 2. Set up Environment

```bash
python -m venv venv
source venv/bin/activate     # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Run Django Server

```bash
python manage.py runserver
```

### 4. Open in Browser

Visit: `http://127.0.0.1:8000/`

---

## 🧪 Testing

- You can test the web app by switching user roles on the homepage.
- Try submitting dummy data (within real value ranges).
- Review prediction and probability confidence.

---

## 📬 Contact

Made with ❤️ by **Prashansa Agarwal**

- 📧 Email: prashansaagarwal101@gmail.com
- 💼 LinkedIn: www.linkedin.com/in/prashansa-agarwal/
- 🌐 GitHub: github.com/prashansa19/

---

> If you found this useful, please ⭐️ the repo and share!
