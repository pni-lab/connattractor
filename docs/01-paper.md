---
title: Connectome-Based Attractor Dynamics Underlie Brain Activity in Rest, Task, and Disease
subject: manuscript draft
#subtitle: Optional Subtitle
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
  fcHNN: functional connectome-based Hopfield Neural Network
  FcHNN: functional connectome-based Hopfield Neural Network
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

## Introduction

Brain function is characterized by the continuous activation and deactivation of anatomically distributed neuronal 
populations {cite:p}`buzsaki2006rhythms`.
Irrespective of the presence or absence of explicit stimuli, brain regions appear to work in concert, giving rise to a
rich and spatiotemporally complex fluctuation {cite:p}`bassett2017network`.
This fluctuation is neither random nor stationary over time {cite:p}`liu2013time; zalesky2014time`.
It is organized around large-scale gradients {cite:p}`margulies2016situating; huntenburg2018large` and exhibits quasi-periodic properties, with a limited number of recurring patterns known as "brain states" {cite:p}`greene2023everyone; vidaurre2017brain; liu2013time`.

A wide variety of descriptive techniques have been previously employed to characterize whole-brain dynamics {cite:p}`smith2012temporally; vidaurre2017brain; liu2013time; chen2018human`. 
These efforts have provided accumulating evidence not only for the existence of dynamic brain states but also for their clinical 
significance {cite:p}`hutchison2013dynamic; barttfeld2015signature; meer2020movie`. 
However, the underlying driving forces remain elusive due to the descriptive nature of such studies.

Conventional computational approaches attempt to solve this puzzle by going all the way down to the biophysical properties of single neurons, and aim to construct a model of larger neural populations, or even the entire brain 
{cite:p}`breakspear2017dynamic`.
These approaches have shown numerous successful applications {cite:p}`murray2018biophysical; kriegeskorte2018cognitive; heinz2019towards`.
However, such models need to estimate a vast number of neurobiologically motivated free parameters to fit the data. This hampers their ability to effectively bridge the gap between explanations at the level of single neurons and the complexity of behavior {cite:p}`breakspear2017dynamic`.
Recent efforts using coarse-grained brain network models {cite:p}`schirner2022dynamic; schiff1994controlling; papadopoulos2017development; seguin2023brain` and linear network control theory  {cite:p}`chiem2021structure; scheid2021time; gu2015controllability` opted to trade biophysical fidelity to phenomenological validity.

Such models have provided insights into some of the inherent key characteristics of the brain as a dynamic system; for instance, the importance of stable patterns, so-called "attractor states", in governing brain dynamics {cite:p}`deco2012anatomy; golos2015multistability; hansen2015functional`. While attractor networks have become established models of micro-scale canonical brain circuits in the last four decades {cite:p}`khona2022attractor`, these studies highlighted that attractor dynamics are essential characteristics of macro-scale brain dynamics as well. However, the standard practice among these studies is the use of models that capitalize on information about the structural wiring of the brain, leading to the grand challenge of modeling the relationship between the structural wiring of the brain and functional connectivity.

The "neuroconnectionist" approach {cite:p}`doerig2023neuroconnectionist` makes another step towards trading biophisical detail to "cognitive/behavioral fidelity" {cite:p}`kriegeskorte2018cognitive`, by using artificial neural networks (ANNs) that are trained to perform various tasks, as brain models. However, the need to train ANNs for specific tasks inherently limits their ability to explain task-independent, spontaneous neural dynamics {cite:p}`richards2019deep`.

Here we propose a minimal phenomenological model for large-scale brain dynamics that combines the advantages of large-scale attractor network models {cite:p}`golos2015multistability`, neuroconnectionism {cite:p}`doerig2023neuroconnectionist`, and recent advances in undersanding the flow of brain activity across regions {cite:p}`cole2016activity`, to investigate brain dynamics.
Similar to neuroconnectionism, we utilize an ANN as an abstract, high-level computational model of the brain.
However, our model is not explicitly trained for a specific task. Instead, we set its weights empirically. 

Specifically, we employ a continuous-space Hopfield Neural Network (HNN) {cite:p}`hopfield1982neural; krotov2023new`, similar to the spin-glass and Hopfield-style attractor network models applied e.g. by {cite}`deco2012anatomy; golos2015multistability`, where the nodes of the network model represent large-scale brain areas. However, in contrast to these previos efforts that starting from the structural wiring of the brain, we initialize the edge weights of the network based on direct estimates node-to-node information transfer. Our decision to employ a direct proxy of interregional communication, rather than biophisical wiring, capitalizes on the "activity flow" {cite:p}`cole2016activity; ito2017cognitive` principle, a toroughgly validated phenomenological model of the association between brain activity and functional connectivity, as measuured with functional magneic resonance imaging.
This allows us to circumvent the necessity of comprehensively understanding and accurately modeling structural-functional coupling in the brain. Instead, we can concentrate on the overarching dynamical properties of the system.

Based on the topology of the functional connectome, our model establishes an energy level for any arbitrary activation patterns and determines a "trajectory of least action" towards one of the finite number of stable patterns, known as *attractor states*, that minimize this energy. In the proposed framework, macro-scale brain dynamics can be conceptualized as an intricate, high-dimensional path on the energy landscape ({numref}`concept`C), arising from the activity flow {cite:p}`cole2016activity` within the functional connectome and constrained by the "gravitational pull" of the attractor states of the system.
The generative nature of the proposed framework offers testable predictions for the effect of various perturbations and alterations of these dynamics, from task-induced activity to changes related to brain disorders.


