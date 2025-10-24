---
subject: Manuscript draft
#subtitle: Optional Subtitle
short_title: Methods

abbreviations:
  fMRI: functional Magnetic Resonance Imaging
  fcANN: functional connectivity-based Attractor Neural Network
  HNN: Hopfield Neural Network
  ANN: Artificial Neural Network
  ABIDE: Autism Brain Imaging Data Exchange
  ASD: Autism Spectrum Disorder
  MCC: Middle Cingulate Cortex
  ACC: Anterior Cingulate Cortex
  pg: perigenual
  PFC: Prefrontal Cortex
  dm: dorsomedial
  dl: dorsolateral
  STG: Superior Temporal Gyrus
  MTG: Middle Temporal Gyrus
  ITG: Inferior Temporal Gyrus
  Caud/Acc: Caudate-Accumbens
  SM: Sensorimotor
  V1: Primary Visual
  A1: Primary Auditory
  Hipp: Parahippocampal Gyrus
  Precun: Precuneus
  SMA: Supplementary Motor Cortex
  IPL: Inferior Parietal Lobule
  FEP: Free Energy Principle
  FEP-ANN: Free-energy minimizing Attractor Neural Network

exports:
  - format: pdf
    template: arxiv_nips
    output: exports/connattractor_methods.pdf
  - format: docx
    hideFooter: true
    output: exports/connattractor_methods.docx

bibliography:
  - bibliography.bib
---


# Methods

### Statistical analysis and reporting

Unless stated otherwise, all hypothesis tests are two-sided. When permutation tests are used, reported p-values are empirical permutation p-values computed as the proportion of null replicates with a test statistic at least as extreme as the observed one (with the usual +1 numerator/denominator correction). We report the statistic used in each comparison (e.g., Pearson correlation r, chi-square dissimilarity, L2 norm of position differences, median iterations to convergence). Degrees of freedom are reported where parametric tests are used; permutation-based p-values do not have degrees of freedom. By default, permutation counts were 1,000, except where explicitly noted (e.g., 50,000 label shuffles in clinical analyses). Confidence intervals based on bootstrap are percentile bootstrap intervals; where shown as 99% CIs, they reflect the percentile range from the bootstrap samples described below.

For multiple comparisons in the clinical analyses, we applied Bonferroni correction across regions and attractor states as specified below.

### Data

