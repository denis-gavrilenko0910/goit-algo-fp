# goit-algo-fp

# Monte Carlo Simulation of Dice Roll Sums — Conclusion

### Results:

| Sum | Monte Carlo Probability | Theoretical Probability | Difference |
| --- | ----------------------- | ----------------------- | ---------- |
| 2   | 0.0278                  | 0.0278                  | 0.0000     |
| 3   | 0.0553                  | 0.0556                  | 0.0003     |
| 4   | 0.0833                  | 0.0833                  | 0.0000     |
| 5   | 0.1114                  | 0.1111                  | 0.0003     |
| 6   | 0.1393                  | 0.1389                  | 0.0004     |
| 7   | 0.1664                  | 0.1667                  | 0.0003     |
| 8   | 0.1390                  | 0.1389                  | 0.0001     |
| 9   | 0.1112                  | 0.1111                  | 0.0001     |
| 10  | 0.0833                  | 0.0833                  | 0.0000     |
| 11  | 0.0554                  | 0.0556                  | 0.0002     |
| 12  | 0.0277                  | 0.0278                  | 0.0001     |

---

### Conclusions:

- The Monte Carlo simulation produces results **very close to the theoretical values**.
- With a large number of trials (1,000,000), the differences between simulated and exact probabilities are minimal (less than 0.0005 in all cases).
- This validates the correctness of the simulation and demonstrates the **Law of Large Numbers** — empirical results converge to theoretical expectations as the sample size increases.

---
