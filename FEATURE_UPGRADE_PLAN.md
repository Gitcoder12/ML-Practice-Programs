# ML-Practice-Programs — Feature Upgrade Plan

## Objective

A learning repository with small NumPy implementations of basic machine-learning algorithms so students can see how the maths works under the hood.

## P0 — correctness and reproducibility

- [ ] Add deterministic toy datasets with known expected outputs and fixed random seeds.
- [ ] Check shape handling, missing values, numerical stability and edge cases for each algorithm.

## P1 — learning experience

- [ ] Add short mathematical derivations and comments connecting equations to code.
- [ ] Compare outputs to scikit-learn reference implementations on documented datasets.

## P2 — breadth and evaluation

- [ ] Add benchmark notebooks that show learning curves and error metrics without unsupported performance claims.
- [ ] Add more foundational algorithms only with tests, derivations and runnable examples.

## Contributor work packages

1. Mathematical derivation and algorithm contract.
2. Deterministic example and edge-case tests.
3. Reference-library comparison with tolerance documentation.
4. Teaching explanation and plot/notebook.

## Definition of done

- [ ] Formula and assumptions are documented.
- [ ] Example is deterministic and outputs are checked.
- [ ] Edge cases and numerical behavior are tested.
- [ ] Any comparison names the reference implementation and tolerance.
