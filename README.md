# Constraints on non-linear tides due to p-g mode coupling from the neutron-star merger GW170817

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
and posterior distribution data. All of the files contain the thinned chained of the posterior samples using the sky localization constraint, chirp mass constraint, common equation of state constraint from [De et al. (2018)](https://arxiv.org/abs/1804.08583), with mass distribution prior distributions for each of the binary neutron stars from [De et al. (2018)](https://arxiv.org/abs/1804.08583). Each file refers to two different mass priors from [De et al. (2018)](https://arxiv.org/abs/1804.08583) and with different choices of the range of f<sub>0</sub>, the turn-on frequency of the p-g mode energy loss.

The data files are:

1. [gaussian_small_f0_range.hdf](https://github.com/sugwg/gw170817-pg-modes/blob/master/gaussian_small_f0_range.hdf), the Gaussian mass distribution in common with De et al. (2018), but with p-g mode instability parameters: saturation frequency (f<sub>0</sub>) between 15 and 100 Hz, amplitude scaling (A) between 10<sup>-10</sup> and 10<sup>-6</sup>, and frequency evolution exponent (n) between -1.1 and 2.999.
2. [gaussian_large_f0_range.hdf](https://github.com/sugwg/gw170817-pg-modes/blob/master/gaussian_large_f0_range.hdf), the Gaussian mass distribution in common with De et al. (2018), but with p-g mode instability parameters: saturation frequency (f<sub>0</sub>) between 15 and 800 Hz, amplitude scaling (A) between $10<sup>10</sup> and 10<sup>-6</sup>, and frequency evolution exponent (n) between -1.1 and 2.999.
3. [uniform_small_f0_range.hdf](https://github.com/sugwg/gw170817-pg-modes/blob/master/uniform_small_f0_range.hdf), the uniform mass distribution in common with De et al. (2018), but with p-g mode instability parameters: saturation frequency (f<sub>0</sub>) between 15 and 100 Hz, amplitude scaling (A) between 10<sup>-10</sup> and 10<sup>-6</sup>, and frequency evolution exponent (n) between -1.1 and 2.999. 
4. [uniform_large_f0_range.hdf](https://github.com/sugwg/gw170817-pg-modes/blob/master/uniform_large_f0_range.hdf), the uniform mass distribution in c
ommon with De et al. (2018), but with p-g mode instability parameters: saturation frequency (f<sub>0</sub>) between 15 and 800 Hz, amplitude scaling (A) between 10<sup>10</sup> and 10<sup>-6</sup>, and frequency evolution exponent (n) between -1.1 and 2.999. 

## Notebooks

An ipython notebook is provided, [pg_mode_notebook.ipynb](https://github.com/sugwg/gw170817-pg-modes/blob/master/pg_mode_notebook.ipynb) for regenerating the plots used in "Constraints on non-linear tides due to p-g mode coupling from the neutron-star merger GW170817", with some additional posterior plots. All results are generated using the [PyCBC v1.9.4 release](https://github.com/gwastro/pycbc/releases/tag/v1.9.4) with the addition of a [patch to fix the stationary phase approximation for the effect of nonlinear tides](https://github.com/gwastro/pycbc/pull/2284). The prior distribution plots, Bayes factor calculations, and posterior distribution plots can be generated using the [PyCBC v1.9.4 release](https://github.com/gwastro/pycbc/releases/tag/v1.9.4) with the addition of a [patch to allow logarithmic spaced histograms in posterior plots](https://github.com/gwastro/pycbc/pull/2285). These patches have been merged into the master branch of PyCBC.

## Acknowledgements
We thank Soumi De and Daniel Finstad for helpful discussions. We thank Alex Nitz for writing the initial version of
the code for non-linear tides in PyCBC.

## Funding
The authors were supported by the National Science Foundation grant PHY-1707954.
Computational work was supported by Syracuse University and National Science Foundation grant OAC-1541396.
This research has made use of data obtained from the  [LIGO Open Science Center](http://losc.ligo.org).
