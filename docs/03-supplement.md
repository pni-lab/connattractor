---
title: Supplementary Information
#subtitle: Optional Subtitle
short_title: Supplementary Information

exports:
  - format: pdf
    template: arxiv_nips
    output: exports/connattractor_si.pdf
  - format: docx
    hideFooter: true
    output: exports/connattractor_si.docx
---

## Supplementary Figures

:::{figure} figures/supplement/expl_variance_energy.png
:name: si_expl_variance_energy
**Explained variance in state energy by first two principal components.** See [supplemental_material.ipynb](https://github.com/pni-lab/connattractor/blob/master/notebooks/supplemental_material.ipynb) for details.
:::

:::{figure} figures/supplement/classification_acc_state_basins.png
:name: si_classification_acc_state_basins
**Cross-validation classification accuracy of the fcHNN, when predicting the attractor state from state 
activation.**  See [supplemental_material.ipynb](https://github.com/pni-lab/connattractor/blob/master/notebooks/supplemental_material.ipynb) for details.
:::

:::{figure} figures/supplement/att_state_emergence_over_beta.png
:name: si_att_state_emergence_over_beta
**Parameter sweep of fcHNN parameters threshold and beta.** the number of attractor states is color-coded. See [supplemental_material.ipynb](https://github.com/pni-lab/connattractor/blob/master/notebooks/supplemental_material.ipynb) for details.
:::

:::{figure} figures/supplement/si_convergence.png
:name: si_convergence
**HNNs initialized with the empirical connectome has better convergence properties than permutation-based null models.** Histograms show the number of iterations until convergence with the real (unpermuted) connectome, for 100 random initializations, with various beta values. HNN models based on the permuted connectivity matrix (with retaining symmetry) did not reach convergence in 10000 iterations in more than 98% of the same random initializations. See [convergence-analysis.ipynb](https://github.com/pni-lab/connattractor/blob/master/notebooks/convergence_analysis.ipynb) for details.
:::


:::{figure} figures/supplement/si_state_occupancy_null_model.png
:name: si_state_occupancy_null_models
**Statistical inference of the fcHNN state occupancy prediction with different null models.**
**A** Results with a spatial autocorrelation-preserving null model for the empirical activity patterns. See [null_models.ipynb](https://github.com/pni-lab/connattractor/blob/master/notebooks/null_models.ipynb) for more details.
**B** Results where simulated samples are randomly sampled from a multivariate normal distribution, with the functional connectome as the covariance matrix, and compared to the fcHNN performance. See [supplemental_material.ipynb](https://github.com/pni-lab/connattractor/blob/master/notebooks/supplemental_material.ipynb) for details.
:::

:::{figure} figures/supplement/si_pain_ghost_attractor_sim.png
:name: si_pain_ghost_attractor_sim
**FcHNN can reconstruct the pain "ghost attractor".**
Signal-to-noise values range from 0.003 to 0.009. Asterisk denotes the location of the simulated "ghost attractor". P-values are based on permutation testing, by randomly changing the conditions in a per-participant basis. See [main_analyses.ipynb](https://github.com/pni-lab/connattractor/blob/master/notebooks/main_analyses.ipynb) for more details.
:::

:::{figure} figures/supplement/si_downreg_trajectory_sim.png
:name: si_downreg_trajectory_sim
**FcHNN can reconstruct the changes in brain dynamics caused by the voluntary donwregulation of pain (as contrasted to upregulation)**
Signal-to-noise values range from 0.001 to 0.005. P-values are based on permutation testing, by randomly changing the conditions in a per-participant basis. See [main_analyses.ipynb](https://github.com/pni-lab/connattractor/blob/master/notebooks/main_analyses.ipynb) for more details.
:::

:::{figure} figures/supplement/noise_robustness_weights.png
:name: si_noise_robustness_weights
**Robustness of the fcHNN weights to noise.**
We set the temperature of the fcHNN, so that two attractor states emerge and iteratively add noise to the connectome. 
To account for the change in dynamics, we adjust the temperature (beta) of the noisy fcHNN so that exactly two states emerge. We then highlight the decrease in nodal strength of the noisy connectome (the fcHNN weights) as a reference metric 
vs the correlation of the attractor states that emerge from the noisy connectome. See [supplemental_material.ipynb](https://github.com/pni-lab/connattractor/blob/master/notebooks/supplemental_material.ipynb) for details.
:::

:::{figure} figures/supplement/clinical_results_table.png
:name: si_clinical_results_table
**All significant differences of the mean state activation analysis on the ABIDE dataset; label denotes the region
in the BASC122 atlas.** See [supplemental_material.ipynb](https://github.com/pni-lab/connattractor/blob/master/notebooks/supplemental_material.ipynb) for details.
:::

## Supplementary Tables
```{list-table} **Neurosynth meta-analyses.** The table includes details about the term used for the automated meta-analyses, as well as the number of studies included in the meta-analysis, the total number of reported activations and the maximal Z-statistic from the meta-analysis.
:header-rows: 1
:name: si-tab-neurosynth

* - search term
  - num. studies
  - num. activations
  - max. Z
  
* - pain
  - 516
  - 23295
  - 14.8
  
* - motor
  - 2565
  - 109491
  - 22.5
 
* - auditory
  - 1252
  - 46557
  - 25.3
  
* - visual
  - 3110
  - 115726
  - 15.4
    
* - face
  - 896
  - 31842
  - 26.8
    
* - autobiographical
  - 143
  - 7251
  - 15.7
    
* - theory of mind
  - 181
  - 7761
  - 15.1
    
* - sentences
  - 356
  - 13461
  - 16.5

```

## Supplementary Methods
**Study 4 instructions for upregulation.**
*“During this scan, we are going to ask you to try to imagine as hard as you can that the thermal stimulations are more painful than they are. Try to focus on how unpleasant the pain is, for instance, how strongly you would like to remove your arm from it. Pay attention to the burning, stinging and shooting sensations. You can use your mind to turn up the dial of the pain, much like turning up the volume dial on a stereo. As you feel the pain rise in intensity, imagine it rising faster and faster and going higher and higher. Picture your skin being held up against a glowing hot metal or fire. Think of how disturbing it is to be burned, and visualize your skin sizzling, melting and bubbling as a result of the intense heat.”*

**Study 4 instructions for downregulation.**
*“During this scan, we are going to ask you to try to imagine as hard as you can that the thermal stimulations are less painful than they are. Focus on the part of the sensation that is pleasantly warm, like a blanket on a cold day. You can use your mind to turn down the dial of your pain sensation, much like turning down the volume dial on a stereo. As you feel the stimulation rise, let it numb your arm, so any pain you feel simply fades away. Imagine your skin is very cool, from being outside, and think of how good the stimulation feels as it warms you up.”*



