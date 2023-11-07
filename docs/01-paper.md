---
title: Connectome-Based Attractor Dynamics Underly Brain Activity in Rest, Task, and Disease
subject: manuscript draft
#subtitle: Optional Subtitle
short_title: Manuscript
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

+++ {"part": "key-points"}
**Key Points:**
- We present a simple yet powerful computational model for large-scale brain dynamics
- The model uses a functional connectome-based Hopfield artificial neural network (fcHNN) architecture to compute recurrent "activity flow" through the functional brain connectome
- FcHNN attractor dynamics accurately reconstruct the dynamic repertoire of the brain in resting conditions
- FcHNNs conceptualize both task-induced and pathological changes in brain activity as a non-linear shift in these dynamics
- Our approach is validated using large-scale neuroimaging data from seven studies
- FcHNNs offers a simple and interpretable computational alternative to conventional descriptive analyses of brain function

+++

+++ {"part": "abstract"}
Understanding large-scale brain dynamics is a grand challenge in neuroscience. 
We propose functional connectome-based Hopfield Neural Networks (fcHNNs) as a model of macro-scale brain dynamics, arising from recurrent activity flow among brain regions. An fcHNN is neither optimized to mimic certain brain characteristics, nor trained to solve specific tasks; its weights are simply initialized with empirical functional connectivity values.
In the fcHNN framework, brain dynamics are understood in relation to so-called attractor states, i.e. neurobiologically meaningful low-energy activity configurations.
Analyses of 7 distinct datasets demonstrate that fcHNNs can accurately reconstruct and predict brain dynamics under a wide range of conditions, including resting and task states and brain disorders.
By establishing a mechanistic link between connectivity and activity, fcHNNs offers a simple and interpretable  computational alternative to conventional descriptive analyses of brain function. Being a generative framework, fcHNNs can yield mechanistic insights and hold potential to uncover novel treatment targets.
+++

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
However, the need to estimate a vast number of free parameters in such models hampers their ability to effectively bridge the gap between explanations at the level of single neurons and the complexity of behavior {cite:p}`breakspear2017dynamic`.
Recent efforts using coarse-grained brain network models {cite:p}`schirner2022dynamic; schiff1994controlling; papadopoulos2017development; seguin2023brain` and linear network control theory  {cite:p}`chiem2021structure; scheid2021time; gu2015controllability` opted to trade biophysical fidelity to phenomenological validity. The challenge for such models lies in modelling the relation between the structural wiring of the brain and functional connectivity.
The "neuroconnectionist" approach, on the other hand, {cite:p}`doerig2023neuroconnectionist` aims at "cognitive/behavioral fidelity" {cite:p}`kriegeskorte2018cognitive`, by using artificial neural networks (ANNs) that are trained to perform various tasks, as brain models. However, the need to train ANNs for specific tasks inherently limits their ability to explain task-independent, spontaneous neural dynamics {cite:p}`richards2019deep`.

Here we propose a novel approach that combines the advantages of large-scale network models and neuroconnectionism, to investigate brain dynamics.
Similar to neuroconnectionism, we utilize an ANN as a high-level computational model of the brain.
However, our model is not explicitly trained for a specific task. Instead, we set its weights empirically, with data based on the "activity flow" {cite:p}`cole2016activity; ito2017cognitive` across regions within the functional brain connectome, as measured with functional magnetic resonance imaging (fMRI, {numref}`concept`B). 

Specifically, we employ a continuous-space Hopfield Neural Network (HNN) {cite:p}`hopfield1982neural; krotov2023new`, with its nodes representing large-scale brain areas, and its weights initialized with the functional connectivity values between these areas.
Based on the topology of the functional connectome, this architecture establishes an energy level for any arbitrary activation patterns and determines a "trajectory of least action" towards one of the finite number of stable patterns, known as *attractor states*, that minimize this energy.
In this simple yet powerful framework, brain dynamics can be conceptualized as an intricate, high-dimensional path on the energy landscape ({numref}`concept`C), arising from the activity flow {cite:p}`cole2016activity` within the functional connectome and constrained by the "gravitational pull" of the attractor states of the system.
Given its generative nature, the proposed model offers testable predictions for the effect of various perturbations and alterations of these dynamics, from task-induced activity to changes related to brain disorders.

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

In the present work, we use HNNs to explore the functional connectome's attractor-dynamics with the aid of a streamlined, low-dimensional representation of the energy landscape.
Subsequently, we use a diverse set of experimental, clinical and meta-analytic studies to evaluate our model's ability to reconstruct various characteristics of resting state brain dynamics, as well as its capacity to detect and explain changes induced by experimental tasks or alterations in brain disorders.

## Results

### Connectome-based Hopfield network as a model of brain dynamics

