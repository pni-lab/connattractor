---
title: Attractor states of the functional brain connectome orchestrate large-scale brain dynamics
subject: manuscript draft
#subtitle: Optional Subtitle
short_title: Manuscript
authors:
    - name: Robert Englert
      affiliations:
        - Department of Diagnostic and Interventional Radiology and Neuroradiology,  University Medicine Essen, Germany
      email: robert.englert@uk-essen.de
      
    - name: Balint Kincses
      affiliations:
        - Department of Neurology, University Medicine Essen, Germany
        
    - name: Raviteja Kotikalapudi
      affiliations:
        - Department of Neurology, University Medicine Essen, Germany
        
    - name: Giuseppe Gallitto
      affiliations:
        - Department of Neurology, University Medicine Essen, Germany
        
    - name: Jialin Li
      affiliations:
        - Department of Neurology, University Medicine Essen, Germany
        - Max Planck School of Cognition, Leipzig, Germany
        
    - name: Kevin Hoffschlag
      affiliations:
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
  HNN: Hopfield Neural Network
  ANN: Artificial Neural Network
  fcHNN: functional connectome-based Hopfield Neural Network
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
    output: exports/connattractor_manuscript.docx

bibliography:
  - bibliography.bib
---

+++ {"part": "key-points"}
**Key Points:**
- We present a simple yet powerful computational model for large-scale brain dynamics
- The model uses a functional connectome-based Hopfield artificial neural network (fcHNN) architecture to compute recurrent "activity flow" through the functional brain connectome
- FcHNNs accurately reconstruct the dynamic repertoire of the brain in resting conditions
- FcHNNs conceptualize both task-induced and pathological changes in brain activity as a shift in these dynamics
- Our approach is validated using data from seven studies involving approximately 1000 participants
+++

+++ {"part": "abstract"}
Understanding large-scale brain dynamics is a grand challenge in neuroscience. 
We propose functional connectome-based Hopfield neural networks (fcHNNs) as a model of macro-scale brain dynamics, arising from recurrent activity flow among brain regions. An fcHNN is neither optimized to mimic certain brain characteristics, nor trained to solve specific tasks; its weights are simply initialized with empirical functional connectivity values.
In the fcHNN framework, brain dynamics are understood in relation to so-called attractor states, i.e. neurobiologically meaningful low-energy activity configurations.
Analyses of 7 distinct datasets demonstrate that fcHNNs can accurately reconstruct and predict brain dynamics under a wide range of conditions, including resting and task states and brain disorders.
By establishing a mechanistic link between connectivity and activity, fcHNNs offers a simple and interpretable  computational alternative to conventional descriptive analyses of brain function. Being a generative framework, fCHNNs can yield mechanistic insights and hold potential to uncover novel treatment targets.
+++

## Introduction

Brain function is characterized by the continuous activation and deactivation of anatomically distributed neuronal 
populations {cite:p}`buzsaki2006rhythms`.

Irrespective of the presence or absence of explicit stimuli, regional activation never seems to occur in isolation 
{cite:p}`bassett2017network`. Brain regions appear to work in concert, giving rise to a
rich and spatiotemporally complex fluctuation {cite:p}`gutierrez2019infraslow`.
This fluctuation is neither random, nor stationary over time {cite:p}`liu2013time; zalesky2014time`.
It exhibits quasi-periodic properties {cite:p}`thompson2014quasi`, with a limited number of
recurring patterns known as "brain states" {cite:p}`greene2023everyone; vidaurre2017brain; liu2013time; richiardi2011decoding`.

From hidden Markov models, to point-process analyses, a wide variety of descriptive techniques have been previously 
employed to characterize whole-brain dynamics {cite:p}`smith2012temporally; vidaurre2017brain; liu2013time; chen2018human`.
These efforts have provided accumulating evidence not only for the existence of dynamic brain states but also for their clinical 
significance {cite:p}`hutchison2013dynamic; barttfeld2015signature; meer2020movie`. 
However, the underlying driving forces remain elusive due to the descriptive nature of such studies.

Questions regarding the mechanisms, that cause these remarkable dynamics, can be addressed through computational models, which have the potential to shift our understanding from mere associations to causal explanations.
Conventional computational approaches attempt to solve this puzzle by going all the way down to the biophysical properties of single neurons, and aim to construct a model of larger neural populations, or even the entire brain 
{cite:p}`breakspear2017dynamic`.
These approaches have shown numerous successful applications {cite:p}`murray2018biophysical; kriegeskorte2018cognitive; heinz2019towards`.
However, the estimation of the vast number of free parameters in such models presents a grand challenge, hampering the ability of these techniques to effectively bridge the gap between explanations at the level of single neurons and the complexity of behavior {cite:p}`breakspear2017dynamic`. As a result, several recent approaches have opted to trade biophysical detail for computational simplicity. They utilize phenomenological, coarse-grained brain network models {cite:p}`schirner2022dynamic; schiff1994controlling; papadopoulos2017development` of neural activity or linear network control theory  {cite:p}`luppi2023transitions; chiem2021structure; gu2017optimal; scheid2021time; gu2015controllability`, to gain insights into how structural connectivity constrains brain dynamics.

