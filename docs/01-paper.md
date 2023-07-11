---
title: The attractor states of the functional brain connectome
subject: Preprint
#subtitle: Optional Subtitle
short_title: ConnAttractor Preprint
authors:
    - name: Robert Englert
      affiliations:
        - University Medicine Essen
      #orcid: 0000-0002-7859-8394
      email: robert.englert@uk-essen.de

    - name: Tamas Spisak
      affiliations:
        - University Medicine Essen
      #orcid: 0000-0002-7859-8394
      email: tamas.spisak@uk-essen.de
      corresponding: True

exports:
  - format: pdf
    template: arxiv_nips
    output: exports/connattractor_manuscript.pdf
#  - format: docx
#    template: curvenote
#    output: exports/connattractor_manuscript.docx
---
+++ {"part": "key-points"}
**Key Points:**

- We propose a high-level computational model of "activity flow" across brain regions
- The model considers the funcional brain connectome as an already-trained Hopfield neural network
- It defines an energy level for any arbitrary brain activation patterns
- and a trajectory towards one of the finite number of stable patterns (attractor states) that minimize this energy
- The model reproduces and explains the dynamic repertoir of the brain's spontanous activity at rest
- It conceptualizes both task-induced and pathological changes in brain activity as a shift on the "attractor landscape"
- We validate our findings on healthy and clinical samples (~2000 participants)

+++

+++ {"part": "abstract"}

**Abstract:**

todo

+++

# Introduction

