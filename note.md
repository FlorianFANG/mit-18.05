
### C1 Intro, counting and set
- **Probability**: given known probability, answer questions logically with probability rules. The answer is unique.
- **Statistics**: given set of data, figure out probability(How? Beyesian, or Frequencist...). The answer is not unique.

### C2 Probability basic
- Experiment: repeatable procedure with certained outcomes
- **Sample space ($\Omega$)**: set of all possible outcomes. A sample space could be discrete or continuous, each could be again finite or infinite.
- **Event**: subset of ($\Omega$)
- Probability function: mapping from a outcome to probability (for discrete sample space)
- Probability density:  mapping from a range of outcomes to probability (for continuous sample space)
  
**Rules of probability**
* $0 \leq P(\omega) \leq 1, \forall \omega \in \Omega$
* $\sum\limits_{i} P(\omega_{i}) = 1$
* $P(E) = \sum\limits_{\omega \in E} P(\omega), \forall E \subset \Omega$
* $P(\bar{E}) = 1 - P(E),\forall E \subset \Omega$
* $P(L\cup R) = P(L) + P(R) - P(L \cap R)$

### C3 Conditional probability, independence & Beyes' Theorem
**Conditional probability** & multiplication rule:
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

**Bayes' Theorem** (invert conditional probability):
$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)} = \frac{P(B|A) \cdot P(A)}{\sum\limits_{i}P(B|A_{i})P(A_{i})} $$

### C4 Discrete radom variables
For a sample space $\Omega$ with discrete outcomes, a random variable $X$ is a mapping:
$$X:\Omega \rightarrow \mathbb{R} $$

$X = a$ means a subset $S \subset \Omega$ such that $\forall s \in S, X(s) = a$

**Probability mass function** $p(a)$ denotes the probability when $X = a$:
$$p(a) = P(X = a)$$
**Cumulative distribution function** $F(a)$ gives the total probability when $X \leq a$:
$$F(a) = P(X \leq a)$$ 

##### Important distribution
1. $X \sim Bernoulli(p)$ 
$X \in \{0, 1\}$ and $P(X=1)=p, P(X=0)=1-p$
2. $X \sim Binomial(n, p)$: n independent trials of $Bernoulli(p)$
$$P(X=k)=\binom{k}{n}p^{k}(1-p)^{(n-k)} $$
3. $X \sim geometric(p)$: how many $0$s before the first $1$:
$$P(X=a)=(1-p)^{a}p $$
4. $X \sim uniform(N)$:
$$\forall x \in [1, N], P(X=x) = \frac{1}{N}$$

**Expectation**:
$$E(X) = \sum\limits_{j=1}^{n}p(x_{j})x_{j}$$

**Properties of Expectation**:
1. $E(aX+bY) =aE(X) + bE(Y)$
2. $E(h(X)) = \sum\limits_{j=1}^{n}p(x_{j})h(x_{j})$


### C5 Variance of discrete random variable
**Variance**: 
$$Var(X) = E((X-E(X)^2)$$
**Standard deviation**:
$$\sigma = \sqrt{Var(X)}$$

**Properties of Variance**:
1. if $X$ and $Y$ is independent then $Var(X+Y) = Var(X)+Var(Y)$
2. $\forall a,b \in Cnst, Var(aX+b) = a^2Var(X)$
3. $Var(X) = E(X^2)-E(X)^2$
   
$X$ is **continunous random variable** if :
$$\forall a \leq b, P(a \leq X \leq b) = \int_a^bf(x)dx$$
where $f(x)$ is probability density function (but not probability! So $f(x) > 1$ is possible. The integration of $f(x)$ is actually the probability)

cdf for continunous random variable:
$$F(b) = P(X \leq b) = \int_{-\infty}^bf(x)dx$$

**Analogy with physic:**
- probability mass function $p(x)$ (for discrete random variable): just like mass of an object
- probability density function $f(x)$ (for continunous random variable): just like density of a point of an object. we cannot say "mass of a point", neither "probability of a single continunous value. it is always "probability of a **RANGE** of continunous values.

**Expectation of continunous random variable:**
$$E(X) = \int_a^bxf(x)dx$$

### C6 Law of large number & Central Limit Theorem
Suppose $X_1, X_2, ..., X_n...$ be i.i.d random variables with mean $\mu$ and variance $\sigma^2$.

Let $S_n = \sum\limits_{i=1}^{n}X_i$ and $\bar{X_n} = \frac{S_n}{n}$

**LLT**:
$$\forall a > 0, \lim_{n\rightarrow \infty}P(|\bar{X_n} - \mu| < a) = 1$$
**CLT**:
$$S_n \sim \mathcal{N}(n\mu, n\sigma^2), \bar{X_n} \sim \mathcal{N}(\mu, \sigma^2/n)$$

### C7 Joint Distribution
Suppose $X$ and $Y$ two random variables.

- Discrete case
  
  **joint pmf**: $p(x, y)$ such that $\sum\limits_{i}\sum\limits_{j}p(x_i,y_i)=1$

  **joint cdf**: $F(x,y) = P(X\leq x, Y\leq y) = \sum\limits_{x_i \leq x}\sum\limits_{y_j \leq y}p(x_i,y_i)$

  **marginal pmf**: $p_X(x) = \sum\limits_{j}p(x_i,y_j)$, $p_Y(y) = \sum\limits_{i}p(x_i,y_j)$

- Continunous case
  
  **joint pdf**: $f(x,y)$ such that $\int_{a}^{b}\int_{c}^{d}f(x,y)dxdy = 1$ 

  **joint cdf**: $F(x,y) = \int_{a}^{y}\int_{c}^{x}f(u,v)dudv$

  **marginal pdf**: $f_X(x) = \int_{c}^{d}f(x,y)dy$, $f_Y(y) = \int_{a}^{b}f(x,y)dx$


Two events $A$ and $B$ is independent if $P(A\cap B) =P(A)P(B)$

Two random variables $X$ and $Y$ if $p(x, y) = p_X(x)p_Y(y)$ or $f(x,y)=f_X(x)f_Y(y)$

**Covariance** (dimension = $[X][Y]$)

Suppose $X$ and $Y$ two random variables with means $\mu_X$ and $\mu_Y$:
$$Cov(X, Y) = E((X-\mu_X)(Y-\mu_Y))$$

$X$ and $Y$ are independent $\implies$ $Cov(X, Y)=0$

$Cov(X, Y)=0$  $\color{red}{DO NOT}$  $\implies$ $X$ and $Y$ are independent

**Correlation**: covariance of standarization of $X$ and $Y$ (dimensionless)
$$Cor(X,Y) = \rho = \frac{Cov(X,Y)}{\sigma_X \sigma_Y}$$