# Constraints on nonlinear tides due to p-g mode coupling from the neutron-star merger GW170817

**Steven Reyes<sup>1</sup> and Duncan A Brown<sup>1</sup>**

**<sup>1</sup>Department of Physics, Syracuse University, Syracuse, NY 13244, USA**

## License

![Creative Commons License](https://i.creativecommons.org/l/by-sa/3.0/us/88x31.png "Creative Commons License")

This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0 United States License](http://creativecommons.org/licenses/by-sa/3.0/us/).

## Introduction

This notebook is a companion to the paper presented at [arXiv:1808.07013](https://arxiv.org/abs/1808.07013). It demonstrates how to make the figures in the paper and compute the Bayes factors comparing the analyses with and without the effect of nonlinear tides.

We encourage use of these data in derivative works. If you use the material provided here, please cite the paper using the reference:

```
@article{Reyes:2018bee,
      author         = "Reyes, Steven and Brown, Duncan A.",
      title          = "{Constraints on non-linear tides due to $p$-$g$ mode
                        coupling from the neutron-star merger GW170817}",
      year           = "2018",
      eprint         = "1808.07013",
      archivePrefix  = "arXiv",
      primaryClass   = "astro-ph.HE",
      SLACcitation   = "%%CITATION = ARXIV:1808.07013;%%"
}
```
## Data
We provide the data from thinned posterior samples from the MCMC chains used to produce Bayes factor calculations
and posterior distribution data. All of the files contain the thinned chained of the posterior samples using the sky localization constraint, chirp mass constraint, common equation of state constraint from [De et al. (2018)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.121.091102), with mass distribution prior distributions for each of the binary neutron stars from [De et al. (2018)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.121.091102). Each file refers to two different mass priors from [De et al. (2018)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.121.091102) and with different choices of the range of f0, the turn-on frequency of the p-g mode energy loss.

There are 4 main categories of data files presented in this data release:

#### Full-Power-Posterior MCMC Files

The set of data files is the thinned full-power-posterior MCMC runs. They contain the data produced from the MCMC analyses such as posterior sample values, log-likelihood values, and the set of inverse-temperatures used in the parallel tempering.

We list the files below with the corresponding prior-distribution choices for the file. All of the files use the  common equation of state tidal deformability in common with De et al. (2018).

1. The Gaussian mass distribution is shared with De et al. (2018), but with the additional p-g mode instability parameters: saturation frequency ($f_0$) between $15$ and $800$ Hz, amplitude scaling ($A$) between $10^{-10}$ and $10^{-6}$, and spectral index ($n$) between $-1.1$ and $2.999$. There is a $\delta \phi > 0.1$ radians constraint also applied to this prior. The file is: `thinned_results_files/gauss_broad_f0.hdf`

2. The Gaussian mass distribution is shared with De et al. (2018), but with the additional p-g mode instability parameters: saturation frequency ($f_0$) between $15$ and $100$ Hz, amplitude scaling ($A$) between $10^{-10}$ and $10^{-6}$, and spectral index ($n$) between $-1.1$ and $2.999$. There is a $\delta \phi > 0.1$ radians constraint also applied to ths prior. The file is: `thinned_results_files/gauss_narrow_f0.hdf`

3. The uniform mass distribution is shared with De et al. (2018), but with p-g mode instability parameters: saturation frequency ($f_0$) between $15$ and $800$ Hz, amplitude scaling ($A$) between $10^{-10}$ and $10^{-6}$, and spectral index ($n$) between $-1.1$ and $2.999$. There is a $\delta \phi > 0.1$ radians constraint also applied to ths prior. The file is: `thinned_results_files/uni_broad_f0.hdf`

4. The files below represent 9 runs of the same analysis but with different random seeds chosen for the analysis. The uniform mass distribution in common with De et al. (2018), but with p-g mode instability parameters: saturation frequency ($f_0$) between $15$ and $100$ Hz, amplitude scaling ($A$) between $10^{-10}$ and $10^{-6}$, and spectral index ($n$) between $-1.1$ and $2.999$. There is a $\delta \phi > 0.1$ radians constraint also applied to this prior. The files are:

 a. `thinned_results_files/uni_narrow_f0_v1.hdf`

 b. `thinned_results_files/uni_narrow_f0_v2.hdf`

 c. `thinned_results_files/uni_narrow_f0_v3.hdf`

 d. `thinned_results_files/uni_narrow_f0_v4.hdf`

 e. `thinned_results_files/uni_narrow_f0_v5.hdf`

 f. `thinned_results_files/uni_narrow_f0_v6.hdf`

 g. `thinned_results_files/uni_narrow_f0_v7.hdf`

 h. `thinned_results_files/uni_narrow_f0_v8.hdf`

 i. `thinned_results_files/uni_narrow_f0_v9.hdf`
 
5. The uniform mass distribution is shared with De et al. (2018), but with p-g mode instability parameters: saturation frequency ($f_0$) between $10$ and $100$ Hz, amplitude scaling ($A$) between $10^{-10}$ and $10^{-5.5}$, and spectral index ($n$) between $-1$ and $2.999$. There is no $\delta \phi$ constraint applied to ths prior. This analysis is meant to be similar to the p-g mode study conducted in `Abbott, B. et al. 2019, Physical Review Letters, 122, 061104`. The file is: `thinned_results_files/lvc_sim.hdf`

6. The thinned, full 51 temperature power posterior MCMC file from De et al. (2018) for the Gaussian mass distribution with common equation of state constraint. The file is presented here for convenience as: `thinned_results_files/gauss_ceos.hdf`

7. The thinned, full 51 temperature power posterior MCMC file from De et al. (2018) for the uniform mass distribution with common equation of state constraint. The file is presented here for convenience as: `thinned_results_files/uni_ceos.hdf`


#### Power-Posterior-Fitting Factor MCMC Files

This set of data pertains to a particular prior choice on p-g mode parameters that include the log-likelihood of the samples of the data and the fitting factor for these samples with a `TaylorF2` non-spinning, mass-only template bank.

There are 9 runs in total. The runs are only different in that they used different random seeds for the analysis.

The prior choice for these runs: The common equation of state tidal deformability and uniform mass distribution are in common with De et al. (2018), but with p-g mode instability parameters: saturation frequency ($f_0$) between $15$ and $100$ Hz, amplitude scaling ($A$) between $10^{-10}$ and $10^{-6}$, and spectral index ($n$) between $-1.1$ and $2.999$. There is a $\delta \phi > 0.1$ radians constraint also applied to these analysis.

These files contain the keys: `['amplitude', 'dphi', 'f0', 'logl', 'mass1', 'mass2', 'max_mass1', 'max_mass2', 'max_match', 'n']`, where `amplitude`, `dphi`, `f0`, `n`, `mass1`, `mass2`, denote the parameter values from the MCMC run. The key, `logl`, denotes the log-likelihood of the parameter relative to the data. The other four parameters refer to the fitting factor relative to a non-spinning, mass-only template bank. The key, `max_match` refers to the maximum match between one of these templates and the particular MCMC parameter. The keys, `max_mass1` and `max_mass2` refer to the mass pair in the template bank that had the maximum match with the MCMC tuple. The inverse-temperatures can be found in the previous files. Matching proper temperatures to the proper samples is done in example scripts below.

The 9 files are:

1. `results_overlap_files/uni_narrow_f0_match_logl_v1.hdf`

2. `results_overlap_files/uni_narrow_f0_match_logl_v2.hdf`

3. `results_overlap_files/uni_narrow_f0_match_logl_v3.hdf`

4. `results_overlap_files/uni_narrow_f0_match_logl_v4.hdf`

5. `results_overlap_files/uni_narrow_f0_match_logl_v5.hdf`

6. `results_overlap_files/uni_narrow_f0_match_logl_v6.hdf`

7. `results_overlap_files/uni_narrow_f0_match_logl_v7.hdf`

8. `results_overlap_files/uni_narrow_f0_match_logl_v8.hdf`

9. `results_overlap_files/uni_narrow_f0_match_logl_v9.hdf`

We also present the template bank used to conduct this analysis. The LIGO Livingston PSD as analyzed in the MCMC analyses was used to construct the template bank and to evaluate the overlap values.

1. `uniform_m_1p0_2p0_non_spin_99p9mm_loose_chirp_cut_v2.hdf`


#### Evidence Convergence Files

The next set of data files are evidence-convergence files that show the evidence in the MCMC analyses as a function of MCMC iteration. These were generated as a means to track the convergence of the evidence of the analyses.

1. The Gaussian mass distribution is shared with De et al. (2018), but with the additional p-g mode instability parameters: saturation frequency ($f_0$) between $15$ and $800$ Hz, amplitude scaling ($A$) between $10^{-10}$ and $10^{-6}$, and spectral index ($n$) between $-1.1$ and $2.999$. There is a $\delta \phi > 0.1$ radians constraint also applied to this prior. The file is: `evidence_convergence_files/gauss_broad_f0_evidence_convergence.hdf`

2. The Gaussian mass distribution is shared with De et al. (2018), but with the additional p-g mode instability parameters: saturation frequency ($f_0$) between $15$ and $100$ Hz, amplitude scaling ($A$) between $10^{-10}$ and $10^{-6}$, and spectral index ($n$) between $-1.1$ and $2.999$. There is a $\delta \phi > 0.1$ radians constraint also applied to ths prior. The file is: `evidence_convergence_files/gauss_narrow_f0_evidence_convergence.hdf`

3. The uniform mass distribution is shared with De et al. (2018), but with p-g mode instability parameters: saturation frequency ($f_0$) between $15$ and $800$ Hz, amplitude scaling ($A$) between $10^{-10}$ and $10^{-6}$, and spectral index ($n$) between $-1.1$ and $2.999$. There is a $\delta \phi > 0.1$ radians constraint also applied to ths prior. The file is: `evidence_convergence_files/uni_broad_f0_evidence_convergence.hdf`

4. The files below represent 9 runs of the same analysis but with different random seeds chosen for the analysis. The uniform mass distribution in common with De et al. (2018), but with p-g mode instability parameters: saturation frequency ($f_0$) between $15$ and $100$ Hz, amplitude scaling ($A$) between $10^{-10}$ and $10^{-6}$, and spectral index ($n$) between $-1.1$ and $2.999$. There is a $\delta \phi > 0.1$ radians constraint also applied to this prior. The files are

 a. `evidence_convergence_files/uni_narrow_f0_v1_evidence_convergence.hdf`

 b. `evidence_convergence_files/uni_narrow_f0_v2_evidence_convergence.hdf`

 c. `evidence_convergence_files/uni_narrow_f0_v3_evidence_convergence.hdf`

 d. `evidence_convergence_files/uni_narrow_f0_v4_evidence_convergence.hdf`

 e. `evidence_convergence_files/uni_narrow_f0_v5_evidence_convergence.hdf`

 f. `evidence_convergence_files/uni_narrow_f0_v6_evidence_convergence.hdf`

 g. `evidence_convergence_files/uni_narrow_f0_v7_evidence_convergence.hdf`

 h. `evidence_convergence_files/uni_narrow_f0_v8_evidence_convergence.hdf`

 i. `evidence_convergence_files/uni_narrow_f0_v9_evidence_convergence.hdf`
 
5. The uniform mass distribution is shared with De et al. (2018), but with p-g mode instability parameters: saturation frequency ($f_0$) between $10$ and $100$ Hz, amplitude scaling ($A$) between $10^{-10}$ and $10^{-5.5}$, and spectral index ($n$) between $-1$ and $2.999$. There is no $\delta \phi$ constraint applied to ths prior. This analysis is meant to be similar to the p-g mode study conducted in `Abbott, B. et al. 2019, Physical Review Letters, 122, 061104`. The file is: `evidence_convergence_files/lvc_sim_evidence_convergence.hdf`

6. The thinned, full 51 temperature power posterior MCMC file from De et al. (2018) for the Gaussian mass distribution with common equation of state constraint. The file is presented here for convenience as: `evidence_convergence_files/gauss_ceos_evidence_convergence.hdf`

7. The thinned, full 51 temperature power posterior MCMC file from De et al. (2018) for the uniform mass distribution with common equation of state constraint. The file is presented here for convenience as: `evidence_convergence_files/uni_ceos_evidence_convergence.hdf`

#### Combined Posterior-Only File

The last data file is a convenience posterior-only file that combines 9 analyses together into one posterior file.

1. This file is `combined_posterior_file/only_posterior_9_combined_uni_narrow_f0.hdf`. It only contains samples from the posterior, $\beta=1$, in the parallel tempering analyses. It is used for the posterior plotting for Figure 3.

## Notebooks

An ipython notebook is provided, [pg_mode_notebook.ipynb](https://github.com/sugwg/gw170817-pg-modes/blob/master/pg_mode_notebook.ipynb) for regenerating the plots used in "Constraints on nonlinear tides due to p-g mode coupling from the neutron-star merger GW170817", with some additional posterior plots. All results are generated using the [PyCBC v1.12.3 release](https://github.com/gwastro/pycbc/releases/tag/v1.12.3).

## Acknowledgements
We thank Reed Essick, and Nevin Weinberg for helpful discussion and pointing out errors in our Bayes factor calculation in an earlier draft of the arXiv manuscript~\citep{Essick:2018wvj}. We thank Chaitanya Afle, Nils Andersson, Soumi De, Daniel Finstad, and Pantelis Pnigouras for helpful discussions. We thank Alex Nitz for writing the initial version of the code for nonlinear tides in PyCBC.

## Funding
The authors were supported by the National Science Foundation grant PHY-1707954. Computational work was supported by Syracuse University and National Science Foundation grant OAC-1541396. This research has made use of data obtained from the [Gravitational Wave Open Science Center](https://www.gw-openscience.org/about/).
