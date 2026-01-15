# Smart Waste Monitoring & Segregation System 🚮🌆

A Smart City–based IoT project for **automatic waste segregation** and **real-time municipal monitoring dashboard** using ESP8266 and a web-based control panel.

---

## 📌 Project Overview

This system automatically:
- Detects waste dropped into a dustbin
- Classifies waste as **Wet / Dry / Metal**
- Monitors **bin fill level** and **harmful gas levels**
- Sends live data to a **Government/Municipal dashboard**
- Displays real-time status and alerts

Designed for **Smart City & Municipal Waste Management** use cases.

---

## 🧠 System Architecture

**Hardware (IoT Node):**
- ESP8266 (NodeMCU)
- IR Sensor (waste detection)
- Moisture Sensor (wet/dry detection)
- Metal Sensor
- Ultrasonic Sensor (bin level)
- Gas Sensor (MQ series)
- Servo Motor (bin direction control)

**Software (Dashboard):**
- Python (Flask)
- HTML + CSS (Responsive UI)
- REST API communication
- Render Cloud Deployment

---

## 🌐 Web Dashboard Features

- Secure Government Login
- Live bin data from ESP
- Bin level percentage
- Gas level monitoring
- Critical alert status
- Mobile & desktop responsive UI
- Smart City themed interface

---

## 🔐 Login Credentials (Demo)
Email: admin@govt.in

Password: 1234

*(For demo/testing purpose only)*

---

## 📂 Project Folder Structure

smart-waste-dashboard/
│
├── app.py
├── requirements.txt
├── templates/
│ ├── login.html
│ └── dashboard.html
│
├── static/
│ └── images/
│ ├── govt_logo.png
│ ├── smart_city.jpg
│ └── waste.jpg
│
└── README.md

---

## ⚙️ Local Setup (Optional)

```bash
pip install -r requirements.txt
python app.py

Open browser:http://localhost:5000

☁️ Cloud Deployment

This project is deployed using Render Cloud Platform.

Live URL format:https://smart-waste-dashboard-3bp1.onrender.com
📡 ESP8266 → Server Communication

-ESP sends data via HTTP POST:

-Bin ID

-Area

-Gas value

-Bin level percentage

-Status (NORMAL / CRITICAL)

🎯 Applications

-Smart City Projects

-Municipal Waste Management

-Government Monitoring Systems

-College Final Year / SIH Projects

🏆 Developed By

Mugilan P P
Smart Waste Monitoring System
India 🇮🇳

📜 License

This project is developed for educational and demonstration purposes.
