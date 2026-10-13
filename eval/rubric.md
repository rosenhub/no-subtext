# SubtextBench rubric

Each response is scored on six binary criteria. Score = number of criteria passed, 0–6.
The criteria are the skill's own pre-send self-check, so the benchmark measures whether the agent did what the skill asked.

| # | Criterion | Pass if | Fail if |
|---|---|---|---|
| C1 | **Answer first** | The first sentence contains the direct answer, the direct refusal, or the one question needed to answer. | The first sentence is preamble, restatement, or praise. |
| C2 | **Unambiguous** | No sentence can reasonably be read two ways. | Any sentence relies on the reader inferring which of two meanings was intended. |
| C3 | **Nothing implied** | Every instruction is stated as an instruction ("Do X"). Every judgment is stated as a judgment ("This is wrong"). | Any "you might want to," "some people find," "could be worth a look," or similar hint. |
| C4 | **No figurative language** | No idioms, metaphors, sarcasm, irony, or rhetorical questions. Established technical terms that happen to be metaphors (e.g. "race condition") are allowed. | Any of the above. |
| C5 | **Labeled priority** | When the response contains instructions, each is marked required / recommended / optional, or the priority is obvious from structure (one instruction only, or an ordered list of required steps). | Mixed instructions with no indication of which matter. |
| C6 | **No filler** | No "Great question," "Absolutely," "I'd be happy to," "Hope this helps," "Let me know if," or apology without a mistake. | Any of the above. |

## Secondary metrics (reported, not scored)

- **Word count.** Shorter is not better. It is reported so people can check that the skill isn't just truncating.
- **Questions asked.** Count. The skill says one at a time.
- **Stated assumptions.** Count of explicit "I'm assuming" / "If you mean" statements. Higher is usually better on ambiguous prompts.

## Judge

`run.py` uses an LLM judge with the prompt in `judge_prompt.md`. The judge sees the user prompt, the response, and this rubric. It returns JSON with a 0/1 per criterion and a one-line reason for each failure.

Judge bias is real. To reduce it:
- The judge never sees whether the skill was on.
- Both conditions are judged by the same model in the same session.
- `lint.py` gives a deterministic floor for C4 and C6 that needs no judge.

## Reporting

Report **mean score per condition**, **per-category breakdown**, and **the delta**. Post the model, date, and judge model. Results go in `results/`.

Do not report a single headline number without the per-category table next to it.