We obtained functional MRI data from seven sources (see [tab-samples](#tab-samples)). MRI sequence parameters for studies 1–4 are summarized in Supplementary Table {numref}`si-tab-mri`.
We included three resting-state studies with healthy volunteers (study 1, study 2, study 3, $n_{total}=118$), one task-based study (study 4, $n_{total}=33$ participants, nine runs each), an individual-participant meta-analytic activation map of pain (study 5, $n_{total}=603$ from 20 studies), eight task-based activation patterns obtained from coordinate-based meta-analyses via Neurosynth (study 6, 14,371 studies in total; see {numref}`Supplementary Table %s <si-tab-neurosynth>`), and a resting-state dataset focusing on autism spectrum disorder (ASD) from ABIDE (study 7, $n_{total}=1,112$, {cite}`di2014autism`).

```{list-table} **Datasets and studies.** The table includes details about the study modality, analysis aims, sample size used for analyses, mean age, gender ratio, and references.
:header-rows: 1
:name: tab-samples

* - study
  - modality
  - analysis
  - n
  - age (mean±sd)
  - \%female
  - references
* - study 1
  - resting state
  - discovery
  - 41
  - 26.1±3.9
  - 37%
  - [](10.1038/s41467-019-13785-z)
* - study 2
  - resting state
  - replication
  - 48
  - 24.9±3.5
  - 54%
  - [](10.1038/s41467-019-13785-z)
* - study 3
  - resting state
  - replication
  - 29
  - 24.8±3.1
  - 53%
  - [](10.1038/s41467-019-13785-z)
* - study 4
  - task-based
  - pain self-regulation
  - 33
  - 27.9 ± 9.0 
  - 66%
  - [](https://doi.org/10.1371/journal.pbio.1002036)
* - study 5 (Metaanalysis)
  - task-based
  - IPD meta-analysis pain map
  - n=603 (20 studies)
  - 26.3 ± 5.9
  - 39%
  - {cite}`zunhammer2021meta`
* - study 6 (Neurosynth)
  - task-based
  - coordinate-based meta-analyses
  - 14371 studies in total
  - N/A
  - N/A
  - [](https://doi.org/10.1038/nmeth.1635)
* - study 7 (ABIDE, NYU sample)
  - resting state
  - Autism Spectrum Disorder
  - ASD: 98; NC: 74
  - 15.3±6.6
  - 20.9%
  - {cite}`di2014autism`
```

Study 1 was used to evaluate whether the resting‑state functional connectome can be treated as an attractor network, to optimize the temperature ($\beta$) and noise ($\epsilon$) parameters of the fcANN model, and to evaluate the proposed approach for reconstructing resting‑state brain dynamics. Studies 2 and 3 served as replication datasets. Studies 1–3 are well suited to examine replicability and generalizability; data were acquired in three centers across two countries, by different research staff, with different scanners (Philips, Siemens, GE) and imaging sequences. Further details on studies 1–3 are described in [](10.1038/s41467-019-13785-z). The ability of the proposed approach to model task‑based perturbations of brain dynamics was evaluated in study 4, which consisted of nine task‑based fMRI runs for each of the 33 healthy volunteers. In all runs, participants received heat pain stimulation. Each stimulus lasted 12.5 seconds, with a 3‑second ramp‑up and 2‑second ramp‑down and 7.5 seconds at target temperature. Six temperature levels were administered (44.3°C, 45.3°C, 46.3°C, 47.3°C, 48.3°C, 49.3°C). We used run 1 (passive experience), run 3 (down‑regulation), and run 7 (up‑regulation). In runs 3 and 7, participants were asked to cognitively increase (regulate up) or decrease (regulate down) pain intensity. No self‑regulation instructions were provided in run 1. See {cite:t}`woo2015distinct` for details.
Pain control signal for our task-based trajectory analyses on data from study 4 was derived from our individual participant meta-analysis of 20 pain fMRI studies (study 5, n=603). For details, see {cite:t}`zunhammer2021meta`.
To obtain fMRI activation maps for other tasks, we used Neurosynth ([](https://doi.org/10.3389/conf.fninf.2011.08.00058)), a web-based platform for large-scale, automated synthesis of fMRI data. We performed eight coordinate-based meta-analyses with the terms "motor", "auditory", "visual", "face", "autobiographical", "theory mind", "language", and "pain" ({numref}`Supplementary Table %s <si-tab-neurosynth>`) and obtained Z-score maps from a two-way ANOVA, comparing coordinates reported for studies with and without the term of interest and testing for a nonzero association between term use and voxel activation.
In study 7 (ABIDE), we obtained preprocessed regional time-series data from the Preprocessed Connectome Project {cite:p}`craddock2013towards`, as shared at https://osf.io/hc4md by {cite:t}`dadi2019benchmarking`. Preprocessed time-series data were obtained with the 122-region version of the BASC (Bootstrap Analysis of Stable Clusters) brain atlas {cite:p}`bellec2010multi`.

### Preprocessing and time-series extraction

Functional MRI data from studies 1–4 were preprocessed with our in-house analysis pipeline, the RPN-pipeline (https://github.com/spisakt/RPN-signature). The RPN-pipeline is based on PUMI (Neuroimaging Pipelines Using Modular workflow Integration, https://github.com/pni-lab/PUMI), a nipype-based {cite:p}`gorgolewski2011nipype` workflow management system. It capitalizes on tools from FSL {cite:p}`jenkinson2012fsl`, ANTs {cite:p}`avants2011reproducible`, and AFNI {cite:p}`cox1996afni`, with code partially adapted from C-PAC {cite:p}`craddock2013towards` and niworkflows {cite:p}`esteban2019fmriprep`, as well as in-house Python routines.

Brain extraction from both anatomical and structural images, as well as tissue segmentation from the anatomical images, was performed with FSL BET and FAST. Anatomical images were linearly and nonlinearly co-registered to the 1 mm MNI152 standard brain template with ANTs (see https://gist.github.com/spisakt/0caa7ec4bc18d3ed736d3a4e49da7415 for parameters).
Functional images were co-registered to the anatomical images with FSL FLIRT’s boundary-based registration. All resulting transformations were saved for further use. Preprocessing of functional images was performed in native space, without resampling. Realignment-based motion correction was performed with FSL MCFLIRT. The resulting six head motion estimates (three rotations, three translations), their squared terms, their derivatives, and the squared derivatives (Friston-24 expansion, {cite}`friston1996movement`) were calculated as nuisance signals. Additionally, head motion was summarized as framewise displacement (FD) time series, according to Power’s method {cite:p}`power2012spurious`, for use in censoring and exclusion. After motion correction, outliers (e.g., motion spikes) in time‑series data were attenuated using AFNI despike. The union of eroded white‑matter maps and ventricle masks was transformed to native functional space and used to extract noise signals for anatomical CompCor correction {cite:p}`behzadi2007component`.

In a nuisance regression step, six CompCor parameters (the first six principal components of noise-region time series), the Friston‑24 motion parameters, and the linear trend were removed with a general linear model. On the residual data, temporal band‑pass filtering was performed with AFNI’s 3dBandpass to retain the 0.008–0.08 Hz band. To further attenuate motion artifacts, potentially motion‑contaminated time frames, defined by a conservative FD > 0.15 mm threshold, were dropped (scrubbing, {cite}`satterthwaite2013improved`). Participants were excluded if more than 50% of frames were scrubbed.

The 122‑parcel BASC (Bootstrap Analysis of Stable Clusters) atlas {cite:p}`bellec2010multi` was individualized by transforming it to each participant’s native functional space (nearest‑neighbour interpolation) and masking by that participant’s grey‑matter mask to retain only grey‑matter voxels. Voxel time series were then averaged within BASC regions.

All these preprocessing steps are part of the containerized version of the RPN-pipeline (https://spisakt.github.io/RPN-signature), which we run with default parameters for all studies, as in [](10.1038/s41467-019-13785-z).

### Functional connectome

Regional time series were ordered into large-scale functional modules (defined by the 7‑parcel level of the BASC atlas) for visualization.
Next, in all datasets, we estimated study‑level mean connectivity matrices by regularized partial correlation via the Ledoit–Wolf shrinkage estimator {cite:p}`https://doi.org/10.1016/S0047-259X(03)00096-4`, as implemented in Nilearn {cite:p}`abraham2014machine`. The precision matrix was obtained by inverting the shrinkage covariance, and partial correlations were derived from the precision; diagonal elements were set to zero. 


### fcANN inference (FEP-ANN) and update rules

Our fcANN instantiates the inference dynamics of free-energy-minimizing attractor neural networks (FEP-ANNs) at the macro-scale. Each node represents a brain region with continuous activity $\boldsymbol{\sigma} = (\sigma_1,\dots,\sigma_m)$, and couplings are given by the symmetrized matrix $\boldsymbol{J}$ (see Functional connectome). Unless noted otherwise, biases are zero ($\boldsymbol{b}=\boldsymbol{0}$).

Deterministic inference. In the noise‑free symmetric case, activities are updated by repeatedly applying a sigmoidal nonlinearity to the weighted input

```{math}
:label: fep-deterministic-update
\boldsymbol{\sigma}^{(t+1)} = S\!\left( \beta\, \boldsymbol{J}\, \boldsymbol{\sigma}^{(t)} \right),
```

where $S$ is a smooth odd sigmoid (we used $\tanh$ as a practical, fast surrogate for the Langevin function) and $\beta$ is the inverse temperature (precision) scaling the couplings. As the inference rule was derived as a gradient descent on free energy, iterations monotonically decrease the free energy function and therefore converge to a local free‑energy minimum without any external optimizer. Thus, convergence does not require any optimization procedure with an external optimizer. Instead, it arises as the fixed point of repeated local inference updates, which implement gradient descent on free energy in the deterministic symmetric case (see main text).

Stochastic (Langevin‑style) inference. For generative modeling of dynamics, we adopt a slight variation of the FEP‑ANN inference rule: starting from the deterministic update above, we add zero‑mean Gaussian noise directly to the post‑activation state (Langevin‑style)

```{math}
:label: langevin-update
\boldsymbol{\sigma}^{(t+1)} = S\!\left( \beta\, \boldsymbol{J}\, \boldsymbol{\sigma}^{(t)} \right) + \boldsymbol{\omega}^{(t)}, \quad \boldsymbol{\omega}^{(t)} \sim \mathcal{N}(\boldsymbol{0}, \epsilon^2 \boldsymbol{I}).
```

This explicit additive Gaussian noise differs from the continuous‑Bernoulli noise implied by the theoretical derivation but aligns with common Langevin formulations and was empirically robust. We use deterministic updates to identify attractors and study convergence; we use stochastic updates as a generative model of multistable dynamics.

### fcANN convergence and attractors

We investigated convergence under the deterministic update (Eq. [](#fep-deterministic-update)) by contrasting iterations-to-convergence of the empirical fcANN against a permutation-based null. The null was constructed by randomly permuting the upper triangle of $\boldsymbol{J}$ and reflecting it to preserve symmetry (destroying topology while preserving weight distribution). For each of 1,000 permutations, we initialized both models with the same random state and counted iterations to convergence. Statistical significance of faster convergence in the empirical connectome was assessed via a one-sided Wilcoxon signed-rank test on paired iteration counts (1,000 pairs), testing whether the empirical connectome converges in fewer iterations than its permuted counterpart. We repeated this procedure across inverse-temperature values $\beta \in \{0.035, 0.040, 0.045, 0.050, 0.055, 0.060\}$ (yielding 2–8 attractor states). See {numref}`Supplementary Figure %s <si_convergence>` for detailed results.


### fcANN projection

We mapped out the fcANN state space by initializing the model with a random input and applying the stochastic update (Eq. [](#langevin-update)) for $10^5$ iterations, storing visited activity configurations. We performed principal component analysis (PCA) on the samples and used the first two PCs as the coordinate system for the fcANN projection. Using multinomial logistic regression, we predicted attractor identity from the first two PCs. Performance was evaluated with 10-fold cross-validation and a two-sided permutation test (1,000 label permutations within folds). We visualized attractor positions and decision boundaries based on this classifier. The fcANN projection is used for visualization; unless otherwise noted, inferential comparisons between empirical and simulated data are performed in the full 122-dimensional space.


### Parameter optimization
Based on the convergence analysis, we selected the inverse temperature providing the fastest median convergence ($\beta = 0.04$) for subsequent analyses, to minimize computational costs. We then optimized the stochastic noise level $\epsilon$ for the Langevin-style update by comparing the full 122-dimensional distributions of empirical and fcANN-generated data.

Specifically, for eight $\epsilon$ values spaced logarithmically between 0.1 and 1, we generated samples with Eq. [](#langevin-update) and computed the 2‑Wasserstein (Earth Mover’s) distance between the 122‑dimensional empirical and simulated distributions (after per‑region z‑scoring). As a null, we drew surrogate samples from a covariance‑matched multivariate normal distribution $\mathcal{N}(\boldsymbol{0}, \boldsymbol{\Sigma})$, where $\boldsymbol{\Sigma}$ is the empirical covariance of the regional time series. For each $\epsilon$, we generated 1,000 null surrogates and contrasted the empirical Wasserstein distance to the null distribution, summarizing the separation with Glass’s $\Delta$ and permutation p‑values. We selected $\epsilon = 0.37$ for all subsequent analyses.

### Replicability

We obtained the four attractor states in study 1, as described above. We then constructed two other fcANNs, based on the study-mean functional connectome obtained in studies 2 and 3 and  obtained all attractor states of these models, with the same parameter settings ($\beta = 0.04$ and $\epsilon = 0.37$) as in study 1. In both replication studies we found four attractor states. The spatial similarity of attractor states across studies was evaluated by Pearson's correlation coefficient.

### Evaluation: resting state dynamics

To evaluate the explanatory power of the fcANN projection, we performed PCA on the preprocessed fMRI time frames from study 1 (analogous to the methodology of the fcANN projection, but on the empirical time‑series data).
Next, we fitted linear regression models using the first two fcANN‑based or data‑based PCs as regressors to reconstruct the real fMRI time frames. In‑sample explained variances and confidence intervals were calculated for both models with bootstrapping (100 samples; percentile 99% CIs). Differences in explained variance between fcANN‑ and data‑based PCs were assessed with a two‑sided percentile bootstrap on the difference in $R^2$. To evaluate out‑of‑sample generalization of the PCs (fcANN‑ and data‑based) from study 1, we calculated how much variance they explain in study 2.

Similarity between state occupancy and distribution was calculated during parameter optimization. More detail on the associated null models can be found in {numref}`Supplementary Figure %s <si_state_occupancy_null_models>`.

To confirm that the real and fcANN temporal sequences (from the stochastic relaxation) display similar temporal autocorrelation properties, we compared both to their randomly shuffled variant with a "flow analysis".
First, we calculated the direction on the fcANN projection plane between each successive TR (a vector on the fcANN projection plane for each TR transition), both for the empirical and the shuffled data.
Next, we obtained two‑dimensional binned means for both the x and y coordinates of these transition vectors (pooled across all participants), calculated over a 100×100 grid of uniformly distributed bins in the [−6, 6] range (arbitrary units) and applied Gaussian smoothing with $\sigma=5$ bins (same approach as described in the [](#Parameter-optimization) section). 
Finally, we visualized the difference between the binned-mean trajectories of the empirical and the shuffled data as a "streamplot", with the Python package matplotlib.
The same approach was repeated with the fcANN-generated data. The similarity of the real and fcANN-generated flow analysis was quantified with Pearson's correlation coefficient (two-sided); p-values were obtained with permutation testing (1,000 permutations), by shuffling temporal order (for resting-state analyses) or condition labels (for task analyses; see below).


### Evaluation: task-based dynamics

We used study 4 to evaluate the ability of the fcANN approach to capture and predict task-induced alterations in large-scale brain dynamics.
First, runs 1, 3 and 7, investigating the passive experience and the down- and up-regulation of pain, respectively, were preprocessed with the same workflow used to preprocess studies 1-3 ([](#preprocessing-and-time-series-extraction)). Regional time series were grouped into "pain" and "rest" blocks, with a 6-second delay to adjust for the hemodynamic response time. All activation time frames were transformed to the fcANN projection plane obtained from study 1. Within-participant differences in the average location on the fcANN projection were calculated and visualized with radial plots, showing the participant-level mean trajectory on the projection plane from rest to pain (circles), as well as the group-level trajectory (arrow). The significance of the position difference and energy difference of the participant-level mean activations on the projection plane was tested with a two-sided permutation test (1,000 permutations), using the L2 norm of the two-dimensional position difference and the absolute energy difference, respectively, as test statistics, and randomly swapping the conditions within each participant.

To further highlight the difference between the task and rest conditions, a "flow analysis" was performed to investigate the dynamic trajectory differences between the conditions rest and pain. The analysis method was identical to the flow analysis of the resting state data ([](#evaluation-resting-state-dynamics)). First, we calculated the direction in the projection plane between each successive TR during the rest conditions (a vector on the fcANN projection plane for each TR transition). Next, we obtained two-dimensional binned means for the x and y coordinates of these transition vectors (pooled across all participants), calculated over a two-dimensional grid of 100×100 uniformly distributed bins in the [-6,6] range (arbitrary units) and applied Gaussian smoothing with $\sigma=5$ bins. 
The same procedure was repeated for the pain condition and the difference in the mean directions between the two conditions was visualized as “streamplots” (using Python’s matplotlib). We used the same approach to quantify the difference in characteristic state transition trajectories between the up- and downregulation conditions. The empirically estimated trajectory differences (from real fMRI data) were contrasted to the trajectory differences predicted by the fcANN model from study 1. The similarity between real and simulated flow maps was quantified with Pearson’s correlation coefficient (two-sided), and significance was assessed via permutation testing (1,000 permutations) by randomly swapping condition labels within participants.

To obtain fcANN-simulated state transitions in resting conditions, we used the stochastic relaxation procedure (Eq. [](#langevin-update)), with $\mathbf{\mu}$ set to zero.
To simulate the effect of pain-related activation on large-scale brain dynamics, we set $\mu_i$ during the stochastic relaxation procedure to a value representing pain-elicited activity in region i. The region-wise activations were obtained calculating the parcel-level mean activations from the meta-analytic pain activation map from {cite:p}`zunhammer2021meta`, which contained Hedges' g effect sizes from an individual participant-level meta-analysis of 20 pain studies, encompassing a total of n=603 participants. The whole activation map was scaled with five different values ranging from $10^{-3}$ to $10^{-1}$, spaced logarithmically, to investigate various signal-to-noise scenarios.
We obtained the activity patterns of $10^5$ iterations from this stochastic relaxation procedure and calculated the state transition trajectories with the same approach used with the empirical data.
Next we calculated the fcANN-generated difference between the rest and pain conditions and compared it to the actual difference through a permutation test with 1,000 permutations, randomly swapping the conditions within each participant in the real data and using Pearson's correlation coefficient between the real (permuted) and fcANN-generated flow maps as the test statistic.
From the five investigated signal-to-noise values, we chose the one that provided the highest similarity to the real pain vs. rest trajectory difference.

When comparing the simulated and real trajectory differences between pain up- and downregulation, we used the same procedure, with two differences. First, when calculating the simulated state transition vectors for the self-regulation conditions, we used the same procedure as for the pain condition, but introduced and additional signal in the nucleus accumbens, with a negative and positive sign, for  up- and downregulation, respectively. We did not optimize the signal-to-noise ratio for the nucleus accumbens signal but, instead, simply used the value optimized for the pain vs. rest contrast (For a robustness analysis, see {numref}`Supplementary figure %s <si_downreg_trajectory_sim>`).


### Clinical data

To demonstrate the sensitivity of the fcANN approach to clinically relevant alterations of large-scale brain dynamics in autism spectrum disorder (ASD), we obtained data from n=172 individuals, acquired at the New York University Langone Medical Center (NYU) as shared in the Autism Brain Imaging Data Exchange dataset ([study 7](#tab-samples): ABIDE, {cite:p}`di2014autism`). We focused on the largest ABIDE imaging center to ensure that results were not biased by center effects. We excluded high‑motion cases similarly to studies 1–4, i.e., by scrubbing volumes with FD > 0.15 and excluding participants with >50% of data scrubbed. Time‑series data were pooled and visualized on the fcANN projection of study 1, separately for ASD and control participants. 
Next, for each participant, we grouped time frames from the regional time‑series data according to the corresponding attractor states (obtained with the fcANN model from study 1) and averaged time frames corresponding to the same attractor state to calculate participant‑level mean attractor activations.
We assessed mean attractor‑activity differences between groups with a two‑sided permutation test, randomly reassigning group labels 50,000 times. Reported effect sizes in the clinical tables are mean activation differences. Note that activation time series were standard‑scaled independently for each region, so effect size can be interpreted as the proportion of regional variability.
We adjusted the significance threshold with a Bonferroni-correction, accounting for tests across 4 states and 122 regions, resulting in $\alpha = 0.0001$. 
Finally, we calculated trajectory differences between the two groups, as predicted by the group‑specific fcANNs (initialized with the ASD and TDC connectomes), and—similarly to the approach used in study 4—contrasted the fcANN predictions with trajectory differences observed in real rsfMRI data. As in the previous flow analyses, we tested the significance of the similarity (Pearson's correlation) between predicted and observed trajectory differences with a two‑sided permutation test (1,000 permutations), by shuffling group labels.