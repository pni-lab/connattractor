---
title: Functional Connectivity-based Attractor Dynamics in Rest, Task, and Disease
subject: revised manuscript
short_title: Manuscript
authors:
    - name: Robert Englert
      affiliations:
        - Center for Translational Neuro- and Behavioral Sciences (C-TNBS), University Medicine Essen, Germany
        - Department of Diagnostic and Interventional Radiology and Neuroradiology, University Medicine Essen, Germany
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
        - Center for Translational Neuro- and Behavioral Sciences (C-TNBS), University Medicine Essen, Germany
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
        - Department of Diagnostic and Interventional Radiology and Neuroradiology, University Medicine Essen, Germany
        - Center for Translational Neuro- and Behavioral Sciences (C-TNBS), University Medicine Essen, Germany
      orcid: 0000-0002-2942-0821
      email: tamas.spisak@uk-essen.de
      corresponding: True

abbreviations:
  fMRI: functional Magnetic Resonance Imaging
  ANN: Artificial Neural Network
  fcANN: functional connectivity-based Attractor Neural Network
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
- Based on the theory of artificial attractor neural networks emerging from first principles of self-organization
- Model dynamics accurately reconstruct several characteristics of resting-state brain dynamics and confirm theoretical predictions of emergent attractor self-orthogonalization
- Our model captures both task-induced and pathological changes in brain activity
- fcANNs offer a simple and interpretable computational alternative to conventional descriptive analyses of brain function


+++ {"part": "abstract"}
Functional brain connectivity has been instrumental in uncovering the large-scale organization of the brain and its relation to various behavioral and clinical phenotypes.
Understanding how this functional architecture relates to the brain's dynamic activity repertoire is an essential next step towards interpretable generative models of brain function.
We propose functional connectivity-based Attractor Neural Networks (fcANNs), a theoretically inspired model of macro-scale brain dynamics, simulating recurrent activity flow among brain regions based on first principles of self-organization. In the fcANN framework, brain dynamics are understood in relation to attractor states; neurobiologically meaningful activity configurations that minimize the free energy of the system.
We provide the first evidence that large-scale brain attractors - as reconstructed by fcANNs — exhibit an approximately orthogonal organization, which is a signature of the self-orthogonalization mechanism of the underlying theoretical framework of free‑energy‑minimizing attractor networks.
Analyses of 7 distinct datasets demonstrate that fcANNs can accurately reconstruct and predict brain dynamics under a wide range of conditions, including resting and task states, and brain disorders.
By establishing a formal link between connectivity and activity, fcANNs offer a simple and interpretable computational alternative to conventional descriptive analyses.
+++

## Introduction

Brain function is characterized by the continuous activation and deactivation of anatomically distributed neuronal 
populations {cite:p}`buzsaki2006rhythms`.
Irrespective of the presence or absence of explicit stimuli, brain regions appear to work in concert, giving rise to rich and spatiotemporally complex fluctuations {cite:p}`bassett2017network`.
These fluctuations are not random {cite:p}`liu2013time; zalesky2014time`; they organize around large-scale gradients {cite:p}`margulies2016situating; huntenburg2018large` and exhibit quasi-periodic properties, with a limited number of recurring patterns often termed as "brain substates" {cite:p}`greene2023everyone; https://doi.org/10.1016/j.celrep.2020.108128; vidaurre2017brain; liu2013time`.
A wide variety of descriptive techniques have been previously employed to characterize whole-brain dynamics {cite:p}`smith2012temporally; vidaurre2017brain; liu2013time; chen2018human`. 
These efforts have provided accumulating evidence not only for the existence of dynamic brain substates but also for their clinical significance {cite:p}`hutchison2013dynamic; barttfeld2015signature; meer2020movie`. 
However, the underlying driving forces remain elusive due to the descriptive nature of such studies.

Conventional computational approaches attempt to solve this puzzle by going all the way down to the biophysical properties of single neurons, and aim to construct a model of larger neural populations, or even the entire brain 
{cite:p}`breakspear2017dynamic`.
These approaches have shown numerous successful applications {cite:p}`murray2018biophysical; kriegeskorte2018cognitive; heinz2019towards`.
However, such models need to estimate a vast number of neurobiologically motivated free parameters to fit the data. This hampers their ability to effectively bridge the gap between explanations at the level of single neurons and the complexity of behavior {cite:p}`breakspear2017dynamic`.
Recent efforts using coarse-grained brain network models {cite:p}`schirner2022dynamic; schiff1994controlling; papadopoulos2017development; seguin2023brain` and linear network control theory {cite:p}`chiem2021structure; scheid2021time; gu2015controllability` opted to trade biophysical fidelity to phenomenological validity.
Such models have provided insights into some of the inherent key characteristics of the brain as a dynamic system; for instance, the importance of stable patterns, the *"attractor states"*, in governing brain dynamics {cite:p}`deco2012anatomy; golos2015multistability; hansen2015functional`. While attractor networks become established models of micro-scale canonical brain circuits in the last four decades {cite:p}`khona2022attractor`, these studies suggest that attractor dynamics are essential characteristics of macro-scale brain dynamics as well {cite:p}`https://doi.org/10.1016/j.cobeha.2025.101546`.
Attractor networks, however, come in many flavors and the specific forms and behaviors of these networks are heavily influenced by the chosen inference and learning rules, making it unclear which variety should be in focus when modeling brain dynamics. 
Given that the brain showcases not only multiple signatures of attractor dynamics but also the ability to evolve and adapt through self-organization (i.e., in the absence of any centralized control), investigating attractor models from the point of view of self-organization may be key to narrow down the set of viable models.

In our recent theoretical work {cite:p}`10.48550/ARXIV.2505.22749`, we identified the class of attractor networks that emerge from first principles of self-organization - as articulated by the Free Energy Principle (FEP) {cite:p}`https://doi.org/10.1038/nrn2787; https://doi.org/10.1016/j.physrep.2023.07.001` - and identified the emergent inference and learning rules guiding the dynamics of such systems. 
This theoretical framework reveals that the minimization of variational free energy locally - e.g., by individual network nodes - gives rise to a dual dynamic: simultaneous inference (updating activity) and learning (optimizing connectivity).
The emergent inference process in these systems is equivalent to local Bayesian update dynamics for the individual network nodes, homologous to the stochastic relaxation observed in conventional Boltzmann neural network architectures (e.g. stochastic Hopfield networks, {cite:p}`hopfield1982neural; koiran1994dynamics`), and in line with the empirical observation that activity in the brain "flows" following similar dynamics {cite:p}`doi:10.1038/nn.4406; doi:10.1016/j.neuroimage.2023.120300; https://doi.org/10.48550/arXiv.2402.02191`. Importantly, in this framework, attractor states are not simply an epiphenomenon of collective dynamics, but serve as global priors in the Bayesian sense, that get combined with the current activity configuration so that the updated activity samples from the posterior (akin to a Markov-Chain Monte Carlo (MCMC) sampling process).

Learning, on the other hand, emerges in this framework in the form of a distinctive coupling plasticity - a local, incremental learning rule - that continuously adjusts coupling weights to preserve low free energy in anticipation of future sensory encounters following a contrastive predictive coding scheme {cite:p}`10.48550/ARXIV.2207.12316`, effectively implementing action selection in the active inference sense {cite:p}`https://doi.org/10.1016/j.neubiorev.2016.06.022`. Importantly, the learning dynamics emerging in our theoretical framework provide a strong, testable hypothesis: if the brain operates as a free energy minimizing attractor network, its large-scale attractors should be approximately orthogonal to each other. This is not a general property of all recurrent (attractor) neural networks, but a direct consequence of free energy minimization, shown both mathematically and with simulations in {cite:p}`10.48550/ARXIV.2505.22749`. 
As our theoretical framework - by design - embraces multiple valid levels of description (through coarse-graining), it is well-suited to serve as a basis for a computational model of large-scale brain dynamics.

In the present work, we translate the results of this novel theoretical framework into a computational model of macro-scale brain dynamics and deploy a diverse set of experimental, clinical, and meta-analytic studies to perform an initial investigation of several of its predictions. We start by showing that—if large-scale brain dynamics evolve and organize according to the emergent rules of this framework—the corresponding attractor model can be effectively approximated from functional connectivity data, as measured with resting‑state fMRI. 
Based on the network topology spanned by functional connectivity, our model assigns a free energy level for any arbitrary activation pattern and determines a "trajectory of least action" towards one of a finite number of attractor states that minimize this energy ({numref}`concept`). 
We then perform an initial investigation of the robustness and biological plausibility of the attractor states of the reconstructed network and whether it is able to reproduce various characteristics of resting‑state brain dynamics. Importantly, we directly test the framework's prediction on the emergence of (approximately) orthogonal attractor states. 
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
**Functional connectivity-based attractor neural networks as models of macro-scale brain dynamics.** <br/>
**A** Free‑energy‑minimizing artificial neural networks {cite:p}`10.48550/ARXIV.2505.22749` are a form of recurrent stochastic artificial neural networks that, similarly to classical Hopfield networks {cite:p}`hopfield1982neural; koiran1994dynamics`, can serve as content‑addressable ("associative") memory systems. More generally, through the learning rule emerging from local free‑energy minimization, the weights of these networks will encode a global internal model of the external world. The priors of this internal generative model are represented by the attractor states of the network that—as a special consequence of free‑energy minimization—will tend to be orthogonal to each other. During stochastic inference (local free‑energy minimization), the network samples from the posterior that combines these priors with the previous brain substates (also encompassing incoming stimuli), akin to Markov chain Monte Carlo (MCMC) sampling.
**B** In accordance with this theoretical framework, we consider regions of the brain as nodes of a free‑energy‑minimizing artificial neural network. Instead of initializing the network with the structural wiring of the brain or training it to solve specific tasks, we set its weights empirically, using information about the interregional "activity flow" across regions, as estimated via functional brain connectivity. Applying the inference rule of our framework—which displays strong analogies with the relaxation rule of Hopfield networks and the activity flow principle that links activity to connectivity in brain networks—results in a generative computational model of macro‑scale brain dynamics, that we term a functional connectivity‑based (stochastic) attractor neural network (fcANN).  
**C** The proposed computational framework assigns a free energy level, a probability density and a "trajectory of least action" towards an attractor state to any brain activation pattern and predicts changes of the corresponding dynamics in response to alterations in activity and/or connectivity.
The theoretical framework underlying the fcANNs - based on the assumption that the brain operates as a free energy minimizing attractor network - draws formal links between attractor dynamics and multi-level Bayesian active inference.
:::

