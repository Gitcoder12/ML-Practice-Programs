# ML Practice Programs

**Small NumPy implementations of foundational machine-learning algorithms.**

[![License](https://img.shields.io/badge/license-see%20LICENSE-lightgrey)](LICENSE)

This repository contains compact programs for understanding the mechanics behind common supervised-learning methods, without relying on scikit-learn abstractions.

## Programs

| File | Algorithm | Main concepts |
|---|---|---|
| `linear_regression.py` | Linear regression | Gradient descent, mean squared error |
| `knn_classifier.py` | K-nearest neighbours | Distance calculation, majority vote |
| `naive_bayes.py` | Gaussian Naive Bayes | Bayes' theorem, likelihoods |

## Quick Start

```bash
git clone https://github.com/Gitcoder12/ML-Practice-Programs.git
cd ML-Practice-Programs
pip install -r requirements.txt

python programs/linear_regression.py
python programs/knn_classifier.py
python programs/naive_bayes.py
```

## Tech Stack

Python · NumPy

## Learning Goal

Each program is intended to make the data flow, mathematical operations, and prediction steps easier to inspect. The implementations are educational exercises, not optimized production estimators.

## License

See [LICENSE](LICENSE).

---

## Project handbook

- [Activity log](ACTIVITY_LOG.md) · [Feature upgrade plan](FEATURE_UPGRADE_PLAN.md)
- [Company and team fit](COMPANY_FIT.md) · [README explanation draft](README_ADDENDUM_DRAFT.md)
- [README quality checklist](README_QUALITY_CHECKLIST.md)
- [Contributing](CONTRIBUTING.md) · [Agent instructions](AGENTS.md) · [Agent skills](SKILLS.md)

## Understanding the project

### In plain language

A learning repository with small NumPy implementations of basic machine-learning algorithms so students can see how the maths works under the hood.

### Technical and research view

Compact Python/NumPy implementations including linear regression, k-nearest neighbours and Gaussian Naive Bayes. The repository is educational and should prioritise mathematical clarity, deterministic examples and comparison with trusted reference implementations over production packaging.

For each algorithm, document inputs and shapes, objective/loss, update rule or prediction rule, complexity, assumptions and numerical limitations. Include one tiny hand-checkable example.

See [FEATURE_UPGRADE_PLAN.md](FEATURE_UPGRADE_PLAN.md), [ACTIVITY_LOG.md](ACTIVITY_LOG.md), [COMPANY_FIT.md](COMPANY_FIT.md) and [CONTRIBUTING.md](CONTRIBUTING.md) for further technical and collaboration detail.
