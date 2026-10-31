"""Quick capture from the terminal.

    python -m language_os.cli add Korean 사랑 "love" --reading sarang --source "Crash Landing on You"
    python -m language_os.cli log Korean 30 "watched episode with subs"
    python -m language_os.cli list --language Korean
    python -m language_os.cli stats
"""
import argparse

from . import db


def main():
    p = argparse.ArgumentParser(prog="language_os")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add", help="add a vocab word")
    a.add_argument("language")
    a.add_argument("word")
    a.add_argument("meaning")
    a.add_argument("--reading", default="")
    a.add_argument("--example", default="")
    a.add_argument("--source", default="")

    s = sub.add_parser("log", help="log a study session")
    s.add_argument("language")
    s.add_argument("minutes", type=int)
    s.add_argument("activity")
    s.add_argument("--notes", default="")
    s.add_argument("--day", help="YYYY-MM-DD, defaults to today")

    l = sub.add_parser("list", help="list vocab")
    l.add_argument("--language")
    l.add_argument("--status", choices=db.STATUSES)
    l.add_argument("--text", default="")

    sub.add_parser("stats", help="streak and totals")

    args = p.parse_args()
    if args.cmd == "add":
        ok = db.add_word(args.language, args.word, args.meaning, args.reading, args.example, args.source)
        print("added" if ok else "already in vocab")
    elif args.cmd == "log":
        db.log_study(args.language, args.minutes, args.activity, args.notes, args.day)
        print("logged")
    elif args.cmd == "list":
        for r in db.search_vocab(args.language, args.status, args.text):
            print(f"{r['id']:>4} [{r['status']:<8}] {r['language']}: {r['word']} {r['reading']} - {r['meaning']}")
    elif args.cmd == "stats":
        log = db.list_log(limit=100000)
        print(f"streak: {db.streak()} days | sessions: {len(log)} | minutes: {sum(r['minutes'] for r in log)}")
        print(f"words: {len(db.search_vocab())}")


if __name__ == "__main__":
    main()
