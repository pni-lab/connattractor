---
subject: Manuscript draft
#subtitle: Optional Subtitle
short_title: Methods

abbreviations:
  fMRI: functional Magnetic Resonance Imaging
  fcHNN: functional connectome-based Hopfield Neural Network
  HNN: Hopfield Neural Network
  ANN: Artificial Neural Network
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
    output: exports/connattractor_methods.pdf
  - format: docx
    hideFooter: true
    output: exports/connattractor_methods.docx

bibliography:
  - bibliography.bib
---


# Methods

### Data

We obtained functional MRI data from 7 different sources ([](tab-samples)).
We included three resting state studies with healthy volunteers (study 1, study 2, study 3, $n_{total}=118$), one task-based study (study 4, $n_{total}=33$ participants, 9 runs each), an individual participant meta-analytic pain activation map of pain (study 5, $n_{total}=603$ from 20 different studies), 8 task-based activation patterns obtained from coordinate-based meta-analyses via Neurosynth (study 6, 14371 studies in total, see {numref}`Supplementary Table %s <si-tab-neurosynth>`) and a resting state dataset focusing on ASD from the ABIDE (Autism Brain Imaging Data Exchange, study 6, $n_{total}=1112$, {cite}`di2014autism`).

```{list-table} **Datasets and studies.** The table includes details about the study modality, analysis aims, sample size used for analyses, mean age, gender ratio, and references.
:header-rows: 1
:name: tab-samples

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
  - 27.9 ± 9.0 
  - 66%
  - [](https://doi.org/10.1371/journal.pbio.1002036)
* - study 5 (Metaanalysis)
  - task-based
  - IPD meta-analysis pain map
  - n=603 (20 studies)
  - 26.3 ± 5.9
  - 39%
  - {cite}`zunhammer2021meta`
* - study 6 (Neurosynth)
  - task-based
  - coordinate-based meta-analyses
  - 14371 studies in total
  - N/A
  - N/A
  - [](https://doi.org/10.1038/nmeth.1635)
* - study 7 (ABIDE, NYU sample)
  - resting state
  - Autism Spectrum Disorder
  - ASD: 98; NC: 74
  - 15.3±6.6
  - 20.9%
  - {cite}`di2014autism`
```

