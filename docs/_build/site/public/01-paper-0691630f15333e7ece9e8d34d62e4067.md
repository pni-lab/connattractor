---
title: Functional Connectivity-based Attractor Dynamics in Rest, Task, and Disease
subject: manuscript revision
short_title: Manuscript
authors:
    - name: Robert Englert
      affiliations:
        - Center for Translational Neuro- and Behavioral Sciences (C-TNBS), University Medicine Essen, Germany
        - Department of Diagnostic and Interventional Radiology and Neuroradiology,  University Medicine Essen, Germany
      email: robert.englert@uk-essen.de
      
    - name: Balint Kincses
      affiliations:
        - Center for Translational Neuro- and Behavioral Sciences (C-TNBS), University Medicine Essen, Germany
        - Department of Neurology, University Medicine Essen, Germany
        
    - name: Raviteja Kotikalapudi
      affiliations:
        - Center for Translational Neuro- and Behavioral Sciences (C-TNBS), University Medicine Essen, Germany
        - Department of Neurology, University Medicine Essen, Germany
        
    - name: Giuseppe Gallitto
      affiliations:
        - Center for Translational Neuro- and Behavioral Sciences (C-TNBS), University Medicine Essen, Germany
        - Department of Neurology, University Medicine Essen, Germany
        
    - name: Jialin Li
      affiliations:
        - Center for Translational Neuro- and Behavioral Sciences (C-TNBS), University Medicine Essen, Germany
        - Department of Neurology, University Medicine Essen, Germany
        - Max Planck School of Cognition, Leipzig, Germany
        
    - name: Kevin Hoffschlag
      affiliations:
        - Center for Translational Neuro- and Behavioral Sciences (C-TNBS), University Medicine Essen, Germanys
        - Department of Neurology, University Medicine Essen, Germany
    
    - name: Choong-Wan Woo
      affiliations:
        - Center for Neuroscience Imaging Research, Institute for Basic Science, Suwon, South Korea
        - Department of Biomedical Engineering, Sungkyunkwan University, Suwon, South Korea
        
    - name: Tor D. Wager
      affiliations:
        - Department of Psychological and Brain Sciences, Dartmouth College, Hanover, NH, USA

    - name: Dagmar Timmann
      affiliations:
        - Department of Neurology, University Medicine Essen, Germany
        - Center for Translational Neuro- and Behavioral Sciences (C-TNBS), University Medicine Essen, Germany
      
    - name: Ulrike Bingel
      affiliations:
        - Department of Neurology, University Medicine Essen, Germany
        - Center for Translational Neuro- and Behavioral Sciences (C-TNBS), University Medicine Essen, Germany

    - name: Tamas Spisak
      affiliations:
        - Department of Diagnostic and Interventional Radiology and Neuroradiology,  University Medicine Essen, Germany
        - Center for Translational Neuro- and Behavioral Sciences (C-TNBS), University Medicine Essen, Germany
      orcid: 0000-0002-2942-0821
      email: tamas.spisak@uk-essen.de
      corresponding: True

abbreviations:
  fMRI: functional Magnetic Resonance Imaging
  ANN: Artificial Neural Network
  fcANN: functional connectome-based Hopfield Neural Network
  HNN: Hopfield Neural Network
  PC: Principal Component
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

exports:
  - format: pdf
    template: arxiv_nips
    output: exports/connattractor_manuscript.pdf
  - format: docx
    hideFooter: true
    output: exports/connattractor_manuscript.docx

bibliography:
  - bibliography.bib
---

% {"part": "key-points"}
**Key Points:**
- We present a simple yet powerful generative computational model for large-scale brain dynamics
- The model uses a functional connectivity-based attractor artificial neural network (fcANN) architecture rooted in first principles of self-organization
- We provide first evidence that the brain's functional organization approximates a Kanter-Sompolinsky projector network
- fcANN attractor dynamics accurately reconstruct the several characteristics of resting state brain dynamics and confirm theoretical predictions of attractor orthogonality
- fcANNs conceptualize both task-induced and pathological changes in brain activity as a non-linear alteration of these dynamics
- Our approach is validated using large-scale neuroimaging data from seven studies
- fcANNs offers a simple and interpretable computational alternative to conventional descriptive analyses of brain function
%+++


%+++ {"part": "abstract"}

```{card}
:header: Abstract

Understanding large-scale brain dynamics is a grand challenge in neuroscience. 
We propose functional connectivity-based Hopfield Neural Networks (fcANNs), a theoretically-inspired model of macro-scale brain dynamics, simulating recurrent activity flow among brain regions based on first principles of self-organization. An fcANN is neither optimized to mimic certain brain characteristics, nor trained to solve specific tasks; its weights are simply initialized with empirical functional connectivity values.
In the fcANN framework, brain dynamics are understood in relation to attractor states, i.e. neurobiologically meaningful activity configurations that minimize the free energy of the system.
Analyses of 7 distinct datasets demonstrate that fcANNs can accurately reconstruct and predict brain dynamics under a wide range of conditions, including resting and task states and brain disorders.
By establishing a mechanistic link between connectivity and activity, fcANNs offers a simple and interpretable  computational alternative to conventional descriptive analyses of brain function. Being a generative framework, fcANNs can yield mechanistic insights and hold potential to uncover novel treatment targets.
```

%+++

## Introduction

Brain function is characterized by the continuous activation and deactivation of anatomically distributed neuronal 
populations {cite:p}`buzsaki2006rhythms`.
Irrespective of the presence or absence of explicit stimuli, brain regions appear to work in concert, giving rise to a rich and spatiotemporally complex fluctuation {cite:p}`bassett2017network`.
This fluctuation is neither random nor stationary over time {cite:p}`liu2013time; zalesky2014time`.
It is organized around large-scale gradients {cite:p}`margulies2016situating; huntenburg2018large` and exhibits quasi-periodic properties, with a limited number of recurring patterns often termed as "brain states" {cite:p}`greene2023everyone; vidaurre2017brain; liu2013time`.
A wide variety of descriptive techniques have been previously employed to characterize whole-brain dynamics {cite:p}`smith2012temporally; vidaurre2017brain; liu2013time; chen2018human`. 
These efforts have provided accumulating evidence not only for the existence of dynamic brain states but also for their clinical significance {cite:p}`hutchison2013dynamic; barttfeld2015signature; meer2020movie`. 
However, the underlying driving forces remain elusive due to the descriptive nature of such studies.

Conventional computational approaches attempt to solve this puzzle by going all the way down to the biophysical properties of single neurons, and aim to construct a model of larger neural populations, or even the entire brain 
{cite:p}`breakspear2017dynamic`.
These approaches have shown numerous successful applications {cite:p}`murray2018biophysical; kriegeskorte2018cognitive; heinz2019towards`.
However, such models need to estimate a vast number of neurobiologically motivated free parameters to fit the data. This hampers their ability to effectively bridge the gap between explanations at the level of single neurons and the complexity of behavior {cite:p}`breakspear2017dynamic`.
Recent efforts using coarse-grained brain network models {cite:p}`schirner2022dynamic; schiff1994controlling; papadopoulos2017development; seguin2023brain` and linear network control theory {cite:p}`chiem2021structure; scheid2021time; gu2015controllability` opted to trade biophysical fidelity to phenomenological validity.
Such models have provided insights into some of the inherent key characteristics of the brain as a dynamic system; for instance, the importance of stable patterns, the *"attractor states"*, in governing brain dynamics {cite:p}`deco2012anatomy; golos2015multistability; hansen2015functional`. While attractor networks become established models of micro-scale canonical brain circuits in the last four decades {cite:p}`khona2022attractor`, these studies suggest that attractor dynamics are essential characteristics of macro-scale brain dynamics as well {cite:p}`https://doi.org/10.1016/j.cobeha.2025.101546`.
Attractor networks, however, come in many flavors and the specific forms and behaviors of these networks are heavily influenced by the chosen inference and learning rules, making it unclear which variety should be in focus when modeling brain dynamics. 
Given that the brain showcases not only multiple signatures of attractor dynamics but also the ability to evolve and adapt through self-organization (i.e. in lack of any centralized control), investigating attractor models from the point-of-view of self-organization may be key to narrow down the the set of viable models.

In our recent theoretical work {cite:p}`10.48550/ARXIV.2505.22749`, we identified the class of attractor networks that emerge from first principles of self-organization - as articulated by the Free Energy Principle (FEP) {cite:p}`https://doi.org/10.1038/nrn2787; https://doi.org/10.1016/j.physrep.2023.07.001` - and identified the emergent inference and learning rules guiding the dynamics of such systems. 
This theoretical framework reveals that the minimization of variational free energy locally - e.g., by individual network nodes - gives rise to a dual dynamic: simultaneous inference (updating activity) and learning (optimizing connectivity).

The emergent inference process in these systems is equivalent to local Bayesian update dynamics for the individual network nodes, homologous to the stochastic relaxation observed in conventional Boltzmann neural network architectures (e.g. stochastic Hopfield networks, {cite:p}`hopfield1982neural; koiran1994dynamics`), and in line with the empirical observation that activity in the brain "flows" following similar dynamics {cite:p}`doi:10.1038/nn.4406; doi:10.1016/j.neuroimage.2023.120300; https://doi.org/10.48550/arXiv.2402.02191`. Importantly, in our framework, attractor states are not simply an epiphenomenon of collective dynamics, but serve as global priors in the Bayesian sense, that get combined with the current activity configuration so that the updated activity samples from the posterior (akin to a Markov-Chain Monte Carlo sampling process).

