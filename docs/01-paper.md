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

:::{figure} figures/concept.*
:name: concept
**Connectome-based Hopfield networks as models of macros-scale brain dynamics.** <br/><br/>
**A)** Hopfield artificial neural networks (ANNs)  are a form of recurrent ANNs that serve as content-addressable ("associative") memory systems. Hopfield networks can be trained to store a finite number of patterns (e.g. via Hebbian learning). During the training procedure, the weights of the Hopfield ANN are trained so that the stored patterns become stable attractor states of the network. Thus, when the trained network is presented partial or noisy variations of the stored patterns, it can effectively reconstruct the original pattern via an iterative relaxation procedure that converges to the attractor states.
**B)** Instead of training the Hopfield network to specific tasks, we use the topology of the functional brain connectome to define the weights of the Hopfield network. Following form the strong analogies between the relaxation rule of Hopfield networks and the activity flow principle that links activity to connectivity in brain networks, we propose the constructed connectome-based Hopfield network as a computational model for macro-scale brain dynamics.  **C)** The proposed computational framework assigns an energy level, an attractor state and a position in a low-dimensional embedding to brain activation patterns. Additionally, it models how the whole state-space of viable activation patterns is restricted by the dynamics of the system how alterations in activity and/or connectivity modify these dynamics.
:::

In this simplistic yet powerful framework, both spontaneous and task-induced brain dynamics can be conceptualized as a high-dimensional path that meanders on the reconstructed energy landscape in a way that is restricted by the "gravitational pull" of the attractors states.
The framework provides a generative model for both resting state and task-related brain dynamics, offering novel perspectives on the mechanistic origins of resting state brain states and task-based activation maps.

In this study, we explore the attractor states of the functional brain connectome and construct a low-dimensional representation of the energy landscape.
Subsequently, we rigorously test the proposed model through a series of experiments conducted on data obtained from 7 studies encompassing a total of n≈2000 individuals.

These experiments provide converging evidence for the validity of connectome-based Hopfield networks as models of brain dynamics and demonstrate their potential to illuminate fundamental and translational questions in neuroscience.

# Results

