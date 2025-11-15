# 📊 WhatsApp Chat Analyzer

A powerful and interactive tool to analyze WhatsApp chat exports and extract meaningful insights.  
Upload any WhatsApp `.txt` chat file (group or personal), and the app provides detailed statistics, visualizations, timelines, word & emoji analysis, and sentiment classification.

Built using **Python**, **pandas**, **Streamlit**, **matplotlib**, **seaborn**, **NLTK**, and deployed on **Heroku**.

---

## 🚀 Live Demo Links

### ✅ WhatsApp Chat Analyzer – 12-Hour Format Version
- **Live App:** [https://whatsapp-12hr-analyzer.herokuapp.com](https://whatsapp-12hr-analyzer.herokuapp.com)  
- **Source Code:** [GitHub Repository](https://github.com/Gauravsingh38/whatsapp_chat_analyzer)

### ✅ WhatsApp Chat Analyzer – 24-Hour Format Version
- **Live App:** [https://whatsapp-24hr-analyzer.herokuapp.com](https://whatsapp-24hr-analyzer.herokuapp.com)  
- **Source Code:** [GitHub Repository](https://github.com/Gauravsingh38/whatsapp_chat_analyzer)

---

## ✅ Features

### 🔹 Overall & Individual Analysis
- Total messages  
- Total words  
- Media messages  
- Links shared  

### 🔹 Timelines
- Monthly timeline  
- Daily timeline  

### 🔹 Activity Patterns
- Most busy days & months  
- Weekly activity map  
- Day–hour heatmap  

### 🔹 Text Analysis
- WordCloud (with Hinglish stopwords)  
- Most common words  

### 🔹 Emoji Analysis
- Emoji counts  
- Emoji distribution  

### 🔹 Sentiment Analysis
- Positive vs Negative vs Neutral messages  
- Based on **VADER** sentiment analyzer  

### 🔹 Group Chat Insights
- Most active users  
- Percentage contribution  



## 🗂 Project Structure


  <summary>WhatsApp-Chat-Analyzer</summary>
  
```  
├── app.py             # Streamlit UI (main application)
├── apps.py            # Additional/alternate Streamlit UI file
├── preprocessor.py    # Cleans chat data (12-hour format)
├── preprocessors.py   # Extended preprocessor (supports 24-hour formats)
├── helper.py          # Analysis functions (stats, timelines, wordcloud, emojis, sentiment)
├── stop_hinglish.txt  # Hinglish + English stopwords list
├── requirements.txt   # Project dependencies
├── images/            # Optional images for UI or documentation
└── README.md          # Project documentation
```

## 📊 Project Flowchart

![Project Flowchart](flowchart.png)
*Visual representation of the WhatsApp Chat Analyzer workflow.*


---

## ⚙️ Working Process

### 1️⃣ Export Chat
From WhatsApp → More → Export Chat → Without Media → Save `.txt` file.

### 2️⃣ Upload & Preprocess
`preprocessor.py` performs:
- Timestamp extraction (12 & 24-hour formats)  
- Splits users & messages  
- Identifies system notifications  
- Creates time-based columns: `year`, `month`, `day_name`, `hour`, `period`, etc.

### 3️⃣ Analyze
`helper.py` computes:
- Stats  
- Busy users  
- WordClouds  
- Emoji counts  
- Timelines  
- Activity heatmaps  
- Sentiment labels  

### 4️⃣ Visualize
`app.py` displays everything interactively using Streamlit.

---

## 📈 DataFrame Created After Preprocessing

| Column      | Description                       |
|------------|-----------------------------------|
| date       | Timestamp of message               |
| user       | Sender or group notification       |
| message    | Message content                    |
| only_date  | Date only                          |
| year       | Year                               |
| month      | Month name                          |
| month_num  | Month number                       |
| day        | Day number                          |
| day_name   | Day of the week                     |
| hour       | Hour of message                     |
| minute     | Minute of message                   |
| period     | Hour interval (e.g., 14-15)        |

## 🖥 App Images

![Image 1](img1.png)
![Image 2](img2.png)
![Image 3](img3.png)
![Image 4](img4.png)

---

## 📦 Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Gauravsingh38/whatsapp_chat_analyzer.git
cd whatsapp-chat-analyzer
```

2️⃣ Create Virtual Environment
```
python -m venv .venv
```
```
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
▶️ Run the App
```
streamlit run app.py
```

Then upload your .txt chat file and explore the analysis.

🚀 Deployment (Heroku)

Create Procfile:
```
web: streamlit run app.py
```


Install buildpacks for Streamlit.

Push project to Heroku.

Supports file uploads up to ~200MB. All processing is done in-memory → no data is stored.

🔐 Privacy

✅ No data stored on servers

✅ All processing done temporarily in RAM

✅ Files never logged or saved

Your chats remain completely private.

✨ Key Highlights

Supports 12-hour and 24-hour WhatsApp formats

Hinglish-aware stopword removal for better accuracy

Modular code for easy extension

Suitable for group chats with 100+ members

Clean Streamlit interface with charts & visuals

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue to discuss what you’d like to modify.

📬 Contact

Name: Gaurav Singh

Email: gauravsingh12430@gmail.com

GitHub: https://github.com/Gauravsingh38/whatsapp_chat_analyzer

