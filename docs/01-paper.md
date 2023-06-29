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
This fluctuation is neither random, nor stationary over time [](https://doi.org/10.1073/pnas.1216856110), [](https://doi.org/10.1073/pnas.1400181111). It shows quasi-periodic properties ([](https://doi.org/10.1016/j.neuroimage.2013.09.029)), with a limited number of recurring patterns known as “brain states” ([](https://doi.org/10.1073/pnas.1705120114), [](https://doi.org/10.1073/pnas.1216856110), [](https://doi.org/10.1016/j.neuroimage.2010.05.081)).

Whole-brain dynamics have previously been characterized with various descriptive techniques ([](https://doi.org/10.1073/pnas.1121329109), [](https://doi.org/10.1073/pnas.1705120114), [](https://doi.org/10.1073/pnas.1216856110)), providing accumulating evidence not only for the existence, but also for the high neurobiological and clinical significance, of such dynamics ([](https://doi.org/10.1016/j.neuroimage.2013.05.079), [](https://doi.org/10.1073/pnas.1418031112), [](10.1038/s41467-020-18717-w)). However, due to the nature of such studies, the underlying driving forces remain elusive.

% Brain state dynamics can be assessed with multiple techniques, dynamic connectivity analysis (), including independent component analysis ([](https://doi.org/10.1073/pnas.1121329109)), hidden markov models ([](https://doi.org/10.1073/pnas.1705120114)) or point-process analyses to capture co-activation patterns (CAPs, [](https://doi.org/10.1073/pnas.1216856110), [](https://doi.org/10.1016/j.neuroimage.2015.01.057), [](https://doi.org/10.3389/fnsys.2013.00101), [](https://doi.org/10.1038/s41467-020-18717-w))

Questions regarding the mechanisms that cause these remarkable dynamics can be addressed through computational models, which have the potential to shift our understanding from mere associations to causal explanations.
Conventional computational approaches try to solve the puzzle by delving all the way down to the biophysical properties of single neurons and then aim to construct a model of larger neural populations, or even the entire brain ([](https://doi.org/10.1038/nn.4497)).
While such approaches have demonstrated numerous successful applications ([](https://doi.org/10.1038/s41593-018-0210-5), [](https://doi.org/10.1093/schbul/sby154)), the estimation of all the free parameters in such models presents a grand challenge. This limitation hampers the ability of these techniques to effectively bridge the gap between explanations at the level of single neurons and the complexity of behavior ([](https://doi.org/10.1038/nn.4497)).

An alternative approach, known as "neuroconnectomism" ([](https://doi.org/10.1038/s41583-023-00705-w)) shifts the emphasis from "biophysical fidelity" of models to "cognitive/behavioral fidelity" ([](https://doi.org/10.1038/s41593-018-0210-5)), by using artificial neural networks (ANNs) that were trained to perform various tasks, as brain models.
While this novel approach has already significantly contributed to expanding our understanding of the general computational principles of the brain (see https://doi.org/10.1038/s41583-023-00705-w), the requirement of training ANNs for specific tasks poses inherent limitations in their capacity to explain the spontaneous macro-scale dynamics of neural activity (https://doi.org/10.1038/s41593-019-0520-2).

In this work, we adopt a middle ground between traditional computational modeling and neuroconnectionism to investigate the phenomenon of brain dynamics.
On one hand, similar to neuroconnectionism, our objective is not to achieve a comprehensive bottom-up understanding of neural mechanisms. Instead, we utilize an artificial neural network (ANN) as a high-level computational model of the brain.
On the other hand, we do not train our ANN for a specific task. Instead, we empirically set its weights based on  data about the "activity flow" ([](http://dx.doi.org/10.1038/nn.4406), [](http://dx.doi.org/10.1038/s41467-017-01000-w)) across regions within the functional brain connectome, as measured with functional magnetic resonance imaging (fMRI). 
We employ a neurobiologically motivated ANN architecture, a continuous-space Hopfield network ([](https://doi.org/10.1073/pnas.79.8.2554), [](https://doi.org/10.1038/s42254-023-00595-y)).

Within this architecture, the topology of the functional connectome naturally defines an energy level for any arbitrary activation patterns and a trajectory towards one of the finite number of stable patterns that minimize this energy, the so-called attractor states.
Our model also offers a natural explanation for brain state dynamics.
In the presence of weak noise, the system does not converge into an equilibrium state but undergoes "bifurcation", enabling it to traverse extensive regions of the state space, moving on a path restricted by the "gravitational pull" of different attractor states.

In this simplistic yet powerful framework, both spontaneous and task-induced brain dynamics can be conceptualized as a high-dimensional path that meanders on the reconstructed energy landscape in a way that is restricted by the "gravitational pull" of the attractors states.
The framework provides a generative model for both resting state and task-related brain dynamics, offering novel perspectives on the mechanistic origins of resting state brain states and task-based activation maps.

In this study, we explore the attractor states of the functional brain connectome and construct a low-dimensional representation of the energy landscape.
Subsequently, we rigorously test the proposed model through a series of experiments conducted on data obtained from 7 studies encompassing a total of n≈2000 individuals.

These experiments provide converging evidence for the validity of connectome-based Hopfield networks as models of brain dynamics and demonstrate their potential to illuminate fundamental and translational questions in neuroscience.

> ToDo: more on the significance


# Results

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

- significance

> A further scenario rests on the role of ghost attractors [109](https://www.nature.com/articles/nn.4497#ref-CR109 "Deco, G. & Jirsa, V.K. Ongoing cortical activity at rest: criticality, multistability, and ghost attractors. J. Neurosci. 32, 3366–3375 (2012).", a dynamic landscape of remnant attractors each of which has an incomplete basin, hence allowing the system to 'wander' through large swathes of the phase space under the influence of weak noise [110](https://www.nature.com/articles/nn.4497#ref-CR110 "Tsuda, I. Toward an interpretation of dynamic neural activity in terms of chaotic dynamical systems. Behav. Brain Sci. 24, 793–810 discussion 810–848 (2001).").


# Methods

+++ {"part": "acknowledgements"}

Todo

+++

+++ {"part": "data-availability"}

Todo

+++
