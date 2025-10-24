---
title: Supplementary Information
#subtitle: Optional Subtitle
short_title: Supplementary Information

exports:
  - format: pdf
    template: arxiv_nips
    output: exports/connattractor_si.pdf
  - format: docx
    hideFooter: true
    output: exports/connattractor_si.docx
---

## Supplementary Figures

:::{figure} figures/supplement/si_orthogonality.png
:name: si_orthogonality
**Eigenstructure and projector tests of the fcANN** <br/>
**A**: Eigenvalue spectra of the empirical coupling matrix J (left) and null model 1 (coupling matrix based on phase randomized timeseries data, recalculated for each permutation) (right). **B**: Eigenvector–attractor alignment calculated from the empirical (left) and phase-randomized data (right). Attractors were obtained by deterministic relaxation from random initial states (with collapsing sign‑duplicates); alignment is the absolute cosine between collapsed attractor vectors and the top eigenvectors of J. **C**: Weight correspondence between J and its Kanter–Sompolinsky (K–S) analog. From the measured attractors we formed Σ (columns are attractors) and C=ΣᵀΣ/N, then computed the pseudo‑inverse projector $J_{KS}=(1/N)ΣC⁻¹Σᵀ$. Similarity was quantified as the cosine between the off‑diagonal elements of J and $J_{KS}$. The gray histogram shows the null distribution from null model 2 (symmetry‑preserving permutations of J, but see [Source notebook](https://github.com/pni-lab/connattractor/blob/master/notebooks/ks-test.ipynb) for similar results with null model 1, i.e. phase randomized timeseries data); for each of the 1000 permutations $p$ we recomputed the own attractors of the surrogate network and $J_{KS}^{(p)}$. The red dashed line marks the empirical value; the one‑sided p‑value is the fraction of null cosines ≥ the empirical cosine. The empirical network shows stronger eigenvector–attractor alignment and substantially higher J↔J_KS off‑diagonal correspondence than the null, consistent with approximate K–S projector behavior.
:::

:::{figure} figures/supplement/si_fcann_projection.png
:name: si_fcann_projection
**Schematic representation of the fcANN projection.**
The fcANN projection is a 2-dimensional visualization of the fcANN dynamics, based on the first two principal components (PCs) of the states sampled from the stochastic relaxation procedure. The first two PCs yield a clear separation of the attractor states, with the two symmetric pairs of attractor states located at the extremes of the first and second PC. 
To map the attractors' basins on the space spanned by the first two PCs, we obtained the attractor state of each point visited during the stochastic relaxation and fit a multinomial logistic regression model to predict the attractor state from the first two PCs. 
The resulting model accurately predicted attractor states of arbitrary brain activity patterns, achieving a cross-validated accuracy of 96.5% (permutation-based p<0.001).
The attractor basins were visualized by using the decision boundaries obtained from this model. We propose the 2-dimensional fcANN projection as a simplified visual representation of brain dynamics, and use it as a basis for all subsequent analyses in this work.
:::

:::{figure} figures/supplement/expl_variance_energy.png
:name: si_expl_variance_energy
**Explained variance in state energy by first two principal components.** See [supplemental_material.ipynb](https://github.com/pni-lab/connattractor/blob/master/notebooks/supplemental_material.ipynb) for details.
:::

:::{figure} figures/supplement/classification_acc_state_basins.png
:name: si_classification_acc_state_basins
**Cross-validation classification accuracy of the fcANN, when predicting the attractor state from state 
activation.**  See [supplemental_material.ipynb](https://github.com/pni-lab/connattractor/blob/master/notebooks/supplemental_material.ipynb) for details.
:::

:::{figure} figures/supplement/att_state_emergence_over_beta.png
:name: si_att_state_emergence_over_beta
**Parameter sweep of fcANN parameters threshold and beta.** The number of attractor states is color‑coded. See [supplemental_material.ipynb](https://github.com/pni-lab/connattractor/blob/master/notebooks/supplemental_material.ipynb) for details.
:::

:::{figure} figures/supplement/si_convergence_jittered.png
:name: si_convergence
**fcANNs initialized with the empirical connectome have better convergence properties than permutation‑based null models.** We investigated the convergence properties of functional connectome‑based ANNs in study 1 by contrasting the number of iterations until reaching convergence to a permutation‑based null model. In more detail, the null model was constructed by randomly permuting the upper triangle of the original connectome and filling up the lower triangle to get a symmetric network (symmetry of the weight matrix is a general requirement for convergence). This procedure was repeated 1000 times. In each repetition, we initialized both the original and the permuted fcANN with the same random input and counted the number of iterations until convergence. Each point on the plot shows an iteration number; the lines connect iteration numbers corresponding to the original and permuted matrices initialized with the same input. Statistical significance of the faster convergence in the empirical connectome was assessed via a one‑sided Wilcoxon signed‑rank test (i.e., a non‑parametric paired test) on the paired iteration values (1,000 pairs), with the null hypothesis that the empirical connectome converges in fewer iterations than the permuted connectome. The whole procedure was repeated with $\beta=0.3, 0.35, 0.4, 0.5$ and $0.6$ (providing 2–8 attractor states). See [convergence-analysis.ipynb](https://github.com/pni-lab/connattractor/blob/master/notebooks/convergence_analysis.ipynb) for details.
:::


:::{figure} figures/supplement/si_state_occupancy_null_model.png
:name: si_state_occupancy_null_models
**Statistical inference of the fcANN state occupancy prediction with different null models.**
**A** Results with a spatial autocorrelation-preserving null model for the empirical activity patterns. See [null_models.ipynb](https://github.com/pni-lab/connattractor/blob/master/notebooks/null_models.ipynb) for more details.
**B** Results where simulated samples are randomly sampled from a multivariate normal distribution, with the functional connectome as the covariance matrix, and compared to the fcANN performance. See [supplemental_material.ipynb](https://github.com/pni-lab/connattractor/blob/master/notebooks/supplemental_material.ipynb) for details.
:::

:::{figure} figures/supplement/si_pain_ghost_attractor_sim.png
:name: si_pain_ghost_attractor_sim
**FcANN can reconstruct the pain "ghost attractor".**
Signal-to-noise values range from 0.003 to 0.009. Asterisk denotes the location of the simulated "ghost attractor". P-values are based on permutation testing, by randomly changing the conditions in a per-participant basis. See [main_analyses.ipynb](https://github.com/pni-lab/connattractor/blob/master/notebooks/main_analyses.ipynb) for more details.
:::

:::{figure} figures/supplement/si_downreg_trajectory_sim.png
:name: si_downreg_trajectory_sim
**fcANN can reconstruct the changes in brain dynamics caused by the voluntary downregulation of pain (as contrasted to upregulation)**
Signal-to-noise values range from 0.001 to 0.005. P-values are based on permutation testing, by randomly changing the conditions in a per-participant basis. See [main_analyses.ipynb](https://github.com/pni-lab/connattractor/blob/master/notebooks/main_analyses.ipynb) for more details.
:::

:::{figure} figures/supplement/noise_robustness_weights.png
:name: si_noise_robustness_weights
**Robustness of the fcANN weights to noise.**
We set the temperature of the fcANN, so that two attractor states emerge and iteratively add noise to the connectome. 
To account for the change in dynamics, we adjust the temperature (beta) of the noisy fcANN so that exactly two states emerge. We then highlight the decrease in nodal strength of the noisy connectome (the fcANN weights) as a reference metric 
vs the correlation of the attractor states that emerge from the noisy connectome. See [supplemental_material.ipynb](https://github.com/pni-lab/connattractor/blob/master/notebooks/supplemental_material.ipynb) for details.
:::

:::{figure} figures/supplement/clinical_results_table.png
:name: si_clinical_results_table
**All significant differences of the mean state activation analysis on the ABIDE dataset; label denotes the region
in the BASC122 atlas.** See [supplemental_material.ipynb](https://github.com/pni-lab/connattractor/blob/master/notebooks/supplemental_material.ipynb) for details.
:::

## Supplementary Tables

```{list-table} **MRI acquisition parameters.** TR: repetition time; TE: echo time; FA: flip angle; FOV: field of view; EPI: echo‑planar imaging; SPGR: spoiled gradient recall; SENSE/GRAPPA/ASSET: parallel imaging factors. Study 5-7 are metaanalyses or multi-center studies with varying data. Sequence parameters for these studies are available in the respective publications.
:header-rows: 1
:name: si-tab-mri

* - Parameter
  - Study 1
  - Study 2
  - Study 3
  - Study 4
* - Scanner / head coil
  - Philips Achieva X 3T; 32‑ch
  - Siemens Magnetom Skyra 3T; 32‑ch
  - GE Discovery MR750w 3T; 20‑ch
  - Philips Achieva TX 3T; head coil per site
* - Anatomical sequence
  - T1 MPRAGE
  - T1 MPRAGE
  - T1 3D IR‑FSPGR
  - T1 SPGR (high‑resolution)
* - Anatomical TR / TE
  - 8500 ms / 3.9 ms
  - 2300 ms / 2.07 ms
  - 5.3 ms / 2.1 ms
  - — / —
* - Anatomical resolution / FOV
  - 1×1×1 mm³; 256×256×220 mm³
  - 1×1×1 mm³; 256×256×192 mm³
  - 1×1×1 mm³; 256×256×172
  - —
* - Resting‑state EPI TR / TE / FA
  - 2500 ms / 35 ms / 90°
  - 2520 ms / 35 ms / 90°
  - 2500 ms / 27 ms / 81°
  - 2000 ms / 20 ms / —
* - Phase enc.
  - COL
  - A>>P
  - A>>P
  - —
* - FOV (voxels × slices)
  - 240×240×132; 40 slices
  - 230×230×132; 38 slices
  - 96×96×44; 44 slices
  - 64×64; 42 slices
* - Slice thickness / gap / order
  - 3 mm / 0.3 mm / interleaved
  - 3 mm / 0.48 mm / interleaved
  - 3 mm / 0 mm / interleaved
  - 3 mm / — / interleaved
* - Acceleration / fat suppression
  - SENSE 3× / SPIR
  - GRAPPA 2× / Fat sat.
  - ASSET 2× / Fat sat.
  - SENSE 1.5× / —
* - Volumes / dummies / scan time
  - 200 / 5 / 8 min 37 s
  - 290 / 5 / 12 min 11 s
  - 240 / 0 / 10 min
  - — / — / —
```

```{list-table} **Neurosynth meta-analyses.** The table includes details about the term used for the automated meta-analyses, as well as the number of studies included in the meta-analysis, the total number of reported activations and the maximal Z-statistic from the meta-analysis.
:header-rows: 1
:name: si-tab-neurosynth

* - search term
  - num. studies
  - num. activations
  - max. Z
  
* - pain
  - 516
  - 23295
  - 14.8
  
* - motor
  - 2565
  - 109491
  - 22.5
 
* - auditory
  - 1252
  - 46557
  - 25.3
  
* - visual
  - 3110
  - 115726
  - 15.4
    
* - face
  - 896
  - 31842
  - 26.8
    
* - autobiographical
  - 143
  - 7251
  - 15.7
    
* - theory of mind
  - 181
  - 7761
  - 15.1
    
* - sentences
  - 356
  - 13461
  - 16.5

```

## Supplementary Methods
**Study 4 instructions for upregulation.**
*“During this scan, we are going to ask you to try to imagine as hard as you can that the thermal stimulations are more painful than they are. Try to focus on how unpleasant the pain is, for instance, how strongly you would like to remove your arm from it. Pay attention to the burning, stinging and shooting sensations. You can use your mind to turn up the dial of the pain, much like turning up the volume dial on a stereo. As you feel the pain rise in intensity, imagine it rising faster and faster and going higher and higher. Picture your skin being held up against a glowing hot metal or fire. Think of how disturbing it is to be burned, and visualize your skin sizzling, melting and bubbling as a result of the intense heat.”*

**Study 4 instructions for downregulation.**
*“During this scan, we are going to ask you to try to imagine as hard as you can that the thermal stimulations are less painful than they are. Focus on the part of the sensation that is pleasantly warm, like a blanket on a cold day. You can use your mind to turn down the dial of your pain sensation, much like turning down the volume dial on a stereo. As you feel the stimulation rise, let it numb your arm, so any pain you feel simply fades away. Imagine your skin is very cool, from being outside, and think of how good the stimulation feels as it warms you up.”*

## Supplementary Information 1

**Derivation of the joint steady-state probability of free energy minimizing attractor networks**
See {cite:p}`10.48550/ARXIV.2505.22749` for details on the whole framework.

### Outline

> [!NOTE]
> **Regularity assumptions**
>
> - Existence of a non-equilibrium steady-state density $p^\ast$ with $\Phi=\log p^\ast$ differentiable almost everywhere on its support; stationary edge fluxes are finite.
> - Measurable jump kernel with finite total update rate at each configuration $\sigma$; independent Poisson clocks as specified.
> - Compact support of single-site updates $x\in[-1,1]$ so boundary terms vanish in the summation-by-parts/test-function identities used for solenoidal orthogonality.
> - Sufficient smoothness to justify differentiating the reversible increment at $x=\sigma_i$; mixed partials commute where invoked.

### Setup: Continuous–Bernoulli kernel

We assume that the single-site conditional distribution is the Continuous–Bernoulli on $[-1,1]$ with canonical parameter

$$
\kappa_i(\boldsymbol{\sigma}_{-i}) = b_i + \sum_{j\neq i} J_{ij}\sigma_j
$$

and density (for $x\in[-1,1]$)

$$
K(x\mid \kappa) = h(x) e^{\kappa x - A(\kappa)}, \qquad x\in[-1,1]
$$

with $h(x)=\tfrac12 \mathbf{1}_{[-1,1]}(x)$ and $A(\kappa)=\log(\sinh\kappa)-\log\kappa$ (so the $\kappa\to0$ limit is uniform on $[-1,1]$).

The conditional mean is:

$$
L(\kappa) =\mathbb{E}_{K(\cdot\mid\kappa)}[x] = \coth\kappa - \frac{1}{\kappa}
$$

### 1. Master equation

Let's consider a precise formalization of the asynchronous update procedure: each site $i$ has an independent Poisson clock of rate $\gamma_i$. When it rings, $\sigma_i$ is replaced by a draw $x\sim K(\cdot\mid\kappa_i(\sigma_{-i}))$.

With $\sigma^{(i,x)}$ the configuration equal to $\sigma$ but with coordinate $i$ set to $x$, the transition density is

$$
w_i(\sigma^{(i,x)}\mid\sigma) =\gamma_i K(x\mid\kappa_i(\sigma_{-i}))
$$

The master equation for $p(\sigma,t)$ is

$$
\partial_t p(\sigma,t) =\sum_{i=1}^N\int_{-1}^{1} \Big[ \underbrace{w_i(\sigma\mid\sigma^{(i,x)}) p(\sigma^{(i,x)},t)}_{inflow} - \underbrace{w_i(\sigma^{(i,x)}\mid\sigma) p(\sigma,t)}_{outflow}\Big] dx
$$

> [!NOTE]
> In a small interval $dt$, probability in state $\sigma$ changes by inflow from all one-site predecessors $\sigma^{(i,x)}$ minus outflow from $\sigma$ to those states. Multiple updates within $dt$ are $\mathcal{O}(dt^2)$ and negligible. Because the updated value $x$ is continuous, we integrate over $x\in[-1,1]$.

### 2. Probability currents

Let's denote the site-wise flux density as:

$$
F_i(\sigma \to x) := w_i(\sigma^{(i,x)}\mid\sigma) p^\ast(\sigma)
$$

At steady state $p^\ast$, by definition we have:

$$
\sum_i \int_{-1}^1 \Big(F_i(\sigma^{(i,x)}\to\sigma)-F_i(\sigma\to x)\Big) dx = 0
$$

> [!NOTE]
>  ${\sigma^{(i,x)}}^{(i,\sigma)} = \sigma$

### 3. Detailed balance condition

A special (and maybe the most intuitive) way to satisfy the previous eq. is the case of detailed balance or equilibrium. In this case, every transition is balanced:

$$
F_i(\sigma^{(i,x)}\to\sigma) = F_i(\sigma\to x)
$$

It can be shown that:

$$
w_i(\sigma^{(i,x)}\mid\sigma) p^\ast(\sigma) = w_i(\sigma\mid\sigma^{(i,x)}) p^\ast(\sigma^{(i,x)}) \iff \partial_{\sigma_i}\Phi(\sigma) = \kappa_i(\sigma_{-i}) = b_i + \sum_{k\neq i} J_{ik} \sigma_k
$$

I.e., the log-density $\Phi$ changes by the local slope at $i$ (see detailed derivation below).

Hence for $j\neq i$:

$$
\partial_{\sigma_j}\partial_{\sigma_i}\Phi = J_{ij}, \qquad \partial_{\sigma_i}\partial_{\sigma_j}\Phi = J_{ji}
$$

Mixed partials commute, thus:

$$
J_{ij}=J_{ji} \quad \iff \textit{detailed balance}
$$

Therefore, **equilibrium (detailed balance) is possible only when the coupling is symmetric**.

> [!NOTE]
> **Derivation**
>
> From:
>
> $w_i(\sigma^{(i,x)}\mid\sigma) p^\ast(\sigma) = w_i(\sigma\mid\sigma^{(i,x)}) p^\ast(\sigma^{(i,x)})$
>
> We take logs ($\Phi=\log p^\ast$) and rearrange:
>
> $\Phi(\sigma^{(i,x)}) − \Phi(\sigma) = \log w_i(\sigma^{(i,x)} \mid \sigma) − \log w_i(\sigma \mid \sigma^{(i,x)})$
>
> Substitute $w_i = \gamma_i K(\cdot \mid \kappa)$ with $\kappa = \kappa_i(\sigma_{-i}) = \kappa_i(\sigma^{(i,x)}_{-i})$:
>
> $\Phi(\sigma^{(i,x)}) − \Phi(\sigma) = \big[\log \gamma_i + \log K(x \mid \kappa)\big] − \big[\log \gamma_i + \log K(\sigma_i|\kappa)\big] = \log K(x \mid \kappa) − log K(\sigma_i \mid \kappa)$
>
> Use CB form $\log K(z|\kappa) = \log h(z) + \kappa z − A(\kappa)$:
>
> $\Phi(\sigma^{(i,x)}) − \Phi(\sigma) = \big[ \log h(x) − \log h(\sigma_i)\big] + \kappa(x − \sigma_i)$
>
> ($A(\kappa)$ cancels because $\kappa$ is the same).
>
> For Continuous–Bernoulli on [−1,1], $h(x) = 1/2$ on the support ⇒ $\log h(x) − log h(\sigma_i) = 0$, so:
>
> $$\Phi(\sigma^{(i,x)}) − \Phi(σ) = \kappa(x − \sigma_i)$$
>
> Differentiating at $x=\sigma_i$ yields
>
> $$ \partial_{\sigma_i}\Phi(\sigma) = \kappa_i(\sigma_{-i}) = b_i + \sum_{k\neq i} J_{ik} \sigma_k $$

### 4. Non-equilibrium Steady State (NESS)

Detailed balance (equilibrium) is only one specific way the steady-state condition can hold:

$$
\sum_i \int_{-1}^1 \Big(F_i(\sigma^{(i,x)}\to\sigma)-F_i(\sigma\to x)\Big) dx = 0
$$

Let's consider the general case: an arbitrary (possibly asymmetric) $J$ coupling. $J$ can always be decomposed into:

$$
J = J^{\mathrm{S}} + J^{\mathrm{A}},\qquad J^{\mathrm{S}} := \tfrac12(J+J^\top), \quad J^{\mathrm{A}} := \tfrac12(J-J^\top)
$$

This leads to a decomposition of the edge currents on each directed edge $(\sigma,\sigma^{(i,x)})$:

$$
F_i^{\mathrm{sym}}(\sigma\to x) := \tfrac12\Big(F_i(\sigma\to x)+F_i(\sigma^{(i,x)}\to\sigma)\Big),\qquad
F_i^{\mathrm{sol}}(\sigma\to x) := \tfrac12\Big(F_i(\sigma\to x)-F_i(\sigma^{(i,x)}\to\sigma)\Big)
$$

so that $F_i = F_i^{\mathrm{sym}} + F_i^{\mathrm{sol}}$ and $F_i^{\mathrm{sym}}(\sigma\to x)=F_i^{\mathrm{sym}}(\sigma^{(i,x)}\to\sigma)$.

Since $F_i(\sigma\to x) = e^{\Phi(\sigma)} w_i(\sigma\to x)$, define rates accordingly:

$$
w_i^{\mathrm{sym}}(\sigma\to x) := e^{-\Phi(\sigma)} F_i^{\mathrm{sym}}(\sigma\to x),\qquad
w_i^{\mathrm{sol}}(\sigma\to x) := e^{-\Phi(\sigma)} F_i^{\mathrm{sol}}(\sigma\to x)
$$

so $w_i = w_i^{\mathrm{sym}} + w_i^{\mathrm{sol}}$ and $F_i^{\mathrm{sym}} = e^{\Phi}w_i^{\mathrm{sym}}$, $F_i^{\mathrm{sol}} = e^{\Phi}w_i^{\mathrm{sol}}$.

We proceed in two steps: (i) the antisymmetric component is divergence-free and never changes the steady state; (ii) the remaining symmetric component yields exactly the same $p^\ast$ as the equilibrium distribution obtained by setting $J=J^{\mathrm{S}}$. Finally, as a bonus, we show that the induced circulating flow is indeed tangential to the level sets of $\Phi$, in accordance to the Helmholtz decomposition.

#### i) Antisymmetric component is divergence-free (does not change $p^\ast$).

Starting again from stationarity of the full current,

$$
\sum_i \int_{-1}^1 \Big(F_i(\sigma^{(i,x)}\to\sigma)-F_i(\sigma\to x)\Big) dx = 0
$$

subtract the same identity written with $F^{\mathrm{sym}}$ in place of $F$. Because $F^{\mathrm{sym}}(\sigma\to x)=F^{\mathrm{sym}}(\sigma^{(i,x)}\to\sigma)$ on every edge, its contribution vanishes pairwise, giving

$$
\sum_i \int_{-1}^1 \Big(F_i^{\mathrm{sol}}(\sigma^{(i,x)}\to\sigma)-F_i^{\mathrm{sol}}(\sigma\to x)\Big) dx = 0
$$

Thus $F^{\mathrm{sol}}$ has zero divergence and does not change $p^\ast$.

#### ii) Symmetric component determines $p^\ast$ and matches the equilibrium solution with $J=J^{\mathrm{S}}$.

From Section 3, only $J^{\mathrm{S}}$ can appear in a potential gradient (commuting mixed partials). Therefore

$$
\partial_{\sigma_i}\Phi(\sigma) = b_i + \sum_{k\neq i} J^{\mathrm{S}}_{ik}\,\sigma_k
$$

which integrates to the same $\Phi=\log p^\ast$ you obtain by enforcing detailed balance with the symmetric coupling $J=J^{\mathrm{S}}$ (i.e., in the absence of $J^{\mathrm{A}}$). Equivalently, the symmetric current $F^{\mathrm{sym}}$ is reversible with respect to $p^\ast$ and alone reproduces the same steady state.

#### Note: Tangency to level sets of $\Phi$ (no work against the potential).

Multiply the preceding identity by a test function $\psi(\sigma)$ and integrate over $\sigma$ (“summation by parts”) to obtain

$$
\int d\sigma\, \sum_i\int_{-1}^1 F_i^{\mathrm{sol}}(\sigma\to x)\,\big[\psi(\sigma^{(i,x)})-\psi(\sigma)\big] dx = 0
$$

Taking $\psi=\Phi$ yields

$$
-\int d\sigma\, \sum_i\int_{-1}^1 F_i^{\mathrm{sol}}(\sigma\to x)\,\big[\Phi(\sigma^{(i,x)})-\Phi(\sigma)\big] dx = 0
$$

so the solenoidal current is orthogonal to discrete gradients and flows tangent to the isocontours of $\Phi$ (the level sets of $p^\ast$).

3) Link to $J^{\mathrm{A}}$.

Under the linear Continuous–Bernoulli parametrization, $J^{\mathrm{A}}$ cannot contribute to any scalar potential (mixed partials must commute). Therefore, varying $J^{\mathrm{A}}$ at fixed $J^{\mathrm{S}}$ leaves $\Phi$ and $p^\ast$ unchanged; it only affects the circulating, divergence-free component $F^{\mathrm{sol}}$.

#### Conclusion: explicit steady-state $p^\ast$ for arbitrary $J$

By the results above, only the symmetric component $J^{\mathrm{S}} := \tfrac12(J+J^\top)$ can shape the potential $\Phi=\log p^\ast$. Therefore, for arbitrary (possibly asymmetric) $J$, the non-equilibrium steady-state density takes the Boltzmann-like form:

$$
p^\ast(\sigma) = \frac{1}{Z} \exp\Bigg( \sum_i b_i\,\sigma_i + \sum_{i,j} J^{\mathrm{S}}_{ij}\,\sigma_i\,\sigma_j \Bigg)
$$

with $J^{\mathrm{S}}_{ii}=0$ and partition function

$$
Z = \int_{[-1,1]^N} \exp\Bigg( \sum_i b_i\,\sigma_i + \sum_{i,j} J^{\mathrm{S}}_{ij}\,\sigma_i\,\sigma_j \Bigg) \, d\sigma
$$

The antisymmetric component $J^{\mathrm{A}} := \tfrac12(J-J^\top)$ contributes only to divergence-free (solenoidal) probability currents tangent to the level sets of $\Phi$ and thus does not alter $p^\ast$. This expression matches the manuscript’s stationary density, with $J^{\mathrm{S}}$ playing the role of the effective (symmetric) interaction matrix.

## Supplementary Information 2

Here we provide a concise derivation of how $\sigma$ and $J$ changes as a consequence of free energy minimization resulting in an inference (node update) rule and a local, incremental learning rule, respectively.

For more background and a detailed derivation, see {cite:p}`10.48550/ARXIV.2505.22749`.

Let the instantaneous net input to node $\sigma_i$ be

$$
u_i := b_i + \sum_{j\ne i} J_{ij}\,\sigma_j,
$$

and let $q(\sigma_i)\propto e^{b_q\sigma_i}$ be the variational marginal with mean $L(b_q)$, where $L$ is the Langevin function (the mean of the Continuous–Bernoulli).

### Inference (Hopfield-style)

We start by writing up the local variational free energy from the point of view of a single node $\sigma_i$:

:::{math}
:label: variational-free-energy
F = \mathbb{E}_q[\ln q(\sigma_i)] - \mathbb{E}_q[\ln p(\sigma_{\setminus i}\mid \sigma_i)]
:::

Next we express:

:::{math}
\ln q(\sigma_i)= b_q\,\sigma_i - A(b_q) + \ln h(\sigma_i)
:::

with mean $\mathbb{E}_q[\sigma_i]=L(b_q)=A'(b_q)$.

and

:::{math}
\ln p(\sigma_{\setminus i}\mid \sigma_i) = \text{const} + \sigma_i\,\sum_{j\ne i} J_{ij}\sigma_j.
:::

As it depends on $\sigma_i$ only through the linear slope $\sum_{j\ne i}J_{ij}\sigma_j$:

:::{math}
\mathbb{E}_q[\,\ln p(\sigma_{\setminus i}\mid \sigma_i)\,] = \text{const} + L(b_q)\,\sum_{j\ne i} J_{ij}\sigma_j
:::

Now, we assemble the local free energy (dropping constants independent of $b_q$):

$$
F = (b_q - b_i)\,L(b_q) - \big[A(b_q)-A(b_i)\big] - L(b_q)\sum_{j\ne i}J_{ij}\sigma_j.
$$

Equivalently, using $u_i=b_i+\sum_{j\ne i}J_{ij}\sigma_j$ and $A'(b_q)=L(b_q)$,

$$
F = (b_q - u_i)\,L(b_q) - A(b_q) + \text{const}.
$$

3) Differentiate w.r.t. $b_q$ and use $A'(b_q)=L(b_q)$ to cancel terms:

$$
\frac{\partial F}{\partial b_q} = (b_q-u_i)\,L'(b_q) + L(b_q) - A'(b_q) = (b_q-u_i)\,L'(b_q).
$$

Setting the derivative to zero gives $b_q^\star=u_i$ and therefore the node-wise update

$$
\boxed{\;\mathbb{E}_q[\sigma_i] \;=\; L(b_q^\star) \;=\; L\!\left(b_i + \sum_{j\ne i} J_{ij}\,\sigma_j\right)\;}
$$

which is the stochastic Hopfield/Boltzmann-style activation with the Langevin nonlinearity.

### Learning (Hebb − anti-Hebb)

Make the dependence on $u_i$ explicit by adding and subtracting the CB log-partition $A(u_i)$ (using $\ln p(\sigma_i\mid\sigma_{\setminus i})=u_i\,\sigma_i - A(u_i)+\ln h(\sigma_i)$ and Bayes’ rule):

$$
F = \mathbb{E}_q\big[(b_q-u_i)\,\sigma_i\big] + A(u_i) - A(b_q) + \text{const}.
$$

Now

$$
\frac{\partial F}{\partial u_i} = -\mathbb{E}_q[\sigma_i] + A'(u_i) = -\mathbb{E}_q[\sigma_i] + L(u_i),
$$

and by the chain rule with $\partial u_i/\partial J_{ij}=\sigma_j$ we obtain

$$
\frac{\partial F}{\partial J_{ij}} = \big[\,L(u_i) - \mathbb{E}_q[\sigma_i] \,\big] \, \sigma_j.
$$

Using a stochastic (sample-based) estimate $\mathbb{E}_q[\sigma_i]\approx\sigma_i$ and descending $F$ gives the local update

$$
\boxed{\;\Delta J_{ij} \;\propto\; \underbrace{\sigma_i\sigma_j}_{\text{Hebbian (observed)}} \;-\; \underbrace{L\!\left(b_i+\sum_{k\ne i} J_{ik}\sigma_k\right)\sigma_j}_{\text{anti-Hebbian (predicted)}}\;}
$$

This is a predictive coding-based learning rule that strengthens observed correlations and subtracts those already predicted by the current model.


## Supplementary Information 3

**Self-orthogonalization of attractor states**

To illustrate how the learning rule in free energy minimizing attractor networks gives rise to efficient, (approximately) orthogonal representations of the external states, suppose the network has already learned a pattern $\mathbf{s}^{(1)}$, whose neural representation is the attractor $\boldsymbol{\sigma}^{(1)}$ and associated weights $\mathbf{J}^{(1)}$. When a new pattern $\mathbf{s}^{(2)}$ is presented that is correlated with $\mathbf{s}^{(1)}$, the network's prediction for $\sigma_i^{(2)}$ will be $\hat{\sigma}_i = L(b_i + \sum_{k \neq i} J_{ik}^{(1)} \sigma_k)$. Because inference with $\mathbf{J}^{(1)}$ converges to $\boldsymbol{\sigma}^{(1)}$ and $\boldsymbol{\sigma}^{(2)}$ is correlated with $\boldsymbol{\sigma}^{(1)}$, the prediction $\hat{\boldsymbol{\sigma}}$ will capture variance in $\boldsymbol{\sigma}^{(2)}$ that is 'explained' by $\boldsymbol{\sigma}^{(1)}$.
The learning rule updates the weights based only on the unexplained (residual) component of the variance, the prediction error. In other words, $\hat{\boldsymbol{\sigma}}$ approximates the projection of $\boldsymbol{\sigma}^{(2)}$ onto the subspace already spanned by $\boldsymbol{\sigma}^{(1)}$. Therefore, the weight update primarily strengthens weights corresponding to the component of $\boldsymbol{\sigma}^{(2)}$ that is orthogonal to $\boldsymbol{\sigma}^{(1)}$. 
Thus, the learning effectively encodes this residual, $\boldsymbol{\sigma}^{(2)}_{\perp}$, ensuring that the new attractor components being formed tend to be orthogonal to those already established.

For more details on self-orthogonalization in these networks, including an empirical demonstration, see {cite:p}`10.48550/ARXIV.2505.22749`.


## Supplementary Information 4

**Reconstruction of the attractor network from the activation timeseries.**

We start from Eq. [](steady-state-dist), written in matrix notation: \
$E_{HN}(\bm{\sigma}) = -\frac{1}{2} \sigma^\top J \sigma + \sigma^\top b \\ 
= -\frac{1}{2} \sigma^\top J \sigma + \sigma^\top J J^{-1} b \\
= -\frac{1}{2} \sigma^\top J \sigma + \sigma^\top J J^{-1} b - \frac{1}{2} b^\top J^{-1} b + \frac{1}{2} b^\top J^{-1} b
$ \
\
To complete the square, we added and subtracted  $\frac{1}{2} b^\top J^{-1} b$  within the exponent.
We recognize that  $\sigma^\top J J^{-1} b = \sigma^\top b$. Now add and subtract  $\frac{1}{2} b^\top J^{-1} b$

$
= -\frac{1}{2} \left[\sigma^\top J \sigma - 2 \sigma^\top J J^{-1} b + b^\top J^{-1} b \right] + \frac{1}{2} b^\top J^{-1} b \\
= -\frac{1}{2} \left[\sigma - J^{-1} b \right]^\top J \left[\sigma - J^{-1} b\right] + \frac{1}{2} b^T J^{-1} b
$ \
\
Given that $P(\bm{\sigma}) = \exp(-E_{HN}(\bm{\sigma}))$, the expression simplifies to:
$
P(\sigma) \propto \exp\left(-\frac{1}{2} (\sigma - J^{-1} b)^\top J (\sigma - J^{-1} b) \right)
$ \
\
Note that the term  $\frac{1}{2} b^\top J^{-1} b$  is independent of  $\sigma$; we have absorbed it into the normalization constant. 
\
This is exactly the exponent of a multivariate Gaussian distribution with mean $J^{-1} b$ and covariance matrix $J^{-1}$, meaning that the weight matrix of the attractor network can be reconstructed as the inverse covariance matrix of activation timeseries of the lower-level nodes:
$
\mathbf{J} = -\Lambda = -\Sigma^{-1}
$