## Theoretical background

### Free energy minimizing artificial neural networks

The computational model at the heart of this work is a direct implementation of the inference dynamics that emerge from a recently proposed theoretical framework of free energy minimizing (self-orthogonalizing) attractor networks {cite:p}`10.48550/ARXIV.2505.22749` (FEP-ANNs). 
FEP-ANNs are a class of attractor neural networks that emerge from the Free Energy Principle (FEP) {cite:p}`https://doi.org/10.1038/nrn2787; https://doi.org/10.1016/j.physrep.2023.07.001`. The FEP posits that any self-organizing random dynamical system that maintains its integrity over time (i.e. has a steady-state distribution and a statistical separation from its environment) must act in a way that minimizes its variational free energy. 
FEP-ANNs apply the FEP recursively. We assume a network of $N$ units, where each unit is represented by a single continuous-valued state variable $\sigma_i \in [-1,1]$, so that the activity of the network is described by a vector of states $\bm{\sigma} = (\sigma_1, \sigma_2, \dots, \sigma_N)$ and these states are conditionally independent of each other, given boundary states that realize the necessary statistical separation between them (corresponding to a complex Markov blanket structure in the FEP terminology). 
When assuming $\sigma_i$ states that follow a continuous Bernoulli (a.k.a. truncated exponential: $p(\sigma_i) \propto e^{\kappa_i\sigma_i}$) distribution (parameterized by the single parameter $\kappa_i$) and deterministic couplings $\bm{J}$, the steady-state distribution can be expressed as:

