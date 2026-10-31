# Language OS

Vocab DB and study log for language learning (Korean and Japanese seeded). SQLite + Streamlit.

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

CLI: `python -m language_os.cli add Korean 사랑 "love" --reading sarang`

Note: on Streamlit Community Cloud the disk is ephemeral, so data you add there resets when the app restarts.
