#!/usr/bin/env python3
"""
Deterministic subtext lint. No API key needed.

Checks a response for the patterns the skill bans and that can be detected
without a judge: filler openers/closers (C6), common idioms and hedge
phrases (C3/C4), rhetorical questions (C4), and vague quantities (rule 9).

Usage:
    python lint.py response.md [more.md ...]
    python lint.py --json response.md
    cat response.md | python lint.py -

Exit code is the number of files with at least one finding (max 1 per file),
so it works as a CI gate.
"""
import json
import re
import sys

FILLER = [
    r"\bgreat question\b", r"\bgood question\b", r"\babsolutely!?\b", r"\bcertainly!?\b",
    r"\bi'?d be happy to\b", r"\bhappy to help\b", r"\bof course!\b",
    r"\bhope (this|that) helps\b", r"\blet me know if\b", r"\bfeel free to\b",
    r"\bdon'?t hesitate\b", r"\bthanks for (asking|reaching out)\b",
    r"\bi hope you find\b", r"\bas an ai\b",
]

HEDGE_AS_POLITENESS = [
    r"\byou might want to\b", r"\byou may want to\b", r"\bit might be worth\b",
    r"\bit could be worth\b", r"\bworth (a|another) (look|second look)\b",
    r"\bsome (people|folks|might)\b", r"\bmany people find\b",
    r"\bit really depends\b", r"\bit kind of depends\b", r"\bit sort of depends\b",
    r"\bthere'?s no one[- ]size[- ]fits[- ]all\b", r"\bat the end of the day\b",
    r"\bif i had to (lean|guess|pick)\b", r"\bi'?d probably say\b",
    r"\bcomes down to what feels right\b", r"\ba bit outside\b",
    r"\bnot (quite|really) (something|what) i can\b",
]

IDIOMS = [
    r"\bhit the ground running\b", r"\btough nut to crack\b", r"\blow[- ]hanging fruit\b",
    r"\bmove the needle\b", r"\bon the same page\b", r"\bball is in your court\b",
    r"\bbite the bullet\b", r"\bpiece of cake\b", r"\bsilver bullet\b",
    r"\brule of thumb\b", r"\bin a nutshell\b", r"\bthe elephant in the room\b",
    r"\bback to the drawing board\b", r"\bthink outside the box\b",
    r"\bbang for (the|your) buck\b", r"\btake (it|this) with a grain of salt\b",
    r"\bno[- ]brainer\b", r"\bdouble[- ]edged sword\b", r"\bslippery slope\b",
    r"\bcutting[- ]edge\b", r"\bgame[- ]changer\b", r"\bnail(ed)? it\b",
    r"\bdive (in|into|deep)\b", r"\bunpack (this|that)\b", r"\bcircle back\b",
    r"\bat a glance\b", r"\bunder the hood\b",
]

VAGUE_QUANTITY = [
    r"\ba (few|couple of|handful of|bunch of|number of)\b", r"\bpretty (fast|quick|slow|soon)\b",
    r"\bfairly (fast|quick|slow)\b", r"\bsoon(ish)?\b", r"\bin no time\b",
    r"\bquite a (bit|few|while)\b", r"\ba while\b", r"\bshortly\b",
]

RHETORICAL_Q = [
    r"\bwhy would (anyone|you|we)\b[^.?!]*\?", r"\bwho (wouldn'?t|doesn'?t)\b[^.?!]*\?",
    r"\bisn'?t (it|that) (great|nice|amazing|wonderful)\?", r"\bright\?",
    r"\bmakes sense\?", r"\bsound good\?", r"\bwhat'?s not to (like|love)\?",
]

CHECKS = [
    ("C6 filler", FILLER),
    ("C3 hedge-as-politeness", HEDGE_AS_POLITENESS),
    ("C4 idiom", IDIOMS),
    ("R9 vague quantity", VAGUE_QUANTITY),
    ("C4 rhetorical question", RHETORICAL_Q),
]


def lint(text: str) -> dict:
    findings = []
    low = text.lower()
    for label, patterns in CHECKS:
        for pat in patterns:
            for m in re.finditer(pat, low):
                findings.append({"check": label, "match": text[m.start():m.end()], "pos": m.start()})
    findings.sort(key=lambda f: f["pos"])
    words = len(text.split())
    questions = text.count("?")
    assumptions = len(re.findall(r"\b(i'?m assuming|i assume|if you mean|assuming you)\b", low))
    return {
        "words": words,
        "questions": questions,
        "stated_assumptions": assumptions,
        "findings": findings,
        "clean": not findings,
    }


def main(argv):
    as_json = "--json" in argv
    paths = [a for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 2
    failed = 0
    out = {}
    for p in paths:
        text = sys.stdin.read() if p == "-" else open(p, encoding="utf-8").read()
        r = lint(text)
        out[p] = r
        if not r["clean"]:
            failed += 1
        if not as_json:
            status = "CLEAN" if r["clean"] else f"{len(r['findings'])} finding(s)"
            print(f"{p}: {status}  [{r['words']} words, {r['questions']} question(s), "
                  f"{r['stated_assumptions']} stated assumption(s)]")
            for f in r["findings"]:
                print(f"    {f['check']:<26} \"{f['match']}\"")
    if as_json:
        print(json.dumps(out, indent=2))
    return min(failed, 1)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
