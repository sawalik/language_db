"""Language OS v1 UI.  Run: streamlit run language_os/app.py"""
import sys
from pathlib import Path

import pandas as pd
import streamlit as st

sys.path.insert(0, str(Path(__file__).parent))
from language_os import db, seed_vocab  # noqa: E402

st.set_page_config(page_title="Language OS", layout="wide")
st.title("Language OS")

# Streamlit Cloud has no persistent disk: start with the seed words if the DB is empty.
if not db.search_vocab():
    seed_vocab.main()

known_langs = db.languages()
c1, c2, c3 = st.columns(3)
c1.metric("Study streak", f"{db.streak()} days")
c2.metric("Words", len(db.search_vocab()))
c3.metric("Minutes logged", sum(r["minutes"] for r in db.list_log(limit=100000)))

vocab_tab, log_tab = st.tabs(["Vocab", "Study log"])

with vocab_tab:
    with st.form("add_word", clear_on_submit=True):
        a, b, c = st.columns(3)
        lang = a.text_input("Language", value=known_langs[0] if known_langs else "Korean")
        word = b.text_input("Word")
        reading = c.text_input("Reading / romanization")
        meaning = st.text_input("Meaning")
        d, e = st.columns(2)
        example = d.text_input("Example sentence")
        source = e.text_input("Source (show, episode...)")
        if st.form_submit_button("Add word"):
            if not (lang and word and meaning):
                st.error("Language, word and meaning are required.")
            elif db.add_word(lang, word, meaning, reading, example, source):
                st.success(f"Added {word}")
            else:
                st.warning(f"{word} is already in your {lang} vocab.")

    f1, f2, f3 = st.columns(3)
    flang = f1.selectbox("Filter language", [""] + known_langs, key="vl")
    fstatus = f2.selectbox("Filter status", [""] + list(db.STATUSES))
    ftext = f3.text_input("Search")
    rows = db.search_vocab(flang or None, fstatus or None, ftext)
    if rows:
        df = pd.DataFrame(rows).drop(columns=["created_at"])
        edited = st.data_editor(
            df,
            hide_index=True,
            width="stretch",
            disabled=[c for c in df.columns if c != "status"],
            column_config={"status": st.column_config.SelectboxColumn(options=list(db.STATUSES))},
            key="vocab_editor",
        )
        for old, new in zip(df.itertuples(), edited.itertuples()):
            if old.status != new.status:
                db.set_status(int(old.id), new.status)
                st.rerun()
    else:
        st.info("No words yet.")

with log_tab:
    with st.form("log_study", clear_on_submit=True):
        a, b, c = st.columns(3)
        lang = a.text_input("Language", value=known_langs[0] if known_langs else "Korean", key="ll")
        minutes = b.number_input("Minutes", min_value=1, value=30)
        day = c.date_input("Day")
        activity = st.text_input("Activity (e.g. watched K-drama with subs)")
        notes = st.text_area("Notes", height=70)
        if st.form_submit_button("Log session"):
            if lang and activity:
                db.log_study(lang, int(minutes), activity, notes, day.isoformat())
                st.success("Logged")
                st.rerun()
            else:
                st.error("Language and activity are required.")

    per_day = db.minutes_per_day()
    if per_day:
        st.bar_chart(pd.DataFrame(per_day).set_index("day"))
        st.dataframe(pd.DataFrame(db.list_log()), hide_index=True, width="stretch")
