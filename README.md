
# ML Deployment Project: Iris Flower Classification

This project demonstrates a full-stack machine learning deployment using **Streamlit** and **scikit-learn**. It predicts the species of Iris flowers based on user input features.

## 🔍 Model Details
- Dataset: Iris
- Algorithm: Random Forest Classifier
- Library: scikit-learn

## 📁 Folder Structure
```
ml-deployment-project/
│
├── app.py                  # Streamlit UI
├── iris_model.pkl          # Trained ML model
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

## 🚀 How to Run Locally
```bash
# Clone the repository
https://github.com/YOUR_USERNAME/ml-deployment-project.git
cd ml-deployment-project

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scriptsctivate

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py
```

## 🌐 Deployment on AWS EC2
1. Launch an Ubuntu EC2 instance.
2. SSH into the instance:
```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```
3. Install Python and Git:
```bash
sudo apt update
sudo apt install python3-pip git
```
4. Clone your repo and install dependencies:
```bash
git clone https://github.com/YOUR_USERNAME/ml-deployment-project.git
cd ml-deployment-project
pip3 install -r requirements.txt
```
5. Run the app:
```bash
streamlit run app.py --server.port 80 --server.enableCORS false
```

## 🌸 Features
- Interactive sliders for input features
- Real-time prediction of Iris species
- Simple and intuitive UI

## 📦 Requirements
See `requirements.txt` for dependencies.

## 📬 Contact
For questions or suggestions, feel free to open an issue or reach out.
