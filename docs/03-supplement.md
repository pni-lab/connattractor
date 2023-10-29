---
title: Supplementary material
#subtitle: Optional Subtitle
short_title: Supplement
---
:::{figure} figures/supplement/expl_variance_energy.png
:name: expl_variance_energy
**Explained variance in state energy by first two principal components** <br/><br/>
:::

:::{figure} figures/supplement/classification_acc_state_basins.png
:name: classification_acc_state_basins
**Cross-validation classification accuracy of the FCHN, when predicting the attractor state from state 
activation.** <br/><br/>
:::

:::{figure} figures/supplement/clinical_results_table.png
:name: clinical_results_table
**All significant differences of the mean state activation analysis on the ABIDE dataset; label denotes the region
in the BASC122 atlas** <br/><br/>
:::

:::{figure} figures/supplement/att_state_emergence_over_beta.png
:name: att_state_emergence_over_beta
**Parameter sweep of FCHN parameters threshold and beta, highlighting  the emergence of attractor states.** <br/><br/>
:::

:::{figure} figures/supplement/noise_robustness_weights.png
:name: noise_robustness_weights
**Robustness of the FCHN weights to noise.** <br/><br/>
We set the temperature of the FCHN, so that two attractor states emerge and iteratively add noise to the connectome. 
To account for the change 
in dynamics, we adjust the temperature (beta) of the noisy FCHN so that exactly two states emerge. We then highlight the 
decrease in nodal strength of the noisy connectome (the FCHN weights) as a reference metric 
vs the correlation of the attractor states that emerge from the noisy connectome.
:::