First, we explored the attractor states of the functional brain connectome in a sample of n=41 healthy young participants (Study 1). We estimated activity flow in the connectome ([](http://dx.doi.org/10.1038/nn.4406); [](http://dx.doi.org/10.1038/s41467-017-01000-w)) as the study-level average of regularized partial correlations among the resting state fMRI timeseries of m = 122 functionally defined brain regions (see Methods). We then used the standardized functional connectome as the $w_{ij}$  weights of a continuous-state Hopfield network ([](https://doi.org/10.1073/pnas.79.8.2554), [](https://doi.org/10.1162/neco.1994.6.3.459)) consisting of $m$ neural units, each having an activity $a_i \in [-1,1]$. We then repeatedly initialized the Hopfield network with random input activations and iteratively updated it, until convergence ("relaxation"), according to the following equation:

```{math}
:label: hopfield-update
\dot{a}_i = S(\beta \sum_{j=1}^m w_{ij}a_j - b_i)
```

where $\dot{a}_i$ is the activity of neural unit $i$ in the next iteration and $S(a_j)$ is the sigmoidal activation function $S(a) = tanh(a)$ and $b_i$ is the bias of unit $i$ and $\beta$ is the so-called temperature parameter. The weights $w_{ij}$ are symmetric and the diagonal elements are set to zero.
Importantly, in our implementation, the relaxation of the Hopfield network is in a close analog of the simultaneous and integrative application of the activity flow principle: $\dot{a}_i = \sum_{j=1}^m w_{ij}a_j$, as well as with the inner workings of with neural mass models  ([](https://doi.org/10.1038/nn.4497)).

Hopfiled networks assign an energy to every possible activity configurations (see Methods). which decreases during the relaxation procedure until reaching an equilibrium state with minimal energy ({numref}`attractors`A, [](https://doi.org/10.1073/pnas.79.8.2554); [](https://doi.org/10.1162/neco.1994.6.3.459)).

Similarly to neural mass models ([](https://doi.org/10.1098/rstb.2005.1638)), adding weak Gaussian noise to the connectome-based Hopfield network prevents the system reaching equilibrium and induces a stochastic walk that may traverse extensive regions of the state space, visiting the basins of multiple attractor states ({numref}`attractors`B).

To construct a low-dimensional embedding of the resulting state space, we applied principal component analysis (PCA) to the states visited during this stochastic walk. Largely independnet on the free parameters $\beta$ (temperature) and $\sigma$ (variance of the noise), the first two principal components (PCs) explained **XX**% of the variance in the state space.

On the low-dimensional embedding, which we refer to as the Hopfield state space projection, we observed a clear separation of the attractor states ({numref}`attractors`C), with the first PC aligned with an attractor-state pair similar to the default mode network (DMN) and the second PC an attractor state-pair differentiating between sensory-motor and visual regions. The Hopfield state space projection was largely consistent across different values of $\sigma$ and different datasets  (see Methods).

To identify the attractor basins on the reconstructed state space ({numref}`attractors`C), we obtained the attractor state of each point visited during the stochastic walk and fit a multinomial logistic regression model to predict the attractor state from the first two PCs. The resulting model achieved a high prediction accuracy (**XX**% in study 1, with $\beta$=0.04 and $\sigma=0.37$, see Supplementary Material X for other parameter settings). Attractor bases were visualized based on the decision boundaries of this  model ({numref}`attractors`C).



The number of attractor states depends on the temperature of the network ($\beta$ in Eq. [](#hopfield-update)), with higher temperatures leading to more attractor states. In the limit of infinite temperature, the network is reduced to a random walk on the state space, with no attractor states. In the limit of zero temperature, the network is reduced to a deterministic system with a single attractor state. In the intermediate regime, the network is multistable, with a finite number of attractor states ({numref}`attractors`D).

> ToDo: Description of the attractor states, we chose to go with 4, for the sake if simplicity

:::{figure} figures/embedding_method.*
:name: attractors
Empirical Hopfield-networks.
:::

- introduce the idea in more detail (fig 1)
  - attractor states and added noise
  - construcct validity
- attractor states (fig 1)
- face validity
- clinical validity

> Due to the known noise-tolerance of the applied eANN-s, the proposed approach can be expected to be highly robust/reliable/replicable, which we demonstrate with independent datasets (total n=xxx).

:::{figure} figures/method_overview.*
:name: overview
Empirical Hopfield-networks.
:::

:::{figure} figures/face_validity.png
:name: face-val
Empirical Hopfield-networks reconstruct real brain activity.
:::

:::{figure} figures/state_analysis.*
:name: clinical_validity
Empirical Hopfield-networks.
:::

Here I refer to {numref}`face-val`.

# Discussion

# Neurobiological validity

The activity flow principle has been shown to successfully predict held out brain activations by combining the activations and connection weights to the target region [1]. The proposed empirical Hopfield network builds on the knowledge derived from this framework, combining the architecture of a Hopfield network with the connectome as its pre-trained weights. Given an input activation for every region, the network will iterate upon this input state until a mathematical minimum is reached, producing an attractor state. An attractor state represents a configuration of activations in every region and is considered a recalled memory of the network. The network topology is multistable, producing different stable attractor states based on the temperature of the network and the initial activation pattern, which stimulates the network.

- significance

> A further scenario rests on the role of ghost attractors [109](https://www.nature.com/articles/nn.4497#ref-CR109 "Deco, G. & Jirsa, V.K. Ongoing cortical activity at rest: criticality, multistability, and ghost attractors. J. Neurosci. 32, 3366–3375 (2012).", a dynamic landscape of remnant attractors each of which has an incomplete basin, hence allowing the system to 'wander' through large swathes of the phase space under the influence of weak noise [110](https://www.nature.com/articles/nn.4497#ref-CR110 "Tsuda, I. Toward an interpretation of dynamic neural activity in terms of chaotic dynamical systems. Behav. Brain Sci. 24, 793–810 discussion 810–848 (2001).").

# Methods

```{list-table} Overview of study sampels
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
* - study 3 (ABIDE)
  - resting state
  - Autism Spectrum Disorder
  - ASD: 98, NC: 74
  - >todo
  - >todo
  - >todo
* - study 4 (ADNI)
  - resting state
  - Alzheimer's Disease vs. Mild Cognitive Impairment
  - AD:, MCI: 
  - >todo
  - >todo
  - >todo
* - study 5 (COBRE)
  - resting state
  - Schizophrenia
  - SCH: , HC:
  - >todo
  - >todo
  - >todo
* - study 6
  - task-based
  - pain self-regulation
  - 33
  - >todo
  - >todo
  - [](https://doi.org/10.1371/journal.pbio.1002036)
```



+++ {"part": "acknowledgements"}

Todo

+++

+++ {"part": "data-availability"}

Todo

+++
