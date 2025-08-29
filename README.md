## Setup
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt
cd backend
uv main:app --reload
cd ..
cd frontend
streamlit run main.py
