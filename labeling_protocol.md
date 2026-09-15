# Labeling Protocol (Codebook)

**Project:** From User Feedback to Product Decisions — Comparing Traditional and Semantic NLP Methods for Product Issue Discovery
**Purpose of this document:** to record how reviews are labeled into product-issue categories, and the rules used for difficult cases, so the human-labeled reference set ("answer key") is consistent, transparent, and defensible.
**Status:** Working protocol. Core rules are locked; a few category-scheme items remain open (see Section 7).

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

---

## 3. Category scheme (the buckets)

Working category list (each review's primary label comes from this list):

- **Performance / Crashes** — app crashing, freezing, not loading, slowness.
- **Notifications** — reminders or notifications not working or misbehaving.
- **Navigation / Usability** — hard to use, confusing layout, workflow friction.
- **Account / Login** — sign-in, sign-up, authentication failures.
- **Boards / Task Management** — core board, card, list, checklist functionality.
- **Integrations / Sync** — syncing across devices, connecting other tools.
- **Feature Request** — asking for something that does not currently exist.
- **Positive / No Issue** — praise or satisfaction with no actionable problem.
- **Other** — actionable or on-topic but not fitting the categories above.

**Scope decision (locked):** *all* reviews are labeled, including praise. "Positive / No Issue" is a real, valid category — not a discard pile. This decision was made because roughly two-thirds of the reading sample was non-actionable praise; that is a real property of the data and is kept inside the study rather than removed.

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

- **Vague praise (the majority of the sample).** Reviews expressing satisfaction with no specific problem (e.g. "excellent app", "so useful") are labeled **Positive / No Issue**.
- **Ambiguous / uninterpretable reviews.** Some reviews cannot be confidently understood (e.g. "i want to update this app" — unclear whether it refers to updating the app or updating a review). These are treated as non-actionable and are *not* forced into a specific issue category.
- **Negative but non-specific reviews.** Some reviews express dissatisfaction while naming no product area (e.g. "not what I'm looking for"). Because there is no locatable issue, these are treated as non-actionable rather than assigned to an issue bucket.
- **Loud but thin reviews.** Some reviews are emotionally strong but specify little (e.g. a review threatening to uninstall over a "forced change to Workspaces limiting usability"). **Rule: a review is actionable if it names a specific product area or change a team could act on, even if the description is vague or emotional.** Under this rule such a review is labeled by the product area it names (here, Navigation / Usability).

### 5.4 Data-quality issues surfaced during labeling

- **Non-English reviews.** Despite requesting English-only during collection, some non-English reviews appear (e.g. a review in Spanish). This shows the language filter is imperfect and is recorded as a data limitation to address before or during analysis.

---

## 6. Acknowledged limitations and future directions

- **Single-label simplification.** Real reviews are often multi-issue, but the primary evaluation uses one label per review. This is a deliberate scope choice made because the clustering methods assign one group per review and standard metrics assume one true label. The multi-issue reality is acknowledged, recorded in the secondary column, and flagged as a candidate for a future **multi-label** analysis rather than implemented now.
- **Subjectivity of labels.** Borderline reviews can be labeled differently by different people. This is mitigated by the documented rules above and by comparing independent labelings to gauge agreement.
- **Rating vs. text mismatch and self-selection.** Star ratings do not always match text sentiment, and reviewers skew toward strong positive/negative experiences — both limit how representative the labels are of all users.

---

## 7. Open items (not yet finalized)

These are deliberately left open pending further work or professor input, and should not be filled in arbitrarily:

- **Final lock of the category list** — in particular whether "Other" should be split (e.g. a distinct "Non-actionable / Unclear" bucket separate from actionable-but-uncategorized).
- **Whether to filter very short / non-actionable reviews before clustering**, given that a large share of reviews carry little issue signal.
- **Final labeling sample size** (how many reviews to label as the reference set).

---

*This protocol is a living document and will be updated as the category list is finalized and as further edge cases appear during full labeling.*