First, we explored the attractor states of the functional connectome in a sample of n=41 healthy young 
participants ([study 1](tab-samples), see Methods [](tab-samples) for details). We estimated interregional activity flow {cite:p}`cole2016activity; ito2017cognitive` 
as the study-level average of regularized partial correlations among the resting state fMRI timeseries of m = 122 
functionally defined brain regions (see [Methods](#Functional-connectome) for details). We then used the standardized 
functional connectome as the $w_{ij}$  weights of a fully connected recurrent ANN, specifically a continuous-state Hopfield network {cite:p}`hopfield1982neural; koiran1994dynamics`, consisting of $m$ neural units, each having an activity 
$a_i \in [-1,1] \subset \mathbb{R})$. Hopfield networks can be initialized by an arbitrary activation pattern (consisting of $m$ activation values) and iteratively updated (i.e. "relaxed") until their energy converges a local minimum, that is, to one of the finite number of attractor states (see [Methods](#connectome-based-hopfield-networks)). The relaxation procedure is based on a simple rule; in each iteration, the activity of a region is constructed as the weighted average of the activities of all other regions, with weights defined by the connectivity between them. The average is then transformed by a sigmoidal activation function, to keep it in the desired [-1,1] interval.
This can be expressed by the following equation:

```{math}
:label: hopfield-update
\dot{a}_i = S(\beta \sum_{j=1}^m w_{ij}a_j - b_i)
```

where $\dot{a}_i$ is the activity of neural unit $i$ in the next iteration and $S(a_j)$ is the sigmoidal activation 
function ($S(a) = tanh(a)$ in our implementation) and $b_i$ is the bias of unit $i$ and $\beta$ is the so-called temperature parameter. For the sake of simplicity, we set $b_i=0$ in all our experiments. We refer to this architecture as a functional connectivity-based Hopfield Neural Network (fcHNN).
The relaxation of a fcHNN model can be conceptualized as the repeated application of the activity flow principle {cite:p}`cole2016activity; ito2017cognitive` , simultaneously for all regions: $\dot{a}_i = \sum_{j=1}^m w_{ij}a_j$. The update rule also exhibits analogies with network control theory {cite:p}`gu2015controllability` and the inner workings of neural mass models, as applied e.g. in dynamic causal modeling {cite:p}`daunizeau2012stochastic`.

Hopfield networks assign an energy value to each possible activity configuration {cite:p}`hopfield1982neural; koiran1994dynamics`, which decreases during the relaxation procedure until reaching an equilibrium state with minimal energy ({numref}`attractors`A, top panel).
We used a large number of random initializations to obtain all possible attractor states of the connectome-based 
Hopfield network in study 1 ({numref}`attractors`A, bottom panel).

:::{figure} figures/embedding_method.png
:name: attractors
**Attractor states and state-space dynamics of connectome-based Hopfield networks** <br/><br/>
**A** Top: During so-called relaxation procedure, activities in the nodes of an fcHNN model are iteratively updated based on the activity of all other regions and the connectivity between them. The energy of a
connectome-based Hopfield network decreases during the relaxation procedure until reaching an equilibrium state with 
minimal energy, i.e. an attractor state. Bottom: Four attractor states of the fcHNN derived from the
group-level functional connectivity matrix from [study 1](tab-samples) (n=44). 
**B** Top: In presence of weak noise (stochastic update), the system 
does not converge to equilibrium anymore. Instead, activity traverses on the state landscape in a way 
restricted by the topology of the connectome and the "gravitational pull" of the attractor states. Bottom: We sample 
the "state landscape" by running the stochastic relaxation procedure for an extended amount of time (e.g. 100.000 consecutive
stochastic updates), each point representing an activation configuration or state. To construct a 
low-dimensional representation of the state space, we take the first two principal components of the simulated activity
patterns. The first two principal components explain approximately 58-85% of the variance of state energy (depending 
on the noise parameter $\sigma$, see {numref}`Supplementary Figure %s <si_expl_variance_energy>`).
**C** We map all states of the state space sample to their corresponding attractor state, with the conventional 
Hopfield relaxation procedure (A). The four attractor states are also visualized in their corresponding position on the
PCA-based projection. The first two principal components yield a clear separation of the attractive state basins 
(cross-validated classification accuracy: 95.5%, {numref}`Supplementary Figure %s <si_classification_acc_state_basins>`). We refer to the resulting visualization
as the fcHNN projection and use it to visualize fcHNN-derived and empirical brain dynamics throughout the rest of 
the manuscript.
**E** At its simplest form, the fcHNN framework entails only two free hyperparameters: the temperature parameter 
$\beta$ (left) that controls the number of attractor states and the noise parameter of the stochastic relaxation 
$\sigma$. To avoid overfitting these parameters to the empirical data, we set $\beta=0.04$ and $\sigma=0.37$ for the 
rest of the paper (dotted boxes).
:::

Consistent with theoretical expectations, we observed that increasing the temperature parameter $\beta$ led to an 
increasing number of attractor states ({numref}`attractors`E, left, {numref}`Supplementary Figure %s <si_att_state_emergence_over_beta>`), appearing in symmetric pairs 
(i.e. $a_i^{(1)} = -a_i^{(2)}$). For simplicity, we set the temperature parameter for the rest of the paper to a value
resulting in 4 distinct attractor states ($\beta=0.4$).

FcHNNs, without any modifications, always converge to an equilibrium state.
To incorporate stochastic fluctuations in neuronal activity {cite:p}`robinson2005multiscale`, we introduced weak 
Gaussian noise to the fcHNN relaxation procedure. This procedure, referred to as stochastic relaxation, prevents the system from reaching equilibrium and, somewhat similarly to stochastic DCM {cite:p}`daunizeau2012stochastic`, induces complex system dynamics ({numref}`attractors`B).

In order to enhance interpretability, we obtained the first two principal components (PCs) of the states sampled from the stochastic relaxation procedure.
The resulting two-dimensional embedding ({numref}`attractors`B, bottom plot) exhibited high consistency across different values of $\beta$ and $\sigma$ ({numref}`attractors`E).
For all subsequent analyses, we set $\sigma=0.37$ (based a coarse optimization procedure aimed at reconstructing the bimodal distribution of empirical data, {numref}`attractors`E right). On the low-dimensional embedding, which we refer to as the *fcHNN projection*, we observed a clear separation of the attractor states ({numref}`attractors`C), with the two symmetric pairs of attractor states located at the extremes of the first and second PC. 
To map the attractor basins on the space spanned by the first two PCs ({numref}`attractors`C), we obtained the attractor state of each point visited during the stochastic relaxation and fit a multinomial logistic regression model to predict the attractor state from the first two PCs. 
The resulting model accurately predicted attractor states of arbitrary brain activity patterns, achieving a cross-validated accuracy of 96.5%.
The attractor basins were visualized by using the decision boundaries obtained from this model. ({numref}`attractors`C). We propose the 2-dimensional fcHNN projection depicted on ({numref}`attractors`C) as a simplified representation of brain dynamics, and use it as a basis for all subsequent analyses in this work.

### Reconstruction of resting state brain dynamics

The spatial patterns of the obtained attractor states exhibit high neuroscientific relevance and closely resemble previously described large-scale brain systems. ({numref}`rest-validity`A). The first pair of attractors (mapped on PC1, horizontal axis) resemble the two complementary “macro” systems described, among others, by {cite:t}`golland2008data` and {cite:t}`cioli2014differences` as well as the two "primary" brain states observed by {cite:t}`chen2018human` and the 'unimodal-to-transmodal' principal gradient of {cite:t}`margulies2016situating` and {cite:t}` huntenburg2018large`. A common interpretation of these two patterns is that they represent (i) an “extrinsic” system linked to the immediate sensory environment and (ii) an "intrinsic" system for higher-level internal context.
The other pair of attractors spans an orthogonal axis, and resemble to patterns commonly associated with perception–action cycles {cite:p}`fuster2004upper`, and described as a gradient across sensory-motor modalities {cite:p}`huntenburg2018large`, recruiting regions associated with active inference (e.g. motor cortices) and perceptual inference (e.g visual areas).

:::{figure} figures/face_validity.png 
:name: rest-validity
**Connectome-based Hopfield networks reconstruct characteristics of real resting state brain activity.**<br/><br/>
**A** The four attractor states of the fcHNN model from study 1 reflect brain activation 
patterns with high neuroscientific relevance, representing sub-systems previously associated with "internal context"
(blue), "external context" (yellow), "action" (red) and "perception" (green)
{cite:p}`golland2008data; cioli2014differences; chen2018human; fuster2004upper; margulies2016situating`.
**B** The attractor states show excellent replicability in two external datasets (study 2 and 3, mean correlation 0.93). 
**C** The fcHNN projection (first two PCs of the fcHNN state space) explains significantly more variance (p<0.0001) in the real 
resting state fMRI data than principal components derived from the real resting state data itself and generalizes 
better (p<0.0001) to out-of-sample data (study 2). Error bars denote 99% bootstrapped confidence intervals.
**D** The fcHNN of study 1 seeded with real activation maps (gray dots) of an example participant. All activation maps converge to one of the four attractor states during the relaxation procedure (without noise) and the system reaches equilibrium. Trajectories are colored by attractor state.
**E** Illustration of the stochastic relaxation procedure in the same fcHNN model, seeded from a single starting point (activation pattern). The system does not converge to an attractor state but instead traverses the state space in a way restricted by the topology of the connectome and the "gravitational pull" of the attractor states. The shade of the trajectory changes with increasing number of iterations. The trajectory is smoothed with a moving average over 10 iterations for visualization purposes.
**F** Real resting state fMRI data of an example participant from study 1, plotted on the fcHNN projection. The shade of the trajectory changes with an increasing number of iterations.
**G** Flow map of the mean trajectories (i.e. the timeframe-to-timeframe transition direction) in fcHNN-generated data, as compared to a shuffled null model representing zero temporal autocorrelation. The flow map reveals that the "gravitational pull" of the attractor states gives rise to a characteristic temporal autocorrelation structure. 
**H** A similar pattern can be found in real data (flow analysis of all participants from study 1 pooled, as compared to a shuffled null model representing zero temporal autocorrelation).
**I** The fcHNN analysis accurately predicts (p<0.0001) the fraction of time spent on the basis of the four attractor 
states in real restring state fMRI data (study 1) and, 
**J**, reconstructs the characteristic bimodal distribution of the real resting state data.
**K** Stochastic fcHNNs are capable of self-reconstruction: the timeseries resulting from the stochastic relaxation procedure 
mirror the co-variance structure of the functional connectome the fcHNN model was initialized with. 
:::

The discovered attractor states demonstrate remarkable replicability (mean Pearson's 
correlation 0.93) across the discovery dataset (study 1) and two independent replication datasets 
([study 2 and 3](tab-samples), {numref}`rest-validity`C). Moreover, they were found to be robust to noise added to the connectome ({numref}`Supplementary Figure %s <si_noise_robustness_weights>`).

Further analysis in study 1 showed that connectome-based Hopfield models accurately reconstructed multiple 
characteristics of true resting-state data.
First, the two axes of the fcHNN projection accounted for a substantial amount of variance in the real resting-state fMRI data in study 1 (mean $R^2=0.399$) and generalized well to out-of-sample data (study 2, mean $R^2=0.396$)  ({numref}`rest-validity`E). Remarkably, the explained variance of the fcHNN projection significantly exceeded that of a PCA performed directly on the real resting-state fMRI data itself ($R^2=0.37$ and $0.364$ for in- and out-of-sample analyses).

Second, fcHNN analyses accurately reconstructed various aspects of true resting state brain dynamics. 
Panel D on {numref}`rest-validity` shows that, with the conventional Hopfield relaxation procedure, individual activation maps converge to one of the four attractor states. When weak noise is introduced to the system (stochastic relaxation, panel E), the system does not converge to an attractor state but the resulting path is still influenced by the attractor states' gravity. The empirical timeseries data exhibits a similar pattern not only visually (panel F), but also when quantifying the average trajectories of flow, as compared to null-models of zero temporal autocorrelation (randomized timeframe order), reflecting the "gravitational pull" of attractor states ({numref}`rest-validity` G and H, see [Methods](#evaluation-resting-state-dynamics) fro analysis details). 

During stochastic relaxation, the fcHNN model was found to spend approximately three-quarters of the time on the basis of the first two attractor states and one-quarter on the basis of the second pair of attractor states (approximately equally distributed between pairs). We observed strikingly similar temporal occupancies in the real data {numref}`rest-validity`D), statistically significant with various null models ({numref}`Supplementary Figure %s <si_state_occupancy_null_models>`). Fine-grained details of the bimodal distribution observed in the real resting-state fMRI data were also convincingly reproduced by the fcHNN model ({numref}`rest-validity`F and {numref}`attractors`E).

Finally, fcHNNs were found to generate signal that preserves the covariance structure of the real functional connectome, indicating that dynamic systems of this type (including the brain) inevitably "leak" their underlying structure into the activity time series, strengthening the construct validity of our approach ({numref}`rest-validity`D).

### An explanatory framework for task-based brain activity

Next to reproducing various characteristics of spontaneous brain dynamics, fcHNNs can also be used to model responses to various perturbations. We obtained task-based fMRI data from a study by {cite:t}`woo2015distinct` ([study 4](tab-samples), n=33, see {numref}`rest-validity`), investigating the neural correlates of pain and its self-regulation. 

We found that activity changes due to pain (taking into account hemodynamics, see [Methods](#evaluation-task-based-dynamics)) were characterized on the fcHNN projection by a shift towards the attractor state of action/execution (permutation test for mean projection difference by randomly swapping conditions, p<0.001, {numref}`task-validity`A, left). Energies, as defined by the fcHNN, were also significantly different between the two conditions (p<0.001), with higher energies during pain stimulation.

When participants were instructed to up- or downregulate their pain sensation (resulting in increased and decreased pain reports and differential brain activity in the nucleus accumbens, NAc (see {cite}`woo2015distinct` for details), we observed further changes of the location of momentary brain activity patterns on the fcHNN projection (p<0.001, {numref}`task-validity`A, right), with downregulation pulling brain dynamics towards the attractor state of internal context and perception. Interestingly, self-regulation did not trigger significant energy changes (p=0.36). 

:::{figure} figures/task_validity.png
:name: task-validity
**Empirical Hopfield-networks reconstruct real task-based brain activity.** <br></br>
**A** Functional MRI time-frames during pain stimulation from [study 4](tab-samples) (second fcHNN projection plot)
and self-regulation (third and fourth) are distributed differently on the fcHNN projection than brain states 
during rest (first projection, permutation test, p<0.001 for all). Energies, as defined by the Hopfield model, are also
significantly different between rest and the pain conditions (permutation test, p<0.001), with higher energies during 
pain stimulation. Triangles denote participant-level mean activations in the various blocks (corrected for 
hemodynamics). Small circle plots show the directions of the change for each individual (points) as well as the mean direction
across participants (arrow), as compared to the reference state (downregulation for the last circle plot, rest for all 
other circle plots).
**B** Flow-analysis (difference in the average timeframe-to-timeframe transition direction) reveals a non-linear difference in brain dynamics during pain and rest (left). When introducing weak pain-related signal in the fcHNN model during stochastic relaxation, it accurately reproduces these non-linear flow differences (right).
**C** Simulating activity in the Nucleus Accumbens (NAc) (the region showing significant activity differences in {cite}`woo2015distinct`) reconstructs the observed non-linear flow difference between up- and downregulation (left).
**D** Schematic representation of brain dynamics during pain and its up- and downregulation, visualized on the fcHNN  projection. In the proposed framework, pain does not simply elicit a direct response in certain regions, but instead, shifts spontaneous brain dynamics towards the "action" attractor, converging to a characteristic "ghost attractor" of pain. Down-regulation by NAc activation exerts force towards the attractor of internal context, leading to the brain less frequent "visiting" pain-associated states.
**E** Visualizing meta-analytic activation maps (see {numref}`Supplementary Table %s <si-tab-neurosynth>` for details) on the fcHNN projection captures intimate relations between the corresponding tasks and **F** serves as a basis for a fcHNN-based theoretical interpretative framework for spontaneous and task-based brain dynamics. In the proposed framework, task-based activity is not a mere response to external stimuli in certain brain locations but a perturbation of the brain's characteristic dynamic trajectories, constrained by the underlying functional connectivity. From this perspective, "activity maps" from conventional task-based fMRI analyses capture time-averaged differences in these whole brain dynamics. 
:::

Next, we conducted a "flow analysis" on the fcHNN projection, quantifying how the average timeframe-to-timeframe transition direction differs on the fcHNN projection between conditions (see [Methods](#evaluation-task-based-dynamics)).
This analysis unveiled that during pain ({numref}`task-validity`B, left side), brain activity tends to gravitate towards a distinct point on the projection on the boundary the basins of the internal and action attractors, which we term the "ghost attractor" of pain (similar to {cite}`vohryzek2020ghost`). In case of downregulation (as compared to upregulation), brain activity is pulled away from the pain-related "ghost attractor" ({numref}`task-validity`C, left side), towards the attractor of internal context.

Our fcHNN was able to accurately reconstruct these non-linear dynamics by adding a small amount of realistic "control signal" (similarly to network control theory {cite}`liu2011controllability; gu2015controllability`). To simulate the alterations in brain dynamics during pain stimulation, we acquired a meta-analytic pain activation map {cite:p}`zunhammer2021meta` (n=603) and incorporated it as a control signal added to each iteration of the stochastic relaxation procedure. The ghost attractor found in the empirical data was present across a relatively wide range of signal-to-noise (SNR) values ({numref}`Supplementary Figure %s <si_pain_ghost_attractor_sim>`). Results with SNR=0.005 are presented on {numref}`task-validity`B, right side (Pearson's r = 0.46, p=0.005 based on randomizing conditions on a per-participant basis).

The same model was also able to reconstruct the observed non-linear differences in brain dynamics between the up- and downregulation conditions (Pearson's r = 0.62, p=0.023) without any further optimization (SNR=0.005, 
{numref}`task-validity`C, right side). The only change we made to the model was the addition (downregulation) or 
subtraction (upregulation) of control signal in the NAc (the region in which {cite:p}`woo2015distinct` observed significant changes between up- and downregulation), introducing a signal difference of $\Delta$SNR=0.005 (the same value we found optimal in the pain-analysis). Results were reproducible with lower NAc SNRs, too ({numref}`Supplementary Figure %s <si_downreg_trajectory_sim>`).

To provide a comprehensive picture on how tasks and stimuli other than pain map onto the fcHNN projection, we obtained various task-based meta-analytic activation maps from Neurosynth (see [Methods](#evaluation-task-based-dynamics)) and plotted them on the fcHNN projection ({numref}`task-validity`E). This analysis reinforced and extended our interpretation of the four investigated attractor states and shed more light on how various functions are mapped on the axes of internal vs. external context and perception vs. action.
In the coordinate system of the fcHNN projection, visual processing is labeled "external-perception", sensory-motor processes fall into the "external-active" domain, language, verbal cognition and working memory belongs to the "internal-active" region and long-term memory as well as social and autobiographic schemata fall into the "internal-perception" regime ({numref}`task-validity`F).

### Clinical relevance

We obtained data from n=172 autism spectrum disorder (ASD) and typically developing control (TDC) individuals, acquired at the New York University Langone Medical Center, New York, NY, USA (NYU) and generously shared in the Autism Brain Imaging Data Exchange dataset ([study 7](tab-samples): ABIDE, {cite:p}`di2014autism`.
After excluding high-motion cases (see [Methods](#clinical-data)), we visualized the distribution of time-frames on the fcHNN-projection separately for the ASD and TDC groups ({numref}`clinical-validity`A).
First, we assigned all timeframes to one of the 4 attractor states with the fcHNN from study 1 and found several significant differences in the mean activity on the attractor basins (see [Methods](#clinical-data)) of the ASD group as compared to the respective controls ({numref}`clinical-validity`B).
Strongest differences were found on the "action-perception" axis ({numref}`tab-clinical-results`), with increased activity of the sensory-motor and middle cingular cortices during "action-execution" related states and increased visual and decreased sensory and auditory activity during "perception" states, likely reflecting the widely acknowledged, yet poorly understood, perceptual atypicalities in ASD {cite:p}`hadad2019perception`. ASD related changes in the internal-external axis were characterized by more involvement of the posterior cingulate, the precuneus, the nucleus accumbens, the dorsolateral prefrontal cortex (dlPFC), the cerebellum (Crus II, lobule VII) and inferior temporal regions during activity of the internalizing subsystem ({numref}`tab-clinical-results`). While similar, default mode network (DMN)-related changes have often been attributed to an atypical integration of information about the “self” and the “other” {cite:p}`padmanabhan2017default`, a more detailed fcHNN-analysis may help to further disentangle the specific nature of these changes.

:::{figure} figures/state_analysis.*
:name: clinical-validity
**Connectome-based Hopfield analysis of autism spectrum disorder.** <br></br>
**A** The distribution of time-frames on the fcHNN-projection separately for ASD patients and typically developing control (TDC) participants. <br></br>
**B** We quantified attractor state activations in the Autism Brain Imaging Data Exchange datasets ([study 7](tab-samples)) as the 
individual-level mean activation of all time-frames belonging to the same attractor state. This analysis captured alterations similar to those previously associated to ASD-related perceptual atypicalities (visual, auditory and somatosensory cortices) as well as atypical integration of information about the “self” and the “other” (default mode network regions). All results are corrected for multiple comparisons across brain regions and attractor states (122*4 comparisons) with Bonferroni-correction. See {numref}`tab-clinical-results` and {numref}`Supplementary Figure %s <si_clinical_results_table>` for detailed results. <br></br>
**C** The comparison of data generated by fcHNNs initialized with ASD and TDC connectomes, respectively, revealed a characteristic pattern of differences in the system's dynamics, with increased pull towards (and potentially a higher separation between) the action and perception attractors and a lower tendency of trajectories going towards the internal and external attractors. <br></br>
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

Thus, we contrasted the characteristic trajectories derived from the fcHNN models of the two groups (initialized with the group-level functional connectomes). Our fcHNN-based flow analysis predicted that in ASD, there is an increased likelihood of states returning towards the middle from the internal-external axis and an increased likelihood of states transitioning towards the extremes of the action-perception axis ({numref}`clinical-validity`C). We observed a highly similar pattern in the real data (Pearson's correlation: 0.66), statistically significant after permutation testing (shuffling the group assignment, p=0.009).

## Discussion

In this study, we have introduced and validated a simple yet robust network-level generative computational framework that elucidates how activity propagation within the functional connectome orchestrates large-scale brain dynamics, leading to the spontaneous emergence of brain states, gradients and characteristic dynamic responses to perturbations.

The construct validity of our model is rooted in the activity flow principle, first introduced by {cite:t}`cole2016activity`. The activity flow principle states that activity in a brain region can be predicted by a weighted combination of the activity of all other regions, where the weights are set to the functional connectivity of those regions to the held-out region. This principle has been shown to hold across a wide range of experimental and clinical conditions {cite:p}`cole2016activity; ito2017cognitive; mill2022network; hearne2021activity; chen2018human`.
The proposed approach is based on the intuition that the repeated, iterative application of the activity flow equation exhibits close analogies with a type of recurrent artificial neural networks, known as Hopfield networks {cite:p}`hopfield1982neural`.

Hopfield networks have been widely acknowledged for their relevance for brain function, including the ability to store and recall memories {cite:p}`hopfield1982neural`, self-repair {cite:p}`murre2003selfreparing`,
a staggering robustness to noisy or corrupted inputs {cite:p}`hertz1991introduction` (see also {numref}`Supplementary Figure %s <si_noise_robustness_weights>`) and the ability to produce multistable dynamics organized by the "gravitational pull" of a finite number of attractor states {cite:p}`khona2022attractor`. While many of such properties of Hopfield networks have previously been proposed as a model for micro-scale neural systems (see {cite}`khona2022attractor` for a review), the proposed link between macro-scale activity propagation and Hopfield networks allows transferring the vast body of knowledge on Hopfield networks to the study of large-scale brain dynamics.

Integrating Cole's activity flow principle with the HNN architecture mandates the initiation of network weights with functional connectivity values, specifically partial correlations as suggested by {cite:t}`cole2016activity`.
Considering the functional connectome as weights of an already trained neural network distinguishes our methodology not only from conventional biophysical and phenomenological computational modeling strategies, which usually rely on the structural connectome to model polysynaptic connectivity {cite:p}`cabral2017functional`, but also from "neuroconnectionist" approaches that employ explicit training procedures {cite:p}`doerig2023neuroconnectionist`.

In contrast to finely detailed biophysical models with many free parameters, the basic form of the fcHNN approach comprises solely two, easily interpretable  "hyperparameters" (temperature and noise) and yields notably consistent outcomes across an extensive range of these parameters ({numref}`Supplementary Figure %s <si_expl_variance_energy>`, {numref}`%s <si_att_state_emergence_over_beta>`, {numref}`%s <si_state_occupancy_null_models>`, {numref}`%s <si_pain_ghost_attractor_sim>`, {numref}`%s <si_downreg_trajectory_sim>`). To underscore the potency of this simplicity and stability, in the present work, we avoided any unnecessary parameter optimization. It is likely, however, that extensive parameter optimization could further improve the performance of the model.

%Another advantage of fcHNNs over more detailed models is that fcHNNs establish a simple and easily interpretable link between two highly prevalent metrics of brain function: functional connectivity and brain activity. This connection is not solely phenomenological, but also mathematical, facilitating the exploration and prediction of alterations in the system's dynamics in response to perturbations affecting both activity and connectivity.

The proposed model is different from, but compatible with, linear network control theory-based (Gu et al., 2015) approaches. The fact that fcHNNs work with direct activity flow estimates, means however, that we do not have to tackle the challenge of modelling the structural-functional coupling {cite:p}`seguin2023brain`. Further, the fcHNN approach allows us to leverage on knowledge about the underlying ANN architecture. Specifically, Hopfield attractor dynamics provide a mechanistic account for the emergence of large-scale canonical brain networks (Zalesky et al., 2014) ), and shed light to the origin of characteristic task-responses that are accounted by "ghost attractors" in the system {cite:p}`deco2012ongoing; vohryzek2020ghost`.

As fcHNNs do not need to be trained to solve any explicit tasks, they are well suited to examine spontaneous brain dynamics. However, it is worth mentioning that fcHNNs are compatible with the neuroconnectionist approach (Doerig et al., 2021), as well.
Like any other ANNs, fcHNNs can also be further trained via established ANN training techniques (e.g. via the Hebbian learning rule) to "solve" various tasks or to match altered dynamics during development or in clinical populations. In this promising future direction, the training procedure itself becomes part of the model, providing testable hypotheses about the formation, and various malformations, of brain dynamics.

Given its simplicity, it is remarkable, if not surprising, how accurately the fcHNN model is able to reconstruct and predict brain dynamics under a wide range of conditions. Particularly interesting is the result that the two-dimensional fcHNN projection can explain more variance in real resting state fMRI data than the first two principal components derived from the data itself. 
A plausible explanation for the remarkable reconstruction performance is that, through their known noise tolerance, fcHNNs are able to capture essential principles of the underlying dynamic processes even if our empirical measurements are corrupted by noise and low sampling rate.
 Indeed, fcHNN attractor states were found to be robust to noisy weights ({numref}`Supplementary Figure %s <si_noise_robustness_weights>`) and highly replicable across datasets acquired at different sites, with different scanners and imaging sequences (study 2 and 3). The observed level of replicability allowed us to re-use the fcHNN model constructed with the connectome of study 1 for all subsequent analyses, without any further fine-tuning or study-specific parameter optimization.

 Conceptually, the notion of a global attractor model of the brain network is not new {cite:p}`deco2012ongoing`. The present work shows, however, that the brain as an attractor network necessarily 'leaks' its code in form of the partial correlation across the regional timeseries, posing fcHNNs as the preferred technique to uncover its large-scale attractor states. We demonstrate that the reconstructed attractor states are not solely local minima in the state-space but act as a driving force for the dynamic trajectories of brain activity. Attractor-dynamics may be the main driving factor for the spatial and temporal autocorrelation structure of the brain, recently described to be predictive of network topology in relation to age, subclinical symptoms of dementia, and pharmacological manipulations with serotonergic drugs {cite:p}`shinn2023functional`. 
Nevertheless, attractor states should not be confused with the conventional notion of brain states {cite:p}`chen2015introducing` and large-scale functional gradients {cite:p}`margulies2016situating`. In the fcHNN framework, attractor states can rather be conceptualized as "Platonic idealizations" of brain activity, that are continuously approximated - but never reached - by the brain, resulting in re-occurring patterns (brain states) and smooth gradual transitions (large-scale gradients).

Relying on previous work, we can establish a relatively straightforward (although somewhat speculative) correspondence between attractor states and brain function, mapping brain activation on the axes of internal vs. external context {cite:p}`golland2008data; cioli2014differences`, as well as perception vs. action {cite:p}`fuster2004upper`.
This four-attractor architecture exhibits an appealing analogy with Friston's free energy principle {cite:p}`friston2006free` that postulate the necessary existence of subsystems for active and perceptual inference as well as a hierarchically organized (i.e. external and internal) subsystems that give rise to consciousness {cite:p}`ramstead2023inner, lee2023life`.

Both conceptually and in terms of analysis practices, resting and task states are often treated as separate phenomena. However, in the fcHNN framework, the differentiation between task and resting states is considered an artificial dichotomy. 
Task-based brain activity in the fcHNN framework is not a mere response to external stimuli in certain brain locations but a perturbation of the brain's characteristic dynamic trajectories, with increased preference for certain locations on the energy landscape ("ghost attractors").
In our analyses, the fcHNN approach capture and predict participant-level activity changes induced by pain and its self-regulation and gave a mechanistic account for how relatively small activity changes in a single region (NAcc) may result in a significantly altered pain experience.

Brain dynamics can not only be perturbed by task or other types of experimental or naturalistic interventions, but also by pathological alterations. Here we have demonstrated (study 7) that fcHNN-based analyses can characterize and predict altered brain dynamics in autism spectrum disorder (ASD). The observed ASD-associated changes in brain dynamics are indicative of a reduced ability to flexibly switch between perception and internal representations, corroborating previous findings that in ASD, sensory-driven connectivity transitions do not converge to transmodal areas {cite:p}`hong2019atypical`. Such findings are in line with previous reports of a reduced influence of context on the interpretation of incoming sensory information in ASD (e.g. the violation of Weber's law) {cite:p}`hadad2019perception`.

Together, our findings open up a series of exciting opportunities for the better understanding of brain function in health and disease.

First, the 2-dimensional fcHNN projection offers a streamlined framework not only for the visualization, but also for the *interpretation*, of brain activity patterns, as it conceptualizes changes related to various behavioral or clinical states or traits as a shift in brain dynamics in relation to brain attractor states.

Second, fcHNN analyses may provide insights into the causes of changes in brain dynamics, by for instance, identifying the regions or connections that act as an "Achilles heel" in generating such changes. Such analyses could, for instance, aid the differentiation of primary causes and secondary effects of particular activity or connectivity changes in various clinical conditions.

Third, the fcHNN approach can provide testable predictions about the effects of pharmacological interventions as well as non-invasive brain stimulation (e.g. transcranial magnetic or direct current stimulation, focused ultrasound, etc) and neurofeedback. Obtaining the optimal stimulation or treatment target within the fcHNN framework (e.g. by means of network control theory {cite:p}`liu2011controllability`) is one of the most promising future directions with the potential to significantly advance the development of novel, personalized treatment approaches.

In this initial work, we presented the simplest possible implementation of the fcHNN concept. It is clear that the presented analyses exploit only a small proportion of the richness of the full state-space dynamics reconstructed by the fcHNN model. 
There are many potential ways to further improve the utility of the fcHNN approach. Increasing the number of reconstructed attractor states (by increasing the temperature parameter), investigating higher-dimensional dynamics, fine-tuning the hyperparameters, testing the effect of different initializations and perturbations are all important direction for future work, with the potential to further improve the model's accuracy and usefulness.

% **other potential topics**:
% - is the functional connectome stationary? Why don't we use dynamic connectivity? See arguments by the Cole-group. Also, the fcHNN model can actually probably also reproduce task-based connectivity, when adding a task-related control signal to the stochastic relaxation procedure (as on Fig. 3). Thus it could be a model of how task-based connectivity and dynamic connectivity changes arise from the underlying rs-fMRI connectome. Maybe it could be even better to use "latent-FC" a'la McCormick, 2022, [](https://doi.org/10.1162/netn_a_00234))
% - why no HRF modelling (could be a possible extension, but it is also not part of the activity flow approach and we don't reconstruct time series, per-se, but rather activations)
% - the fcHNN model is not a model of brain function, but a model of brain dynamics. It does not strive to explain various brain regions ability to perform certain computations, but the brain's characteristic dynamic "trajectories", and how these are perturbed by tasks and other types of interventions.

## Conclusion

To conclude, here we have proposed a lightweight, high-level computational framework that accurately captures and predicts brain dynamics under a wide range of conditions. The framework models large-scale activity flow in the brain with a recurrent artificial neural network architecture that, instead of being trained to solve specific tasks or mimic certain dynamics, is simply initialized with the empirical functional connectome. The framework identifies neurobiologically meaningful attractor states and provides a model for how these restrict brain dynamics. The proposed framework, referred to as the connectome-based Hopfield neural network (fcHNN) model, can accurately reconstruct and predict brain dynamics under a wide range of conditions, including resting states, task-induced activity changes and brain disorders. FcHNNs establish a conceptual link between connectivity and activity, provide a mechanistic account for the emergence of brain states, gradients and autocorrelation structure and offer a simple, robust, and highly interpretable computational alternative to conventional descriptive approaches to investigating brain function. The generative nature of the proposed model opens up a series of exciting opportunities for future research, including predicting the effect, and understanding the mechanistic bases, of various interventions; thereby paving the way for designing novel treatment approaches.


+++ {"part": "acknowledgements"}
## Acknowledgements

The work was supported by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation; projects ‘TRR289 - Treatment Expectation’, ID 422744262 and ‘SFB1280 - Extinction Learning’, ID 316803389) and by IBS-R015-D1 (Institute for Basic Science; C.W.-W.).
+++

+++ {"part": "data-availability"}

## Analysis source code
https://github.com/pni-lab/connattractor

## Project website
https://pni-lab.github.io/connattractor/

## Data availability
Study 1, 2 and 4 is available at openneuro.org (ds002608, ds002608, ds000140). Data for study 3 is available upon request. Data for study 5-6 is available at the github page of the project: https://github.com/pni-lab/connattractor. Study 7 is available at https://fcon_1000.projects.nitrc.org/indi/abide/, preprocessed data is available at http://preprocessed-connectomes-project.org/.
+++
