# Labeling Protocol (Codebook)

**Project:** From User Feedback to Product Decisions — Comparing Traditional and Semantic NLP Methods for Product Issue Discovery  
**Purpose of this document:** to record how reviews are labeled into product-issue categories, and the rules used for difficult cases, so the human-labeled reference set ("answer key") is consistent, transparent, and defensible.  
**Status:** Category scheme and core rules are finalized (Sections 3–4). A small number of downstream items remain open (Section 7).  
**Last updated:** September 27, 2026.  

---

## 1. Why this document exists

The project compares two NLP methods by how well their automatically-formed groups of reviews match a set of human-assigned labels. Those human labels are the reference the methods are scored against, so the labeling must be *consistent* (the same kind of review is labeled the same way every time) and *documented* (the reasoning is written down, not held in someone's head). This protocol is that documentation.

A note held throughout: labeling is partly subjective — two reasonable people can disagree on a borderline review. The response to that is not to pretend the labels are perfectly objective, but to make the rules explicit so that decisions are made the same way each time.

---

## 2. How the categories were developed

The categories were built using a **hybrid approach** — a starting list decided in advance, then refined by reading real reviews.

- **Deductive (top-down) part:** a draft category list from the project proposal was used as a starting frame.
- **Inductive (bottom-up) part:** a random, reproducible sample of 40 real reviews was read closely, and the draft categories were revised based on what reviews actually said — confirming categories that appeared, questioning ones that didn't, and noticing gaps.

In research terms this is a **hybrid deductive–inductive coding scheme**: an a priori list refined through iterative review of the data.

A key revision from this process: the original single "Other" catch-all was found to be doing several different jobs at once (vague praise, genuinely unclear reviews, and actionable-but-uncategorized reviews). It was therefore split into three distinct categories (8, 9, and 10 below) so that each carries one clear meaning.

---

## 3. Category scheme (the buckets) — FINALIZED

Every review's primary label comes from this list of ten categories:

1. **Performance / Crashes** — app crashing, freezing, not loading, slowness.
2. **Notifications** — reminders or notifications not working or misbehaving.
3. **Navigation / Usability** — hard to use, confusing layout, workflow friction.
4. **Account / Login** — sign-in, sign-up, authentication failures.
5. **Boards / Task Management** — core board, card, list, checklist functionality.
6. **Integrations / Sync** — syncing across devices, connecting other tools.
7. **Feature Request** — asking for something that does not currently exist.
8. **Positive / No Issue** — praise or satisfaction with no actionable problem.
9. **Non-actionable / Unclear** — not praise, but no usable issue either: vague complaints, ambiguous wording, or "meh" reviews that name no specific problem.
10. **Other** — a *real, actionable* issue that genuinely does not fit categories 1–7.

**Important distinction between categories 9 and 10:** category 9 means *"no usable signal"* (there is no actionable issue to extract), while category 10 means *"a genuine issue that did not have a box"* (there is a real issue, but no matching category). Keeping these separate is deliberate: if category 10 fills up during labeling, that is a signal that a real product-issue category is missing from the scheme and should be added.

**Why "Positive / No Issue" (8) is kept separate from "Non-actionable / Unclear" (9):** although both lack an action item, they carry different information. Positive reviews are expected to be one of the largest categories (roughly 59% of reviews are 5-star), and the share of satisfied users is itself a meaningful product signal. Collapsing praise into a generic non-actionable bucket would hide that signal and would prevent testing whether the NLP methods can separate praise from problems. They are therefore kept distinct.

**Scope decision (locked):** *all* reviews are labeled, including praise. Non-actionable reviews are a real and large part of the data and are kept inside the study rather than removed.

---

## 4. Core labeling rules (locked)

### 4.1 One primary label per review
Each review receives exactly **one primary label** from the category list. This primary label is the *only* label used when scoring the NLP methods.

*Why one label:* the clustering methods place each review in exactly one group, so the evaluation math needs exactly one "true" category per review to compare against. Allowing many labels per review would break the standard comparison metrics.

### 4.2 Secondary labels (recorded, not scored)
If a review clearly raises more than one issue, the additional issue(s) are written in a separate **secondary** column.

- Secondary labels are a **record only** — they are never used in the evaluation math.
- **Multiple secondary labels are allowed**, comma-separated (see Section 5.1).
- Their purpose is to preserve the truth that reviews are often multi-issue, and to keep the door open to a future multi-label analysis without re-labeling.

Analogy used while designing this: the **primary label is the graded answer on a test; the secondary labels are margin notes** — the grade only looks at the answer, but the notes are kept.

### 4.3 Tiebreak ladder for choosing the primary label
For a single-issue review there is no tie and the primary label is obvious. When a review has **two or more genuinely equal issues**, the primary label is chosen by working *down this ladder* until one issue wins:

1. **Bug / problem beats feature request** — a broken thing is more urgent to a product team than a wish.
2. **If both are the same type, the more specific issue wins** — concrete beats vague.
3. **If still tied, the more severe / more blocking issue wins** — e.g. "can't log in at all" beats "checklist won't edit."
4. **If still tied, the issue mentioned first in the review wins** — used only as a last resort, after all meaningful distinctions are exhausted, purely for consistency.

Every issue that does *not* win the primary slot is recorded as a secondary label.

---

## 5. Edge cases and how they are resolved

This section captures the specific questions and edge cases identified while building the protocol, grouped by theme.

### 5.1 Reviews with multiple issues

- **Reviews that fit more than one bucket.** Discovered directly while labeling the sample — some reviews genuinely describe two or more issues (e.g. a review asking for list-color customization *and* reporting that files can't be attached on Android tablet). Resolved by the single-primary-label + secondary-notes system (4.2) and the tiebreak ladder (4.3).
- **What if a review has three or more actionable issues?** The primary label is the ladder winner; **all** remaining issues go into the secondary column, comma-separated. Nothing is dropped — the secondary column has no cap, because it is never scored and costs nothing to extend.
- **What if two issues both satisfy the top of the primary rule (e.g. two bugs)?** The choice is **not** made randomly. The tiebreak ladder continues past the first rule — specificity, then severity, then (only as a final fallback) order of mention — so the outcome is deterministic and repeatable rather than a coin flip.
- **Making sure rare categories are not lost.** A rare category that loses the primary slot is **automatically preserved in the secondary column**, because secondary records every non-primary issue. For this reason, rarity is deliberately *not* added as a competing primary-selection rule — doing so would conflict with the ladder. The catch-all secondary already protects small categories.

### 5.2 Reviews where the star rating and the text disagree

- **Rating/text mismatch.** Some reviews carry a rating that contradicts their text (e.g. a review describing a login failure but giving 5 stars). **Rule: label on the content of the text, not on the star rating.** The star rating is a separate signal and is not used to decide the issue category. This mismatch is itself noted as a data limitation.

### 5.3 Non-actionable, ambiguous, and low-specificity reviews

- **Vague praise (a large share of the data).** Reviews expressing satisfaction with no specific problem (e.g. "excellent app", "so useful") are labeled **Positive / No Issue** (category 8).
- **Ambiguous but plausibly actionable reviews.** When a review is ambiguous but has a plausible actionable reading, it is labeled by that actionable category rather than as Unclear, so a possible product signal is not erased. For example, "Nice & easy to use, can add graph representation also" is read as a request and labeled 
- **Negative but non-specific reviews.** Some reviews express dissatisfaction while naming no product area (e.g. "not what I'm looking for"). Because there is no locatable issue, these are labeled **Non-actionable / Unclear** (category 9) rather than an issue bucket.
- **Loud but thin reviews.** Some reviews are emotionally strong but specify little (e.g. a review threatening to uninstall over a "forced change to Workspaces limiting usability"). **Rule: a review is actionable if it names a specific product area or change a team could act on, even if the description is vague or emotional.** Under this rule such a review is labeled by the product area it names (here, Navigation / Usability).

### 5.4 Data-quality issues surfaced during labeling

- **Non-English reviews.** Despite requesting English-only during collection, some non-English reviews appear (e.g. a review in Spanish). Because they carry no usable signal for an English-language analysis, they are labeled 
- **Non-actionable / Unclear** (category 9). This is also recorded as a data limitation, since it shows the language filter is imperfect.

---

## 6. Acknowledged limitations and future directions

- **Single-label simplification.** Real reviews are often multi-issue, but the primary evaluation uses one label per review. This is a deliberate scope choice made because the clustering methods assign one group per review and standard metrics assume one true label. The multi-issue reality is acknowledged, recorded in the secondary column, and flagged as a candidate for a future **multi-label** analysis rather than implemented now.
- **Subjectivity of labels.** Borderline reviews can be labeled differently by different people. This is mitigated by the documented rules above and by comparing independent labelings to gauge agreement.
- **Rating vs. text mismatch and self-selection.** Star ratings do not always match text sentiment, and reviewers skew toward strong positive/negative experiences — both limit how representative the labels are of all users.

---

## 7. Open items (not yet finalized)

The category scheme (Section 3) is now finalized. The following downstream items remain open and should be decided based on further work or professor input, not filled in arbitrarily:

- **Whether to filter very short / non-actionable reviews before clustering**, given that a large share of reviews carry little issue signal.

*Resolved since the previous version:* the labeling reference set has been set at **200 reviews**, drawn as a random, reproducible sample (fixed seed) that excludes the 40 reviews used earlier for category development. Non-English reviews are labeled Non-actionable / Unclear (Section 5.4), and the rule for ambiguous-but-plausibly-actionable reviews has been documented (Section 5.3).

---

*This protocol is a living document and will be updated as the remaining open items are settled and as further edge cases appear during full labeling.*