1. Clone the repository
        ↓
2. Open the project
        ↓
3. Create a virtual environment
        ↓
4. Activate it
        ↓
5. Install requirements.txt
        ↓
6. Install Ollama
        ↓
7. Pull the required model
        ↓
8. Run the Streamlit app
        ↓
9. Use the application successfully



# 🚀 AI Prompt Optimizer

An AI-powered Prompt Optimizer built using **Python**, **Streamlit**, and **Ollama**. This application transforms simple prompts into professional, detailed, and well-structured prompts suitable for AI models.

---

# 📌 Features

* ✨ Convert simple prompts into professional prompts
* 🤖 Uses local LLM through Ollama
* 🎨 Interactive Streamlit UI
* ⚡ Fast inference
* 💻 Runs completely on your local machine
* 🔒 No external API required (when using Ollama)

---

# 🛠 Tech Stack

* Python 3.11+ (or your installed version)
* Streamlit
* Ollama
* Phi-3 Mini (or any supported Ollama model)
* SQLite (optional for prompt history)

---

# 📂 Project Structure

```text
prompt_optimizer/

│── app.py
│── main.py
│── database.py
│── prompt_engineer.py
│── prompt.db
│── requirements.txt
│── README.md
```

---

# 📦 Python Packages Used

Install all dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit
pip install ollama
pip install requests
```

(Optional)

```bash
pip install fastapi
pip install uvicorn
```

---

# 🐍 Check Python Version

```bash
python --version
```

or

```bash
python3 --version
```

---

# 🤖 Install Ollama

Download Ollama from:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```

---

# 📥 Download Model

Example:

```bash
ollama pull phi3:mini
```

Check installed models:

```bash
ollama list
```

Run model:

```bash
ollama run phi3:mini
```

---

# ▶️ Create Virtual Environment

Mac/Linux

```bash
python3 -m venv .venv
```

Activate

```bash
source .venv/bin/activate
```

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

---

# 📦 Install Requirements

```bash
pip install -r requirements.txt
```

If requirements.txt does not exist:

```bash
pip freeze > requirements.txt
```

---

# ▶️ Run Streamlit App

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

# 🔍 Check Running Ollama Models

```bash
ollama ps
```

Installed models:

```bash
ollama list
```

---

# 🛑 Stop Ollama

If running in the terminal:

```text
Ctrl + C
```

Or:

```bash
pkill ollama
```

---

# 📄 Generate requirements.txt

```bash
pip freeze > requirements.txt
```

---

# 🔍 Find Imported Python Packages

To list imports used in the project:

```bash
grep -R "^import " .
grep -R "^from " .
```

Or, inside VS Code, search for:

```
import
```

or

```
from
```

to see all imported libraries.

---

# 📜 Install Packages from requirements.txt

```bash
pip install -r requirements.txt
```

---

# 🚀 Future Improvements

* Prompt History
* User Personas
* SQLite Database
* FastAPI Backend
* Oracle Cloud Deployment
* Authentication
* Prompt Scoring
* Export Prompt

---

# 👨‍💻 Author

Developed as a Generative AI learning project using Python, Streamlit, and Ollama.

💡 One important recommendation

Instead of manually writing package names, generate requirements.txt from your environment after activating your virtual environment:

pip freeze > requirements.txt

Then anyone can clone your project and simply run:

pip install -r requirements.txt
