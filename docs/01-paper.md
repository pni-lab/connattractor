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
#  - format: docx
#    template: curvenote
#    output: exports/connattractor_manuscript.docx
---
+++ {"part": "key-points"}
**Highglights:**

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



Brain function is accompanied by the activation and deactivation of anatomically distributed neuronal populations. While changes in the activity of a single brain area is often associated with various tasks or conditions, in reality, regional activation never occurs in isolation (ref). Regardless of the presence or absence of explicit stimuli, brain regions seem to work in concert, resulting in a rich and complex spatiotemporal fluctuation over time. This fluctuation shows quasi-periodic properties ([](https://doi.org/10.1016/j.neuroimage.2013.09.029 "Persistent link using digital object identifier")), with a limited number of recurring states known as “brain states” ([](https://doi.org/10.1016/j.cub.2019.06.017), [](https://doi.org/10.1073/pnas.1705120114)). These states are often interpreted as sporadic intervals during which information can be efficiently exchanged between a characteristic subset of brain regions ([](https://doi.org/10.1016/j.neuroimage.2013.05.079), [](https://doi.org/10.1073/pnas.1216856110), [](https://doi.org/10.1073/pnas.1400181111)). Brain state dynamics can be assessed with multiple techniques, including independent component analysis (ref), co-activation patterns ([](https://doi.org/10.1073/pnas.1216856110)) and hidden markov models ([](https://doi.org/10.1073/pnas.1705120114)).

While such efforts, by their nature, do not shed light on the driving forces of the complex spatiotemporal dance of brain acctity, they provide accumulating evidence for the neurobiological relevance of these dynamics, with promising perspectives for facilitating the clinical translation of functional neuroimaging techniques ([](https://doi.org/10.1038/s41591-020-1142-7)).

Why does such interregional communication manifest in co-activation? Which activiy configurations does the brain visit and which not? How do these relate to each other? How does this dyanmic repertoir of activation patterns result in task-related activity maps, as obtained with functional magnetic resonance imaging? What is the meaning of activity and connectivity differences across individuals or in various clinical conditions?

Traditional tools of computational neuroscience try to address these and similar questions whith methods of varying complexity from those based on the Fokker–Planck equation, to neural mass and neural field models. Commons amongst these models is the assumption that spatiotemporal patterns of neural dynamics arise from interactions between functionally specialized cell populations connected by a topologically complex array of short- and long-range axonal connections([](https://doi.org/10.1038/nrn2575), [](https://doi.org/10.1038/nrn3962)), the latter ofen being estimated at macroscopic scales by diffusion magnetic resonance imaging (dMRI).

These models have found broad success in modeling seizures^[11](https://www.nature.com/articles/nn.4497#ref-CR11 "Breakspear, M. et al. A unifying explanation of primary generalized seizures through nonlinear brain modeling and bifurcation analysis. Cereb. Cortex 16, 1296–1313 (2006).")^, encephalopathies^[12](https://www.nature.com/articles/nn.4497#ref-CR12 "Roberts, J.A., Iyer, K.K., Finnigan, S., Vanhatalo, S. & Breakspear, M. Scale-free bursting in human cortex following hypoxia at birth. J. Neurosci. 34, 6557–6572 (2014)."),[13](https://www.nature.com/articles/nn.4497#ref-CR13 "Bojak, I., Stoyanov, Z.V. & Liley, D.T. Emergence of spatially heterogeneous burst suppression in a neural field model of electrocortical activity. Front. Syst. Neurosci. 9, 18 (2015).")^, sleep^[14](https://www.nature.com/articles/nn.4497#ref-CR14 "Phillips, A.J. & Robinson, P.A. A quantitative model of sleep-wake dynamics based on the physiology of the brainstem ascending arousal system. J. Biol. Rhythms 22, 167–179 (2007).")^, anesthesia^[15](https://www.nature.com/articles/nn.4497#ref-CR15 "Bojak, I. & Liley, D.T. Modeling the effects of anesthesia on the electroencephalogram. Phys. Rev. E 71, 041902 (2005).")^, resting-state brain networks^[16](https://www.nature.com/articles/nn.4497#ref-CR16 "Honey, C.J., Kötter, R., Breakspear, M. & Sporns, O. Network structure of cerebral cortex shapes functional connectivity on multiple time scales. Proc. Natl. Acad. Sci. USA 104, 10240–10245 (2007)."),[17](https://www.nature.com/articles/nn.4497#ref-CR17 "Deco, G., Jirsa, V., McIntosh, A.R., Sporns, O. & Kötter, R. Key role of coupling, delay, and noise in resting brain fluctuations. Proc. Natl. Acad. Sci. USA 106, 10302–10307 (2009).")^ and the human alpha rhythm^[18](https://www.nature.com/articles/nn.4497#ref-CR18 "Robinson, P.A., Rennie, C.J. & Rowe, D.L. Dynamics of large-scale brain activity in normal arousal states and epileptic seizures. Phys. Rev. E 65, 041924 (2002)."),[19](https://www.nature.com/articles/nn.4497#ref-CR19 "Freyer, F. et al. Biophysical mechanisms of multistability in resting-state cortical rhythms. J. Neurosci. 31, 6353–6361 (2011).")^, and as a tool for multimodal data fusion^[20](https://www.nature.com/articles/nn.4497#ref-CR20 "Valdes-Sosa, P.A. et al. Model driven EEG/fMRI fusion of brain oscillations. Hum. Brain Mapp. 30, 2701–2721 (2009).")^. Technical advances in model inversion (estimating the likelihood and parameters of a model from empirical data) place mean field models within reach of widespread application to cognitive neuroscience^[21](https://www.nature.com/articles/nn.4497#ref-CR21 "Daunizeau, J., Stephan, K.E. & Friston, K.J. Stochastic dynamic causal modelling of fMRI data: should we care about neural noise? Neuroimage 62, 464–481 (2012).")^.

*Nevertheless, there is no broadly accepted mathematical theory for the collective activity of neuronal populations and such models have shown limited success to bridge levels of explanations from singel neurons to complex behavior, mainly due to the grand challenges of estimatkng all free parameters.*

> Todo: shorten and focus on the fact that most comp models aim to solve the task all the way: to construct a "biophysical model" that accounts for empirical brain data and behavior.

Thus, the penetration of dynamic models of large-scale brain activity into mainstream neuroscience has been slow, and they may be unknown to many neuroscientists.

An alternative approach: Neuroconnectomist approach ([](https://doi.org/10.1038/s41583-023-00705-w))

> A further scenario rests on the role of ghost attractors^[109](https://www.nature.com/articles/nn.4497#ref-CR109 "Deco, G. & Jirsa, V.K. Ongoing cortical activity at rest: criticality, multistability, and ghost attractors. J. Neurosci. 32, 3366–3375 (2012).")^, a dynamic landscape of remnant attractors each of which has an incomplete basin, hence allowing the system to 'wander' through large swathes of the phase space under the influence of weak noise^[110](https://www.nature.com/articles/nn.4497#ref-CR110 "Tsuda, I. Toward an interpretation of dynamic neural activity in terms of chaotic dynamical systems. Behav. Brain Sci. 24, 793–810 discussion 810–848 (2001).")^.

In this work, we aim for:

- simpliest, highest-level genrative computational model: a multistable dynamic system with **maximal empirical validity**
- bypass the challenges of estimating parameters, by  building on the activity. flow
- **no mechanistic model, not aiming to explain biophisical background**
- links to Neuroconnectomism

> - multistable
> - dynamical systems theory

Our framework - with minimal and reasonable assumptions about the “activity flow” (ref: Cole-papers) between two, functionally connected regions - considers the stationary functional brain network as an already-trained artificial neural network.  In the proposed framework, the topology of the stationary brain connectome defines a cost (energy) for any arbitrary brain activation patterns and a trajectory towards one of the finite number of stable patterns that minimize this cost (so-called attractor states).

- noise

Here we propose these attractors states as robust and neurobiologically relevant characteristics of the functional brain connectome, with a wide variety of potential applications.

We demonstrate that the proposed attractor states highly resemble to the dynamic brain states commonly observed by dynamic functional connectivity methods (e.g. CAP-analyses (ref)) and provide a proof-of-concept for the biomedical validity of our framework, by showing that the average brain activations corresponding to the attractor states during resting sate display manifold significant associations to cognition.

Due to the known noise-tolerance of the applied eANN-s, the proposed approach can be expected to be highly robust/reliable/replicable, which we demonstrate with independent datasets (total n=xxx).

List all the aims: hierarchy, generalizability etc

# Results

- introduce the idea in more detail (fig 1)
  - attractor states and added noise
  - construcct validity
- attractor states (fig 1)
- face validity
- clinical validity





:::{figure} figures/face_validity.png
:name: face-val
Empirical Hopfield-networks reconstruct real brain activity.
:::

Here I refer to {numref}`face-val`.

# Discussion

- significance

# Methods

+++ {"part": "acknowledgements"}

Todo

+++

+++ {"part": "data-availability"}

Todo

+++
