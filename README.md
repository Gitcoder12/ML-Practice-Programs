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

## Examples Used
- Predicting house prices with linear regression
- Classifying a sample using k-nearest neighbours
- Applying Bayes' theorem to spam classification


---

## Comparison with Existing Open-Source Projects

ML Practice Programs is a small educational collection implementing foundational algorithms in NumPy to expose the underlying mathematics and mechanics. These projects provide relevant implementation and learning comparisons.

| Project | Established focus | Relationship to ML Practice Programs |
|---|---|---|
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | Production-oriented classical machine-learning algorithms and evaluation utilities | Far broader, optimized and tested library; this repository intentionally prioritizes readable educational implementations over feature completeness or production performance. |
| [NumPy](https://github.com/numpy/numpy) | Core numerical arrays and vectorized computation in Python | The numerical foundation used by this project; the repository builds selected ML algorithms on top of NumPy rather than reimplementing array primitives. |
| [micrograd](https://github.com/karpathy/micrograd) | A compact educational autograd engine and neural-network example | A useful teaching reference for understanding model internals; this repository focuses on classical algorithms such as regression, KNN and Naive Bayes. |

### Where this repository is different
- **From-scratch learning:** selected algorithms are implemented directly with NumPy rather than hidden behind a high-level estimator API.
- **Small, inspectable examples:** each program is intended to isolate a core concept such as gradient descent, distance calculation or Bayes' rule.
- **Classical ML emphasis:** the current set is a compact foundation rather than a broad model zoo.

### Where established projects are stronger
scikit-learn provides much broader algorithm coverage, optimized implementations, extensive validation and mature evaluation utilities. NumPy is foundational infrastructure, not a direct competitor. This repository should not claim better accuracy, speed or reliability.

### Evidence and limitations
Add unit tests and reference comparisons for each algorithm, including shape validation, edge cases, deterministic behavior and numerical stability. Demonstration accuracy on synthetic data is not a generalization benchmark. This is an educational-scope comparison, not a performance ranking.
