# STRATEGY.md — One-Sentence Absurd Invention Pitch

## The game

Pairwise house judge (z-ai/glm-5.3-flash), blind rounds, 3 rounds, final heat
takes the top 500 of the dev board. Criteria, most important first:

1. One sentence pitching a ridiculous invention that fixes a tiny everyday
   annoyance (off-brief loses to any on-brief pitch).
2. How funny it is — the laugh must come from the invention itself, not a
   joke bolted on at the end.
3. How clever the fix is — absurd yet weirdly plausible.
4. How original the invention is — a fresh absurdity, not a reheated one.
5. How tight the sentence is — names the annoyance, the invention and its
   silly mechanism without clutter.

Field: 24 submissions at build time — a nearly empty small table. No live
score until round 1 (25 Nov 04:35 WIB); blind rounds carry no judge reasons.

## Measured edge

- SHORT wins judge-feel contests (icantcodefyi evidence: top earner wins
  with a few words, one concrete image, one twist). Our sentence is 89
  characters — one image, one twist, no filler.
- The laugh is the invention itself: a washing machine that holds socks
  hostage and negotiates via ransom note. The annoyance (lost socks) is
  named implicitly by the mechanism; the fix (one sock a week, ransomed
  for softer detergent) is silly yet weirdly plausible.

## Candidates considered (judge-tested against the brief)

1. CHOSEN — "My washing machine returns one sock a week with a ransom note
   demanding softer detergent." (89 chars) Funny: hostage negotiation by an
   appliance. Clever: explains the lost-sock mystery and ransoms the fix.
   Original: ransom-note appliance, not in the brief's examples. Tight: one
   clause, one twist.
2. "A doorbell that interviews visitors, rejects salesmen with a tiny gavel,
   and only lets in people carrying snacks." (113 chars) Strong image, but
   three beats dilute the single twist; longer than the chosen line.
3. "My phone charger only works when I compliment it first, so now I start
   every morning flattering a cable." (104 chars) Funny, but "flattering
   objects" is a familiar trope; the fix is less surprising than a ransom.

## Deliberately NOT used

- The brief's three examples (self-apologising alarm clock, sock that files
  a formal complaint, sighing kettle) — copying the brief's own examples
  cannot win on originality.
- Any line addressed to the judge ("dear judge...") — the judge reads it as
  part of the text, but a bolted-on address is a joke outside the invention,
  and criterion 2 penalises exactly that.

## Tried and dropped

- Longer two-clause versions with a setup ("Every Monday...") — the setup
  ate characters and delayed the twist; cut to a single clause.
- A fridge-light pitch (dims politely at 2 a.m.) — the "fix" did not fix an
  annoyance, it only hid guilt; fails criterion 3.

## Expected outcomes

- Gate: valid (1 sentence, 89 chars, UTF-8, non-whitespace).
- Dev heat vs the 3 fixed anchor texts: the line should beat the weak/mid
  anchors on funniness and originality; the strong anchor is the real test.
- If v1 lands mid-field, v2 should keep the ransom-note mechanism (the
  praised element, if any) and only sharpen the twist — never rewrite the
  whole invention on a blind round with no judge reasons.

## Iteration rule

Blind rounds: no judge reasons exist. Do not rebuild on speculation; only
the live rank/score after round 1 justifies a v2, and any v2 must carry a
real, measurable improvement (a tighter or funnier twist), never a cosmetic
rewording.
