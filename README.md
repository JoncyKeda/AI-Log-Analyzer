# 🧾 AI Log Analyzer
---

## 📌 Overview

**AI Log Analyzer** is an AI-powered tool that helps developers and DevOps engineers analyze system logs efficiently. It automatically detects error patterns, extracts relevant log entries, and provides intelligent insights such as root causes and suggested fixes using a Large Language Model (LLM).

This project demonstrates how AI can be used to simplify debugging and improve system monitoring workflows.

---

## ✨ Features

* 📂 Upload log files (.txt)
* 🔍 Automatic error detection using pattern matching
* 🧠 AI-powered root cause analysis
* 💡 Suggested fixes and debugging insights
* ⚡ Simple and interactive UI (Streamlit)

---

## 🧠 Tech Stack

* **Python**
* **Streamlit**
* **Regex (Log Parsing)**
* **OpenAI API (LLM)**

---

## 🏗️ Architecture

```id="c3r8vh"
Log File Input
      ↓
Log Parsing (Regex)
      ↓
Error Extraction
      ↓
LLM Analysis
      ↓
- Root Cause
- Error Type
- Suggested Fixes
      ↓
Streamlit UI
```

---

## 📂 Project Structure

```id="3zt0lg"
ai-log-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── parser.py
│   └── analyzer.py
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone Repository

```bash id="yn6g4b"
git clone https://github.com/your-username/ai-log-analyzer.git
cd ai-log-analyzer
```

---

### 2️⃣ Install Dependencies

```bash id="4j3dvh"
pip install -r requirements.txt
```

---

### 3️⃣ Set OpenAI API Key

#### 🔹 Mac/Linux:

```bash id="p5af3r"
export OPENAI_API_KEY=your_api_key
```

#### 🔹 Windows:

```bash id="1hv2pu"
set OPENAI_API_KEY=your_api_key
```

---

### 4️⃣ Run Application

```bash id="dbpt6g"
streamlit run app.py
```

---

## 💡 Example Log Input

```text id="bntv2h"
ERROR: Database connection failed
Exception: Timeout occurred
WARNING: Retry attempt failed
```

---

## 🧠 Example Output

* Root Cause: Database connection timeout
* Error Type: Network/Database failure
* Suggested Fix: Check database server status and connection settings

---

## 🎯 Use Cases

* Debugging application errors
* Monitoring system logs
* DevOps automation tools
* Production issue analysis

---

## 📬 Author

**Joncy Keda - AI Developer**