```{math}
:label: steady-state-dist
p^*(\bm{\sigma}) \propto \exp\Big(\sum_i b_i \sigma_i + \frac{1}{2}\sum_{i,j} J^{\mathrm{S}}_{ij} \sigma_i \sigma_j\Big)
```
where $b_i$ represents the local evidence or bias for each unit $i$ (e.g. external input or intrinsic excitability of a brain region), $J^{\mathrm{S}} = \frac{1}{2}(J + J^\top)$ is the symmetric component of the coupling weights between units $i$ and $j$, and $\beta$ is an inverse temperature or precision parameter. 
Note that while this steady-state distribution has the same functional form as continuous-state Boltzmann machines or stochastic Hopfield networks, the true coupling weights $J$ do not have to be symmetric as usually assumed in those architectures. Asymmetric couplings break detailed balance, meaning that $p^*$ is no longer an equilibrium distribution. However, the antisymmetric component $J^{\mathrm{A}} = \frac{1}{2}(J - J^\top)$ does not contribute to the steady-state distribution $p^*$ as it only induces circulating (solenoidal) flow in the state space which is tangential to the level sets of $p^*$. Thus, while the overall framework can describe general attractor networks with asymmetric couplings and non-equilibrium steady states (NESS), it also implies that knowing only the symmetric component of the coupling weights is sufficient to reconstruct the steady-state distribution $p^*$ of the underlying system. This is a highly useful property for the purposes of the present study, where the couplings are reconstructed from resting state fMRI data, without any explicit information about the directionality of functional connections. For a detailed derivation of the steady state distribution, see {cite:p}`10.48550/ARXIV.2505.22749` and [](#Supplementary-Information-1).

Knowing the steady-state distribution of a free-energy-minimizing attractor network, we can derive two types of emergent dynamics from the single imperative of free energy minimization: inference and learning. 

#### Inference: stochastic relaxation dynamics
Inference arises from minimizing free energy with respect to the states $\sigma$. For a single unit, this yields a local update rule homologous to the relaxation dynamics in Hopfield networks:

```{math}
:label: fep-update
\mathbb{E}_{q}[\sigma_i] = L(b_q) = \underbrace{ L \left( \underbrace{ b_i}_{\textit{bias}} + \underbrace{\sum_{j \ne i} J_{ij} \sigma_j}_{\textit{weighted input}} \right) }_{ \textit{sigmoid (Langevin)} } 
```

where $L$ is a sigmoidal activation function (a Langevin function in our case). This rule dictates that each unit updates its activity stochastically, based on a weighted sum of the activity of other units, plus its own intrinsic bias. See {cite:p}`10.48550/ARXIV.2505.22749` and [](#Supplementary-Information-2) for a detailed derivation of the inference dynamics.

Note that the rule is expressed in terms of the expected value of the state $\sigma_i$, which is a stochastic quantity. However, in the limiting case of symmetric couplings (which is the case throughout the present study) and least-action dynamics (i.e. no noise), this update rule reduces to the classical relaxation dynamics of (continuous-state) Hopfield networks. 
In the present study, we use both the deterministic (“least action”) and stochastic variants of the inference rule. The former identifies attractor states; the latter serves as a generative model for large‑scale, multistable brain dynamics.

In the present study, we make the simplifying assumption that all nodes have zero bias ($\bf{b} = \bf{0}$). Furthermore, we allow investigating different scaling factors for the $J$ couplings matrix (given the uncertainties around the magnitude of association in the functional connectome) by introducing a "scaling factor" $\beta$. This leads to the following update rule:

:::{math}
:label: simple-update
\sigma_i^{(t+1)} = L\left(\beta\sum_{j \ne i} J_{ij} \sigma_j^{(t)} \right) + \textit{noise}
:::

The scaling factor $\beta$ is analogous to the inverse temperature parameter known in Hopfield networks and Boltzmann machines.

In the basic framework {cite:p}`10.48550/ARXIV.2505.22749`, inference is a gradient descent on the variational free energy landscape with respect to the states $\sigma$ and can be interpreted as a form of approximate Bayesian inference, where the expected value of the state $\sigma_i$ is interpreted as the posterior mean given the attractor states currently encoded in the network (serving as a macro-scale prior) and the previous state, including external inputs (serving as likelihood in the Bayesian sense). The stochastic update, therefore, is equivalent to a Markov chain Monte Carlo (MCMC) sampling from this posterior distribution. The inverse temperature parameter $\beta$, in this regard, can be interpreted as the precision of the prior encoded in $J$. This is easy to conceptualize by considering the limiting case of infinite precision, where the system simplifies to a binary-state Hopfield network ($\beta → \infty$, $L(\beta u_i) → sign(u_i)$ on $[-1,1]$) that directly and deterministically converges to the (infinite-precision) prior, completely overriding the Bayesian likelihood (i.e., network input).

### Free energy minimizing attractor networks as a model of large-scale brain dynamics

Taken together, the novel framework of free energy minimizing attractor networks not only motivates the use of a specific, emergent class of attractor networks as models for large-scale brain dynamics, but also provides a formal connection between these dynamics and Bayesian inference.
The present study leverages this theoretical foundation. We aim to model large-scale brain dynamics as a free energy minimizing attractor network. 
According to our framework, such networks can be reconstructed from the activation time‑series data measured in their nodes. Specifically, the weight matrix of the attractor network can be reconstructed as the negative inverse covariance matrix of the regional activation time series: $\bm{J} = -\bm{\Lambda} = -\bm{\Sigma}^{-1}$, where $\bm{\Sigma}$ is the covariance matrix of the activation time series in all regions, and $\bm{\Lambda}$ is the precision matrix. For a detailed derivation, see [](#Supplementary-Information-4). Note that this approach can naturally be reduced to different "coarse‑grainings" of the system, by pooling network nodes with similar functional properties. In the case of resting‑state fMRI data, this corresponds to pooling network nodes into functional parcels. Drawing upon concepts such as the center manifold theorem {cite:p}`https://doi.org/10.1137/0520069`, it is posited that rapid, fine‑grained dynamics at lower descriptive levels converge to lower‑dimensional manifolds, upon which the system evolves via slower processes at coarser scales. It has been previously argued {cite:p}`https://doi.org/10.1162/netn_a_00343` that the temporal and spatial scales of fMRI data happen to align relatively well with the characteristic scales corresponding to meaningful large‑scale "coarse‑grainings" of brain dynamics.

Thus, we can **reconstruct FEP‑ANNs from functional connectivity data simply by considering the functional connectome (inverse covariance or partial correlation) as the coupling weights** between the nodes of the network, which themselves correspond to brain regions (as defined by the chosen functional brain parcellation). We refer to such network models as functional connectivity‑based attractor neural networks—**fcANNs** for short.

Having estimates of the weight matrix $J$ of the attractor network, we can now rely on the deterministic and stochastic versions of the inference procedure (eq. [](#simple-update)) in order to investigate this system. Running the deterministic update to a uniformly drawn sample of initial states, we can identify all attractor states of the network. The stochastic update, on the other hand, can be used to sample from the posterior distribution of the activity states, and thus serves as a generative computational model of the brain dynamics.

### Testable predictions of the theoretical framework

#### Self-orthogonalization as a signature of free energy attractor networks
So far, we have only discussed free energy minimization in terms of the activity of the nodes of the network. However, free energy minimization also gives rise to a specific learning rule for the couplings $J$ of the network. This learning rule is a specific local, incremental, contrastive (predictive coding-based) plasticity rule to adjust connection strengths:

:::{math}
:label: learning-rule
\Delta J_{ij} \propto \underbrace{\sigma_i \sigma_j}_{\textit{observed correlation (Hebbian)}} - \underbrace{ L(b_i + \sum_{k\neq i} J_{ik}\,\sigma_k ) \sigma_j}_{\textit{predicted correlation (anti-Hebbian)}}
::: 

 A detailed derivation of the learning dynamics can be found in {cite:p}`10.48550/ARXIV.2505.22749` and [](#Supplementary-Information-2). 
In the present work, we do not implement this learning rule in our computational model, as the coupling weights $J$ are reconstructed directly from the empirical fMRI activation time series data.

However, this specific learning rule has an important implication for the attractor states of the FEP-ANN: it will naturally drive them towards (approximate) orthogonality during learning. For a mathematical motivation of the mechanisms underlying this important property, termed self-orthogonalization, see {cite:p}`10.48550/ARXIV.2505.22749` and [](#Supplementary-Information-3).
Self-orthogonalization is far from being a generic property of all attractor networks (and it is also not a consequence of the above formulated inference dynamics). It has, however, remarkable implications for the computational efficiency of the network and the robustness of its representations. Attractor networks with orthogonal attractor states, often termed the Kanter-Sompolinsky projector neural network {cite:p}`https://doi.org/10.1103/PhysRevA.35.380`, are the computationally most efficient varieties of general attractor networks, with maximal memory capacity and perfect memory recall (without error). Importantly, in Kanter-Sompolinsky projector networks, **the eigenvectors of the coupling matrix and the attractors become equivalent**, providing an important signature for detecting such networks in empirical data. 

Importantly, in the present study we reconstruct attractor networks from functional connectivity data (fcANNs) without relying on the learning rule of the FEP-ANN framework (eq. [](#learning-rule)) which imposes orthogonality on the attractors.
Thus, if, in these empirically reconstructed fcANNs, an alignment between the eigenvectors of the coupling matrix and the attractors is observed, it can be considered strong evidence that the system approximates a Kanter–Sompolinsky projector network. As FEP-ANNs—together with some other, related models (e.g., "dreaming neural networks" {cite:p}`https://doi.org/10.1038/304158a0; 10.1109/ICPR.1994.576884; 10.1088/0305-4470/24/21/026; https://doi.org/10.1016/j.neunet.2019.01.006`)—provide a plausible and mathematically rigorous mechanistic model for the emergence of architectures approximating Kanter–Sompolinsky projector networks through biologically plausible local learning rules, this alignment between the eigenvectors of the coupling matrix and the attractors can be considered a signature of an underlying FEP-ANN.
We will directly test this prediction in the present study, by investigating the orthogonality of the attractor states of the fcANN model reconstructed from empirical fMRI data. 

:::{note}
From the perspective of Bayesian (active) inference, orthogonal attractor states constitute an orthogonal basis set of priors, allowing efficient generalization within the spanned subspace during the stochastic MCMC inference process (see {cite:p}`10.48550/ARXIV.2505.22749` for details).
:::

#### Convergence, multistability, biological plausibility and prediction capacity

Beyond (approximate) attractor orthogonality, our framework provides additional testable predictions. If the functional connectome can indeed be considered a proxy for the coupling weights $J$ of an underlying attractor network, we can expect that (i) the reconstructed fcANN model will exhibit multiple stable attractor states, with large basins and biologically plausible spatial patterns, (ii) the relaxation dynamics of the reconstructed model will display fast convergence to attractor states, and (iii) the stochastic relaxation dynamics yield an efficient generative model of the empirical resting‑state brain dynamics as well as perturbations thereof caused either by external inputs (stimulations and tasks) or pathologies.

### Research questions
We have structured the present work around 7 research questions we address in the present study:

##### Q1 - Is the brain an approximate K‑S projector ANN (FEP‑ANN prediction)? 
We test whether fcANN‑derived brain attractor states closely resemble the eigenvectors of the functional connectome matrix, in contrast to null models based on temporally phase‑randomized time series data (preserving the frequency spectrum and the temporal autocorrelation of data, but destroying conditional dependencies across regions), denoted as **NM1**. Furthermore, in a supplementary analysis, we quantify the similarity of the functional connectome to the weights of an optimal Kanter–Sompolinsky (K‑S) network with the same eigenvectors. The similarity (cosine similarity) is contrasted against repeating the same approach on permuted coupling matrices (but retaining symmetry, **NM2**)

##### Q2 - Is the functional connectome well suited to function as an attractor network? 
We contrast the convergence properties of fcANN deterministic relaxation dynamics with null models with permuted coupling weights (preserving symmetry, sparsity and weight distributions, destroying topological structure) *NM2*. 

##### Q3 - What are the optimal parameters for the fcANN model? 
The number of attractor states is a function of the inverse temperature parameter $\beta$. For simplicity, we fix $\beta=0.04$ (4 attractor states) in the current analysis. We perform a rough optimization of the noise parameter $\epsilon$ by benchmarking the fcANN's ability to capture non‑Gaussian conditional distributions in the data. This is benchmarked by computing a Wasserstein distance between the distributions of empirical and simulated data and contrasting it to the null model of a multivariate normal distribution with covariance matched to that of the empirical data (**NM3**, representing the case of Gaussian‑only conditionals).

##### Q4 - Do fcANNs display biologically plausible attractor states? 
We qualitatively demonstrate that attractor states obtained with different inverse temperature parameters $\beta$ and different noise levels ($\epsilon$) exhibit large basins and that these attractor states exhibit spatial patterns consistent with known large‑scale brain systems. 

##### Q5 - Can fcANNs reproduce the characteristics of resting‑state brain activity?
We compare how well fcANN attractor states explain variance in unseen (in‑ and out‑of‑sample) empirical time series data, relative to the principal components of the empirical data itself. Statistical significance is evaluated via bootstrapping.
Furthermore, we compare various characteristics (state occupancy, distribution, temporal trajectory) of the data generated by fcANNs via stochastic updates to empirical resting‑state data. As null models, we use covariance‑matched multivariate normal distributions (NM3)

##### Q6 - Can resting‑state fMRI‑based fcANNs predict large‑scale brain dynamics elicited by tasks or stimuli?
We test whether fcANNs initialized from resting‑state functional connectomes and perturbed with weak, condition‑specific control signals predict task‑evoked large‑scale dynamics (pain vs. rest; up‑ vs. down‑regulation). We compare simulated and empirical differences on the fcANN projection and flow fields during stochastic updates. As a null model, we use condition‑label shuffling (NM5).

##### Q7 - Can resting‑state fMRI‑based fcANNs predict altered brain dynamics in clinical populations?
We test whether fcANNs initialized with group‑level resting‑state connectomes from autism spectrum disorder (ASD) patients and typically developing controls (TDC) predict observed group differences in dynamics (state occupancy, attractor‑basin activations, flow fields). We compare fcANN‑generated dynamics between ASD‑ and TDC‑initialized models and evaluate similarity to empirical contrasts. As a null model, we use group‑label shuffling (NM5).

For a summary of null modelling approaches and research questions, see {numref}`tab-null-models` and {numref}`tab-research-questions`.


::::{list-table} Null models
:header-rows: 1
:name: tab-null-models
* - Short name
  - Brief description
  - Invariant to
  - Destroys
* - **NM1** Temporal phase randomization
  - Phase‑randomize time series data independently for each region; recalculate connectivity.
  - Time‑series power spectrum and autocorrelation
  - Conditional dependencies across regions
* - **NM2** Symmetry‑preserving matrix permutation
  - Shuffle off‑diagonal entries of `J` while keeping symmetry
  - Weight distribution and symmetry
  - Topological structure, clusteredness
* - **NM3** Covariance‑matched Gaussian
  - Draw time frames from a multivariate normal with covariance equal to the functional connectome's covariance
  - Gaussian conditionals
  - Nonlinear and non‑Gaussian conditionals, temporal autocorrelation
* - **NM4** Temporal order permutation
  - Randomly permute time‑frame order within runs; used for flow analyses
  - Spatial autocorrelation
  - Temporal autocorrelation
* - **NM5** Condition shuffling
  - permute condition labels, either within participant (e.g., pain vs. rest; up- vs. down-regulation) or between participant (shuffle patient vs. control labels)
  - Marginal distributions and overall data structure
  - Condition-specific associations and effects
::::


::::{list-table} Research questions, methodological approaches, and null models
:header-rows: 1
:name: tab-research-questions
* - **Research Question**
  - **Methodological Approach**
  - **Null Model**
* - **Q1.** Is the brain an approximate K-S projector ANN (FEP-ANN prediction)?
  - Compare eigenvectors of coupling matrix with attractor states
  - NM1-2
* - **Q2.** Is the functional connectome well suited to function as an attractor network?
  - Measure iterations to convergence in deterministic relaxation
  - NM2
* - **Q3.** What are the optimal parameters for the fcANN model?
  - We fix $\beta=0.04$ (4 attractor states) for simplicity. We perform a rough optimization of the noise parameter $\epsilon$ in stochastic relaxation to match empirical data distribution.
  - NM3
* - **Q4.** Do fcANNs display biological plausible attractor states?
  - Identify attractor states, report basin sizes and assess spatial patterns with different inverse temperature parameters and noise levels
  - qualitative
* - **Q5.** Can fcANNs reproduce the characteristics of resting‑state brain activity?
  - Compare stochastic dynamics (state occupancy, distribution, temporal trajectory) with empirical resting state data
  - NM3-4
* - **Q6.** Can resting‑state fMRI‑based fcANNs predict large‑scale brain dynamics elicited by tasks or stimuli?
  - Contrast pain vs. rest dynamics with data generated by fcANNs and pain‑associated control signal
  - NM5
* - **Q7.** Can resting‑state fMRI‑based fcANNs predict altered brain dynamics in clinical populations?
  - Contrast autism spectrum disorder patients vs. typically developing control participants' observed brain dynamics with data generated by fcANNs initialized with the respective functional connectomes
  - NM5
::::

## Results

### Functional connectivity-based attractor networks (fcANNs) as a model of brain dynamics

First, we constructed a functional connectivity-based attractor network (fcANN) based on resting-state fMRI data in a sample of n=41 healthy young participants ([study 1](#tab-null-models)). Details are described in the [Methods](#tab-null-models). In brief, we estimated interregional activity flow {cite:p}`cole2016activity; ito2017cognitive` as the study-level average of regularized partial correlations among the resting-state fMRI time series of m=122 functional parcels of the BASC brain atlas (see [Methods](#Functional-connectome) for details). We then used the standardized functional connectome as the $J_{ij}$ weights of a fully connected recurrent fcANN model, see [Methods](#connectome-based-hopfield-networks)). 

Next, we applied the deterministic relaxation procedure to a large number of random initializations (n=100000) to obtain all possible attractor states of the fcANN in study 1 ({numref}`attractors`A).
Consistent with theoretical expectations, we observed that increasing the inverse temperature parameter $\beta$ led to an increasing number of attractor states ({numref}`attractors`E, left, {numref}`Supplementary Figure %s <si_att_state_emergence_over_beta>`), appearing in symmetric pairs (i.e. $\sigma_i^{(1)} = -\sigma_i^{(2)}$, see {numref}`attractors`G).

To test research question **Q1**, we matched the eigenvectors of the coupling matrix to the attractor state with which they exhibit the highest correlation.
We compared eigenvector–attractor correlations with a null model based on phase‑randomized surrogate time‑series data (NM1). We found that the eigenvectors of the coupling matrix and the attractor states are significantly more strongly aligned (as measured with Pearson's correlation coefficient) than those in the null model (two‑sided empirical permutation test; 1,000 permutations; correlations and p‑values for the first six eigenvector–attractor pairs are reported in {numref}`attractors`A), providing evidence that large‑scale brain organization approximates a Kanter–Sompolinsky projector network architecture ({numref}`attractors`A). Eigenvectors with the highest eigenvalues tended to be aligned with the attractor states with the highest fractional occupancy (ratio of time spent on their basins during simulations with stochastic relaxation; see {numref}`attractors`F). No such pattern was observed in the null model ({numref}`attractors`B). Further evidence for the functional connectome's close resemblance to a Kanter–Sompolinsky projector network is provided by the orthogonality of the attractor states to each other ({numref}`attractors`C) and additional analyses reported in {numref}`Supplementary Figure %s <si_orthogonality>`.

Next, to support the visualization of further analyses, we constructed a simplified, 2‑dimensional visual representation of fcANN dynamics, which we apply throughout the remaining manuscript as a high‑level visual summary.
This 2‑dimensional visualization, referred to as the *fcANN projection*, is based on the first two principal components (PCs) of the states sampled from the stochastic relaxation procedure ({numref}`attractors`D–F and {numref}`Supplementary Figure %s <si_fcann_projection>`). On this simplified visualization, we observed a clear separation of the attractor states ({numref}`attractors`D), with the two symmetric pairs of attractor states located at the extremes of the first and second PC. 
To map the attractors' basins on the space spanned by the first two PCs ({numref}`attractors`C), we obtained the attractor state of each point visited during the stochastic relaxation and fit a multinomial logistic regression model to predict the attractor state from the first two PCs. 
The resulting model accurately predicted attractor states of arbitrary brain activity patterns, achieving a cross-validated accuracy of 96.5% (two-sided empirical permutation p<0.001; 1,000 label permutations within folds).
This allows us to visualize attractor basins on this 2-dimensional projection by delineating the decision boundaries obtained from this model ({numref}`Supplementary Figure %s <si_fcann_projection>` as black lines in {numref}`attractors`G-H). In the rest of the manuscript, we use this 2-dimensional fcANN projection depicted on ({numref}`attractors`D-H) as a simplified visual representation of brain dynamics.

Panel D on {numref}`attractors` uses the fcANN projection to visualize the conventional Hopfield relaxation procedure. It depicts the trajectory of individual activation maps (sampled randomly from the time series data in study 1) until converging to one of the four attractor states. 
Panel E shows that the system does not converge to an attractor state with the stochastic relaxation procedure. The resulting path is still influenced by the attractor states' "gravitational pull", resulting in multistable dynamics that resemble the empirical time series data (example data on panel F).

:::{figure} figures/rsfmri_validity.png
:name: attractors
**Attractor states and state-space dynamics of connectome-based Hopfield networks** <br/>
**A** Leading eigenvectors of the empirical coupling matrix `J` (upper in each pair) closely match fcANN attractor states (lower in each pair). Numbers under each pair report Pearson correlation and two‑sided p‑values based on 1,000 surrogate data realizations, generated by phase‑randomizing the true time series and recomputing the connectivity matrix. For the comprehensive results of the eigenvector–attractor alignment analysis (including a supplementary analysis on weight similarity to the analogous Kanter–Sompolinsky projector network) see {numref}`Supplementary Figure %s <si_orthogonality>`.
**B** Example matches from a single permutation of the permutation‑based null distribution. For each symmetry‑preserving permutation of `J`, we recomputed the corresponding eigenvectors and attractors and re‑matched them. The maps are visibly mismatched and correlations are near zero, illustrating the null against which the empirical correlations in panel A are evaluated.
**C** Left panel: Free‑energy‑minimizing attractor networks have been shown to establish approximately orthogonal attractor states (right), even when presented with correlated patterns (left, adapted from {cite:t}`10.48550/ARXIV.2505.22749`). fcANN analysis reveals that the brain also exhibits approximately orthogonal attractors. On all three polar plots, pairwise angles between attractor states are shown. Angles concentrating around 90° in the empirical fcANN are consistent with predictions of free‑energy‑minimizing (Kanter–Sompolinsky‑like) networks. (Note, however, that in high‑dimensional spaces, random vectors would also tend to be approximately orthogonal.)
**D** The fcANN of study 1 seeded with real activation maps (gray dots) of an example participant. All activation maps converge to one of the four attractor states during the deterministic relaxation procedure (without noise) and the system reaches equilibrium. Trajectories are colored by attractor state.
**E** Illustration of the stochastic relaxation procedure in the same fcANN model, seeded from a single starting point (activation pattern). With stochastic relaxation, the system no longer converges to an attractor state, but instead traverses the state space in a way restricted by the topology of the connectome and the "gravitational pull" of the attractor states. The shade of the trajectory changes with increasing number of iterations. The trajectory is smoothed with a moving average over 10 iterations for visualization purposes.
**F** Real resting state fMRI data of an example participant from study 1, plotted on the fcANN projection. The shade of the trajectory changes with an increasing number of iterations. The trajectory is smoothed with a moving average over 10 iterations for visualization purposes.
**G** Consistent with theoretical expectations, we observed that increasing the inverse temperature parameter $\beta$ led to an increasing number of attractor states, emerging in a nested fashion (i.e. the basin of a new attractor state is fully contained within the basin of a previous one). When contrasting the functional connectome-based ANN with a null model based on symmetry-retaining permuted variations of the connectome (NM2), we found that the topology of the original (unpermuted) functional brain connectome makes it significantly better suited to function as an attractor network than the permuted null model. Table contains the median number of iterations until convergence for the original and permuted connectomes for different temperature parameters $\beta$ and the p‑value derived from a one-sided Wilcoxon signed-rank test (i.e. a non-parametric paired test) comparing the iteration values for each random null instance (1,000 pairs) to the iteration number observed with the original matrix and the same random input; with the null hypothesis that the empirical connectome converges in fewer iterations than the permuted connectome. 
**H** We optimized the noise parameter $\epsilon$ of the stochastic relaxation procedure for 8 different $\epsilon$ values over a logarithmic range between $\epsilon=0.1$ and $1$ and contrasted the similarity (Wasserstein distance) between the 122-dimensional distribution of the empirical and the fcANN-generated data against null data generated from a covariance-matched multivariate normal distribution (1000 surrogates). We found that the fcANN reached multistability with $\epsilon>0.19$ and provided the most accurate reconstruction of the real data with $\epsilon=0.37$, as compared with its accuracy in retaining the null data, suggesting that the fcANN model is capable of capturing non-Gaussian conditionals in the data. Glass's $Delta$ quantifies the distance from the null mean, expressed in units of null standard deviation.
:::

In study 1, we investigated the convergence process of the fcANN (research question **Q2**) and contrasted it with a null model based on permuted variations of the connectome (while retaining the symmetry of the matrix, NM2). This null model preserves the sparseness and the degree distribution of the connectome, but destroys its topological structure (e.g. clusteredness). We found that the topology of the original (unpermuted) functional brain connectome makes it significantly better suited to function as an attractor network than the permuted null model.
For instance, with $\beta=0.04$, the median iteration number for the original and permuted fcANNs to reach convergence was 383 and 3543.5 iterations, respectively ({numref}`attractors`G, {numref}`Supplementary Figure %s <si_convergence>`). Similar results were observed, independent of the inverse temperature parameter $\beta$.
We set the temperature parameter for the rest of the paper to a value of $\beta=0.04$, resulting in 4 distinct attractor states. The primary motivation for selecting $\beta=0.04$ was to reduce the computational burden and the interpretational complexity for further analyses. However, as with increasing temperature attractor states emerge in a nested fashion, we expect that the results of the following analyses would be, although more detailed, qualitatively similar with higher $\beta$ values.

Next, in line with research question **Q3**, we optimized the noise parameter $\epsilon$ of the stochastic relaxation procedure for 8 different $\epsilon$ values over a logarithmic range between $\epsilon=0.1$ and $1$ and contrasted the similarity (Wasserstein distance) between the 122-dimensional distribution of the empirical and the fcANN-generated data against null data generated from a covariance-matched multivariate normal distribution (1000 surrogates). We found that the fcANN reached multistability with $\epsilon>0.19$ and provided the most accurate reconstruction of the non-Gaussian conditional dependencies in the real data with $\epsilon=0.37$, as compared to its accuracy in retaining the covariance-matched multivariate Gaussian null data (NM3 {numref}`attractors`H; Wasserstein distance: 10.2, Glass's $Delta$ (distance from null mean, expressed in units of null standard deviation): -11.63, p<0.001 one-sided).
Based on this coarse optimization procedure, we set $\epsilon=0.37$ for all subsequent analyses. 

### Reconstruction of resting state brain dynamics

Next, we visualized and qualitatively assessed the neuroscientific relevance of the spatial patterns of the obtained attractor states (**Q4**, {numref}`rest-validity`A), and found that they closely resemble previously described large-scale brain systems.
The spatial patterns associated with first pair of attractors (mapped on PC1 on the 2-dimensional projection, horizontal axis, e.g. on {numref}`attractors`D-H) show a close correspondence to two commonly described complementary brain systems, that have been previously found in anatomical, functional, developmental, and evolutionary hierarchies, as well as gene expression, metabolism, and blood flow, (see {cite}`sydnor2021neurodevelopment` for a review), and reported under various names, like intrinsic and extrinsic systems {cite:p}`golland2008data`, Visual-Sensorimotor-Auditory and Parieto-Temporo-Frontal "rings" {cite:p}`cioli2014differences`, "primary" brain substates {cite:p}`chen2018human`, unimodal-to-transmodal principal gradient {cite:p}`margulies2016situating; huntenburg2018large` or sensorimotor-association axis {cite:p}`sydnor2021neurodevelopment`. 
A common interpretation of these two patterns is that they represent (i) an "intrinsic" system for higher-level internal context, commonly referred to as the *default mode network* {cite:p}`raichle2001default` and (ii) an anti-correlated "extrinsic" system linked to the immediate sensory environment, showing similarities to the recently described "action mode network" {cite:p}`https://doi.org/10.1038/s41583-024-00895-x`.
The other pair of attractors - spanning an approximately orthogonal axis - resemble patterns commonly associated with perception–action cycles {cite:p}`fuster2004upper`, and described as a gradient across sensorimotor modalities {cite:p}`huntenburg2018large`, recruiting regions associated with active (e.g. motor cortices) and perceptual inference (e.g., visual areas).

:::{figure} figures/face_validity.png 
:name: rest-validity
**Connectome-based attractor networks reconstruct characteristics of real resting-state brain activity.**<br/>
**A** The four attractor states of the fcANN model from study 1 reflect brain activation 
patterns with high neuroscientific relevance, representing sub-systems previously associated with "internal context"
(blue), "external context" (yellow), "action" (red) and "perception" (green)
{cite:p}`golland2008data; cioli2014differences; chen2018human; fuster2004upper; margulies2016situating; https://doi.org/10.1038/s41583-024-00895-x`.
**B** The attractor states show excellent replicability in two external datasets (study 2 and 3, overall mean correlation 0.93). 
**C** The first two PCs of the fcANN state space (the "fcANN projection") explain significantly more variance (two-sided percentile bootstrap p<0.0001 on $\Delta R^2$, 100 resamples) in the real resting-state fMRI data than principal components derived from the real resting-state data itself and generalizes 
better (two-sided percentile bootstrap p<0.0001) to out-of-sample data (study 2). Error bars denote 99% percentile bootstrapped confidence intervals (100 resamples).
**D** The fcANN analysis reliably predicts various characteristics of real resting-state fMRI data, such as the fraction of time spent on the basis of the four attractors (first column, p=0.007, contrasted to the multivariate normal null model NM3), the distribution of the data on the fcANN-projection (second column, p<0.001, contrasted to the multivariate normal null model NM3) and the temporal autocorrelation structure of the real data (third column, p<0.001, contrasted to a null model based on permuting time-frames). The latter analysis was based on flow maps of the mean trajectories (i.e. the characteristic timeframe-to-timeframe transition direction) in fcANN-generated data, as compared to a shuffled null model representing zero temporal autocorrelation. For more details, see [Methods](#evaluation-resting-state-dynamics). Furthermore, we demonstrate that - in line with the theoretical expectations - fcANNs "leak" their weights during stochastic inference (rightmost column): the time series resulting from the stochastic relaxation procedure mirror the covariance structure of the functional connectome the fcANN model was initialized with. While the "self-reconstruction" property in itself does not strengthen the face validity of the approach (no unknown information is reconstructed), it is a strong indicator of the model's construct validity; i.e. that systems that behave like the proposed model inevitably "leak" their weights into the activity time series.
:::

The discovered attractor states demonstrate high replicability across the discovery dataset (study 1) and two independent replication datasets ([study 2 and 3](#tab-samples), {numref}`rest-validity`C; overall mean Pearson's correlation 0.93, pooled across datasets and attractor states). In a supplementary analysis, we have also demonstrated the robustness of fcANNs to imperfect functional connectivity measures: fcANNs were found to be significantly more robust to noise added to the coupling matrix than nodal strength scores (used as a reference with the same dimensionality; see {numref}`Supplementary Figure %s <si_noise_robustness_weights>` for details).

Further analysis in study 1 showed that connectome-based attractor models accurately reconstructed multiple characteristics of true resting-state data (**Q5**).
First, the two "axes" of the fcANN projection (corresponding to the first four attractors) accounted for a substantial amount of variance in the real resting-state fMRI data in study 1 (mean $R^2=0.399$) and generalized well to out-of-sample data (study 2, mean $R^2=0.396$)  ({numref}`rest-validity`E). The variance explained by the attractors significantly exceeded that of the first two PCs derived directly from the real resting-state fMRI data itself ($R^2=0.37$ and $0.364$ for in- and out-of-sample analyses). PCA—by identifying variance-heavy orthogonal directions—aims to explain the highest amount of variance possible in the data (with the assumption of Gaussian conditionals). While empirical attractors are closely aligned to the PCs (i.e. eigenvectors of the inverse covariance matrix), the alignment is only approximate. Here we quantified whether attractor states are a better fit to the unseen data than the PCs. Obviously, due to the otherwise strong PC–attractor correspondence, this is expected to be only a small improvement. However, this provides important evidence for the validity of our framework, as—together with our analysis addressing Q3—it shows that attractors are not just a complementary, perhaps "noisier" variety of the PCs, but a "substrate" that generalizes better to unseen data than the PCs themselves. 

Second, during stochastic relaxation, the fcANN model was found to spend approximately three-quarters of the time on the basins of the first two attractor states and one-quarter on the basins of the second pair of attractor states (approximately equally distributed between pairs). We observed similar temporal occupancies in the real data ({numref}`rest-validity`D left column), statistically significant against a covariance-matched multivariate Gaussian null model (NM3, 1,000 surrogates each; observed $\chi^2=21.57$, p<0.001; Glass $\Delta$ = -5.17; see {numref}`Supplementary Figure %s <si_state_occupancy_null_models>` for details and for an alternative null model based on spatial phase-randomization). Fine-grained details of the distribution with bimodal appearance, observed in the real resting-state fMRI data were also convincingly reproduced by the fcANN model ({numref}`rest-validity`F and {numref}`attractors`D, second column).

Third, not only spatial activity patterns but also time series generated by the fcANN are similar to empirical time series data. Next to the visual similarity shown on {numref}`attractors`E and F, we observed a statistically significant similarity between the average trajectories of fcANN-generated and real time series "flow" (i.e. the characteristic timeframe-to-timeframe transition direction, Pearson's r = 0.88, p<0.001, Glass $\Delta$ = 4.41), as compared to null models of zero temporal autocorrelation (randomized timeframe order; two-sided empirical permutation test on Pearson's r with 1,000 permutations; {numref}`rest-validity`D, third column; [Methods](#evaluation-resting-state-dynamics)). 

Finally, we have demonstrated that - as expected from theory - fcANNs generate signal that preserves the covariance structure of the functional connectome they were initialized with, indicating that dynamic systems of this type (including the brain) inevitably "leak" their underlying structure into the activity time series, strengthening the construct validity of our approach ({numref}`rest-validity`D).

### An explanatory framework for task-based brain activity

Next to reproducing various characteristics of spontaneous brain dynamics, fcANNs can also be used to model responses to various perturbations (**Q6**). We obtained task-based fMRI data from a study by {cite:t}`woo2015distinct` ([study 4](#tab-samples), n=33, see {numref}`rest-validity`), investigating the neural correlates of pain and its self-regulation. 

We found that activity changes due to pain (taking into account hemodynamics, see [Methods](#evaluation-task-based-dynamics)) were characterized on the fcANN projection by a shift toward the attractor state of action/execution (NM5: two-sided permutation test on the L2 norm of the mean projection difference; 1,000 within-participant label swaps; p<0.001; Glass's $\Delta$ = 4.34; {numref}`task-validity`A, left). Energies, as defined by the fcANN, were also significantly different between the two conditions (NM5: two-sided permutation test on absolute energy difference; 1,000 label swaps; p<0.001; Glass's $\Delta$ = 3.14), with higher energies during pain stimulation.

When participants were instructed to up- or downregulate their pain sensation (resulting in increased and decreased pain reports and differential brain activity in the nucleus accumbens, NAc (see {cite}`woo2015distinct` for details), we observed further changes in the location of momentary brain activity patterns on the fcANN projection (two-sided permutation test on the L2 norm of the mean projection difference; 1,000 label swaps; p<0.001; Glass's $\Delta$ = 4.1; {numref}`task-validity`A, right), with downregulation pulling brain dynamics toward the attractor state of internal context and perception. Interestingly, self-regulation did not trigger significant energy changes (two-sided permutation test on absolute energy difference; 1,000 label swaps; p=0.37; Glass's $\Delta$ = 0.4). 

:::{figure} figures/task_validity.png
:name: task-validity
**Functional connectivity-based attractor networks reconstruct real task-based brain activity.** <br>
**A** Functional MRI time-frames during pain stimulation from [study 4](#tab-samples) (second fcANN projection plot)
and self-regulation (third and fourth) are distributed differently on the fcANN projection than brain substates 
during rest (first projection, permutation test, p<0.001 for all). Energies, as defined by the Hopfield model, are also
significantly different between rest and the pain conditions (permutation test, p<0.001), with higher energies during 
pain stimulation. Triangles denote participant-level mean activations in the various blocks (corrected for 
hemodynamics). Small circle plots show the directions of the change for each individual (points) as well as the mean direction across participants (arrow), as compared to the reference state (downregulation for the last circle plot, rest for all other circle plots).
**B** Flow-analysis (difference in the average timeframe-to-timeframe transition direction) reveals a nonlinear difference in brain dynamics during pain and rest (left). When introducing weak pain-related signal in the fcANN model during stochastic relaxation, it accurately reproduces these nonlinear flow differences (right).
**C** Simulating activity in the Nucleus Accumbens (NAc) (the region showing significant activity differences in {cite}`woo2015distinct`) reconstructs the observed nonlinear flow difference between up- and downregulation (left).
**D** Schematic representation of brain dynamics during pain and its up- and downregulation, visualized on the fcANN  projection. In the proposed framework, pain does not simply elicit a direct response in certain regions, but instead, shifts spontaneous brain dynamics towards the "action" attractor, converging to a characteristic "ghost attractor" of pain. Down-regulation by NAc activation exerts force towards the attractor of internal context, leading to the brain less frequent "visiting" pain-associated states.
**E** Visualizing meta-analytic activation maps (see {numref}`Supplementary Table %s <si-tab-neurosynth>` for details) on the fcANN projection captures intimate relations between the corresponding tasks and **F** serves as a basis for a fcANN-based theoretical interpretative framework for spontaneous and task-based brain dynamics. In the proposed framework, task-based activity is not a mere response to external stimuli in certain brain locations but a perturbation of the brain's characteristic dynamic trajectories, constrained by the underlying functional connectivity. From this perspective, "activity maps" from conventional task-based fMRI analyses capture time-averaged differences in these whole brain dynamics. 
:::

Next, we conducted a "flow analysis" on the fcANN projection, quantifying how the average timeframe-to-timeframe transition direction differs on the fcANN projection between conditions (see [Methods](#evaluation-task-based-dynamics)).
This analysis unveiled that during pain ({numref}`task-validity`B, left side), brain activity tends to gravitate toward a distinct point on the projection on the boundary of the basins of the internal and action attractors, which we term the "ghost attractor" of pain (similar to {cite}`vohryzek2020ghost`). In case of downregulation (as compared to upregulation), brain activity is pulled away from the pain-related "ghost attractor" ({numref}`task-validity`C, left side), toward the attractor of internal context.

Our fcANN was able to accurately reconstruct these nonlinear dynamics by adding a small amount of realistic "control signal" (similarly to network control theory, see e.g. {cite}`liu2011controllability` and {cite}`gu2015controllability`). To simulate the alterations in brain dynamics during pain stimulation, we acquired a meta-analytic pain activation map {cite:p}`zunhammer2021meta` (n=603) and incorporated it as a control signal added to each iteration of the stochastic relaxation procedure. The ghost attractor found in the empirical data was present across a relatively wide range of signal-to-noise (SNR) values ({numref}`Supplementary Figure %s <si_pain_ghost_attractor_sim>`). Results with SNR=0.005 are presented in {numref}`task-validity`B, right side (Pearson's r = 0.46; two-sided permutation p=0.005 based on NM5: randomizing conditions on a per-participant basis; 1,000 permutations; Glass's $\Delta$ = 2.19).

The same model was also able to reconstruct the observed nonlinear differences in brain dynamics between the up- and downregulation conditions (Pearson's r = 0.62; p=0.023 based on two-sided permutation test NM5: randomly shuffling conditions in a per-participant basis; 1,000 permutations; Glass's $\Delta$ = 1.84) without any further optimization (SNR=0.005, {numref}`task-validity`C, right side). The only change we made to the model was the addition (downregulation) or subtraction (upregulation) of control signal in the NAc (the region in which {cite:p}`woo2015distinct` observed significant changes between up- and downregulation), introducing a signal difference of $\Delta$SNR=0.005 (the same value we found optimal in the pain-analysis). Results were reproducible with lower NAc SNRs, too ({numref}`Supplementary Figure %s <si_downreg_trajectory_sim>`).

To provide a comprehensive picture on how tasks and stimuli other than pain map onto the fcANN projection, we obtained various task-based meta-analytic activation maps from Neurosynth (see [Methods](#evaluation-task-based-dynamics)) and plotted them on the fcANN projection ({numref}`task-validity`E). This analysis reinforced and extended our interpretation of the four investigated attractor states and shed more light on how various functions are mapped on the axes of internal vs. external context and perception vs. action.
In the coordinate system of the fcANN projection, visual processing is labeled "external-perception", sensory-motor processes fall into the "external-active" domain, language, verbal cognition and working memory belongs to the "internal-active" region and long-term memory as well as social and autobiographic schemata fall into the "internal-perception" regime ({numref}`task-validity`F).

### Clinical relevance

To demonstrate fcANN models' potential to capture altered brain dynamics in clinical populations (**Q7**), we obtained data from n=172 autism spectrum disorder (ASD) and typically developing control (TDC) individuals, acquired at the New York University Langone Medical Center, New York, NY, USA (NYU) and generously shared in the Autism Brain Imaging Data Exchange dataset ([study 7](#tab-samples): ABIDE, {cite:p}`di2014autism`).
After excluding high-motion cases (with the same approach as in studies 1–4, see [Methods](#clinical-data)), we visualized the distribution of time-frames on the fcANN-projection separately for the ASD and TDC groups ({numref}`clinical-validity`A).
First, we assigned all timeframes to one of the 4 attractor states with the fcANN from study 1 and found several significant differences in the mean activity on the attractor basins (see [Methods](#clinical-data)) of the ASD group as compared to the respective controls ({numref}`clinical-validity`B).
Strongest differences were found on the "action-perception" axis ({numref}`tab-clinical-results`), with increased activity of the sensory-motor and middle cingular cortices during "action-execution" related states and increased visual and decreased sensory and auditory activity during "perception" states, likely reflecting the widely acknowledged, yet poorly understood, perceptual atypicalities in ASD {cite:p}`hadad2019perception`. ASD related changes in the internal-external axis were characterized by more involvement of the posterior cingulate, the precuneus, the nucleus accumbens, the dorsolateral prefrontal cortex (dlPFC), the cerebellum (Crus II, lobule VII) and inferior temporal regions during activity of the internalizing subsystem ({numref}`tab-clinical-results`). While similar, default mode network (DMN)-related changes have often been attributed to an atypical integration of information about the "self" and the "other" {cite:p}`padmanabhan2017default`, a more detailed fcANN-analysis may help to further disentangle the specific nature of these changes.

:::{figure} figures/state_analysis.png
:name: clinical-validity
**Connectome-based Hopfield analysis of autism spectrum disorder.** <br>
**A** The distribution of time-frames on the fcANN-projection separately for ASD patients and typically developing control (TDC) participants. <br>
**B** We quantified attractor state activations in the Autism Brain Imaging Data Exchange datasets ([study 7](#tab-samples)) as the 
individual-level mean activation of all time-frames belonging to the same attractor state. This analysis captured alterations similar to those previously associated with ASD-related perceptual atypicalities (visual, auditory and somatosensory cortices) as well as atypical integration of information about the "self" and the "other" (default mode network regions). All results are corrected for multiple comparisons across brain regions and attractor states (122×4 comparisons) with Bonferroni correction. See {numref}`tab-clinical-results` and {numref}`Supplementary Figure %s <si_clinical_results_table>` for detailed results. <br>
**C** The comparison of data generated by fcANNs initialized with ASD and TDC connectomes, respectively, revealed a characteristic pattern of differences in the system's dynamics, with increased pull towards (and potentially a higher separation between) the action and perception attractors and a lower tendency of trajectories going towards the internal and external attractors. <br>
***Abbreviations**: MCC: middle cingulate cortex, ACC: anterior cingulate cortex, pg: perigenual, PFC: prefrontal cortex, dm: dorsomedial, dl: dorsolateral, STG: superior temporal gyrus, ITG: inferior temporal gyrus, Caud/Acc: caudate-accumbens, SM: sensorimotor, V1: primary visual, A1: primary auditory, SMA: supplementary motor cortex, ASD: autism spectrum disorder, TDC: typically developing control.*
:::

:::{list-table} **The top ten largest changes in average attractor-state activity between autistic and control individuals.**  Mean attractor-state activity changes are presented in the order of their absolute effect size. Reported effect sizes are mean attractor activation differences. Note that activation time series were standard scaled independently for each region, so effect size can be interpreted as showing the differences as a proportion of regional variability. All p-values are based on permutation tests (shuffling the group assignment) and corrected for multiple comparisons (via Bonferroni's correction).  For a comprehensive list of significant findings, see {numref}`Supplementary Figure %s <si_clinical_results_table>`.
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
 * - cerebellum lobule VIIb (medial part)
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

Thus, we contrasted the characteristic trajectories derived from the fcANN models of the two groups (initialized with the group-level functional connectomes). Our fcANN-based flow analysis predicted that in ASD, there is an increased likelihood of states returning towards the middle (more noisy states) from the internal-external axis and an increased likelihood of states transitioning towards the extremes of the action-perception axis ({numref}`clinical-validity`C). We observed a highly similar pattern in the real data (Pearson's r = 0.66), statistically significant after two-sided permutation testing (shuffling the group assignment; 1,000 permutations; p=0.009).

## Discussion

The notion that the brain functions as an attractor network has long been proposed {cite:p}`freeman1987simulation; https://doi.org/10.1017/CBO9780511623257; deco2012ongoing; deco2012anatomy; golos2015multistability; hansen2015functional; vohryzek2020ghost`, although the exact functional form of the network underlying large-scale brain dynamics - or at least useful approximation thereof - remained elusive.
The theoretical framework of free energy minimizing attractor neural networks (FEP-ANN) {cite:p}`10.48550/ARXIV.2505.22749` identifies a specific class of attractor networks that emerge from first principles of self-organization - as articulated by the Free Energy Principle (FEP) {cite:p}`https://doi.org/10.1038/nrn2787; https://doi.org/10.1016/j.physrep.2023.07.001`. Therefore it provides a plausible candidate model for large-scale brain attractor dynamics and yields testable predictions - measurable signatures of these special attractor networks that can be validated empirically.
In this study, we have introduced, and performed initial validation of, a simple and robust network-level generative computational model, rooted in the FEP-ANN framework and providing the opportunity to test these predictions empirically. Our model, termed a functional connectivity-based attractor network (fcANN), exploits special characteristics of the emergent inference rule of FEP-ANNs. This is a stochastic rule that governs how activity evolves in time with a given set of fixed coupling weights and leads to a Markov chain Monte Carlo (MCMC) sampling process. As a consequence, the activation time series data measured in each network node can be used to reconstruct the attractor network's internal structure. Specifically, the coupling weights can be estimated as the negative inverse covariance matrix of the activation time series data.
fcANN modeling applies this concept to large-scale brain dynamics as measured by resting-state fMRI data (as an estimate of weights corresponding to the steady-state distribution of the system).

The core idea underlying the fcANN reconstruction approach - the use of functional connectivity as a proxy for weighted information flow in the brain - is in line with previous empirical observations about the relationship between functional connectivity and brain activity, as articulated by the activity flow principle, first introduced by {cite:t}`cole2016activity`. The activity flow principle states that activity in a brain region can be predicted by a weighted combination of the activity of all other regions, where the weights are set to the functional connectivity of those regions to the held-out region. This principle has been shown to hold across a wide range of experimental and clinical conditions {cite:p}`cole2016activity; ito2017cognitive; mill2022network; hearne2021activity; chen2018human`.
Considering that the repeated, iterative application of the activity flow equation (extended with an arbitrary sigmoidal activation function) naturally reproduces certain types of recurrent artificial neural networks, e.g. Hopfield networks {cite:p}`hopfield1982neural`, yields an intuitive understanding of how the fcANN model works.

However, beyond this analogy, we need concrete evidence that the fcANN model and the underlying FEP-ANN framework is a valid model of large-scale brain dynamics.  

Here we have tested multiple predictions of the FEP-ANN framework. Most importantly FEP-ANNs - through their emergent predictive coding-based learning rule - have been shown to develop approximately orthogonal attractor representations, and thereby approximate the so-called Kanter-Sompolinsky projector neural networks (K-S network, for short) {cite:p}`https://doi.org/10.1103/PhysRevA.35.380`. K-S networks are a special class of attractor networks that have been shown to be highly effective for pattern recognition and learning {cite:p}`kanter1987associative`. In these networks, the attractor states are orthogonal to each other, and become equivalent with those eigenvectors of the coupling matrix, that have positive eigenvalues. 
This is a very strong prediction: K-S networks are a very special class of attractor networks, which do not arise from conventional learning rules, like Hebbian learning. To date, the predictive coding-based learning rule of FEP-ANNs is the only known local, incremental learning rule that can effectively approximate K-S networks in a single phase (but see "dreaming neural networks" {cite:p}`https://doi.org/10.1038/s41593-021-00899-0` for a similar, two-phase approach).
Thus, showing that fcANN models approximate K-S networks can be interpreted as evidence for the brain functioning akin to a FEP-ANN. Our results show that this is indeed the case: the fcANN models reconstructed from resting-state fMRI data approximate K-S networks, and thereby exhibit approximately orthogonal attractor states.

In the FEP-ANN framework, approximate attractor orthogonality has important computational implications: it allows the system achieve maximal "storage capacity" (the number of attractors that can be stored and retrieved without interference). Furthermore, in the FEP-ANN framework, attractor states can be interpreted as learned priors that capture the statistical structure of the environment, while the stochastic dynamics implement posterior sampling. Orthogonal attractors emerge as an efficient way to span the subspace of interest, fostering generalization to unseen data (as long as it is from the subspace spanned by the existing attractors).

Next, we have demonstrated that fcANN models exhibit multiple biologically plausible attractor states, with large basins and showed that the relaxation dynamics of the reconstructed model display fast convergence to attractor states - another signature that the functional connectome being a valid proxy for the coupling weights of an underlying attractor network.
Relying on previous work, we can establish a relatively straightforward (although somewhat speculative) correspondence between attractor states and brain function, mapping brain activation on the axes of internal vs. external context {cite:p}`golland2008data; cioli2014differences`, as well as perception vs. action {cite:p}`fuster2004upper`.
In our framework, the attractor states can be interpreted as learned priors that capture the statistical structure of the environment, while the stochastic dynamics implement posterior sampling. This connection suggests that canonical resting-state networks may represent the brain's internal generative model of the world, continuously updated through the emergent learning dynamics we described theoretically.
Furthermore, the relation between fcANN models and the FEP-ANN framework substantiates that the reconstructed attractor states are not solely local minima in the state space but act as a driving force for the dynamic trajectories of brain activity.
We argue that attractor dynamics may be the main driving factor for the spatial and temporal autocorrelation structure of the brain, recently described to be predictive of network topology in relation to age, subclinical symptoms of dementia, and pharmacological manipulations with serotonergic drugs {cite:p}`shinn2023functional`. 
Nevertheless, attractor states should not be confused with the conventional notion of brain substates {cite:p}`chen2015introducing; https://doi.org/10.1016/j.celrep.2020.108128` and large-scale functional gradients {cite:p}`margulies2016situating`. In the fcANN framework, attractor states can rather be conceptualized as "Platonic idealizations" of brain activity, that are continuously approximated - but never reached - by the brain, resulting in re-occurring patterns (brain substates) and smooth gradual transitions (large-scale gradients).

Considering the functional connectome as weights of a neural network distinguishes our methodology from conventional biophysical and phenomenological computational modeling strategies, which usually rely on the structural connectome to model polysynaptic connectivity {cite:p}`cabral2017functional; deco2012anatomy; golos2015multistability; hansen2015functional`. Given the challenges of accurately modeling the structure-function coupling in the brain {cite:p}`seguin2023brain`, such models are currently limited in terms of reconstruction accuracy, hindering translational applications.
By working with direct, functional MRI-based activity flow estimates, fcANNs bypass the challenge of modeling the structural-functional coupling and are able to provide a more accurate representation of the brain's dynamic activity propagation (although at the cost of losing the ability to provide biophysical details on the underlying mechanisms).
Another advantage of the proposed model is its simplicity. While many conventional computational models rely on the optimization of a high number of free parameters, the basic form of the fcANN approach comprises solely two, easily interpretable  "hyperparameters" (temperature and noise) and yields notably consistent outcomes across an extensive range of these parameters ({numref}`Supplementary Figure %s <si_expl_variance_energy>`, {numref}`%s <si_att_state_emergence_over_beta>`, {numref}`%s <si_state_occupancy_null_models>`, {numref}`%s <si_pain_ghost_attractor_sim>`, {numref}`%s <si_downreg_trajectory_sim>`). To underscore the potency of this simplicity and stability, in the present work, we avoided any unnecessary parameter optimization, leaving a negligible chance of overfitting. It is likely, however, that extensive parameter optimization could further improve the accuracy of the model.

Further, the fcANN approach links brain dynamics directly to dynamical systems theory and the free energy principle, conceptualizes the emergence of large-scale canonical brain networks (Zalesky et al., 2014) in terms of multistability, and sheds light on the origin of characteristic task-responses that are accounted for by "ghost attractors" in the system {cite:p}`deco2012ongoing; vohryzek2020ghost`.
As fcANNs do not need to be trained to solve any explicit tasks, they are well suited to examine spontaneous brain dynamics. However, it is worth mentioning that fcANNs can also be further trained via the predictive coding-based learning rule of FEP-ANNs, to "solve" various tasks or to match developmental dynamics or pathological alterations. In this promising future direction, the training procedure itself becomes part of the model, providing testable hypotheses about the formation, and various malformations, of brain dynamics. A promising application of this is to consider structural brain connectivity (as measured by diffusion MRI) as a sparsity constraint for the coupling weights and then train the fcANN model to match the observed resting-state brain dynamics. If the resulting structural-functional ANN model is able to closely match the observed functional brain substate dynamics, it can be used as a novel approach to quantify and understand the structural functional coupling in the brain.

Given its simplicity, it is noteworthy how well the fcANN model is able to reconstruct and predict brain dynamics under a wide range of conditions.
First and foremost, we have found that the topology of the functional connectome seems to be well suited to function as an attractor network, as it converges much faster than the respective null models.
Second, we found that the two-dimensional fcANN projection can explain more variance in real (unseen) resting-state fMRI data than the first two principal components derived from the data itself. This may indicate that through the known noise tolerance of attractor neural networks, fcANNs are able to capture essential characteristics of the underlying dynamic processes even if our empirical measurements are corrupted by noise and low sampling rate.
Indeed, fcANN attractor states were found to be robust to noisy weights ({numref}`Supplementary Figure %s <si_noise_robustness_weights>`) and highly replicable across datasets acquired at different sites, with different scanners and imaging sequences (study 2 and 3). The observed high level of replicability allowed us to re-use the fcANN model constructed with the functional connectome of study 1 for all subsequent analyses, without any further fine-tuning or study-specific parameter optimization.

Both conceptually and in terms of analysis practices, resting and task states are often treated as separate phenomena. However, in the fcANN framework, the differentiation between task and resting states is considered an artificial dichotomy. 
Task-based brain activity in the fcANN framework is not a mere response to external stimuli in certain brain locations but a perturbation of the brain's characteristic dynamic trajectories, with increased preference for certain locations on the energy landscape ("ghost attractors").
In our analyses, the fcANN approach captured and predicted participant-level activity changes induced by pain and its self-regulation and gave a mechanistic account for how relatively small activity changes in a single region (NAcc) may result in a significantly altered pain experience.
Our control-signal analysis is different from, but compatible with, linear network control theory-based approaches {cite:p}`liu2011controllability; gu2015controllability`. Combining network control theory with the fcANN approach could provide a powerful framework for understanding the effects of various tasks, conditions, and interventions (e.g., brain stimulation) on brain dynamics.

Brain dynamics can not only be perturbed by task or other types of experimental or naturalistic interventions, but also by pathological alterations. Here we provide an initial demonstration (study 7) of how fcANN-based analyses can characterize and predict altered brain dynamics in autism spectrum disorder (ASD). The observed ASD-associated changes in brain dynamics are indicative of a reduced ability to flexibly switch between perception and internal representations, corroborating previous findings that in ASD, sensory-driven connectivity transitions do not converge to transmodal areas {cite:p}`hong2019atypical`. Such findings are in line with previous reports of a reduced influence of context on the interpretation of incoming sensory information in ASD (e.g., the violation of Weber's law) {cite:p}`hadad2019perception`.

Our findings open up a series of exciting opportunities for the better understanding of brain function in health and disease.
First, fcANN analyses may provide insights into the causes of changes in brain dynamics, by, for instance, identifying the regions or connections that act as an "Achilles' heel" in generating such changes. Such control analyses could, for instance, aid the differentiation of primary causes and secondary effects of activity or connectivity changes in various clinical conditions. Rather than viewing pathology as static connectivity differences, our approach suggests that disorders may reflect altered attractor landscapes that bias brain dynamics toward maladaptive states. This perspective could inform the development of targeted interventions that aim to reshape these landscapes through neurofeedback, brain stimulation, or pharmacological approaches.

Second, as a generative model, fcANNs provide testable predictions about the effects of various interventions on brain dynamics, including pharmacological modulations as well as non-invasive brain stimulation (e.g., transcranial magnetic or direct current stimulation, focused ultrasound, etc.) and neurofeedback. Obtaining the optimal stimulation or treatment target within the fcANN framework (e.g., by means of network control theory {cite:p}`liu2011controllability`) is one of the most promising future directions with the potential to significantly advance the development of novel, personalized treatment approaches.

Third, the theoretical integration of the fcANN model with the FEP-ANN framework positions our work within a broader scientific program that seeks to understand the brain as a self-organizing, information-processing system governed by fundamental physical and computational principles. The empirical validation of attractor orthogonality represents a crucial step toward establishing this unified framework for understanding brain function across scales and contexts.

The proposed approach is not without limitations. First, fcANNs do not incorporate information about anatomical connectivity and do not explicitly model biophysical details. Thus, in its present form, the model is not suitable to study the structure-function coupling and cannot yield mechanistic explanations underlying (altered) polysynaptic connections, at the level of biophysical details.
Nevertheless, our approach showcases that many characteristics of brain dynamics, like multistability, temporal autocorrelations, states and gradients, can be explained, and predicted, by a very simple nonlinear phenomenological model. 
Second, our model assumes a stationary functional connectome, which seems to contradict notions of dynamic connectivity. However, while the underlying FEP-ANN framework focuses on the long-term steady-state distribution of the system, it also naturally incorporates multistable fluctuations and the related dynamic connectivity changes through the stochastic relaxation dynamics. This is in line with the notion of "latent functional connectivity", an intrinsic brain network architecture built up from connectivity properties that are persistent across brain substates {cite:p}`https://doi.org/10.1162/netn_a_00234`.

In this initial work, we presented the simplest possible implementation of the fcANN concept. It is clear that the presented analyses exploit only a small proportion of the richness of the full state-space dynamics reconstructed by the fcANN model. 
There are many potential ways to further improve the utility of the fcANN approach. Increasing the number of reconstructed attractor states (by increasing the temperature parameter), investigating higher-dimensional dynamics, fine-tuning the hyperparameters, and testing the effect of different initializations and perturbations are all important directions for future work, with the potential to further improve the model's accuracy and usefulness.

## Conclusion

Here we have proposed a principled, lightweight, theory‑driven framework that instantiates the inference dynamics of free‑energy‑minimizing attractor networks (FEP‑ANNs) to model large‑scale brain activity. Initialized with empirical functional connectivity, the fcANN links brain connectivity to activity and identifies neurobiologically meaningful attractor states underlying large-scale brain dynamics. We demonstrated that the fcANN models display signs of attractor self-orthogonalization - a hallmark of FEP‑ANN systems. The proposed framework provides a simple, interpretable, and predictive basis for studying rest, task perturbations, and disease, and for model‑guided interventions.


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
Studies 1, 2 and 4 are available at openneuro.org (ds002608, ds002608, ds000140). Data for study 3 are available upon request. Data for studies 5-6 are available at the GitHub page of the project: https://github.com/pni-lab/connattractor. Study 7 is available at https://fcon_1000.projects.nitrc.org/indi/abide/, preprocessed data are available at http://preprocessed-connectomes-project.org/.
%+++
