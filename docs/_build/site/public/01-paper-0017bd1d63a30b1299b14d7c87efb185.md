

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

:::{figure} figures/concept.png
:name: concept
**Connectome-based Hopfield networks as models of macro-scale brain dynamics.** <br/><br/>
**A** Hopfield artificial neural networks (HNNs)  are a form of recurrent artificial neural networks that serve as content-addressable ("associative") memory systems. Hopfield networks can be trained to store a finite number of patterns (e.g. via Hebbian learning a.k.a. "fire together -  wire together"). During the training procedure, the weights of the HNN are trained so that the stored 
patterns become stable attractor states of the network. Thus, when the trained network is presented partial, noisy or corrupted variations of the stored patterns, it can effectively reconstruct the original pattern via an iterative relaxation procedure that converges to the attractor states.
**B** We consider regions of the brain as nodes of a Hopfield network. Instead of initilaizing the network with the structural wiring of the brain or training it to solve specific tasks, we set its weights empirically, using information about the interregional "activity flow" across regions, as estimated via functional brain connectivity. Capitalizing on strong analogies between the relaxation rule of Hopfield networks and the activity flow principle that links activity to connectivity in brain networks, we propose the resulting 
functional connectome-based Hopfield neural network (fcHNN) as a minimal phenomenological model for macro-scale brain dynamics.  
**C** The proposed computational framework assigns an energy level, an attractor state and a position in a 
low-dimensional embedding to brain activation patterns. Additionally, it models how the entire state-space of viable activation patterns is restricted by the dynamics of the system and how alterations in activity and/or connectivity modify these dynamics.
:::

In the present work, we investigate how well the functional connectome is suited to be an attractor network, map the corresponding attractoir states and model itinerant stochastic dynamics traversing the different basins of attraction of the system.
We use a diverse set of experimental, clinical and meta-analytic studies to evaluate our model's ability to reconstruct various characteristics of resting state brain dynamics, as well as its capacity to detect and explain changes induced by experimental conditions or alterations in brain disorders.

