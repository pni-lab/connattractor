---
title: The attractor states of the functional brain connectome
subject: Preprint
#subtitle: Evolve your markdown documents into structured data
short_title: The paper
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

exports:
  - format: pdf
    template: arxiv_nips
    output: exports/connattractor_manuscript.pdf
  - format: docx
    output: exports/connattractor_manuscript.docx
---

+++ {"part": "key-points"}
**Highglights:**
- a
- b

+++

+++ {"part": "abstract"}

Todo

+++

# Introduction

Functional brain connectomics studies the spontaneous co-activation of brain regions and has revolutionized our understanding of the physical basis of mind [ref]. The majority of fMRI connectivity studies assume temporal stationarity, i.e. that the brain connectivity is static for the entire data acquisition period. Such studies have provided a wealth of insights into the neural mechanisms of several behavioral/psychological phenotypes and clinical conditions. However, functional connectivity has been shown to be dynamic; it fluctuates spontaneously over time in a globally coordinated manner. Dynamic functional connectivity has quasi periodic properties (ref), with a limited number of recurring states (“brain states”) [](https://doi.org/10.1016/j.cub.2019.06.017); i.e. sporadic intervals during which information can be efficiently exchanged between a characteristic subset of brain regions [Hutchison et al., 2013, Liu 2013 PNAS, Zalesky, PNAS, 2014]. Brain state dynamics can be assessed with multiple techniques, including independent component analysis (ref), co-activation patterns (Liu 2013 PNAS), … and there is accumulating evidence for the neurobiological relevance of these dynamics, with promising perspectives for facilitating the clinical translation of functional neuroimaging techniques by improving brain based biomarkers (Woo, Nat Med. 2021). 

However, progress is limited by gaps in the mechanistic understanding of how brain activity and functional connectivity dynamically shape each other and how this process leads to the emergence and organization of brain states (ref). 

Here we propose a novel model-based framework that - with minimal, but reasonable assumptions about the “activity flow” (ref: Cole-papers) between two, functionally connected regions - considers the stationary functional brain network as an empirical (i.e. already-trained) artificial neural network (eANN). In the proposed framework, the topology of the stationary brain connectome defines a cost (energy) for any arbitrary brain activation patterns and a trajectory towards one of the finite number of stable patterns that minimize this cost (so-called attractor states).  

Here we propose these attractors states as robust and biomedically relevant characteristics of the functional brain connectome, with a wide variety of potential applications.  

We demonstrate that the proposed attractor states highly resemble to the dynamic brain states commonly observed by dynamic functional connectivity methods (e.g. CAP-analyses (ref)) and provide a proof-of-concept for the biomedical validity of our framework, by showing that the average brain activations corresponding to the attractor states during resting sate display manifold significant associations to cognition. 

Due to the known noise-tolerance of the applied eANN-s, the proposed approach can be expected to be highly robust/reliable/replicable, which we demonstrate with independent datasets (total n=xxx). 

List all the aims: hierarchy, generalizability etc 

# Results

:::{figure} figures/face_validity.*
:name: face-val
Empirical Hopfiled-networks reconstruct real brain activity.
:::

Here I refer to {numref}`face-val`.

# Discussion

# Methods

+++ {"part": "acknowledgements"}

Todo

+++

+++ {"part": "data-availability"}

Todo

+++

