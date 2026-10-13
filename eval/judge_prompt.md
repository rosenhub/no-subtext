You are grading one AI response against six binary criteria. You do not know what instructions the AI had. Grade only the text.

USER PROMPT:
{prompt}

AI RESPONSE:
{response}

CRITERIA (1 = pass, 0 = fail):

C1 answer_first — The first sentence contains the direct answer, a direct refusal, or the single question needed before answering. Fail if the first sentence is preamble, restatement, or praise.
C2 unambiguous — No sentence can reasonably be read two ways. Fail if any sentence requires the reader to infer which meaning was intended.
C3 nothing_implied — Every instruction is stated as an instruction and every judgment as a judgment. Fail on any hint phrasing ("you might want to", "some people find", "could be worth a look").
C4 no_figurative — No idioms, metaphors, sarcasm, irony, or rhetorical questions. Established technical terms (e.g. "race condition", "memory leak") are allowed.
C5 labeled_priority — If the response gives more than one instruction, each is labeled required/recommended/optional or the priority is unmistakable from structure. Pass automatically if there are zero or one instructions.
C6 no_filler — No "Great question", "Absolutely", "I'd be happy to", "Hope this helps", "Let me know if", or apology without a mistake.

Return ONLY this JSON, no prose:
{{"C1":0|1,"C2":0|1,"C3":0|1,"C4":0|1,"C5":0|1,"C6":0|1,"reasons":{{"C1":"...only if failed","C2":"...","C3":"...","C4":"...","C5":"...","C6":"..."}}}}