Brain function is characterized by the continuous activation and deactivation of anatomically distributed neuronal populations.
While the focus of related research is often on the direct mapping between changes in the activity of a single brain area and a specific task or condition, in reality, regional activation never seems to occur in isolation ([](https://doi.org/10.1038/nn.4502)).
Regardless of the presence or absence of explicit stimuli, brain regions seem to work in concert, resulting in a rich and complex spatiotemporal fluctuation ([](https://doi.org/10.1016/j.cub.2019.06.017)).
This fluctuation is neither random, nor stationary over time [](https://doi.org/10.1073/pnas.1216856110); [](https://doi.org/10.1073/pnas.1400181111). It shows quasi-periodic properties ([](https://doi.org/10.1016/j.neuroimage.2013.09.029)), with a limited number of recurring patterns known as “brain states” ([](https://doi.org/10.1073/pnas.1705120114); [](https://doi.org/10.1073/pnas.1216856110); [](https://doi.org/10.1016/j.neuroimage.2010.05.081)).

Whole-brain dynamics have previously been characterized with various descriptive techniques ([](https://doi.org/10.1073/pnas.1121329109); [](https://doi.org/10.1073/pnas.1705120114); [](https://doi.org/10.1073/pnas.1216856110)), providing accumulating evidence not only for the existence, but also for the high neurobiological and clinical significance, of such dynamics ([](https://doi.org/10.1016/j.neuroimage.2013.05.079); [](https://doi.org/10.1073/pnas.1418031112); [](10.1038/s41467-020-18717-w)). However, due to the nature of such studies, the underlying driving forces remain elusive.

% Brain state dynamics can be assessed with multiple techniques, dynamic connectivity analysis (), including independent component analysis ([](https://doi.org/10.1073/pnas.1121329109)), hidden markov models ([](https://doi.org/10.1073/pnas.1705120114)) or point-process analyses to capture co-activation patterns (CAPs, [](https://doi.org/10.1073/pnas.1216856110); [](https://doi.org/10.1016/j.neuroimage.2015.01.057); [](https://doi.org/10.3389/fnsys.2013.00101); [](https://doi.org/10.1038/s41467-020-18717-w))

Questions regarding the mechanisms that cause these remarkable dynamics can be addressed through computational models, which have the potential to shift our understanding from mere associations to causal explanations.
Conventional computational approaches try to solve the puzzle by delving all the way down to the biophysical properties of single neurons and then aim to construct a model of larger neural populations, or even the entire brain ([](https://doi.org/10.1038/nn.4497)).
While such approaches have demonstrated numerous successful applications ([](https://doi.org/10.1038/s41593-018-0210-5); [](https://doi.org/10.1093/schbul/sby154)), the estimation of all the free parameters in such models presents a grand challenge. This limitation hampers the ability of these techniques to effectively bridge the gap between explanations at the level of single neurons and the complexity of behavior ([](https://doi.org/10.1038/nn.4497)).

An alternative approach, known as "neuroconnectomism" ([](https://doi.org/10.1038/s41583-023-00705-w)) shifts the emphasis from "biophysical fidelity" of models to "cognitive/behavioral fidelity" ([](https://doi.org/10.1038/s41593-018-0210-5)), by using artificial neural networks (ANNs) that were trained to perform various tasks, as brain models.
While this novel approach has already significantly contributed to expanding our understanding of the general computational principles of the brain (see [](https://doi.org/10.1038/s41583-023-00705-w)), the requirement of training ANNs for specific tasks poses inherent limitations in their capacity to explain the spontaneous macro-scale dynamics of neural activity ([](https://doi.org/10.1038/s41593-019-0520-2)).

In this work, we adopt a middle ground between traditional computational modeling and neuroconnectionism to investigate the phenomenon of brain dynamics.
On one hand, similar to neuroconnectionism, our objective is not to achieve a comprehensive bottom-up understanding of neural mechanisms. Instead, we utilize an artificial neural network (ANN) as a high-level computational model of the brain ({numref}`concept`A).
On the other hand, we do not train our ANN for a specific task. Instead, we empirically set its weights based on  data about the "activity flow" ([](http://dx.doi.org/10.1038/nn.4406); [](http://dx.doi.org/10.1038/s41467-017-01000-w)) across regions within the functional brain connectome, as measured with functional magnetic resonance imaging (fMRI, {numref}`concept`B).
We employ a neurobiologically motivated ANN architecture, a continuous-space Hopfield network ([](https://doi.org/10.1073/pnas.79.8.2554); [](https://doi.org/10.1038/s42254-023-00595-y)).

Within this architecture, the topology of the functional connectome naturally defines an energy level for any arbitrary activation patterns and a trajectory towards one of the finite number of stable patterns that minimize this energy, the so-called attractor states.
Our model also offers a natural explanation for brain state dynamics.
In the presence of weak noise, the system does not converge into an equilibrium state but undergoes "bifurcation", enabling it to traverse extensive regions of the state space, moving on a path restricted by the "gravitational pull" of different attractor states ({numref}`concept`C).

:::{figure} figures/concept.png
:name: concept
**Connectome-based Hopfield networks as models of macros-scale brain dynamics.** <br/><br/>
**A)** Hopfield artificial neural networks (ANNs)  are a form of recurrent ANNs that serve as content-addressable ("associative") memory systems. Hopfield networks can be trained to store a finite number of patterns (e.g. via Hebbian learning). During the training procedure, the weights of the Hopfield ANN are trained so that the stored patterns become stable attractor states of the network. Thus, when the trained network is presented partial or noisy variations of the stored patterns, it can effectively reconstruct the original pattern via an iterative relaxation procedure that converges to the attractor states.
**B)** Instead of training the Hopfield network to specific tasks, we use the topology of the functional brain connectome to define the weights of the Hopfield network. Following form the strong analogies between the relaxation rule of Hopfield networks and the activity flow principle that links activity to connectivity in brain networks, we propose the constructed connectome-based Hopfield network as a computational model for macro-scale brain dynamics.  **C)** The proposed computational framework assigns an energy level, an attractor state and a position in a low-dimensional embedding to brain activation patterns. Additionally, it models how the whole state-space of viable activation patterns is restricted by the dynamics of the system how alterations in activity and/or connectivity modify these dynamics.
:::

In this simplistic yet powerful framework, both spontaneous and task-induced brain dynamics can be conceptualized as a high-dimensional path that meanders on the reconstructed energy landscape in a way that is restricted by the "gravitational pull" of the attractors states.
The framework provides a generative model for both resting state and task-related brain dynamics, offering novel perspectives on the mechanistic origins of resting state brain states and task-based activation maps.

In the present work, we first explore the attractor states of the functional brain connectome and construct a low-dimensional representation of the energy landscape.
Subsequently, we rigorously test the proposed model through a series of experiments conducted on data obtained from 7 studies encompassing a total of n≈2000 individuals. 

These analyses include evaluation of robustness and replicability, testing the model's ability to reconstrcut various characteristics of resting state brain dynamics as well as its capacity to detect and explain changes induced by tasks or pathological conditions.

These experiments provide converging evidence for the validity of connectome-based Hopfield networks as models of brain dynamics and highlight their potential to provide a fresh perspective on a wide range  of research questions in basic and translational neuroscience.

# Results

## Connectome-based Hopfield network as a model of brain dynamics

First, we explored the attractor states of the functional brain connectome in a sample of n=41 healthy young participants (study 1). We estimated interregional activity flow ([](http://dx.doi.org/10.1038/nn.4406); [](http://dx.doi.org/10.1038/s41467-017-01000-w)) as the study-level average of regularized partial correlations among the resting state fMRI timeseries of m = 122 functionally defined brain regions (BASC brain atlas, see Methods for details). We then used the standardized functional connectome as the $w_{ij}$  weights of a continuous-state Hopfield network ([](https://doi.org/10.1073/pnas.79.8.2554), [](https://doi.org/10.1162/neco.1994.6.3.459)) consisting of $m$ neural units, each having an activity $a_i \in [-1,1]$. Hopfield networks can be initialized by an arbitrary activation pattern ($m$ activations) and iteratively updated, until convergence ("relaxation"), according to the following equation:

```{math}
:label: hopfield-update
\dot{a}_i = S(\beta \sum_{j=1}^m w_{ij}a_j - b_i)
```

where $\dot{a}_i$ is the activity of neural unit $i$ in the next iteration and $S(a_j)$ is the sigmoidal activation function $S(a) = tanh(a)$ and $b_i$ is the bias of unit $i$ and $\beta$ is the so-called temperature parameter. For the sake of simplicity, we set $b_i=0$ in all our experiments.
Importantly, in our implementation, the relaxation of the Hopfield network can be conceptualized as the repeated application of the activity flow principle, simultaneously for all regions: $\dot{a}_i = \sum_{j=1}^m w_{ij}a_j$. The update rule also exhibits strong analogies with the inner workings of neural mass models  ([](https://doi.org/10.1038/nn.4497)) as applied e.g. in dynamic causal modelling (see Discussion for more details).

Hopfiled networks assign an energy to every possible activity configurations (see Methods), which decreases during the relaxation procedure until reaching an equilibrium state with minimal energy ({numref}`attractors`A, top panel, [](https://doi.org/10.1073/pnas.79.8.2554); [](https://doi.org/10.1162/neco.1994.6.3.459)).
We used a large number of random initializations to obtain all possible attractor states of the connectome-based Hopfield network in study 1 ({numref}`attractors`A, bottom panel).

:::{figure} figures/embedding_method.png
:name: attractors
Empirical Hopfield-networks.
:::

We observed that, in line with theory, increasing the temperature parameter $\beta$ results in an increasing number of attractor states (({numref}`attractors`E, left) appearing in symmetric pairs (i.e. $a_i = -a_j$). For the sake of simplicity, we set $\beta=0.4$ for the rest of the paper, resulting in 4 distinct attractor states (2 symmetric pairs).

Without modifications, connectome-based Hopfield networks always converge to an equilibrium state. To account for stochastic fluctuations in neuronal activity ([](https://doi.org/10.1098/rstb.2005.1638)), we add weak Gaussian noise to the connectome-based Hopfield network, to prevent the system reaching equilibrium. This approach, similarly to Stochastic DCM ([](https://doi.org/10.1016/j.neuroimage.2012.04.061))), induces a "stochastic walk" of the internal state (activity pattern) of the network that may traverse extensive regions of the state space, determined by the "gravity field" (basins) of multiple attractor states ({numref}`attractors`B).

We hypothesise that the resulting dynamics reflect many important characteristics of spontaneous activity fluctuations in the brain and may serve as a useful generative computational model of large scale brain dynamics. To sample the resulting state space, we obtained 100.000 iterations (starting from a random seed pattern) of the stochastic relaxation procedure with a Hopfield network initialized with the mean functional connectome in study 1 (n=44).
 Next, to increase interpretability, we obtained the first two components from a principal component analysis (PCA) on the resulting state space sample to construct a low-dimensional embedding. Largely independent on the free parameter $\sigma$ (variance of the noise), the first two principal components (PCs) explained around 15% of the variance in the state space, with low energy states (attractor states) located at the extremes of the PCs ({numref}`attractors`B, bottom plot).
The PCA embedding was found to be largely consistent across different values of $\beta$ and $\sigma$ ({numref}`attractors`E). For all further analyses, we fixed $\sigma=0.37$, as a result of a coarse optimization procedure to reconstruct the bimodal distribution of empirical data on the same projection ({numref}`attractors`E, see Methods for details)
On the low-dimensional embedding, which we refer to as the *Hopfield projection*, we observed a clear separation of the attractor states ({numref}`attractors`C), with the two symmetric pairs of attractor states located at the extremes of the first and second PC.
To map the attractor basins onto the space spanned by the first two PCs ({numref}`attractors`C), we obtained the attractor state of each point visited during the stochastic relaxation and fit a multinomial logistic regression model to predict the attractor state from the first two PCs. The resulting model achieved a high prediction accuracy (out-of-sample accuracy 96.5%). Attractor bases were visualized based on the decision boundaries of this  model ({numref}`attractors`C).
.We propose the Hopfield projection depicted on ({numref}`attractors`C) as a simplified representation of brain dynamics, as modelled by connectome-based Hopfield networks, and use it as a basis for all subsequent analyses in this work.



## Connectome-based Hopfield networks capture key features of resting state brain dynamics

The obtained attractor states resemble familiar, neurobiologically highly plausible patterns ({numref}`rest-validity`A). The first pair of attractors (mapped on PC1) resemble the two complementary “macro” systems described by [](https://doi.org/10.1016/j.neuropsychologia.2007.10.003) and [](https://doi.org/10.1371/journal.pone.0115913): an “extrinsic” system that is more directly linked to the immediate sensory environment and an “intrinsic” system whose activity preferentially relates to changing higher-level, internal context (a.k.a the default mode network). The other attractor pair spans an orthogonal axis between regions commonly associated with active (motor) and passive inference (visual).

During stochastic relaxation, the connectome-based Hopfield network spends three-quarter of the time on the basis of the first two attractor states (equally distributed across the two) and one-quarter on the basis of the second pair (again equally distributed). To test if this characteristic can also be found in real resting state data, we obtained normalized and cleaned mean timeseries in $m=122$ regions from all participants in study 1 obtained the attractor state of each time-frame via the connectome-based Hopfield network. We observed highly similar temporal occupancies to those predicted by the model ($\Chi^2$-test of equal occupancies: p<0.00001, {numref}`rest-validity`B). 

:::{figure} figures/face_validity.png
:name: rest-validity
Empirical Hopfield-networks reconstruct real resting state brain activity.
:::

Importantly, the first two component of the Hopfield projection explained significantly more variance in the real resting state fMRI data in study 1 and generalized better to study 2 (see {numref}`samples` for more details on the studies) than PCA on the real regional timeseries data ({numref}`rest-validity`C).
Attractor states were also found to exhibit a remarkable replicability (mean Pearson's correlation **XX**) across the discovery datasets (study 1) and two independent replication datasets (study 2 and 3, {numref}`rest-validity`E).


> Additional emergent collective properties include some capacity for generalization, familiarity recognition, categorization, error correction, and time sequence retention. The collective properties are only weakly sensitive to details of the modeling or the failure of individual devices. [](https://doi.org/10.1073/pnas.79.8.2554)

> Due to the known noise-tolerance of the applied eANN-s, the proposed approach can be expected to be highly robust/reliable/replicable, which we demonstrate with independent datasets (total n=xxx).


:::{figure} figures/task_validity.png
:name: task-validity
Empirical Hopfield-networks reconstruct real task-based brain activity.
:::

:::{figure} figures/state_analysis.*
:name: clinical-validity
Outlook: Empirical Hopfield-networks' clinical validity.
:::

Here I refer to {numref}`rest-validity`.

# Discussion

## Neurobiological validity

The activity flow principle has been shown to successfully predict held out brain activations by combining the activations and connection weights to the target region [1]. The proposed empirical Hopfield network builds on the knowledge derived from this framework, combining the architecture of a Hopfield network with the connectome as its pre-trained weights. Given an input activation for every region, the network will iterate upon this input state until a mathematical minimum is reached, producing an attractor state. An attractor state represents a configuration of activations in every region and is considered a recalled memory of the network. The network topology is multistable, producing different stable attractor states based on the temperature of the network and the initial activation pattern, which stimulates the network.

- significance

> A further scenario rests on the role of ghost attractors [109](https://www.nature.com/articles/nn.4497#ref-CR109 "Deco, G. & Jirsa, V.K. Ongoing cortical activity at rest: criticality, multistability, and ghost attractors. J. Neurosci. 32, 3366–3375 (2012).", a dynamic landscape of remnant attractors each of which has an incomplete basin, hence allowing the system to 'wander' through large swathes of the phase space under the influence of weak noise [110](https://www.nature.com/articles/nn.4497#ref-CR110 "Tsuda, I. Toward an interpretation of dynamic neural activity in terms of chaotic dynamical systems. Behav. Brain Sci. 24, 793–810 discussion 810–848 (2001).").

# Methods

```{list-table}
:header-rows: 1
:name: samples

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
  - >todo
  - >todo
  - [](https://doi.org/10.1371/journal.pbio.1002036)
* - study 5 (ABIDE)
  - resting state
  - Autism Spectrum Disorder
  - ASD: 98, NC: 74
  - >todo
  - >todo
  - >todo
* - study 6 (ADNI)
  - resting state
  - Alzheimer's Disease vs. Mild Cognitive Impairment
  - AD:, MCI: 
  - >todo
  - >todo
  - >todo
* - study 7 (COBRE)
  - resting state
  - Schizophrenia
  - SCH: , HC:
  - >todo
  - >todo
  - >todo
```

## Hopfield network

The weights $w_{ij}$ have to be symmetric and the diagonal elements are set to zero.

+++ {"part": "acknowledgements"}

Todo

+++

+++ {"part": "data-availability"}

Todo

+++