Learning, on the other hand, emerges in the form of a distinctive coupling plasticity - a local, incremental learning rule - that continuously adjusts coupling weights to preserve low free energy in anticipation of future sensory encounters following a contrastive predictive coding scheme {cite:p}`10.48550/ARXIV.2207.12316`, effectively implementing action selection in the active inference sense {cite:p}`https://doi.org/10.1016/j.neubiorev.2016.06.022`. Importantly, the learning dynamics emerging in our theoretical framework provide a strong, testable hypothesis: if the brain operates as a free energy minimizing attractor network, its large-scale attractors should be approximately orthogonal to each other. This is not a general property of all recurrent (attractor) neural networks, but a direct consequence of free energy minimization, shown both mathematically and with simulations in {cite:p}`10.48550/ARXIV.2505.22749`. 
As our theoretical framework - by design - embraces multiple valid levels of description (through course-graining), it is well-suited to serve as a basis for a computational model of large-scale brain dynamics.

In the present work, we translate the results of our theoretical framework on inference dynamics into a computational model of macro-scale brain dynamics and deploy a diverse set of experimental, clinical and meta-analytic studies to perform an initial investigation of several of its predictions. We start by showing that - if large-scale brain dynamics evolves and organizes according to the emergent rules of this framework - the corresponding attractor model can be effectively approximated from functional connectivity data, as measured with resting state fMRI. 
Based on the network topology spanned by functional connectivity, our model assigns a free energy level for any arbitrary activation patterns and determines a "trajectory of least action" towards one of the finite number of *attractor states*, that minimize this energy ({numref}`concept`). 
We than perform an initial investigation of the robustness and biological plausibility of the attractor states of the reconstructed network and whether it is able to reproduce various characteristics of resting state brain dynamics. Importantly, we directly test the framework's prediction on the emergence of (approximately) orthogonal attractor states. 
Capitalizing on the generative nature of our model, we also demonstrate how it can capture - and potentially explain - the effects of various perturbations and alterations of these dynamics, from task-induced activity to changes related to brain disorders.


%%%%%%%%%%%%%
%As our the current study only implements the inference dynamics, without relying on the core learning mechanism of the theoretical framework that lead to self-orthogonalization (predictive coding based plasticity), that is the applied computational model itself has no built-in preference for orthogonal attractor states.

%However, the standard practice among these studies is the use of models that capitalize on information about the structural wiring of the brain, leading to the grand challenge of modeling the relationship between structural pathways and polysynaptic functional connectivity.

% Like neuroconnectionism, we utilize an ANN as an abstract, high-level computational model of the brain.
% However, our model is not explicitly trained for a specific task. Instead, we set its weights empirically.
% Specifically, we employ a continuous-space Hopfield Neural Network (HNN) {cite:p}`hopfield1982neural; krotov2023new`, similar to the spin-glass and Hopfield-style attractor network models applied e.g. by {cite:t}`deco2012anatomy` or {cite:t}`golos2015multistability`, where the nodes of the network model represent large-scale brain areas.
% However, in contrast to these previous efforts that start from the structural wiring of the brain, we initialize the edge weights of the network based on direct estimates of node-to-node information transfer, as measured with fMRI.
% Our decision to capitalize on a direct proxy of interregional communication, rather than structural pathways, is motivated by the "activity flow" principle {cite:p}`cole2016activity; ito2017cognitive`, a thoroughly validated phenomenological model for the association between brain activity and functional connectivity.
% This allows us to circumvent the necessity of comprehensively understanding and accurately modeling structural-functional coupling in the brain. Instead, we can concentrate on the overarching dynamical properties of the system.
%%%%%%%%

:::{figure} figures/concept.png
:name: concept
**Functional connectivity-based attractor neural networks as models of macro-scale brain dynamics.** <br/><br/>
**A** Free energy minimizing artificial neural networks {cite:p}`10.48550/ARXIV.2505.22749` are a form of recurrent stochastic artificial neural networks that, similarly to classical Hopfield networks {cite:p}`hopfield1982neural; koiran1994dynamics`, can serve as content-addressable ("associative") memory systems. More generally, through the learning rule emerging from local free energy minimization, the weights of these network will encode a global internal model of the external world, as represented by the external inputs (or internal biases) presented to the network. The priors of this internal generative model are represented by the attractor states of the network that - as a special consequence of free energy minimization - will tend to be orthogonal to each other. During stochastic inference (local free energy minimization), the network samples from the posterior that combines these priors with the previous brain states (also encompassing incoming stimuli), akin to Markov-chain Monte Carlo (MCMC) sampling.
**B** In accordance to this theoretical framework, we consider regions of the brain as nodes of a free energy minimizing artificial neural network. Instead of initializing the network with the structural wiring of the brain or training it to solve specific tasks, we set its weights empirically, using information about the interregional "activity flow" across regions, as estimated via functional brain connectivity. Applying the inference rule of our framework - which displays strong analogies with the relaxation rule of Hopfield networks and the activity flow principle that links activity to connectivity in brain networks - results in a generative computational model of macro-scale brain dynamics, that we term functional connectivity-based (stochastic) attractor neural network (fcANN).  
**C** The proposed computational framework assigns a free energy level, a probability density and a trajectory fo least action towards an attractor state to any brain activation pattern and predicts changes of the corresponding dynamics in response to alterations in activity and/or connectivity. Throughout the present paper, we will illustrate these concepts with the aid of a low-dimensional embedding of the state-space, which we will refer to as the fcANN projection. 
The theoretical framework underlying the fcANNs - based on the assumption that the brain operates as a free energy minimizing attractor network - draws formal links between attractor dynamics and multi-level Bayesian active inference.
:::

## Theoretical background

### Free energy minimizing artificial neural networks

The computational model at the heart of this work is a direct implementation of the inference dynamics that emerge from a recently proposed theoretical framework of self-organizing attractor networks {cite:p}`10.48550/ARXIV.2505.22749`. 
Self-organizing attractor networks are a class of attractor neural networks that emerge from the Free Energy Principle (FEP) {cite:p}`https://doi.org/10.1038/nrn2787; https://doi.org/10.1016/j.physrep.2023.07.001`  which posits that any self-organizing system that maintains its integrity over time (i.e. has a steady-state distribution) must act in a way that minimizes its variational free energy. 

Specifically, we assume a network of $N$ units, where each unit is represented by a single continuous-valued state variable $\sigma_i \in [-1,1]$. The activity of the network is described by a vector of states $\bm{\sigma} = (\sigma_1, \sigma_2, \dots, \sigma_N)$. These states are conditionally independent of each other, given boundary states, that realize couplings between them (corresponding to a complex Markov blanket structure in the FEP terminology). 
When assuming $\sigma_i$ states that follow a continuous Bernoulli (a.k.a. truncated exponential: $p(\sigma_i) \propto e^{\kappa_i\sigma_i}$) distribution (parameterized by the single parameter $\kappa_i$) and deterministic couplings $\bm{J}$, the steady-state distribution can be expressed as:

```{math}
:label: steady-state-dist
p^*(\bm{\sigma}) \propto \exp\Big(\sum_i b_i \sigma_i + \frac{1}{2}\sum_{i,j} J^{\mathrm{S}}_{ij} \sigma_i \sigma_j\Big)
```
where $b_i$ represents the local evidence or bias for each unit $i$ (e.g. external input or intrinsic excitability of a brain region), $J^{\mathrm{S}} = \frac{1}{2}(J + J^\top)$ is the symmetric component of the coupling weights between units $i$ and $j$, and $\beta$ is an inverse temperature or precision parameter. 
Note that while this steady-state distribution has the same functional form as continuous-state Boltzmann machines or stochastic Hopfield networks, the true coupling weights $J$ do not have to be symmetric as usually assumed in those architectures. Asymmetric couplings break detailed balance, meaning that $p^*$ is no longer an equilibrium distribution. However, the antisymmetric component $J^{\mathrm{A}} = \frac{1}{2}(J - J^\top)$ does not contribute to the steady-state distribution $p^*$ as it only induces circulating (solenoidal) flow in the state space which is tangential to the level sets of $p^*$. Thus, while the overall framework can describe general attractor networks with asymmetric couplings and non-equilibrium steady states (NESS), it also implies that knowing only the symmetric component of the coupling weights is sufficient to reconstruct the steady-state distribution $p^*$ of the underlying system. This is a highly useful property for the purposes of the present study, where the couplings are reconstructed from resting state fMRI data, without any explicit information about the directionality of functional connections. For a detailed derivation of the steady state distribution, see {cite:p}`10.48550/ARXIV.2505.22749` and [](#Supplementary-Information-1).

Knowing the steady-state distribution of a self-organizing (i.e. free-energy-minimizing) attractor network, we can derivetwo types of emergent dynamics from the single imperative of free energy minimization: inference and learning. 

### Inference: stochastic relaxation dynamics
Inference arises from minimizing free energy with respect to the states $\sigma$. For a single unit, this yields a local update rule homologous to the relaxation dynamics in Hopfield networks:

```{math}
:label: fep-update
\mathbb{E}_{q}[\sigma_i] = L(b_q) = \underbrace{ L \left( \underbrace{ b_i}_{\textit{bias}} + \underbrace{\sum_{j \ne i} J_{ij} \sigma_j}_{\textit{weighted input}} \right) }_{ \textit{sigmoid (Langevin)} } 
```

where $L$ is a sigmoidal activation function (a Langevin function in our case). This rule dictates that each unit updates its activity stochastically, based on a weighted sum of the activity of other units, plus its own intrinsic bias. See {cite:p}`10.48550/ARXIV.2505.22749` and [](#Supplementary-Information-2) for a detailed derivation of the inference dynamics.

Note that the rule is expressed in terms of the expected value of the state $\sigma_i$, which is a stochastic quantity. However, in the limiting case of symmetric couplings (which is the case throughout the present study) and least-action dynamics (i.e. no noise), this update rule reduces to the classical relaxation dynamics of (continuous-state) Hopfield networks. 
In the present study, we will focus use both the deterministic ("least action") and stochastic variant of the inference rule. The former will be used to identify the attractor states of the network, while the latter will be used as a generative computational model for large scale multistable brain dynamics.

In the present study, we make the simplifying assumption that all nodes have zero bias ($\bf{b} = \bf{0}$). Furthermore, we allow investigating different scaling factors for the $J$ couplings matrix (given the uncertainties around the magnitude of association in the functional connectome) by introducing a "scaling factor" $\beta$. This leads to the following update rule:

:::{math}
\sigma_i^{(t+1)} = L\left(\beta\sum_{j \ne i} J_{ij} \sigma_j^{(t)} \right) + \textit{noise}
:::

The scaling factor $\beta$ is analogous to the inverse temperature parameter known in Hopfield networks and Boltzmann machines.

In the basis framework {cite:p}`10.48550/ARXIV.2505.22749`, inference is a gradient descent on the variational free energy landscape with respect to the states $\sigma$ and can be interpreted as a form of approximate Bayesian inference, where the expected value of the state $\sigma_i$ is interpreted as the posterior mean of given the attractor states currently encoded in the network (serving as a macro-scale prior) and the previous state, including external inputs (serving as likelihood in the Bayesian sense). The stochastic update, therefore, is equivalent to a Markov-chain Monte Carlo (MCMC) sampling from this posterior distribution. The inverse temperature parameter $\beta$, in this regard, can be interpreted as the precision of the prior encoded in $J$. This is easy to conceptualize by considering the limiting case of infinite precision, where the system simplifies to a binary-state Hopfield network ($\beta → \infty$, $L(\beta u_i) → sign(u_i)$ on $[-1,1]$) that directly and deterministically converges to the (infinite-precision) prior, completely overriding the the Bayesian likelihood (i.e. network input).

### Free energy minimizing attractor networks as a model of large-scale brain dynamics

Taken together, the novel framework of free energy minimizing attractor networks not only motivates the use of a specific, emergent class of attractor networks as models for large-scale brain dynamics, but also provides a formal connection between these dynamics and Bayesian inference.

The present study leverages this theoretical foundation. We aim to model large-scale brain dynamics as a free energy minimizing attractor network. 

According to our framework, such networks can be reconstructed from the activation timeseries data measured in its nodes. Specifically, the weight matrix of the attractor network can be reconstructed as the negative inverse covariance matrix of the regional activation timeseries: $\bm{J} = -\bm{\Lambda} = -\bm{\Sigma}^{-1}$, where $\bm{\Sigma}$ is the covariance matrix of the activation timeseries in all regions, and $\bm{\Lambda}$ is the precision matrix. For a detailed derivation, see [](#Supplementary-Information-4). Note that this approach can naturally be reduced to different "coarse-grainings" of the system, by pooling network nodes with similar functional properties. In case of resting state fMRI data, this corresponds to pooling network nodes into functional parcels. Drawing upon concepts such as the center manifold theorem {cite:p}`https://doi.org/10.1137/0520069`, it is posited that rapid, fine-grained dynamics at lower descriptive levels converge to lower-dimensional manifolds, upon which the system evolves via slower processes at coarser scales. It has been previously argued {cite:p}`https://doi.org/10.1162/netn_a_00343` that the temporal and spatial scales of fMRI data happen to align relatively well with the characteristic scales corresponding to meaningful large-scale "coarse-grainings" of brain dynamics.

:::{note}
The covariance and precision matrices can often be poor estimates of the true population covariance and precision, especially when the number of time points is low. We recommend using a regularized covariance matrix estimation method, such as the Ledoit-Wolf estimator {cite:p}`doi:10.1016/S0047-259X(03)00096-4`.
:::

Having estimates of the weight matrix $J$ of the attractor network, we can now rely on the deterministic and stochastic versions of the inference procedure (eq. \ref{fep-update}) in order to investigate this system. Running the deterministic update to a uniformly drawn sample of initial states, we can identify all attractor states of the network. The stochastic update, on the other hand, can be used to sample from the posterior distribution of the activity states, and thus serves as a generative computational model of the brain dynamics.

> todo: stochastic and deterministic variants
### Testable predictions of the theoretical framework

#### Self-orthogonalization as a signature of free energy attractor networks
So far, we have only discussed free energy minimization in terms of the activity of the nodes of the network. However, free energy minimization also gives rise to a specific learning rule for the couplings $J$ of the network. This learning rule is a specific local, incremental, contrastive (predictive coding-based) plasticity rule to adjust connection strengths:

:::{math}
:label: learning-rule
\Delta J_{ij} \propto \underbrace{\sigma_i \sigma_j}_{\textit{observed correlation (Hebbian)}} - \underbrace{ L(b_i + \sum_{k\neq i} J_{ik}\,\sigma_k ) \sigma_j}_{\textit{predicted correlation (anti-Hebbian)}}
::: 

 A detailed derivation of the learning dynamics can be found in {cite:p}`10.48550/ARXIV.2505.22749` and [](#Supplementary-Information-2). 
In the present work, we do not implement this learning rule in our computational model, as the coupling weights $J$ are reconstructed directly from the empirical fMRI activation timeseries data.

However, this specific learning rule has an important implication for the free-energy minimizing attractor states of the network: it will naturally drive the attractor states towards (approximate) orthogonality during learning. For a mathematical motivation of the mechanisms underlying this important property, termed self-orthogonalization, see {cite:p}`10.48550/ARXIV.2505.22749` and [](#Supplementary-Information-3).
Self-orthogonalization is far from being a generic property of all attractor networks and it is not a consequence of the above formulated inference dynamics. It has, however, remarkable implications for the efficiency of the network and the robustness of its representations. Attractor networks with orthogonal attractor states, often termed the Kanter-Sompolinsky projector neural network {cite:p}`https://doi.org/10.1103/PhysRevA.35.380`, are the computationally most efficient varieties of general attractor networks, with maximal memory capacity and perfect memory recall (without error). Importantly, in Kanter-Sompolinsky projector networks, **the eigenvectors of the coupling matrix and the attractors become equivalent**, providing an important signature for detecting such networks in empirical data. 

Here we reconstruct attractor networks from functional connectivity data - hereinafter referred to as fcANNs - without relying on the learning rule of the FEP-ANN framework (eq. \ref{learning-rule}) which imposes orthogonality on the attractors.
Thus, if in these emprically reconstructed fcANNs, an alignment between the eigenvectors of the coupling matrix and the attractors is observed, it can be considered as a strong evidence that the studied system approximates a Kanter-Sompolinsky projector network.

As FEP-ANNs - together with some other, related models, e.g. "dreaming neural networks" {cite:p}`https://doi.org/10.1038/304158a0; 10.1109/ICPR.1994.576884; 10.1088/0305-4470/24/21/026; https://doi.org/10.1016/j.neunet.2019.01.006` provide a plausible and mathematicaly rigorous mechanistic model for the emergence of architectures apporxiamting Kanter-Sompolinsky projector network through local learning rules, this alignment between the eigenvectors of the coupling matrix and the attractors can be considered as a signature of an underlying FEP-ANN.

We will directly test this prediction in the present study, by investigating the orthogonality of the attractor states of the fcANN model reconstructed from empirical fMRI data. 

:::{note}
From the perspective of Bayesian (active) inference, orthogonal attractor states constitute an orthogonal basis set of priors, allowing efficient generalization within the spanned subspace during the stochastic MCMC inference process (see {cite:p}`10.48550/ARXIV.2505.22749` for details).
:::

#### Convergence, multistability, biological plausibility and prediction capacity

Next to the prediction of (approximate) attractor orthogonality, our framework provides further testable predictions. If the functional connectome can indeed be considered as a proxy for the coupling weights $J$ of an underlying attractor network, we can expect that (i) the reconstructed fcANN model will exhibit multiple stable attractor states, with large basins and biologically plausible spatial patterns, (ii) the relaxation dynamics of the reconstructed model will display fast convergence to attractor states and (iii) the stochastic relaxation dynamics yield and efficient generative model of the empirical resting state brain dynamics as well as perturbations thereof caused either by external inputs (stimulations and tasks) or pathologies.

#### Null models

The above theoretical predictions will be directly tested in the present study with appropriate null models. 
First, we show that fcANN-derived brain attractor states display a high-level of similarity to the eigenvectors of the functional connectome matrix, in contrast to null models with permuted coupling weights (preserving symmetry, but destroying topological structure, e.g. clusteredness).
Second we qualitatively demonstrate that attractor states obtained with different inverse temperature parameters $\beta$ and diffrerent noise levels exhibit large basins and that these attractor states exhibit spatial patterns consistent with known large-scale brain systems. 
Third, we contrast the convergence properties of the deterministic relaxation dynamics of fcANNs against null models with symmetry-preserving permuted coupling weights. 
Finally, we demonstrate in multiple scenarios that the stochastic relaxation dynamics of the fcANN model yields an efficient generative model of the empirical resting state brain dynamics. When reconstructing the temporal dynamics of resting state brain activity, we employ the multivariate normal distribution as a null model, parametrized with the functional connectome's covariance matrix, which we consider as the implicit model underlying many conventional analyses of fMRI connectivity.
We extend this null modelling strategy with a null model based on spatially autocorrelation-preserving randomization of the real data, benchmarking the ability of the fcANN model to predict large-scale brain dynamics over and beyond the basline determined by spatial autocorrelation structure.


::::{list-table} Null models
:header-rows: 1
:name: tab-null-models
* - Short name
  - Brief description
* - 1. Timeseries phase-randomization
  - Phase randomize timeseries data, independnetly for each reagion, recaluclate connectivity matrix.
* - 2. Symmetry-preserving connectome permutation
  - Shuffle off-diagonal entries of `J` while keeping `J` symmetric; destroys topological structure (e.g., clusteredness) while preserving weight symmetry.
* - 3. Covariance-matched Gaussian
  - Draw time-frames from a multivariate normal with covariance equal to the functional connectome's covariance; matches spatial covariance but lacks nonlinear dynamics and temporal dependencies (temporal autocorrelation).
* - 4. Temporal order permutation
  - Randomly permute timeframe order within runs to destroy temporal autocorrelation while preserving framewise distributions; used for flow analyses.
* - 5. Condition shuffling
  - Permute condition labels, either within participant (e.g., pain vs. rest; up- vs. down-regulation) or between participant (shuffle patient vs. control labels).
::::



::::{list-table} Research questions, methodological approaches, and null models
:header-rows: 1
:name: research-questions-table
* - **Research Question**
  - **Methodological Approach**
  - **Null Model**
* - Is the brain an approximate K-S projector ANN (FEP-ANN prediction)?
  - Compare eigenvectors of coupling matrix with attractor states
  - 1, 2
* - Do fcANNs display biological plausible attractor states?
  - Identify attractor states, report basin sizes and assess spatial patterns with different inverse temperature parameters and noise levels
  - qualitative
* - Is the functional connectome well suited to function as an attractor network?
  - Measure iterations to convergence in deterministic relaxation
  - 2
* - What are the optimal parameters for the fcANN model?
  - We fix $\beta=0.04$ (4 attractor states) for simplicity. We perform a rough optimization of the noise parameter $\sigma$ in stochastic relaxation to match empirical data distribution.
  - 1, 3
* - Can fcHNNs reproduce the characteristics of resting state brain activity?
  - Compare stochastic dynamics (state occupancy, distribution, temporal trajectory) with empirical resting state data
  - 3, 4
* - Can resting state fMRI-based fcHNNs predict large-scale brain dynamics elicited by tasks or stimuli?
  - Contrast pain vs. rest dynamics with data generated by fcHNNs and pain-associated control signal
  - 5
* - Can resting state fMRI-based fcHNNs predict altered brain dynamics in clinical populations?
  - Contrast autism spectrum disorder patients vs. typically developing control particiapnts' observed brain dynamics with data generated by fcHNNs initialized with the respecive functional connectomes
  - 5
::::


## Results

### Functional connectivity-based attractor networks (fcANNs) as a model of brain dynamics

First, we investigated the functional connectome as an attractor network in a sample of n=41 healthy young participants ([study 1](tab-samples), see Methods [](tab-samples) for details). We estimated interregional activity flow {cite:p}`cole2016activity; ito2017cognitive` as the study-level average of regularized partial correlations among the resting state fMRI timeseries of m = 122 functional parcels of the BASC brain atlas (see [Methods](#Functional-connectome) for details). We then used the standardized functional connectome as the $w_{ij}$  weights of a fully connected recurrent fcANN model, see [Methods](#connectome-based-hopfield-networks)). 

Next, we applied the deterministic relaxation procedure to a sufficiently large number of random initializations (n=100000) to obtain all possible attractor states of the fcANN in study 1 ({numref}`attractors`A).
Consistent with theoretical expectations, we observed that increasing the inverse temperature parameter $\beta$ led to an increasing number of attractor states ({numref}`attractors`E, left, {numref}`Supplementary Figure %s <si_att_state_emergence_over_beta>`), appearing in symmetric pairs (i.e. $a_i^{(1)} = -a_i^{(2)}$, see {numref}`attractors`G).

To test research question Q1, we matched the eigenvectors of the coupling matrix to the attractor state with which they exhibit the highest correlation.
The eigenvector-attractor correlations were compared to a null model based on permuted coupling weights (preserving symmetry, but destroying topology). We found that the eigenvectors of the coupling matrix and the attractor states are significantly stronger  aligned, than those in the null model, providing evidence for the existence of a Kanter-Sompolinsky projector network ({numref}`attractors`A). With the unpermuted fcHNN, eigenvectors with the highest eigenvalues tended to be aligned with the attractor states with the highest fractional occupancy. No such pattern was observed in the null model ({numref}`attractors`B). Further evidence for the functional connectome's close resemblance to a Kanter-Sompolinsky projector network is provided by the orthogonality of the attractor states to each other ({numref}`attractors`C) and additional analyses reported in {numref}`Supplementary Figure %s <si_orthogonality>`.

Next, to support the visualization of further analyses, we constructed a simplified, 2-dimensional visual representation of fcANN dynamics, which we apply throughout the reminaing of the manuscipt as a high-level visual summary.
This 2-dimensional visulaization, referred to as the *fcANN projection*, is simply based on the first two principal components (PCs) of the states sampled from the stochastic relaxation procedure ({numref}`attractors`D-F and {numref}`Supplementary Figure %s <si_fcann_projection>`). On this simplified visualization, we observed a clear separation of the attractor states ({numref}`attractors`D), with the two symmetric pairs of attractor states located at the extremes of the first and second PC. 
To map the attractors' basins on the space spanned by the first two PCs ({numref}`attractors`C), we obtained the attractor state of each point visited during the stochastic relaxation and fit a multinomial logistic regression model to predict the attractor state from the first two PCs. 
The resulting model accurately predicted attractor states of arbitrary brain activity patterns, achieving a cross-validated accuracy of 96.5% (permutation-based p<0.001).
The attractor basins were visualized by using the decision boundaries obtained from this model ({numref}`Supplementary Figure %s <si_fcann_projection>` and black lines in {numref}`attractors`G-H). In the rest of the manuscript, we use this 2-dimensional fcANN projection depicted on ({numref}`attractors`D-H) as a simplified visual representation of brain dynamics, and use it as a basis for all subsequent analyses in this work.

Panel D on {numref}`attractors` uses the fcANN projection to visualize the conventional Hopfield relaxation procedure. It depicts the trajectory of individual activation maps (sampled randomly from the timeseries data in Study 1) until converging to one of the four attractor states. 
Panel E shows that the system does not converge to an attractor state anymore with the stochastic relaxation procedure. The resulting path is still influenced by the attractor states' "gravitational pull", resulting in a multistable dynamics that resembles the empirical timeseries data (example data on panel F).

:::{figure} figures/rsfmri_validity.png
:name: attractors
**Attractor states and state-space dynamics of connectome-based Hopfield networks** <br/><br/>
**A** Leading eigenvectors of the empirical coupling matrix `J` (left of each pair) closely match the most correlated fcANN attractor states (right of each pair). Attractors were obtained by deterministic Hopfield relaxation from random initial states and collapsing sign‑duplicates; eigenvectors were computed from the symmetrized `J` and sign‑flipped to maximize correlation with their matched attractor. Numbers under each pair report Pearson correlation and a permutation p‑value from a symmetry‑preserving null in which the off‑diagonal entries of `J` are shuffled and attractors are recomputed for each permutation. For the comprehensive results of the eigenvector-attractor alignment analysis, see {numref}`Supplementary Figure %s <si_orthogonality>`.
**B** Example matches from a single permutation of the permutation‑based null distribution. For each symmetry‑preserving permutation of `J`, we recomputed the corresponding eigenvectors and attractors and re‑matched them. The maps are visibly mismatched and correlations are near zero, illustrating the null against which the empirical correlations in panel A are evaluated.
**C** Attractor orthogonality. Pairwise angles between collapsed attractor states concentrate around 90°, consistent with predictions of free‑energy minimizing (Kanter–Sompolinsky‑like) networks (Note however, that in high dimensional spaces, random vectors would also tend to be approximately orthogonal). Angles were computed as θ=arccos((a·b)/(|a||b|)) after z‑scoring patterns and collapsing sign‑duplicates; schematic panels illustrate orthogonalization in theory (left) and in the empirical fcANN (right).
**D** The fcANN of study 1 seeded with real activation maps (gray dots) of an example participant. All activation maps converge to one of the four attractor states during the relaxation procedure (without noise) and the system reaches equilibrium. Trajectories are colored by attractor state.
**E** Illustration of the stochastic relaxation procedure in the same fcANN model, seeded from a single starting point (activation pattern). The system does not converge to an attractor state but instead traverses the state space in a way restricted by the topology of the connectome and the "gravitational pull" of the attractor states. The shade of the trajectory changes with increasing number of iterations. The trajectory is smoothed with a moving average over 10 iterations for visualization purposes.
**F** Real resting state fMRI data of an example participant from study 1, plotted on the fcANN projection. The shade of the trajectory changes with an increasing number of iterations. The trajectory is smoothed with a moving average over 10 iterations for visualization purposes.
**G** Consistent with theoretical expectations, we observed that increasing the temperature parameter $\beta$ led to an increasing number of attractor states, emerging in a nested fashion (i.e. the basin of a new attractor state is fully contained within the basin of a previous one). When contrasting the functional connectome-based HNN with a null model based on symmetry-retaining permuted variations of the connectome, we found that the topology of the original (unpermuted) functional brain connectome makes it significantly better suited to function as an attractor network; than the permuted null model. Table contains the meadian number of iterations until convergence for the original and permuted connectomes for different temperature parameters $\beta$ and the corresponding p-value.
**H** We optimized the noise parameter $\sigma$ of the stochastic relaxation procedure for 8 different $\sigma$ values over a logarithmic range between $\sigma=0.1$ and $1$ so that the similarity (the timeframes distribution over the attractor basins) is maximized between the empirical data and the fcANN-generated data. We used to null models to assess the significance of similarity: one based on multivariate normal data, with the covariance matrix set to the functional connectome's covariance matrix, and one based on spatial phase-randomization. P-values are given in the table at the bottom of the panel. The fcANN only reached multistability with $\sigma>0.19$, and it provided the most accurate reconstruction of the real data with $\sigma=0.37$ (p=0.007, and p<0.001 for the two null models).
:::

In study 1, we have investigated the convergence process of the functional connectivity-based HNN and contrasted it with a null model based on permuted variations of the connectome (while retaining the symmetry of the matrix). This null model preserves the sparseness and the degree distribution of the connectome, but destroys its topological structure (e.g. clusteredness). We found that the topology of the original (unpermuted) functional brain connectome makes it significantly better suited to function as an attractor network; than the permuted null model.
While the original connectome based HNN converged to an attractor state in less than 150 iterations in more than 50% of the cases, the null model did not reach convergence in more than 98% of the cases, even after 10000 iterations ({numref}`attractors`G, {numref}`Supplementary Figure %s <si_convergence>`). This result was robustly observed, independent of the inverse temperature parameter beta.
We set the temperature parameter for the rest of the paper to a value providing the fastest convergence ($\beta=0.4$, median iterations: 107), resulting in 4 distinct attractor states. The primary motivation for selecting $\beta=0.4$ was to reduce computational burden for further analyses. However, as with increasing temperature, attractor states emerge in a nested fashion (i.e. the basin of a new attractor state is fully contained within the basin of a previous one), we expect that the results of the following analyses would be, although more detailed, but qualitatively similar with higher $\beta$ values.

We optimized the noise parameter $\sigma$ of the stochastic relaxation procedure for 8 different $\sigma$ values over a logarithmic range between $\sigma=0.1$ and $1$ so that the similarity (the timeframes distribution over the attractor basins) is maximized between the empirical data and the fcANN-generated data. We contrasted this similarity with two null-models ({numref}`attractors`H). First we generated null-data as random draws from a multivariate normal distribution with co-variance matrix set to the functional connectome's covariance matrix (partial correlation-based connectivity estimates). This serves as a baseline for generating data that optimally matches the empirical data in terms of distribution and spatial autocorrelation, as based on information on the underlying co-variance structure (and given Gaussian assumptions), but without any mechanistic model of the generative process, e.g. without modelling any non-linear and non-Gaussian effects and temporal autocorrelations stemming from recurrent activity flow). We found that The fcANN only reached multistability with $\sigma>0.19$, and it provided more accurate reconstruction of the real data than the null model for $\sigma=0.37$ and $\sigma=0.52$ (p=0.007 and 0.015, $\chi^2$ dissimilarity: 11.16 and 21.57, respectively). 
With our second null model, we investigated whether the fcANN-reconstructed data is more similar to the empirical data than synthetic data with identical spatial autocorrelation structure (generated by spatial phase randomization of the original volumes, see [Methods](#evaluation-resting-state-dynamics)). 
We found that the fcANNs significantly outperform this null model with all investigated $\sigma$ values if $\sigma \geq 0.37$ (p<0.001 for all)
Based on this coarse optimization procedure, we set $\sigma=0.37$ for all subsequent analyses. 

### Reconstruction of resting state brain dynamics

The spatial patterns of the obtained attractor states exhibit high neuroscientific relevance and closely resemble previously described large-scale brain systems. ({numref}`rest-validity`A).
For simplicity, in the remaining of the manuscript, we restrict our analyses to the first 4 attractors, as the corresponding dynamics can be effectively visualized on the 2-dimensional fcANN projection.
The spatial patterns assocated with first pair of attractors (mapped on PC1, horizontal axis) show a close correspondence to two commonly described complementary brain systems, that have been previously found in anatomical, functional, developmental, and evolutionary hierarchies, as well as gene expression, metabolism, and blood flow, (see {cite}`sydnor2021neurodevelopment` for a review), an reported under various names, like intrinsic and extrinsic systems {cite:p}`golland2008data`, Visual-Sensorimotor-Auditory and Parieto-Temporo-Frontal "rings" {cite:p}`cioli2014differences`, "primary" brain states {cite:p}`chen2018human`, unimodal-to-transmodal principal gradient {cite:p}`margulies2016situating; huntenburg2018large` or sensorimotor-association axis {cite:p}`sydnor2021neurodevelopment`. 
A common interpretation of these two patterns is that they represent (i) an "extrinsic" system linked to the immediate sensory environment and (ii) an "intrinsic" system for higher-level internal context, commonly referred to as the *default mode network* {cite:p}`raichle2001default`.
The other pair of attractors spans an orthogonal axis, and resemble to patterns commonly associated with perception–action cycles {cite:p}`fuster2004upper`, and described as a gradient across sensory-motor modalities {cite:p}`huntenburg2018large`, recruiting regions associated with active (e.g. motor cortices) and perceptual inference (e.g visual areas).

:::{figure} figures/face_validity.png 
:name: rest-validity
**Connectome-based Hopfield networks reconstruct characteristics of real resting state brain activity.**<br/><br/>
**A** The four attractor states of the fcANN model from study 1 reflect brain activation 
patterns with high neuroscientific relevance, representing sub-systems previously associated with "internal context"
(blue), "external context" (yellow), "action" (red) and "perception" (green)
{cite:p}`golland2008data; cioli2014differences; chen2018human; fuster2004upper; margulies2016situating`.
**B** The attractor states show excellent replicability in two external datasets (study 2 and 3, mean correlation 0.93). 
**C** The fcANN projection (first two PCs of the fcANN state space) explains significantly more variance (p<0.0001) in the real 
resting state fMRI data than principal components derived from the real resting state data itself and generalizes 
better (p<0.0001) to out-of-sample data (study 2). Error bars denote 99% bootstrapped confidence intervals.
**D** The fcANN analysis reliably predicts various characteristics of real resting state fMRI data, such as the fraction of time spent on the basis of the four attractors (first column, p=0.007, contrasted to the multivariate normal null model), the distribution of the data on the fcANN-projection (second column, p<0.001, contrasted to the multivariate normal null model) and the temporal autocorrelation structure of the real data (third column, p<0.001, contrasted to a null model based on temporally permuted data). This analysis was based on flow maps of the mean trajectories (i.e. the characteristic timeframe-to-timeframe transition direction) in fcANN-generated data, as compared to a shuffled null model representing zero temporal autocorrelation. For more details, see [Methods](#evaluation-resting-state-dynamics). Furthermore, (rightmost column), stochastic fcANNs are capable of self-reconstruction: the timeseries resulting from the stochastic relaxation procedure mirror the co-variance structure of the functional connectome the fcANN model was initialized with. While the self-reconstruction property in itself does not strengthen the face validity of the approach (no unknown information is reconstructed), it is a strong indicator of the model's construct validity; i.e. that systems that behave like the proposed model inevitably "leak" their weights into the activity time series.
:::

The discovered attractor states demonstrate high replicability (mean Pearson's correlation 0.93) across the discovery dataset (study 1) and two independent replication datasets ([study 2 and 3](tab-samples), {numref}`rest-validity`C). Moreover, they were found to be significantly more robust to noise added to the connectome than nodal strengths scores (used as a reference, see {numref}`Supplementary Figure %s <si_noise_robustness_weights>` for details).

Further analysis in study 1 showed that connectome-based attractor models accurately reconstructed multiple characteristics of true resting-state data.
First, the two axes (first two PCs) of the fcANN projection accounted for a substantial amount of variance in the real resting-state fMRI data in study 1 (mean $R^2=0.399$) and generalized well to out-of-sample data (study 2, mean $R^2=0.396$)  ({numref}`rest-validity`E). The explained variance of the fcANN projection significantly exceeded that of the first two PCs derived directly from the real resting-state fMRI data itself ($R^2=0.37$ and $0.364$ for in- and out-of-sample analyses).

Second, during stochastic relaxation, the fcANN model was found to spend approximately three-quarters of the time on the basis of the first two attractor states and one-quarter on the basis of the second pair of attractor states (approximately equally distributed between pairs). We observed similar temporal occupancies in the real data {numref}`rest-validity`D left column), statistically significant with two different null models ({numref}`Supplementary Figure %s <si_state_occupancy_null_models>`). Fine-grained details of the bimodal distribution observed in the real resting-state fMRI data were also convincingly reproduced by the fcANN model ({numref}`rest-validity`F and {numref}`attractors`D, second column).

Third, not only spatial activity patterns but also timeseries generated by the fcANN are similar to empirical timeseries data. Next to the visual similarity shown on {numref}`attractors`E and F, we observed a statistically significant similarity between the average trajectories of fcANN-generated and real timeseries "flow" (i.e. the characteristic timeframe-to-timeframe transition direction), as compared to null-models of zero temporal autocorrelation (randomized timeframe order, {numref}`rest-validity`D, third column [Methods](#evaluation-resting-state-dynamics) for analysis details). 

Finally, fcANNs were found to generate signal that preserves the covariance structure of the real functional connectome, indicating that dynamic systems of this type (including the brain) inevitably "leak" their underlying structure into the activity time series, strengthening the construct validity of our approach ({numref}`rest-validity`D).

### An explanatory framework for task-based brain activity

Next to reproducing various characteristics of spontaneous brain dynamics, fcANNs can also be used to model responses to various perturbations. We obtained task-based fMRI data from a study by {cite:t}`woo2015distinct` ([study 4](tab-samples), n=33, see {numref}`rest-validity`), investigating the neural correlates of pain and its self-regulation. 

We found that activity changes due to pain (taking into account hemodynamics, see [Methods](#evaluation-task-based-dynamics)) were characterized on the fcANN projection by a shift towards the attractor state of action/execution (permutation test for mean projection difference by randomly swapping conditions, p<0.001, {numref}`task-validity`A, left). Energies, as defined by the fcANN, were also significantly different between the two conditions (p<0.001), with higher energies during pain stimulation.

When participants were instructed to up- or downregulate their pain sensation (resulting in increased and decreased pain reports and differential brain activity in the nucleus accumbens, NAc (see {cite}`woo2015distinct` for details), we observed further changes of the location of momentary brain activity patterns on the fcANN projection (p<0.001, {numref}`task-validity`A, right), with downregulation pulling brain dynamics towards the attractor state of internal context and perception. Interestingly, self-regulation did not trigger significant energy changes (p=0.36). 

:::{figure} figures/task_validity.png
:name: task-validity
**Empirical Hopfield-networks reconstruct real task-based brain activity.** <br></br>
**A** Functional MRI time-frames during pain stimulation from [study 4](tab-samples) (second fcANN projection plot)
and self-regulation (third and fourth) are distributed differently on the fcANN projection than brain states 
during rest (first projection, permutation test, p<0.001 for all). Energies, as defined by the Hopfield model, are also
significantly different between rest and the pain conditions (permutation test, p<0.001), with higher energies during 
pain stimulation. Triangles denote participant-level mean activations in the various blocks (corrected for 
hemodynamics). Small circle plots show the directions of the change for each individual (points) as well as the mean direction
across participants (arrow), as compared to the reference state (downregulation for the last circle plot, rest for all 
other circle plots).
**B** Flow-analysis (difference in the average timeframe-to-timeframe transition direction) reveals a non-linear difference in brain dynamics during pain and rest (left). When introducing weak pain-related signal in the fcANN model during stochastic relaxation, it accurately reproduces these non-linear flow differences (right).
**C** Simulating activity in the Nucleus Accumbens (NAc) (the region showing significant activity differences in {cite}`woo2015distinct`) reconstructs the observed non-linear flow difference between up- and downregulation (left).
**D** Schematic representation of brain dynamics during pain and its up- and downregulation, visualized on the fcANN  projection. In the proposed framework, pain does not simply elicit a direct response in certain regions, but instead, shifts spontaneous brain dynamics towards the "action" attractor, converging to a characteristic "ghost attractor" of pain. Down-regulation by NAc activation exerts force towards the attractor of internal context, leading to the brain less frequent "visiting" pain-associated states.
**E** Visualizing meta-analytic activation maps (see {numref}`Supplementary Table %s <si-tab-neurosynth>` for details) on the fcANN projection captures intimate relations between the corresponding tasks and **F** serves as a basis for a fcANN-based theoretical interpretative framework for spontaneous and task-based brain dynamics. In the proposed framework, task-based activity is not a mere response to external stimuli in certain brain locations but a perturbation of the brain's characteristic dynamic trajectories, constrained by the underlying functional connectivity. From this perspective, "activity maps" from conventional task-based fMRI analyses capture time-averaged differences in these whole brain dynamics. 
:::

Next, we conducted a "flow analysis" on the fcANN projection, quantifying how the average timeframe-to-timeframe transition direction differs on the fcANN projection between conditions (see [Methods](#evaluation-task-based-dynamics)).
This analysis unveiled that during pain ({numref}`task-validity`B, left side), brain activity tends to gravitate towards a distinct point on the projection on the boundary the basins of the internal and action attractors, which we term the "ghost attractor" of pain (similar to {cite}`vohryzek2020ghost`). In case of downregulation (as compared to upregulation), brain activity is pulled away from the pain-related "ghost attractor" ({numref}`task-validity`C, left side), towards the attractor of internal context.

Our fcANN was able to accurately reconstruct these non-linear dynamics by adding a small amount of realistic "control signal" (similarly to network control theory, see e.g. {cite}`liu2011controllability` and {cite}`gu2015controllability`). To simulate the alterations in brain dynamics during pain stimulation, we acquired a meta-analytic pain activation map {cite:p}`zunhammer2021meta` (n=603) and incorporated it as a control signal added to each iteration of the stochastic relaxation procedure. The ghost attractor found in the empirical data was present across a relatively wide range of signal-to-noise (SNR) values ({numref}`Supplementary Figure %s <si_pain_ghost_attractor_sim>`). Results with SNR=0.005 are presented on {numref}`task-validity`B, right side (Pearson's r = 0.46, p=0.005 based on randomizing conditions on a per-participant basis).

The same model was also able to reconstruct the observed non-linear differences in brain dynamics between the up- and downregulation conditions (Pearson's r = 0.62, p=0.023) without any further optimization (SNR=0.005, 
{numref}`task-validity`C, right side). The only change we made to the model was the addition (downregulation) or 
subtraction (upregulation) of control signal in the NAc (the region in which {cite:p}`woo2015distinct` observed significant changes between up- and downregulation), introducing a signal difference of $\Delta$SNR=0.005 (the same value we found optimal in the pain-analysis). Results were reproducible with lower NAc SNRs, too ({numref}`Supplementary Figure %s <si_downreg_trajectory_sim>`).

To provide a comprehensive picture on how tasks and stimuli other than pain map onto the fcANN projection, we obtained various task-based meta-analytic activation maps from Neurosynth (see [Methods](#evaluation-task-based-dynamics)) and plotted them on the fcANN projection ({numref}`task-validity`E). This analysis reinforced and extended our interpretation of the four investigated attractor states and shed more light on how various functions are mapped on the axes of internal vs. external context and perception vs. action.
In the coordinate system of the fcANN projection, visual processing is labeled "external-perception", sensory-motor processes fall into the "external-active" domain, language, verbal cognition and working memory belongs to the "internal-active" region and long-term memory as well as social and autobiographic schemata fall into the "internal-perception" regime ({numref}`task-validity`F).

### Clinical relevance

We obtained data from n=172 autism spectrum disorder (ASD) and typically developing control (TDC) individuals, acquired at the New York University Langone Medical Center, New York, NY, USA (NYU) and generously shared in the Autism Brain Imaging Data Exchange dataset ([study 7](tab-samples): ABIDE, {cite:p}`di2014autism`.
After excluding high-motion cases (with the same approach as in Study 1-4, see [Methods](#clinical-data)), we visualized the distribution of time-frames on the fcANN-projection separately for the ASD and TDC groups ({numref}`clinical-validity`A).
First, we assigned all timeframes to one of the 4 attractor states with the fcANN from study 1 and found several significant differences in the mean activity on the attractor basins (see [Methods](#clinical-data)) of the ASD group as compared to the respective controls ({numref}`clinical-validity`B).
Strongest differences were found on the "action-perception" axis ({numref}`tab-clinical-results`), with increased activity of the sensory-motor and middle cingular cortices during "action-execution" related states and increased visual and decreased sensory and auditory activity during "perception" states, likely reflecting the widely acknowledged, yet poorly understood, perceptual atypicalities in ASD {cite:p}`hadad2019perception`. ASD related changes in the internal-external axis were characterized by more involvement of the posterior cingulate, the precuneus, the nucleus accumbens, the dorsolateral prefrontal cortex (dlPFC), the cerebellum (Crus II, lobule VII) and inferior temporal regions during activity of the internalizing subsystem ({numref}`tab-clinical-results`). While similar, default mode network (DMN)-related changes have often been attributed to an atypical integration of information about the "self" and the "other" {cite:p}`padmanabhan2017default`, a more detailed fcANN-analysis may help to further disentangle the specific nature of these changes.

:::{figure} figures/state_analysis.png
:name: clinical-validity
**Connectome-based Hopfield analysis of autism spectrum disorder.** <br></br>
**A** The distribution of time-frames on the fcANN-projection separately for ASD patients and typically developing control (TDC) participants. <br></br>
**B** We quantified attractor state activations in the Autism Brain Imaging Data Exchange datasets ([study 7](tab-samples)) as the 
individual-level mean activation of all time-frames belonging to the same attractor state. This analysis captured alterations similar to those previously associated to ASD-related perceptual atypicalities (visual, auditory and somatosensory cortices) as well as atypical integration of information about the "self" and the "other" (default mode network regions). All results are corrected for multiple comparisons across brain regions and attractor states (122*4 comparisons) with Bonferroni-correction. See {numref}`tab-clinical-results` and {numref}`Supplementary Figure %s <si_clinical_results_table>` for detailed results. <br></br>
**C** The comparison of data generated by fcANNs initialized with ASD and TDC connectomes, respectively, revealed a characteristic pattern of differences in the system's dynamics, with increased pull towards (and potentially a higher separation between) the action and perception attractors and a lower tendency of trajectories going towards the internal and external attractors. <br></br>
***Abbreviations**: MCC: middle cingulate cortex, ACC: anterior cingulate cortex, pg: perigenual, PFC: prefrontal cortex, dm: dorsomedial, dl: dorsolateral, STG: superior temporal gyrus, ITG: inferior temporal gyrus, Caud/Acc: caudate-accumbens,  SM: sensorimotor, V1: primary visual, A1: primary auditory, SMA: supplementary motor cortex, ASD: autism spectrum disorder, TDC: typically developing control.*
:::

:::{list-table} **The top ten largest changes in average attractor-state activity between autistic and control individuals.**  Mean attractor-state activity changes are presented in the order of their absolute effect size. All p-values are based on permutation tests (shuffling the group assignment) and corrected for multiple comparisons (via Bonferroni's correction). For a comprehensive list of significant findings, see {numref}`Supplementary Figure %s <si_clinical_results_table>.
:header-rows: 1
:name: tab-clinical-results
 * - region
   - attractor
   - effect size
   - p-value
 * - primary auditory cortex
   - perception
   - -0.126
   - <0.0001
 * - middle cingulate cortex
   - action
   - 0.109
   - <0.0001
 * - cerebellum lobule VIIb (medial part  )
   - internal context
   - 0.104
   - <0.0001
 * - mediolateral sensorimotor cortex
   - perception
   - -0.099
   - 0.00976
 * - precuneus
   - action
   - 0.098
   - <0.0001
 * - middle superior temporal gyrus
   - perception
   - -0.098
   - <0.0001
 * - frontal eye field
   - perception
   - -0.095
   - <0.0001
 * - dorsolateral sensorimotor cortex
   - perception
   - -0.094
   - 0.00976
 * - posterior cingulate cortex
   - action
   - 0.092
   - <0.0001
 * - dorsolateral prefrontal cortex
   - external context
   - -0.092
   - <0.0001
:::

Thus, we contrasted the characteristic trajectories derived from the fcANN models of the two groups (initialized with the group-level functional connectomes). Our fcANN-based flow analysis predicted that in ASD, there is an increased likelihood of states returning towards the middle (more noisy states) from the internal-external axis and an increased likelihood of states transitioning towards the extremes of the action-perception axis ({numref}`clinical-validity`C). We observed a highly similar pattern in the real data (Pearson's correlation: 0.66), statistically significant after permutation testing (shuffling the group assignment, p=0.009).

## Discussion

In this study, we have introduced and validated a simple and robust network-level generative computational framework that elucidates how activity propagation within the functional connectome orchestrates large-scale brain dynamics, leading to the spontaneous emergence of brain states, smooth gradients among them, and characteristic dynamic responses to perturbations.

The construct validity of our model is rooted in the activity flow principle, first introduced by {cite:t}`cole2016activity`. The activity flow principle states that activity in a brain region can be predicted by a weighted combination of the activity of all other regions, where the weights are set to the functional connectivity of those regions to the held-out region. This principle has been shown to hold across a wide range of experimental and clinical conditions {cite:p}`cole2016activity; ito2017cognitive; mill2022network; hearne2021activity; chen2018human`.
The proposed approach is based on the intuition that the repeated, iterative application of the activity flow equation exhibits close analogies with a type of recurrent artificial neural networks, known as Hopfield networks {cite:p}`hopfield1982neural`.

Hopfield networks have been widely acknowledged for their relevance for brain function, including the ability to store and recall memories {cite:p}`hopfield1982neural`, self-repair {cite:p}`murre2003selfreparing`,
a staggering robustness to noisy or corrupted inputs {cite:p}`hertz1991introduction` (see also {numref}`Supplementary Figure %s <si_noise_robustness_weights>`) and the ability to produce multistable dynamics organized by the "gravitational pull" of a finite number of attractor states {cite:p}`khona2022attractor`. While many of such properties of Hopfield networks have previously been proposed as a model for micro-scale neural systems (see {cite}`khona2022attractor` for a review), the proposed link between macro-scale activity propagation and Hopfield networks allows transferring the vast body of knowledge on Hopfield networks to the study of large-scale brain dynamics.

Integrating Cole's activity flow principle with the HNN architecture mandates the initiation of network weights with functional connectivity values, specifically partial correlations as suggested by {cite:t}`cole2016activity`.
Considering the functional connectome as weights of a neural network distinguishes our methodology from conventional biophysical and phenomenological computational modeling strategies, which usually rely on the structural connectome to model polysynaptic connectivity {cite:p}`cabral2017functional; deco2012anatomy; golos2015multistability; hansen2015functional`. Given the challenges of accurately modelling the structure-function coupling in the brain {cite:p}`seguin2023brain`, such models are currently limited in terms of reconstruction accuracy, hindering translational applications.
By working with direct, functional MRI-based activity flow estimates, fcANNs bypass the challenge of modelling the structural-functional coupling and are able to provide a more accurate representation of the brain's dynamic activity propagation (although at the cost of losing the ability to provide biophysical details on the underlying mechanisms).
Another advantage of the proposed model is its simplicity. While many conventional computational models rely on the optimization of a high number of free parameters, the basic form of the fcANN approach comprises solely two, easily interpretable  "hyperparameters" (temperature and noise) and yields notably consistent outcomes across an extensive range of these parameters ({numref}`Supplementary Figure %s <si_expl_variance_energy>`, {numref}`%s <si_att_state_emergence_over_beta>`, {numref}`%s <si_state_occupancy_null_models>`, {numref}`%s <si_pain_ghost_attractor_sim>`, {numref}`%s <si_downreg_trajectory_sim>`). To underscore the potency of this simplicity and stability, in the present work, we avoided any unnecessary parameter optimization, leaving a negligible chance of overfitting. It is likely, however, that extensive parameter optimization could further improve the accuracy of the model.

Further, the fcANN approach allows us to leverage on knowledge about the underlying ANN architecture. Specifically, Hopfield attractor dynamics provide a mechanistic account for the emergence of large-scale canonical brain networks (Zalesky et al., 2014) ), and shed light to the origin of characteristic task-responses that are accounted by "ghost attractors" in the system {cite:p}`deco2012ongoing; vohryzek2020ghost`.
As fcANNs do not need to be trained to solve any explicit tasks, they are well suited to examine spontaneous brain dynamics. However, it is worth mentioning that fcANNs are compatible with the neuroconnectionist approach (Doerig et al., 2021), as well.
Like any other ANNs, fcANNs can also be further trained via established ANN training techniques (e.g. via the Hebbian learning rule) to "solve" various tasks or to match developmental dynamics or pathological alterations. In this promising future direction, the training procedure itself becomes part of the model, providing testable hypotheses about the formation, and various malformations, of brain dynamics.

Given its simplicity, it is noteworthy, how well the fcANN model is able to reconstruct and predict brain dynamics under a wide range of conditions.
First and foremost, we have found that the topology of the functional connectome seems to be well suited to function as an attractor network, as it converges much faster than permuted null models.
Second, we found that the two-dimensional fcANN projection can explain more variance in real resting state fMRI data than the first two principal components derived from the data itself. This may indicate that through the known noise tolerance of the underlying ANN architecture, fcANNs are able to capture essential principles of the underlying dynamic processes even if our empirical measurements are corrupted by noise and low sampling rate.
 Indeed, fcANN attractor states were found to be robust to noisy weights ({numref}`Supplementary Figure %s <si_noise_robustness_weights>`) and highly replicable across datasets acquired at different sites, with different scanners and imaging sequences (study 2 and 3). The observed high level of replicability allowed us to re-use the fcANN model constructed with the connectome of study 1 for all subsequent analyses, without any further fine-tuning or study-specific parameter optimization.

 Conceptually, the notion of a global attractor model of the brain network is not new {cite:p}`freeman1987simulation; deco2012ongoing; vohryzek2020ghost; deco2012anatomy; golos2015multistability; hansen2015functional`.
The present work shows, however, that the brain as an attractor network necessarily 'leaks its internal weights' in form of the partial correlation across the regional timeseries. This indicates that, partial correlations across neural timeseries data from different regions (i.e. functional connectivity) may be a more straightforward entry point to investigating the brain's attractor dynamics, than estimates of structural connectedness.
Thereby, the fcANN approach provides a simple and interpretable way to infer and investigate the attractor states of the brain, without the need for additional assumptions about the underlying biophysical details. This is a significant advantage, as the functional connectome can be easily and non-invasively acquired in humans, while biophysical details required by other models are hard to measure or estimate accurately.

Furthermore, here we complement previous work on large-scale brain attractor dynamics, by demonstrating that the reconstructed attractor states are not solely local minima in the state-space but act as a driving force for the dynamic trajectories of brain activity.
 We argue that attractor dynamics may be the main driving factor for the spatial and temporal autocorrelation structure of the brain, recently described to be predictive of network topology in relation to age, subclinical symptoms of dementia, and pharmacological manipulations with serotonergic drugs {cite:p}`shinn2023functional`. 
Nevertheless, attractor states should not be confused with the conventional notion of brain states {cite:p}`chen2015introducing` and large-scale functional gradients {cite:p}`margulies2016situating`. In the fcANN framework, attractor states can rather be conceptualized as "Platonic idealizations" of brain activity, that are continuously approximated - but never reached - by the brain, resulting in re-occurring patterns (brain states) and smooth gradual transitions (large-scale gradients).

Relying on previous work, we can establish a relatively straightforward (although somewhat speculative) correspondence between attractor states and brain function, mapping brain activation on the axes of internal vs. external context {cite:p}`golland2008data; cioli2014differences`, as well as perception vs. action {cite:p}`fuster2004upper`.
This four-attractor architecture exhibits an appealing analogy with Friston's free energy principle {cite:p}`friston2006free` that postulates the necessary existence of brain subsystems for active and perceptual inference and proposes that the dynamical dependencies that drive the flow of information in the brain can be represented with a hierarchically nested structure (e.g. external and internal subsystem) that may be an essential ingredient of conscious {cite:p}`ramstead2023inner` and autonomous {cite:p}`lee2023life` agents.

### Theoretical implications and connections to broader research domains

The theoretical foundation underlying our fcANN approach opens several novel research directions that extend beyond traditional neuroimaging analyses. By grounding our model in the Free Energy Principle, we establish formal links between large-scale brain dynamics and fundamental principles of self-organization, Bayesian inference, and information theory.

**Computational neuroscience and artificial intelligence.** The demonstrated orthogonality of brain attractors provides empirical support for theoretical predictions about optimal neural coding {cite:p}`10.48550/ARXIV.2505.22749`. This finding suggests that the brain's functional architecture has evolved to approximate computationally efficient representations, similar to those found in optimal artificial neural networks {cite:p}`kanter1987associative`. The recursive nature of our theoretical framework, where local free energy minimization gives rise to global Bayesian inference, offers a principled approach for developing more brain-inspired AI architectures that naturally balance accuracy and complexity.

**Predictive coding and hierarchical inference.** Our results provide large-scale empirical validation for predictive coding theories {cite:p}`rao1999predictive; friston2010free`, demonstrating that macro-scale brain dynamics can be understood as a hierarchical inference process. The orthogonal attractor states can be interpreted as learned priors that capture the statistical structure of the environment, while the stochastic dynamics implement posterior sampling. This connection suggests that canonical resting-state networks may represent the brain's internal generative model of the world, continuously updated through the emergent learning dynamics we described theoretically.

**Clinical neuroscience and precision medicine.** The framework's ability to predict how connectivity alterations manifest as dynamic changes offers new avenues for understanding psychiatric and neurological disorders. Rather than viewing pathology as static connectivity differences, our approach suggests that disorders may reflect altered attractor landscapes that bias brain dynamics toward maladaptive states. This perspective could inform the development of targeted interventions that aim to reshape these landscapes through neurofeedback, brain stimulation, or pharmacological approaches.

**Developmental and evolutionary neuroscience.** The self-orthogonalization property provides a mechanistic account for how efficient neural representations might emerge through development and evolution. Our framework predicts that brain networks should naturally evolve toward orthogonal configurations to maximize information processing capacity, offering testable hypotheses about neurodevelopmental trajectories and species differences in brain organization.

**Network control and therapeutic applications.** By linking attractor dynamics to control theory, our approach provides a principled framework for predicting the effects of interventions on brain-wide dynamics. The identification of "ghost attractors" for different cognitive and clinical states suggests that targeted perturbations could guide brain dynamics toward desired configurations, opening new possibilities for precision therapeutics in psychiatry and neurology.

This theoretical integration positions our work within a broader scientific program that seeks to understand the brain as a self-organizing, information-processing system governed by fundamental physical and computational principles. The empirical validation of attractor orthogonality represents a crucial step toward establishing this unified framework for understanding brain function across scales and contexts.

Both conceptually and in terms of analysis practices, resting and task states are often treated as separate phenomena. However, in the fcANN framework, the differentiation between task and resting states is considered an artificial dichotomy. 
Task-based brain activity in the fcANN framework is not a mere response to external stimuli in certain brain locations but a perturbation of the brain's characteristic dynamic trajectories, with increased preference for certain locations on the energy landscape ("ghost attractors").
In our analyses, the fcANN approach captured and predicted participant-level activity changes induced by pain and its self-regulation and gave a mechanistic account for how relatively small activity changes in a single region (NAcc) may result in a significantly altered pain experience.
Our control-signal analysis is different from, but compatible with, linear network control theory-based approaches {cite:p}`liu2011controllability; gu2015controllability`. Combining network control theory with the fcANN approach could provide a powerful framework for understanding the effects of various tasks, conditions and interventions (e.g. brain stimulation) on brain dynamics.

Brain dynamics can not only be perturbed by task or other types of experimental or naturalistic interventions, but also by pathological alterations. Here we provide an initial demonstration (study 7) of how fcANN-based analyses can characterize and predict altered brain dynamics in autism spectrum disorder (ASD). The observed ASD-associated changes in brain dynamics are indicative of a reduced ability to flexibly switch between perception and internal representations, corroborating previous findings that in ASD, sensory-driven connectivity transitions do not converge to transmodal areas {cite:p}`hong2019atypical`. Such findings are in line with previous reports of a reduced influence of context on the interpretation of incoming sensory information in ASD (e.g. the violation of Weber's law) {cite:p}`hadad2019perception`.

Our findings open up a series of exciting opportunities for the better understanding of brain function in health and disease.
First, the 2-dimensional fcANN projection offers a simple framework not only for the visualization, but also for the *interpretation*, of brain activity patterns, as it conceptualizes changes related to various behavioral or clinical states or traits as a shift in brain dynamics in relation to brain attractor states.
Second, fcANN analyses may provide insights into the causes of changes in brain dynamics, by for instance, identifying the regions or connections that act as an "Achilles heel" in generating such changes. Such control analyses could, for instance, aid the differentiation of primary causes and secondary effects of activity or connectivity changes in various clinical conditions.
Third, the fcANN approach can provide testable predictions about the effects of pharmacological interventions as well as non-invasive brain stimulation (e.g. transcranial magnetic or direct current stimulation, focused ultrasound, etc.) and neurofeedback. Obtaining the optimal stimulation or treatment target within the fcANN framework (e.g. by means of network control theory {cite:p}`liu2011controllability`) is one of the most promising future directions with the potential to significantly advance the development of novel, personalized treatment approaches.

The proposed approach is not without limitations. First, the fcANN model is obviously a simplification of the brain's dynamics, and it does not aim to explain (i) the brain's ability to perform certain computations, (ii) brain regions' ability to perform certain functions or (iii) biophysical details underlying (altered) polysynaptic connections. Nevertheless, our approach showcases that many characteristics of brain dynamics, like multistability, temporal autocorrelations, states and gradients, can be explained, and predicted, by a very simple nonlinear phenomenological model. 
Second, our model assumes a stationary connectome, which seems to contradict notions of dynamic connectivity. However, with realistically changing control signals, our model can easily reconstruct dynamic connectivity changes, which still stem from an underlying, stationary functional connectivity architecture. This is in line with the notion of "latent functional connectivity"; an intrinsic brain network architecture built up from connectivity properties that are persistent across brain states {cite:p}`https://doi.org/10.1162/netn_a_00234`.

In this initial work, we presented the simplest possible implementation of the fcANN concept. It is clear that the presented analyses exploit only a small proportion of the richness of the full state-space dynamics reconstructed by the fcANN model. 
There are many potential ways to further improve the utility of the fcANN approach. Increasing the number of reconstructed attractor states (by increasing the temperature parameter), investigating higher-dimensional dynamics, fine-tuning the hyperparameters, testing the effect of different initializations and perturbations are all important direction for future work, with the potential to further improve the model's accuracy and usefulness.

## Conclusion

Here we have proposed a lightweight, high-level computational framework that accurately captures and predicts brain dynamics under a wide range of conditions, including resting states, task-induced activity changes and brain disorders. The framework models large-scale activity flow in the brain with a recurrent artificial neural network architecture that, instead of being trained to solve specific tasks or mimic certain dynamics, is simply initialized with the empirical functional connectome. The framework identifies neurobiologically meaningful attractor states and provides a model for how these restrict brain dynamics. 
 The proposed model establishes a conceptual link between connectivity and activity, provides a mechanistic account for the emergence of brain states, gradients and temporal autocorrelation structure and offers a simple, robust, and highly interpretable computational alternative to conventional descriptive approaches to investigating brain function. The generative nature of our proposed model opens up a wealth of opportunities for future research, including predicting the effect, and understanding the mechanistic bases, of various interventions; thereby paving the way for designing novel treatment approaches.


%+++ {"part": "acknowledgements"}
## Acknowledgements

The work was supported by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation; projects 'TRR289 - Treatment Expectation', ID 422744262 and 'SFB1280 - Extinction Learning', ID 316803389) and by IBS-R015-D1 (Institute for Basic Science; C.W.-W.).
%+++

%+++ {"part": "data-availability"}

## Analysis source code
https://github.com/pni-lab/connattractor

## Project website
https://pni-lab.github.io/connattractor/

## Data availability
Study 1, 2 and 4 is available at openneuro.org (ds002608, ds002608, ds000140). Data for study 3 is available upon request. Data for study 5-6 is available at the github page of the project: https://github.com/pni-lab/connattractor. Study 7 is available at https://fcon_1000.projects.nitrc.org/indi/abide/, preprocessed data is available at http://preprocessed-connectomes-project.org/.
%+++
