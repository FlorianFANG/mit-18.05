
### C1 Intro, counting and set
- **Probability**: given known probability, answer questions logically with probability rules. The answer is unique.
- **Statistics**: given set of data, figure out probability(How? Beyesian, or Frequencist...). The answer is not unique.

### C2 Probability basic
- Experiment: repeatable procedure with certained outcomes
- Sample space ($\Omega$): set of all possible outcomes. A sample space could be discrete or continuous, each could be again finite or infinite.
- Event: subset of ($\Omega$)
- Probability function: mapping from a outcome to probability (for discrete sample space)
- Probability density:  mapping from a range of outcomes to probability (for continuous sample space)
  
**Rules of probability**
* $0 \leq P(\omega) \leq 1, \forall \omega \in \Omega$
* $\sum\limits_{i} P(\omega_{i}) = 1$
* $P(E) = \sum\limits_{\omega \in E} P(\omega), \forall E \subset \Omega$
* $P(\bar{E}) = 1 - P(E),\forall E \subset \Omega$
* $P(L\cup R) = P(L) + P(R) - P(L \cap R)$

### C3 Conditional probability, independence & Beyes' Theorem
conditional probability & multiplication rule:
$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$
law of total probability:
$$P(A) = \sum\limits_{i}P(A|B_{i})P(B_{i}) \text{  if  } P(B_{i} \cap B_{j}) = 0$$
$A$ and $B$ is independent if:
$$
\begin{aligned}
P(A|B) &= P(A)\\
\text{or  } P(A \cap B) &= P(A) \cdot P(B)
\end{aligned}
$$

Bayes' Theorem (invert conditional probability):
$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)} = \frac{P(B|A) \cdot P(A)}{\sum\limits_{i}P(B|A_{i})P(A_{i})} $$

### C4 Discrete radom variables
For a sample space $\Omega$ with discrete outcomes, a random variable $X$ is a mapping:
$$X:\Omega \rightarrow \mathbb{R} $$

$X = a$ means a subset $S \subset \Omega$ such that $\forall s \in S, X(s) = a$

Probability mass function $p(a)$ denotes the probability when $X = a$:
$$p(a) = P(X = a)$$
Cumulative distribution function $F(a)$ gives the total probability when $X \leq a$:
$$F(a) = P(X \leq a)$$ 