Another approach, the so-called "neuroconnectionism" {cite:p}`doerig2023neuroconnectionist` shifts the emphasis from "biophysical fidelity" of models to "cognitive/behavioral fidelity" {cite:p}`kriegeskorte2018cognitive`, by using artificial neural networks (ANNs) that are trained to perform various tasks, as brain models. While this novel paradigm has already made significant contributions to expanding our understanding of the general computational principles of the brain (see {cite}`doerig2023neuroconnectionist`, the need to train ANNs for specific tasks inherently limits their ability to explain the spontaneous, and largely task-independent, macro-scale dynamics of neural activity {cite:p}`richards2019deep`.

Here we propose a novel approach that combines the advantages of large-scale phenomenological computational modeling and neuroconnectionism, to investigate brain dynamics.
Similar to neuroconnectionism, we utilize an artificial neural network (ANN) as a high-level computational model of the brain.
However, we do not explicitly train our ANN for a specific task. Instead, we set its weights empirically, with data based on the "activity flow" {cite:p}`cole2016activity; ito2017cognitive` across regions within the functional brain connectome, as measured with functional magnetic resonance imaging (fMRI, {numref}`concept`B). 

Specifically, we employ a continuous-space Hopfield neural network (HNN) {cite:p}`hopfield1982neural; krotov2023new`, with its nodes representing large-scale brain areas. Based on the topology of the functional connectome, this architecture establishes an "energy" level for any arbitrary activation patterns and - similarly to multistable computational brain network models {cite:p}`schirner2022dynamic` - determines a "trajectory of least action" towards one of the finite number of stable patterns, known as *attractor states*, that minimize this energy.
In this simplistic yet powerful framework, activity flow {cite:p}`cole2016activity` across regions gives rise to spontaneous brain dynamics that can be conceptualized as an intricate, high-dimensional path on the energy landscape ({numref}`concept`C), constrained by the "gravitational pull" of the attractors states of the system.
Due to its generative nature, our model offers testable predictions for the effect of various perturbations and alterations of these dynamics, from task-induced activity, to changes related to brain disorders.

:::{figure} figures/concept.png
:name: concept
**Connectome-based Hopfield networks as models of macro-scale brain dynamics.** <br/><br/>
**A** Hopfield artificial neural networks (HNNs)  are a form of recurrent artificial neural networks that serve as content-addressable ("associative") memory systems. Hopfield networks can be trained to store a finite number of patterns (e.g. via Hebbian learning a.k.a. "fire together -  wire together"). During the training procedure, the weights of the HNN are trained so that the stored 
patterns become stable attractor states of the network. Thus, when the trained network is presented partial, noisy or corrupted variations of the stored patterns, it can effectively reconstruct the original pattern via an iterative relaxation procedure that converges to the attractor states.
**B** We consider regions of the brain as nodes of a Hopfield network. Instead of training the Hopfield network to 
specific tasks, we set its weights empirically, with the interregional activity flow estimated via functional
brain connectivity. Capitalizing on strong analogies between the relaxation rule of Hopfield networks and the 
activity flow principle that links activity to connectivity in brain networks, we propose the resulting 
functional connectome-based Hopfield neural network (fcHNN) as a computational model for macro-scale brain dynamics.  
**C** The proposed computational framework assigns an energy level, an attractor state and a position in a 
low-dimensional embedding to brain activation patterns. Additionally, it models how the entire state-space of viable activation patterns is restricted by the dynamics of the system and how alterations in activity and/or connectivity modify these dynamics.
:::

In the present work, we first explore the attractor states of the functional brain connectome and construct a streamlined, low-dimensional representation of the energy landscape.
Subsequently, we rigorously test the proposed model through a series of experiments, conducted on data obtained 
from a heterogenous set of 7 experimental clinical and meta-analytic studies, encompassing a total of n≈1000 individuals.
These analyses evaluate the robustness and replicability of the proposed approach and test its ability to reconstruct various characteristics of resting state brain dynamics, as well as its capacity to detect and explain changes induced by experimental tasks or alterations in various brain disorders.

## Results

### Connectome-based Hopfield network as a model of brain dynamics

First, we explored the attractor states of the functional connectome in a sample of n=41 healthy young 
participants ([study 1](tab-samples)). We estimated interregional activity flow {cite:p}`cole2016activity; ito2017cognitive` 
as the study-level average of regularized partial correlations among the resting state fMRI timeseries of m = 122 
functionally defined brain regions (BASC brain atlas, see Methods for details). We then used the standardized 
functional connectome as the $w_{ij}$  weights of a continuous-state Hopfield network 
{cite:p}`hopfield1982neural; koiran1994dynamics` consisting of $m$ neural units, each having an activity 
$a_i \in [-1,1] \subset \mathbb{R})$. Hopfield networks can be initialized by an arbitrary activation pattern (consisting of 
$m$ activation values) and iteratively updated (i.e. "relaxed") until convergence to one of the finite attractor states is reached. The relaxation procedure is based on a simple rule; in each iteration, the activity of a region is constructed as the weighted average of the activities of all other regions, with weights defined by the connectivity between them. The average is then transformed by a non-linear function (sigmoidal activation function) to keep it in the desired [-1,1] interval.
This can be expressed by the following equation:

```{math}
:label: hopfield-update
\dot{a}_i = S(\beta \sum_{j=1}^m w_{ij}a_j - b_i)
```