Study 1 was used to evaluate the ability of the proposed approach to reconstruct resting state brain activity. Study 2 and 3 served as replications studies for these analyses. Study 1, 2 and 3 is well suited to examine replicability and generalizability; data in these three studies was acquired in 3 different centers from 2 different countries, by different research staff, with different scanners (Philips, Siemens, GE) and different imaging sequences. Further details on study 1-3 are described in [](10.1038/s41467-019-13785-z). The ability of the proposed approach to model task-based perturbation of brain dynamics was evaluated in Study 4, which consisted of nine task-based fMRI runs for each of the 33 healthy volunteers. In all runs, participants received heat pain stimulation. Each stimulus lasted 12.5 seconds, with 3-second ramp-up and 2-second ramp-down periods and 7.5 seconds at target temperature. Six levels of temperature were administered to the participants (level 1: 44.3°C; level 2: 45.3°C; level 3: 46.3°C; level 4: 47.3°C; level 5: 48.3°C; level 6: 49.3°C). In this analysis we used run 1 (passive experience),  run 3 (down-regulation) and run 7 (up-regulation). Participants were asked to cognitively “increase” (regulate-up) or “decrease” (regulate-down) pain intensity. See {cite:t}`woo2015distinct` for details.
Pain control signal for our task-based trajectory analyses on data from study 4 was derived from our participant-level meta-analysis of 20 pain fMRI studies (study 5, n=603). For details, see {cite:t}`zunhammer2021meta`.
To obtain fMRI activation maps for other tasks, we used Neurosynth([](https://doi.org/10.3389/conf.fninf.2011.08.00058)), a web-based platform for large-scale, automated synthesis of functional magnetic resonance imaging (fMRI) data. We performed 8 different coordinate-based meta-analyses with the terms "motor", "auditory", "visual", "face", "autobiographical", "theory mind", "language" and "pain" ({numref}`Supplementary Table %s <si-tab-neurosynth>`) and obtained the Z-score maps from a two-way ANOVA, comparing the coordinates reported for studies with and without the term of interest, and testing for the presence of a non-zero association between term use and voxel activation.
In study 7 (ABIDE), we obtained preprocessed regional timeseries data from the Preprocessed Connectome Project {cite:p}`craddock2013towards`, as shared (https://osf.io/hc4md) by {cite:t}`dadi2019benchmarking`. All preprocessed timeseries data were obtained with the 122-region version of the BASC (Bootstrap Analysis of Stable Clusters) brain atlas {cite:p}`bellec2010multi`.

### Preprocessing and timeseries extraction

Functional MRI data from studies 1-4 was preprocessed with our in-house analysis pipeline, called the RPN-pipeline (https://github.com/spisakt/RPN-signature). The RPN-pipeline is based on PUMI (Neuroimaging Pipelines Using Modular workflow Integration, https://github.com/pni-lab/PUMI), a nipype-based {cite:p}`gorgolewski2011nipype` workflow management system. It capitalizes on tools from FSL {cite:p}`jenkinson2012fsl`, ANTS {cite:p}`avants2011reproducible` and AFNI {cite:p}`cox1996afni`, with code partially adapted from the software tools C-PAC {cite:p}`craddock2013towards` and niworkflows {cite:p}`esteban2019fmriprep`, as well as in-house python routines. We run the containerized version of the pipeline with default parameters, as in [](10.1038/s41467-019-13785-z). 

Brain extraction from both the anatomical and the structural images, as well as tissue-segmentation from the anatomical images was performed with FSL bet and fast. Anatomical images were linearly and non-linearly co-registered to the 1mm-resolution MNI152 standard brain template brain with ANTs (see https://gist.github.com/spisakt/0caa7ec4bc18d3ed736d3a4e49da7415 for parameters).

Functional images were co-registered to the anatomical images with the boundary-based registration technique of FSL flirt. All resulting transformations were saved for further use. The preprocessing of functional images happened in the native image space, without resampling. Realignment-based motion-correction was performed with FSL mcflirt. The resulting six head motion estimates (3 rotations, 3 translations), their squared versions, their derivatives and the squared derivatives (known as the Friston-24-expansion, {cite}`friston1996movement`) were calculated to be used as nuisance signals. Additionally, head motion was summarized as framewise displacement (FD) timeseries, according to Power’s method {cite:p}`power2012spurious`, to be used in data censoring and exclusion. After motion-correction, outliers (e.g. motion spikes) in timeseries data were attenuated using AFNI despike. The union of the eroded white-matter maps and ventricle masks were transformed to the native functional space and used for extracting noise-signal for anatomical CompCor correction {cite:p}`behzadi2007component`.

In a nuisance regression step, 6 CompCor parameters (the 6 first principal components of the noise-region timeseries), the Friston-24 motion parameters and the linear trend were removed from the timeseries data with a general linear model. On the residual data, temporal bandpass filtering was performed with AFNI’s 3DBandpass to retain the 0.008–0.08Hz frequency band. To further attenuate the impact of motion artifacts, potentially motion-contaminated time-frames, defined by a conservative FD>0.15mm threshold, were dropped from the data (known as scrubbing, {cite}`satterthwaite2013improved`). Participants were excluded from further analysis if more than 50% of frames were scrubbed.

The 122-parcel version of the BASC (Multi-level bootstrap analysis of stable clusters) multi-resolution functional brain atlas {cite:p}`bellec2010multi` was individualized; it was transformed to the native functional space of each participant and masked by the  grey-matter mask obtained from the anatomical image, to retain individual grey-matter voxels only. Voxel-timeseries were averaged over these individualized BASC regions.

### Functional connectome

Regional timeseries were ordered into large-scale functional modules (defined by the 7-parcel level of the BASC atlas) for visualization purposes.
Next, in all datasets, we estimated study-level mean connectivity matrices by regularized partial correlation, via the Graphical Lasso algorithm that estimates a sparse precision matrix by solving a Lasso problem and an L1 penalty for sparsity {cite:p}`varoquaux2010detection`, as implemented in nilearn {cite:p}`abraham2014machine`.  Diagonal elements of the matrices were set to zero. 


### Connectome-based Hopfield networks

Hopfield networks, a type of artificial neural network, consist of a single layer of $m$ fully connected nodes {cite:p}`hopfield1982neural`, with activations $\bold{a} = (a_1, \dots, a_m )$. Hopfield networks assign an energy to any arbitrary activity configurations:

```{math}
:label: energy-function
E = - \frac{1}{2}  \bold{a}^{T} \bold{W} \bold{a} + \bold{a}^{T}\bold{b}
```

where $W$ is the weight matrix with element $w_{i,j}$ denoting the weight between nodes i and j and $\bold{b}$ is the bias, which is set to $\bold{b} = 0$ for all experiments. 

 During the so-called relaxation process, the activities of the nodes are iteratively updated until the network converges to a stable state, known as an attractor state. The dynamics of the network are governed by the equation referenced as eq. [](#hopfield-update) of the main text, or in matrix form:

 ```{math}
 :label: hopfield-update-matrix
 \bold{a'} = S(\beta \bold{W} \bold{a} - \bold{b})
 ```

where $\bold{a'} = ({a'}_1, \dots, {a'}_m)$ is the activity in the next iteration and $S(.)$ is the sigmoidal activation function ($S(a) = tanh(a)$ in our implementation) and $\beta$ is the temperature parameter.
During the stochastic relaxation procedure, we add weak Gaussian noise to each node's activity at every iteration:

```{math}
:label: hopfield-update-matrix-stochastic
\bold{a'} = S(\beta \bold{W} \bold{a} - \bold{b}  + \epsilon),
```

 where $ \epsilon \sim \mathcal{N}(\mathbf{\mu}, \sigma)$, with $\sigma$ regulating the amount of noise added and $\mathbf{\mu}$ set to 0, by default.

In this work we propose functional connectome-based Hopfield neural networks (fcHNNs) as a model for large-scale brain dynamics.
FcHNNs are continuous-state Hopfield neural networks with each node representing a brain region and weights initialized with a group-level functional connectivity matrix. The weights are scaled to zero mean and unit standard deviation.

In studies 1-3, we obtained the finite number of attractor states for all fcHNNs by repeatedly ($10^5$ times) initializing the fcHNN with random activations and relaxing them until convergence. 

### fcHNN projection

We mapped out the fcHNN state-space by initializing our fcHNN model with a random input, and applying the stochastic update step for $10^5$ iterations and storing all visited activity configurations.
We performed a principal component analysis (PCA) on the state samples, and proposed the first two principal component (PCs) as the coordinate system for the fcHNN projection. Using a Multinomial Logistic Regression, we predicted to which attractor state each of the state samples converges to, using the first two PCs as features. The model's performance was evaluated with 10-fold cross-validation. We visualized the attractor states position in the projection as well as the decision boundaries between the attractor states, based on this regression model. We set $\beta = 0.04$, which results in 4 attractor states given the connectome of study 1. We generated fcHNN projections in study 1 with four different $\sigma$ values (0.33, 0.35, 0.37, 0.39) and fixed $\sigma$ at 0.37 for all subsequent analyses. The value of $\sigma$ was selected based on visual inspection of the state space distribution and its similarity to real fMRI data in the fcHNN projection (see [](#rest-validity)).


### Replicability

We obtained the four attractor states in study 1, as described above. We then constructed two other fcHNNs, based on the study-mean functional connectome obtained in studies 2 and 3 and  obtained all attractor states of these models, with the same parameter settings ($\beta = 0.04$ and $\sigma = 0.37$) as in study 1. In both replication studies we found four attractor states. The spatial similarity of attractor states across studies was evaluated by Pearson's correlation coefficient.

### Evaluation: resting state dynamics

Analogously to the methodology of the fcHNN projection, we performed PCA on the preprocessed fMRI time-frames from study 1 (based on the empirical regional timeseries data).
To compare the explanatory power of the first two PCs derived from fcHNN-generated data and real fMRI data, we fitted linear regression models which used the first two fcHNN or real data-based PCs as regressors to reconstruct the real fMRI time-frames. In-sample explained variances and the corresponding confidence intervals were calculated for both models with bootstrapping (100 samples). To evaluate the out-of-sample generalization of the PCs (fcHNN- and real data-based) from study 1, we calculated how much variance they can explain in study 2.

To calculate fractional time occupancies of the attractor states in real timeseries vs simulated data, we used each real and simulated timeframe as an input to the fcHNN of study 1 and obtained the corresponding attractor state. Statistical inference on the similarity of the real fractional occupancies and the fcHNN prediction was performed with two different null models. Null model #1 was constructed  by random sampling from a multivariate normal distribution, with the covariance matrix set based on the functional connectome (partial correlations).
Null model #2 was constructed by a spatial autocorrelation preserving randomization of all time-frames in the real data. More detail on the null-models can be found in {numref}`Supplementary figure %s <si_state_occupancy_null_models>`.

To confirm that the real and fcCHNN temporal sequences (from the stochastic relaxation) on display similar temporal autocorrelation properties, we compared both to their randomly shuffled variant with a "flow analysis".
First we calculated the direction on the projection plane between each successive TR (a vector on the fcHNN projection plane for each TR transition), both for the empirical and the shuffled data.
Next, we obtained a two-dimensional binned means for both the x and y coordinates of these transition vectors (pooled across all participants), calculated over a 2-dimensional grid of 100×100 uniformly distributed bins in the [-6,6] range (arbitrary units) and applied a Gaussian smoothing with a $\sigma$ of 5 bins. 
Finally, we visualized the difference between the binned-mean trajectories of the empirical and the shuffled data as a "streamplot", with the Python package matplotlib.
The same approach was repeated with the fcHNN-generated data.


### Evaluation: task-based dynamics

We used study 4 to evaluate the ability of the fcHNN approach to capture and predict task-induced alterations in large-scale brain dynamics.
sFirst, runs 1, 3 and 7 from all participants, which investigated the passive experience and the down- and up-regulation of pain, respectively, was preprocessed with the same workflow used to preprocess studies 1-3. Regional timeseries data was grouped to "pain" and "rest" blocks, with a 6-second delay to adjust for the hemodynamic response function. All activation timeframes were transformed to the fcHNN projection plane obtained from study 1. Within-participant differences of the average location on the fcHNN projection was calculated and visualized with radial plots, showing the participant-level mean trajectory on the projection plane from rest to pain, denoted with circles, as well as the group level trajectory (arrow). The significance of the position difference and energy difference of the participant-level mean activations in the projection plane was tested with a permutation test. We used the L2 norm of the two-dimensional position difference and the absolute energy difference, respectively, as test statistics. The permutation tests were run with 1000 permutations, randomly swapping the conditions.

To further highlight the difference between the task and rest conditions, a "flow analysis" was performed to investigate the dynamic trajectory differences between the conditions rest and pain. The analysis method was identical to the flow analysis of resting sate data. First we calculated the direction in the projection plane between each successive TR during the rest conditions (a vector on the fcHNN projection plane for each TR transition). Next, we obtained a two-dimensional binned means for both the x and y coordinates of these transition vectors (pooled across all participants), calculated over a 2-dimensional grid of 100×100 uniformly distributed bins in the [-6,6] range (arbitrary units) and applied Gaussian smoothing with a $\sigma$ 5 bins. 
The same procedure was repeated for the pain condition and the difference in the mean directions between the two conditions was visualized as “streamplots” (using Python’s matplotlib). We used the same approach to quantify the difference in characteristic state transition trajectories between the up- and downregulation conditions. The empirically estimated trajectory differences (from real fMRI data) were contrasted to the trajectory differences predicted by the fcHNN model from study 1.

To obtain fcHNN-simulated state transitions in resting conditions, we used the stochastic relaxation procedure ({numref}`hopfield-update-matrix-stochastic`), with $\mathbf{\mu}$ set zero.
To simulate the effect of pain-related activation on large-scale brain dynamics, we set $\mu_i$ during the stochastic relaxation procedure to a value representing pain-elicited activity in region i. The region-wise activations were obtained calculating the parcel-level mean activations from the meta-analytic pain activation map from {cite:p}`zunhammer2021meta`, which contained Hedges' g effect sizes from an individual participant-level meta-analysis of 20 pain studies, encompassing a total of n=603 participants. The whole activation map was scaled with five different values ranging from $10^{-3}$ to $10^{-1}$, spaced logarithmically, to investigate various signal-to-noise scenarios.
We obtained the activity patterns of $10^5$ iterations from this stochastic relaxation procedure and calculated the state transition trajectories with the same approach used with the empirical data.
Next we calculated the simulated difference between the rest and pain conditions and compared it to the actual difference through a permutation test with 1000 permutations, using Pearson's correlation coefficient as test statistic.
From the five investigated signal-to-noise values, we chose the one that provided the highest similarity to the real pain vs. rest trajectory difference.

When comparing the simulated and real trajectory differences between pain up- and downregulation, we used the same procedure, with two differences. First, when calculating the simulated state transition vectors for the self-regulation conditions, we used the same procedure as for the pain condition, but introduced and additional signal in the nucleus accumbens, with a negative and positive sign, for  up- and downregulation, respectively. We did not optimize the signal-to-noise ratio for the nucleus accumbens signal but, instead, simply used the value optimized for the pain vs. rest contrast (For a robustness analysis, see {numref}`Supplementary figure %s <si_downreg_trajectory_sim>`).


### Clinical data

To demonstrate the sensitivity of the fcHNN approach to clinically relevant alterations of large-scale brain dynamics in Autism Spectrum Disorder (ASD), we obtained data from n=172 individuals, acquired at the New York University Langone Medical Center, New York, NY, USA (NYU) as shared in the Autism Brain Imaging Data Exchange dataset ([study 7](tab-samples): ABIDE, {cite:p}`di2014autism`. We focused on the largest ABIDE imaging center to ensure that our results are not biased by center effects. We excluded high motion cases similarly to our approach in studies 1-4, i.e. by ignoring ("scrubbing") volumes with FD>0.15 and excluding participants with more than 50% of data scrubbed. Timeseries data was pooled and visualized on the fcHNN projection of study 1, separately for ASD and control participants. 
Next, for each participant, we grouped the timeframes from the regional timeseries data according to the corresponding attractor states (obtained with the fcHNN model from study 1) and averaged timeframes corresponding to the same attractor state to calculated participant-level mean attractor activations.
We assessed mean attractor activity differences between the patient groups with a permutation test, randomly re-assigning the group labels 50000 times. 
We adjusted the significance threshold with a Bonferroni-correction, accounting for tests across 4 states and 122 regions, resulting in $\alpha = 0.0001$. 
Finally, we have calculated the trajectory differences between the two groups, as predicted by the group-specific fcHNNs (initialized with the ASD and TCD connectomes), and - similarly to the approach used in study 4 - we contrasted the fcHNN predictions to the trajectory differences observed in the real rsfMRI data. As in the previous flow analyses, we tested the significance of the similarity between the predicted and observed trajectory differences with a permutation test (1000 permutations), by shuffling group labels.