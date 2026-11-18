# ML Practice Programs

Foundational ML algorithms implemented from scratch in NumPy — no sklearn, no magic. Built to understand what's actually happening inside the models.

## Programs

| File | Algorithm | Concept |
|------|-----------|---------|
| `linear_regression.py` | Linear Regression | Gradient descent, MSE |
| `knn_classifier.py` | K-Nearest Neighbours | Euclidean distance, majority vote |
| `naive_bayes.py` | Gaussian Naive Bayes | Bayes theorem, log-likelihood |

## Run Any Program

```bash
python programs/linear_regression.py
python programs/knn_classifier.py
python programs/naive_bayes.py
```

Requires: `numpy` only.

## Author

Dharavath Satvik — M.Tech CSE, Amity Hyderabad


---

## AI-maintained project notes (secondary — 2026-11-13)

This section supplements the maintainer-authored README above. The original text has been restored verbatim from Git-history baseline `feaca5aded57436f4fae073bbc1cbe0a54c7d1b8`; this addendum does not replace or certify the original claims.

- The current source tree, runtime data and tests are the implementation source of truth. Roadmap items, draft PRs and AI-generated descriptions are not shipped features by themselves.
- Preserve real and maintainer-provided data. Never silently substitute generated or placeholder data. Clearly label and isolate synthetic fixtures.
- Mark unverified sources, identifiers, metrics, benchmark results and external claims as unknown/unverified rather than guessing.
- Verify setup, execution, tests and public claims against the exact current commit before using this repository in a job, research or academic application.
- See [MODEL_AUDIT_ROUTER.md](MODEL_AUDIT_ROUTER.md) for independent model review instructions and the merge gate.

---

## Engineering Audit & Handover — 2026-11-17

**Review scope:** default branch `main`; static inspection of `programs/knn_classifier.py`. Runtime tests were not executed.

### Confirmed findings
- `KNNClassifier.fit()` stores arrays without checking that inputs are non-empty, two-dimensional, length-aligned, or shape-compatible.
- `predict_single()` assumes `fit()` has already been called. Calling it before fitting will fail indirectly rather than raising a clear model-state error.
- When `k` exceeds the number of training samples, slicing silently uses all available samples instead of rejecting or warning about the configuration.
- The example uses a seeded synthetic two-class dataset; its printed accuracy is a demonstration result, not a benchmark on a real dataset.

### Next actions
1. Validate training/prediction shapes, empty arrays, label alignment, and fitted state.
2. Define and test behavior for `k > n_samples` and deterministic vote ties.
3. Add unit tests for distance, fit, prediction, invalid inputs, and the other algorithms.

**Verification status:** static KNN inspection only; example execution and automated tests remain unverified.


---

## Branch Activity & Development History

**Audit date:** 2026-11-18 · **Comparison base:** `main`

| Branch | Difference from `main` | Observed work / changed paths |
|---|---:|---|
| `docs/portfolio-operating-kit-2026-11-13` | 4 ahead / 3 behind | Activity log, agent guidance, company-fit notes, feature plan, README support docs and skills; README has removals as well as additions on this branch |
| `docs/project-status-audit20261116` | Comparison unavailable | GitHub returned 404 for the comparison; recheck branch existence |
| `docs/status-inventory-2026-11-16-v1` | 1 / 1 | Project status inventory: `PROJECT_STATUS.md` |

### Open pull requests observed during this audit

- [PR #2 — project status snapshot](https://github.com/Gitcoder12/ML-Practice-Programs/pull/2)
- [PR #1 — learning roadmap and contributor handbook](https://github.com/Gitcoder12/ML-Practice-Programs/pull/1)

**Verification boundary:** This records Git metadata and changed paths only. Review exact PR head/base and CI before merging. No branches have been merged or deleted by this documentation update.