where $\dot{a}_i$ is the activity of neural unit $i$ in the next iteration and $S(a_j)$ is the sigmoidal activation 
function ($S(a) = tanh(a)$ in our implementation) and $b_i$ is the bias of unit $i$ and $\beta$ is the so-called temperature parameter. For the sake of simplicity, we set $b_i=0$ in all our experiments. We refer to this architecture as a functional connectivity-based Hopfield neural network (fcHNN). Importantly, the relaxation of a fcHNN model can be conceptualized as the repeated 
application of the activity flow principle {cite:p}`cole2016activity; ito2017cognitive` , simultaneously for all 
regions: $\dot{a}_i = \sum_{j=1}^m w_{ij}a_j$. The update rule also exhibits analogies with  {cite:p}`gu2015controllability` and the inner workings of neural mass models {cite:p}`breakspear2017dynamic` as applied e.g. in dynamic causal modeling(see [](#Discussion) for further details).

Hopfield networks assign an energy value to each possible activity configuration (see [Methods](#Connectome-based-Hopfield-networks) for details), which decreases during the relaxation procedure until reaching an equilibrium state with minimal energy ({numref}`attractors`A, top panel,
{cite:p}`hopfield1982neural; koiran1994dynamics`.
We used a large number of random initializations to obtain all possible attractor states of the connectome-based 
Hopfield network in study 1 ({numref}`attractors`A, bottom panel).

:::{figure} figures/embedding_method.png
:name: attractors
**Attractor states and state-space dynamics of connectome-based Hopfield networks** <br/><br/>
**A** Top: During so-called relaxation procedure, activities in the nodes of an fcHNN model are iteratively updated based on the activity of all other regions and the connectivity between them. The energy of a
connectome-based Hopfield network decreases during the relaxation procedure until reaching an equilibrium state with 
minimal energy, i.e. an attractor state. Bottom: Four attractor states of the CHNN derived from the
group-level functional connectivity matrix from [study 1](tab-samples) (n=44). 
**B** Top: Similarly to stochastic dynamic causal modeling, in presence of weak noise (stochastic update), the system 
does not converge to equilibrium anymore. Instead, the system transverses on the state landscape in a way 
restricted by the topology of the connectome and the "gravitational pull" of the attractor states. Bottom: We sample 
the state space by running the stochastic relaxation procedure for an extended amount of time (e.g. 100.000 consecutive
stochastic updates), each point representing a possible activation configuration (state). To construct a 
low-dimensional representation of the state space, we take the first two principal components of the simulated activity
patterns. The first two principal components explain approximately 58-85% of the variance of state energy (depending 
on the noise parameter $\sigma$, see {numref}`Supplementary Figure %s <si_expl_variance_energy>`).
**C** We map all states of the state space sample to their corresponding attractor state, with the conventional 
Hopfield relaxation procedure (A). The four attractor states are also visualized in their corresponding position on the
PCA-based projection. The first two principal components yield a clear separation of the attractive state basins 
(cross-validated classification accuracy: 95.5%, Supplementary Material **X**). We refer to the resulting visualization
as the fcHNN projection and use it to visualize fcHNN-derived and empirical brain dynamics throughout the rest of 
the manuscript.
**E** At its simplest form, the fcHNN framework entails only two free hyperparameters: the temperature parameter 
$\beta$ (left) that controls the number of attractor states and the noise parameter of the stochastic relaxation 
$\sigma$. To avoid overfitting these parameters to the empirical data, we set $\beta=0.04$ and $\sigma=0.37$ for the 
rest of the paper  (dotted boxes).
:::

Consistent with theoretical expectations, we observed that increasing the temperature parameter $\beta$ led to an 
increasing number of attractor states ({numref}`attractors`E, left), appearing in symmetric pairs 
(i.e. $a_i^{(1)} = -a_i^{(2)}$). For simplicity, we set the temperature parameter for the rest of the paper to a value
resulting in 4 distinct attractor states ($\beta=0.4$).

FcHNNs, without any modifications, always converge to an equilibrium state.
To incorporate stochastic fluctuations in neuronal activity {cite:p}`robinson2005multiscale`, we introduced weak 
Gaussian noise to the fcHNN relaxation procedure. This procedure, referred to as stochastic relaxation, prevents the system from reaching equilibrium and, somewhat similarly to stochastic DCM {cite:p}`daunizeau2012stochastic`, induces complex system dynamics (equivalent to brain activity fluctuations in our framework). Such a system may traverse extensive regions of the state space, visiting the basins of multiple attractor states ({numref}`attractors`B).

We hypothesise that the resulting dynamics capture essential characteristics of spontaneous activity fluctuations in the brain and can serve as a valuable generative computational model for large-scale brain dynamics. To sample the resulting state space, we obtained 100,000 iterations of the stochastic relaxation procedure with a Hopfield network initialized with the mean functional connectome in study 1. 

Next, in order to enhance interpretability, we conducted a principal component analysis (PCA) on the resulting state space sample and obtained the first two principal components.
These components were used to construct a low-dimensional embedding ({numref}`attractors`B, bottom plot).
The PCA embedding exhibited high consistency across different values of $\beta$ and $\sigma$ ({numref}`attractors`E).
For all subsequent analyses, we set $\sigma=0.37$, which was determined through a coarse optimization procedure aimed at reconstructing the bimodal distribution of empirical data in the same projection ({numref}`attractors`E, 
see Methods for details). On the low-dimensional embedding, which we refer to as the *fcHNN projection*, we observed a clear separation of the attractor states ({numref}`attractors`C), with the two symmetric pairs of attractor states located at the extremes of the first and second PC. 
To map the attractor basins on the space spanned by the first two PCs ({numref}`attractors`C), we obtained the attractor state of each point visited during the stochastic relaxation and fit a multinomial logistic regression model to predict the attractor state from the first two PCs. 
The resulting model accurately predicted attractor states of arbitrary brain activity patterns, achieving a cross-validated accuracy of 96.5%.
The attractor basins were visualized by using the decision boundaries obtained from this model. ({numref}`attractors`C). We propose the 2-dimensional fcHNN projection depicted on ({numref}`attractors`C) as a simplified representation of brain dynamics, and use it as a basis for all subsequent analyses in this work.


### Reconstruction of resting state brain dynamics

The spatial patterns of the obtained attractor states exhibit high neuroscientific relevance and closely resemble previously described large-scale brain systems. ({numref}`rest-validity`A). The first pair of attractors (mapped on PC1, horizontal axis) resemble the two complementary “macro” systems described, among others, by {cite:t}`golland2008data` and {cite:t}`cioli2014differences` as well as the two "primary" brain states observed by {cite:t}`chen2018human` and the dysphoric and anxiosomatic clusters that have recently been proposed as targets for circuit-based neuromodulation by {cite:t}`siddiqi2020distinct`. A common interpretation of these two patterns is that they represent (i) an “extrinsic” system which exhibits a stronger direct connection to the immediate sensory environment and (ii) an "intrinsic" system, whose activity is primarily associated with dynamic changes in higher-level internal context and closely linked to the default mode network.
The other pair of attractors spans an orthogonal axis connecting regions that are commonly associated with perception–action cycles {cite:p}`fuster2004upper` and recruits regions associated with active inference (e.g. motor cortices) and perceptual inference (e.g visual areas).

:::{figure} figures/face_validity.png 
:name: rest-validity
**Connectome-based Hopfield networks reconstruct characteristics of real resting state brain activity.**<br/><br/>
**A** The four attractor states of the fcHNN model from study 1 reflect brain activation 
patterns with high neuroscientific relevance, representing sub-systems previously associated with 'internal context'
(blue), "external context" (yellow), "action/execution" (red) and "perception" (green)
{cite:p}`golland2008data; cioli2014differences; chen2018human; fuster2004upper`.
**B** The attractor states show excellent replicability in two external datasets (study 2 and 3, mean correlation 0.93). 
**C** The fcHNN projection (first two PCs of the fcHNN state space) explains significantly more variance (p<0.0001) in the real 
resting state fMRI data than principal components derived from the real resting state data itself and generalizes 
better (p<0.0001) to out-of-sample data (study 2). Error bars denote 99% bootstrapped confidence intervals. 
**D** The fcHNN analysis accurately predicts (p<0.0001) the fraction of time spent on the basis of the four attractor 
states in real restring state fMRI data (study 1) and, 
**E**, reconstructs the characteristic bimodal distribution of the real resting state data. 
**F** Stochastic fcHNNs are capable of self-reconstruction: the timeseries resulting from the stochastic relaxation procedure 
mirror the co-variance structure of the functional connectome the fcHNN model was initialized with. 
:::

Importantly, the discovered attractor states demonstrate a remarkable level of replicability (mean Pearson's 
correlation 0.93) across the discovery datasets (study 1) and two independent replication datasets 
([study 2 and 3](tab-samples), {numref}`rest-validity`C).

Further analysis in study 1 showed that connectome-based Hopfield models accurately reconstructed multiple 
characteristics of true resting-state data. 

First, the two-dimensional fcHNN projection (i.e. the first two components of the fcHNN-PCA) accounted for a substantial amount of variance in the real resting-state fMRI data in study 1 (mean $R^2=0.399$) and generalized well to out-of-sample data (study 2, mean $R^2=0.396$)  ({numref}`rest-validity`E). Remarkably, the explained variance of the fcHNN projection significantly exceeded that of a PCA performed directly on the real resting-state fMRI data itself ($R^2=0.37$ and $0.364$ for in- and out-of-sample analyses).

Second, fcHNN analyses accurately reconstructed true resting state brain state dynamics. During stochastic relaxation, the fcHNN model was found to spend approximately three-quarters of the time on the basis of the first two attractor states, with an equal distribution between them. The remaining one-quarter of the time is spent on the basis of the second pair of attractor states, also equally distributed. To test whether we see similar state occupancy ratios in real resting state data, we obtained normalized and cleaned mean timeseries in $m=122$ regions from all participants in study 1 and calculated 
the attractor state of each time-frame via the fcHNN model. We observed strikingly similar temporal occupancies to those predicted by the model. Statistical analysis based on a spatial autocorrelation-preserving null model for the empirical activity patterns (i.e. phase-randomizing the empirical activity maps, see [](#Methods) for details) confirmed that the observed state occupancies are significantly different from what would be expected by chance (p<0.001, {numref}`rest-validity`D).
{numref}`rest-validity`B). Our findings were largely independent of the temperature parameter, see Supplementary Material **X** for details. 

Third, fcHNNs were found to successfully reproduce fine-grained details of the bimodal distribution observed in the real resting-state fMRI data when projected onto the fcHNN projection ({numref}`rest-validity`F and {numref}`attractors`E), suggesting that brain dynamics are governed by a limited number of attractor states that emerge from the flow of activity across functional connectivity networks.

Finally, during the stochastic relaxation procedure, fcHNNs were found to generate regional time series that 
preserve the covariance structure of the real functional connectome used for network initialization. This result indicates that a dynamic system in which activity flows across nodes of a complex network inevitably 
"leaks" its underlying structure into the activity time series, providing a high level of construct validity for the proposed approach ({numref}`rest-validity`D).

It is important to reiterate that the proposed model was neither explicitly informed about, nor trained or optimized to reconstruct any of the investigated spatial (bi-modal distribution, explanatory performance) or temporal patterns (temporal state occupancy) of the brain. 
The ability of the proposed connectome-based Hopfield model to reconstruct all these characteristics of real data strongly suggests that it captures essential relationships between the topology of the brain's functional connectome and its dynamic activity repertoire. 

### An explanatory framework for task-based brain activity

The proposed framework offers a natural account for how activation patterns in the brain dynamically emerge form the underlying functional connectivity. To illustrate this, we obtained task-based fMRI data from a study by 
{cite:t}`woo2015distinct` ([study 4](tab-samples), n=33, see {numref}`rest-validity`), investigating the neural 
correlates of pain and its self-regulation. 
We found that time-frames obtained from periods with pain stimulation (taking into account hemodynamics, see [](#Methods) for details) show a significantly different distribution on the fcHNN projection than time-frames obtained from periods without pain stimulation (permutation test for mean projection difference, by randomly swapping conditions, p<0.001, {numref}`task-validity`A, left). Energies, as defined by the Hopfield model, were also significantly different between the two conditions (permutation test by randomly swapping conditions within participants, p<0.001), with higher energies during pain stimulation.

When participants were instructed to up- or down-regulate their pain sensation (resulting in increased and decreased pain reports and differential brain activity in the nucleus accumbens, NAc (see {cite}`woo2015distinct` for details), we observed further changes of the location of momentary brain activity patterns on the fcHNN projection, (permutation test by swapping conditions within participants: p<0.001, {numref}`task-validity`A, right). Interestingly, self-regulation did not manifest in significant energy changes (permutation test, p=0.36). 

:::{figure} figures/task_validity.png
:name: task-validity
**Empirical Hopfield-networks reconstruct real task-based brain activity.** <br></br>
**A** Functional MRI time-frames during pain stimulation from [study 4](tab-samples) (second fcHNN projection plot)
and self-regulation (third and fourth) locate significantly differently on the fcHNN projection than brain states 
during rest (first projection, permutation test, p<0.001 for all).  Energies, as defined by the Hopfield model, are also
significantly different between rest and the pain conditions (permutation test, p<0.001), with higher energies during 
pain stimulation. Triangles denote participant-level mean activations in the various blocks (corrected for 
hemodynamics). Circle plots show the directions of the change for each individual (points) as well as the mean direction
across participants (arrow), as compared to the reference state (downregulation for the last circle plot, rest for all 
other circle plots).
**B** Flow-analysis of the single time-frames (based on the vector pointing to the next time-frame)
reveal a non-linear difference in brain dynamics during pain and rest (left). When introducing weak 
pain-related signal in the fcHNN model during stochastic relaxation, it accurately reproduces these non-linear flow 
differences (right).
**C** Simulating activity in the nucleus accumbens (NAc) (the region showing significant activity differences in {cite}`woo2015distinct`) reconstructs the observed non-linear flow difference between up- and downregulation (left).
**D** Schematic representation of brain dynamics during pain and its up- and downregulation, visualized on the fcHNN
projection. In the proposed framework, pain does not simply elicit a direct response in certain regions, but instead, shifts spontaneous brain dynamics towards the "action" subsystem, converging to a characteristic "ghost 
attractor" of pain. Up-regulation by NAc de-activation exerts force towards a similar direction (thus increasing the probability of the emergence of "pain-activations") while down-regulation
by NAc activation exhibit an opposite effect on brain dynamics, leading to the brain less frequent "visiting" 
pain-associated states.
**E** Visualizing meta-analytic activation maps on the fcHNN projection captures intimate relations between the corresponding tasks and **F** serves as a basis for a fcHNN-based theoretical interpretative framework for spontaneous and task-based brain dynamics. In the proposed framework, task-based activity is not a mere response to external stimuli in certain brain locations but a perturbation of the brain's characteristic dynamic trajectories, constrained by the underlying functional connectivity. From this perspective, "activity maps" from conventional task-based fMRI analyses capture time-averaged differences in these whole brain dynamics. 
:::

These results provide an intuitive account for how the underlying functional connectivity of the brain can give rise to different activation patterns, depending on the current input. In the fcHNN framework, change in input (i.e. a task or stimulation) does not simply switch to the brain into a distinct "mode" of operation but acts as 
a perturbation of the system's dynamics, resulting in mean activations changes that are only reliable measurable over an extended period of time, as done by conventional task-based fMRI analyses. 

With the proposed fcHNN approach, we can go beyond the mean activation changes and investigate how the underlying dynamics of the brain are altered by different tasks and conditions. To this end, we conducted a flow analysis on the fcHNN projection, quantifying the average direction of change in brain activity from one time-frame to the next on the fcHNN projection (See [](#Methods) for details).
This analysis unveiled non-linear trajectory patterns, indicating the most probable change in brain activity from a given activity pattern, in a particular condition (pain without self-regulation or upregulation), as 
compared to the reference state (rest and downregulation, respectively). In the case of pain versus rest ({numref}`task-validity`B, left side), brain activity tends to gravitate towards a distinct point on the projection, which we term the "ghost attractor" of pain (similar to {cite}`vohryzek2020ghost`). In terms of attractor states, this belongs to the basin of the attractor corresponding to action/execution. In case of up vs. downregulation ({numref}`task-validity`C, left side), brain activity is pulled generally towards a similar direction, but with a lack of a clear ghost attractor and, from most starting points, likely resulting in states that are closer to the pain-related "ghost attractor" point.

Next, our objective was to evaluate the extent to which the proposed framework can reconstruct the observed non-linear dynamics. To simulate the alterations in brain dynamics during pain stimulation, we acquired a meta-analytic pain activation map {cite:p}`zunhammer2021meta` (n=603) and - similarly to network control theory {cite:p}`gu2015controllability`- incorporated it as additional signal, along with the Gaussian noise, 
during the stochastic relaxation procedure. While incorporating such a signal naturally induces a minor linear shift on the fcHNN projection for each state generated during the stochastic relaxation procedure, this alone could not explain the observed nonlinear dynamics in the real data (Supplementary material **X**). After conducting a 
coarse-grained optimization across five different signal-to-noise (SNR) values (logarithmically spaced between 
0.001 and 0.1), we found that by adding a minimal amount of signal (SNR = 0.01), the fcHNN model achieved a remarkable reconstruction of the observed non-linear disparities in brain dynamics between the pain and rest conditions, including the characteristic pain-related "ghost attractor". (Spearman's $\rho$ = 0.42, p=0.003, 
{numref}`task-validity`B, right side).

The same model was also able to reconstruct the observed non-linear differences in brain dynamics between the up- and downregulation conditions (Spearman's $\rho$ = 0.59, p=0.004) without any further optimization (SNR=0.01, 
{numref}`task-validity`C, right side). The only change we made to the model was the addition (downregulation) or 
subtraction (upregulation) of control signal in the NAc (the region in which {cite:p}`woo2015distinct` observed significant changes between up- and downregulation), with an SNR of 0.01 (the same we found optimal in the previous analysis).

%These findings offer novel insights into the neural mechanisms underlying pain and its self-regulation, providing a mechanistic explanation for the involvement of both nociception-related regions and the NAc (nucleus accumbens) in pain regulation. ({numref}`task-validity`D). Additionally, these findings emphasize that the conceptual differentiation between resting and task states may, to a considerable extent, be an artificial dichotomy. Instead, even in the presence of highly salient stimuli such as pain, the brain remains in a continuous state of flux, which is not radically altered by tasks and stimuli.

% -> discussion

To provide a comprehensive picture on how tasks and stimuli other then pain map onto the fcHNN projection, we obtained various task-based meta-analytic activation maps from Neurosynth (see [Methods](#evaluation-task-based-dynamics)) and plotted them on the fcHNN projection ({numref}`task-validity`E). This analysis reinforced and extended our interpretation of the four investigated attractor states and shed more light on how various functions are mapped on the axes of internal vs. external context and perception vs. action.
In this coordinate system of the fcHNN projection, visual processing is labeled "external-perception", sensory-motor processes "external-active", language, verbal cognition and working memory is labelled "internal-active" and long-term memory as well as social and autobiographic narrative fall into the "internal-perception" regime ({numref}`task-validity`F).

% Together our results on task-based data highlight that the proposed generative framework can be used to simulate and predict brain dynamics under different conditions. Predicting the effect of lower or higher level of activity in certain regions (or lower or higher connectivity between them) on global brain dynamics and responses to various tasks provides unprecedented opportunities for forecasting the effect of interventions, such as pharmacological or non-invasive brain stimulation, on brain function.

### Clinical relevance

Computational models, such as the fcHNN approach, have the potential to make a significant contribution to our mechanistic comprehension of various neurological and psychiatric disorders; which represents a crucial stride towards developing effective treatments. To demonstrate this potential, here we present evidence that fcHNN-based attractor state analysis can effectively capture and predict alterations in resting state brain dynamics of autism spectrum disorder (ASD) patients.
 
We obtained data from n=172 individuals acquired at the New York University Langone Medical Center, New York, NY, USA (NYU) Autism Brain Imaging Data Exchange dataset ([study 7](tab-samples): ABIDE, {cite:p}`di2014autism`.
After excluding high-motion cases (see [](#Methods) for details), we visualized the distribution of time-frames on the fcHNN-projection separately for ASD patients and typically developing control (TDC) participants ({numref}`clinical-validity`A).
Next, we applied the fcHNN model from study 1 to allocate each time-frame of resting state data to one of the 4 attractor states. Then, we compared the average activity during resting state within each state across different clinical groups via permuutation tetsing (randomizing the groups) and corrected the resulting p-values for multiple comparisons across brain regions and attractor states via Bonferroni correction. We found several significant differences in the mean attractor activation of patients as compared to the respective 
controls ({numref}`clinical-validity`B).

:::{figure} figures/state_analysis.*
:name: clinical-validity
**Connectome-based Hopfield analysis as a sensitive tool for the study of clinical disorders.** <br></br>
We quantified attractor state activations in three clinical datasets ([studies 6, 7 and 8](tab-samples)) as the 
individual-level mean activation of all time-frames belonging to the same attractor state. fcHNN analyses of attractor 
state activations revealed significant differences in all three datasets.
**A** Attractor state analysis of individuals with autism spectrum disorder (ASD) and typically developing controls (TD)
captures alterations similar to those previously associated to ASD-related perceptual atypicalities as well as atypical integration of information about the “self” and the “other”.
**B** The most prominent Schizophrenia (SCZ)-related differences (as compared to healthy controls (HC) are related increased 
activity of the internal subsystem and increased visual activations on the basis of the attractor state associated with perception.
**C** In Alzheimer's disease (AD), fcHNN analysis revealed, among others, hyperactivity in the hippocampal formation (collateral sulcus) during perception, a commonly reported finding in AD.
and internal context (both of which together host long-term memory processes, see {numref}`task-validity`F). All 
results are corrected for multiple comparisons across brain regions and attractor states (122*4 comparisons) 
with Bonferroni-correction. See {numref}`tab-clinical-results` Supplementary Table **X** for detailed results. <br></br>
***Abbreviations**: MCC: middle cingulate cortex, ACC: anterior cingulate cortex, pg: perigenual, PFC: prefrontal cortex, dm: dorsomedial, dl: dorsolateral, STG: superior temporal gyrus, MTG: middle temporal gyrus, ITG: inferior temporal gyrus, Caud/Acc: caudate-accumbens,  SM: sensorimotor, V1: primary visual, A1: primary auditory, Hipp: parahippocampal gyrus, Precun: precuneus, SMA: supplementary motor cortex, IPL: inferior parietal lobule, ASD: autism spectrum disorder, SCH: schizophrenia, AD: Alzheimer's disease.*
:::

Strongest differences were found on the "action-perception" axis ({numref}`tab-clinical-results`), with increased activity of the sensory-motor and middle cingular cortices during "action-execution" related states and increased visual and decreased sensory and auditory activity during "perception" states, likely reflecting the widely acknowledged, yet poorly understood, perceptual atypicalities in ASD {cite:p}`hadad2019perception`.
ASD related changes in the internal-external axis were characterized by more involvement of the posterior cingulate, the precuneus, the nucleus accumbens, the dorsolateral prefrontal cortex (dlPFC), the cerebellum (Crus II, lobule VII) and inferior temporal regions during activity of the internalizing subsystem ({numref}`tab-clinical-results`). While similar, default mode network (DMN)-related changes have often been attributed to an atypical integration of information about the “self” and the “other” {cite:p}`padmanabhan2017default`, a more detailed fcHNN-analysis may help to further disentangle the specific nature of these changes.

:::{list-table} **The top ten largest changes in average attractor-state activity beetween autistic and control individuals.**  Mean attractor-state activity changes are presented in the order of their absolute effect size. All p-values are based on permutation tests (shuffling the group assignment) and corrected for multiple comparisons (via Bonferroni's correction). For a comprehensive list of significant findings, see Supplementary Table **X**.
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

Next, we contrasted the charcteristic trajecories derived from the fcHNN models of the two groups (initialized with the group-level functional connectomes, see [](#Methods) for details). FcHNN modelling predicted that in ASD, there is an increasaed likelihood of states returning towards the midle from the internal-external axis and an increased likelihood of states transitioning towards the extrems of the action-perception axis ({numref}`clinical-validity`C). We observed a highly similar pattern in the real data (Pearson's correlation: 0.66), statistically significant after permutation testing (shuffling the group assignment, p=0.009).
The proposed interpretative framework for fcHNNs ({numref}`task-validity`F) suggests that this pattern of state transitions is indicative of a reduced ability to flexibly switch between internal and external modes of processing, and accordingly, which may explain the reduced influence of context on the interpretation of incoming sensory information in ASD (e.g. the violation of Weber's law) {cite:p}`hadad2019perception`.

## Discussion

Regions of the brain are in a constant flux of information exchange, giving rise to characteristic co-activations patterns.
The degree to which activation in a region triggers activation in another is different for every pair of regions, spanning an intricate network, commonly referred to as the functional connectome. 
In this study, we have introduced a simple yet robust framework that elucidates how activity propagation within the functional connectome orchestrates large-scale brain dynamics, leading to distinct brain states accompanied by characteristic dynamic responses to perturbations.
Through a series of experiments, we have demonstrated that the proposed model can effectively reconstruct and predict large-scale brain dynamics across diverse conditions.
The presented approach offers a fresh perspective on large scale brain dynamics and offers unparalleled prospects for forecasting the impact of interventions, including pharmacological treatments or non-invasive brain stimulation, on brain function.
We have implemented the proposed framework in the publicly available Python package [*connattractor*](https://pni-lab.github.io/connattractor/quickstart), enabling researchers to apply the proposed framework to their own data and to further develop the approach.

The construct validity of our model is rooted in the activity flow principle, first introduced by 
{cite:t}`cole2016activity`. The activity flow principle states that activity in a brain region can be predicted by a weighted combination of the activity of all other regions, where the weights are set to the functional connectivity of those regions to the held-out region. This principle has been shown to hold across a wide range of experimental and clinical conditions
{cite:p}`cole2016activity; ito2017cognitive; mill2022network; hearne2021activity; chen2018human`.
The proposed approach is based on the intuition that the repeated, iterative application of the activity flow equation in a system exhibits close analogies with a type of recurrent artificial neural network known as Hopfield networks {cite:p}`hopfield1982neural`.

Hopfield networks have previously been shown to exhibit a series of characteristics that are also highly relevant for 
brain function, including the ability to store and recall memories {cite:p}`hopfield1982neural`, self-repair {cite:p}`murre2003selfreparing`,
a staggering robustness to noisy or corrupted inputs {cite:p}`hertz1991introduction` and the ability to produce 
multistable dynamics organized by the "gravitational pull" of a finite number of attractor states 
{cite:p}`khona2022attractor`. While many of such properties of Hopfield networks have previously been proposed as a model for micro-scale neural systems (see {cite}`khona2022attractor` for a review), the proposed link between macro-scale activity propagation and Hopfield networks allows transferring the vast body of knowledge on Hopfield networks to the study of large-scale brain dynamics.

Integrating Cole's activity flow principle with the Hopfield neural network architecture mandates the initiation of network weights with functional connectivity values, specifically partial correlations as suggested by {cite:t}`cole2016activity`.
Considering the functional connectome as weights of an already trained neural network distinguishes our methodology not only from conventional biophysical and phenomenological computational modeling strategies, which usually rely on the structural connectome as a proxy for polysynaptic connectivity {cite:p}`cabral2017functional`, but also from "neuroconnectionist" approaches that employ explicit training procedures {cite:p}`doerig2023neuroconnectionist`.
Functional connectome-based Hopfield neural network (fcHNN) models can be conceptualized as a streamlined alternative to those methodologies, offering significant advantages.

As compared to finely detailed biophysical models with many free parameters, the basic form of the fcHNN approach comprises solely two "hyperparameters" (temperature and noise) and yields notably consistent outcomes across an extensive range of these parameters (Supplementary Material **X**). To underscore the potency of this simplicity and stability, in the present work, we intentionally minimized the fine-tuning of these parameters. We fixed the temperature parameter at a value that robustly provides 4 attractor states and used a single noise level for all experiments (see Supplementary Material **X** for a detailed analysis of the effect of these parameters). Diminished complexity also comes with more straightforward interpretations. FcHNN models are highly interpretable as they establish a direct link between two highly prevalent metrics of brain function: functional connectivity and brain activity. This connection is not solely phenomenological, but also mathematical, facilitating the exploration and prediction of alterations in the system's dynamics in response to perturbations affecting both activity and connectivity.

The proposed model exhibits also several advantages over linear network control theory-based {cite:p}`gu2015controllability` approaches. First, the fcHNN approach works with direct activity flow estimates and does not require knowledge about the structural-functional coupling in the brain. Second, the fcHNN approach is based on a non-linear ANN architecture, thus, similarly to neuroconnectionist approaches, allows leveraging on knowledge about the ANN architecture itself. Specifically, the fcHNN approach explains emergent properties of the brain, like large-scale canonical brain networks and brain states or the presence of "ghost attractors", via the key concept in the Hopfield network framework, the attractor states. An fcHNN model can be further trained via established ANN training techniques (e.g. via the Hebbian learning rule) to "solve" various tasks or to match altered dynamics during development or in clinical populations. In this interesting future direction, the the training procedure itself becomes part of the model, providing testable hypotheses about the formation, and various malformations, of brain dynamics. 
Importantly, the fcHNN approach is not limited to the analysis of the brain's response to external perturbations but can also be used to study spontaneous brain dynamics.

Given its simplicity, it is remarkable, if not surprising, how accurately the fcHNN model is able to reconstruct and predict brain dynamics under a wide range of conditions. Particularly impressing is the result that the 2-dimensional fcHNN projection can explain more variance in real resting state fMRI data than the first two principal components derived from the data itself. 
A plausible explanation for the extraordinary performance of the fcHNN model in reconstructing brain activity patterns is that it captures essential principles of the underlying dynamic processes that can be used to reconstruct the brain's activation state-space even if our empirical measurements are corrupted by noise and low sampling rate.

The known noise-tolerance of the employed neural network architecture may explain the high replicability of fcHNN attractors across different datasets (study 2 and 3). The observed level of replicability allowed us to re-use the fcHNN model constructed with the connectome of study 1 for all subsequent studies (2-8), without any further fine-tuning or study-specific parameter optimization of the fcHNN model.

Attractor states are a key concept in the fcHNN framework. They are not only local minima in the state-space but act as a driving force for the dynamic trajectories of brain activity. Nevertheless, attractor states should not be confused with the conventional notion of brain states (e.g. co-activation patterns {cite:p}`chen2015introducing`). In the fcHNN framework, attractor states can rather be conceptualized as "Platonic idealizations" of brain activity, that are continuously approximated - but never reached - by the brain, resulting in a complex, clustered distribution of actual brain activation patterns. In or notion, this clusteredness is what gives rise to the commonly described reoccurring quasi-periodic patterns, commonly referred to as brain states. 

Relying on previous work, we can establish a relatively straightforward (although somewhat speculative) mapping between attractor states and brain function. We refer to the first two attractor states as the internal and external subsystems {cite:p}`golland2008data; cioli2014differences`. Both fcHNN-reconstructed and empirical brain activity spans the highest variance along the axis corresponding to this attractor state pair, suggesting that the robust and widely described observation of the brain state we commonly refer to as the DMN is a consequence of the brain's tendency to commute between the two state-space clusters emerging along this primary axis.
The third and fourth attractor states accurately map to the previously described perception-execution axis within the brain {cite:p}`fuster2004upper`. The four investigated attractor states together display an appealing correspondence to recent theories of brain function that capitalize on Friston's free energy principle {cite:p}`friston2006free` and postulate the necessary existence of subsystems for active and perceptual inference {cite:p}`friston2023free` as well as a hierarchically organized (i.e. external and internal) subsystems that give rise to consciousness {cite:p}`ramstead2023inner`.

Both conceptually and in terms of analysis practices, resting and task states are often treated as separate phenomena. However, in the fcHNN framework, the differentiation between task and rest states is considered an artificial dichotomy. 
In the fcHNN framework, the brain is in a constant state of flux, traversing extended areas of the state space. Task-based brain activity in this framework is not a mere response to external stimuli in certain brain locations but a perturbation of the brain's characteristic dynamic trajectories, shifting towards the realms of those attractor states that represent the type of function required by the task or stimulation. In other words brain activity is *perturbed* by external input, rather than predestined. We exemplified this with the case of the self-regulation of pain (study 4).
In our analyses, the fcHNN approach was not only able to capture participant-level activity changes induced by pain and its self-regulation (showing significant differences on the fcHNN projection and in terms of state energy), but also accurately predicted the non-linear changes in activity flow induced by characteristic activity changes and give a mechanistic account for how activity change in a single region (NAcc) may result in a significantly altered pain experience.

Brain dynamics can not only be perturbed by task or other types of experimental or naturalistic interventions, but also by pathological alterations. Here we have demonstarted on clinical data (study 7) that fcHNN-based analysis can characterize and predict altered brain dynamics in autism spectrum disorder (ASD). These preliminary results provide a proof-of-concept regarding the clinical potential of the proposed approach. Future efforts may use the fcHNN framework to fine-tune treatmet approaches (e.g. predict optimal stimulation sites) in case of a wide variety of clinical conditions.

Together, our findings open up a series of exciting opportunities for the better understanding of brain function oin health and disease. 

First, the 2-dimensional fcHNN projection offers a common framework for the visualization and *interpretation* of brain activity patterns, and conceptualizes changes related to various behavioral or clinical states or traits as a shift in brain dynamics along the axes determined by the attractor states.

Second, the fcHNN model's utility extends beyond the sole detection of such altered brain dynamics. By its generative nature, fcHNN analyses may provide insights into the causes of changes in brain dynamics, by for instance, identifying the regions or connections that act as an Achilles heel in generating such changes. Such analyses could, for instance, aid the differentiation of primary causes and secondary effects of particular activity or connectivity changes in various clinical conditions.

Third, the fcHNN approach can provide testable predictions about the effects of interventions on brain functions, like pharmacological or non-invasive brain stimulation (e.g. transcranial magnetic or direct current stimulation, 
focused ultrasound) or neurofeedback. Obtaining the optimal stimulation or treatment target within the fcHNN framework (e.g. by means of network control theory {cite:p}`liu2011controllability`) is one of the most promising future directions with the potential to significantly advance the development of novel, personalized treatment approaches.

In this initial work, we presented the simplest possible implementation of the fcHNN concept. It is clear that the presented analyses exploit only a small proportion of the richness of the full state-space dynamics reconstructed by the fcHNN model. 
There are many potential way to further improve the utility of the fcHNN approach. Increasing the number of reconstructed attractor states (by increasing the temperature parameter), investigating higher-dimensional dynamics, fine-tuned hyperparameters, the effect of 
different initializations and perturbations are all important direction for future work, with the potential to further improve the model's accuracy and usefulness.

> **other potential topics**:
> - is the functional connectome stationary? Why don't we use dynamic connectivity? See arguments by the Cole-group. Also, the fcHNN model can actually probably also reproduce task-based connectivity, when adding a task-related control signal to the stochastic relaxation procedure (as on Fig. 3). Thus it could be a model of how task-based connectivity and dynamic connectivity changes arise from the underlying rs-fMRI connectome. Maybe it could be even better to use "latent-FC" a'la McCormick, 2022, [](https://doi.org/10.1162/netn_a_00234))
> - why no HRF modelling (could be a possible extension, but it is also not part of the activity flow approach and we don't reconstruct time series, per-se, but rather activations)
> - the fcHNN model is not a model of brain function, but a model of brain dynamics. It does not strive to explain various brain regions ability to perform certain computations, but the brain's characteristic dynamic "trajectories", and how these are perturbed by tasks and other types of interventions.

## Conclusion

To conclude, here we have proposed a lightweight, high-level computational framework that accurately captures and predicts brain dynamics under a wide range of conditions. The framework models large-scale activity flow in the brain with a recurrent artificial neural network architecture that, instead of being trained to solve specific tasks or mimic certain dynamics, is simply initialized with the empirical functional connectome. The framework identifies neurobiologically meaningful attractor states and provides a model for how these restrict brain dynamics. The proposed framework, referred to as the connectome-based Hopfield neural network (fcHNN) model, can accurately reconstruct and predict brain dynamics under a wide range of conditions, including resting state, task-induced activity changes, as well as in various brain disorders. fcHNNs establish a conceptual link between connectivity and activity provide and offer a simple, robust, and highly interpretable computational alternative to the conventional descriptive approaches to investigating brain function. The generative nature of the proposed model opens up a series of exciting opportunities for future research, including novel ways of assessing causality and mechanistic understanding, and the possibility to predict the effects of various interventions, thereby paving the way for novel personalized medical approaches.




+++ {"part": "acknowledgements"}
## Acknowledgements

The work was supported by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation; projects ‘TRR289 - Treatment Expectation’, ID 422744262 and ‘SFB1280 - Extinction Learning’, ID 316803389), R01 MH076136 and R01 EB026549.
+++

+++ {"part": "data-availability"}

## Analysis source code
https://github.com/pni-lab/connattractor

## Data availability
Todo

+++
