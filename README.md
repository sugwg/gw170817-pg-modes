# Constraints on non-linear tides due to p-g mode coupling from the neutron-star merger GW170817
**Steven Reyes<sup>1</sup> and Duncan A Brown<sup>1</sup>**
**<sup>1</sup>Department of Physics, Syracuse University, Syracuse, NY 13244, USA**

## License

![Creative Commons License](https://i.creativecommons.org/l/by-sa/3.0/us/88x31.png "Creative Commons License")

This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0 United States License](http://creativecommons.org/licenses/by-sa/3.0/us/).

## Introduction
This notebook is a companion to the paper presented at [](https://).
Supplementary data for GW170817 p-g mode coupling paper

We encourage use of these data in derivative works. If you use the material provided here, please cite the paper using the reference:
```

```
## Data
We provide the data from thinned posterior samples from the MCMC chains used to produce Bayes factor calculations
and posterior distribution plos. All of the files contain the thinned chained of the posterior samples using the sky localization constraint, chirp mass constraint, common equation of state constraint from De et al. (2018), with mass distribution prior distributions for each of the binary neutron stars from De et al. (2018). Each file refers to two different mass priors from De et al. (2018) and with unique p-g mode instability parameter prior distribution choices.

The data files are:
1. [gaussian_small_f0_range.hdf](https://github.com/sugwg/gw170817-pg-modes/gaussian_small_f0_range.hdf), the Gaussian mass distribution in common with De et al. (2018), but with p-g mode instability parameters: saturation frequency ($f_0$) between 15 and 100 Hz, amplitude scaling ($A$) between $10^-10$ and $10^-6$, and frequency evolution exponent ($n$) between -1.1 and 2.999.
2. [gaussian_large_f0_range.hdf](https://github.com/sugwg/gw170817-pg-modes/gaussian_large_f0_range.hdf), the Gaussian mass distribution in common with De et al. (2018), but with p-g mode instability parameters: saturation frequency ($f_0$) between 15 and 800 Hz, amplitude scaling ($A$) between $10^-10$ and $10^-6$, and frequency evolution exponent ($n$) between -1.1 and 2.999.
3. [uniform_small_f0_range.hdf](https://github.com/sugwg/gw170817-pg-modes/uniform_small_f0_range.hdf), the uniform mass distribution in common with De et al. (2018), but with p-g mode instability parameters: saturation frequency ($f_0$) between 15 and 100 Hz, amplitude scaling ($A$) between $10^-10$ and $10^-6$, and frequency evolution exponent ($n$) between -1.1 and 2.999.
4. [uniform_large_f0_range.hdf](https://github.com/sugwg/gw170817-pg-modes/uniform_large_f0_range.hdf), the uniform mass distribution in common with De et al. (2018), but with p-g mode instability parameters: saturation frequency ($f_0$) between 15 and 800 Hz, amplitude scaling ($A$) between $10^-10$ and $10^-6$, and frequency evolution exponent ($n$) between -1.1 and 2.999.

## Notebooks
An ipython notebook is provided, [pg_mode_notebook.ipynb])(https://github.com/sugwg/gw170817-pg-modes/pg_mode_notebook.ipynb) for regenerating the plots used in "Constraints on non-linear tides due to p-g mode coupling from the neutron-star merger GW170817", with some additional posterior plots. The results are used from a branch of the [PyCBC v1.9.4](https://github.com/gwastro/pycbc/releases/tag/v1.9.4) release found at [https://github.com/sugwg/pycbc-nl-tides](https://github.com/sugwg/pycbc-nl-tides) under the branch [nl_tides](https://github.com/sugwg/pycbc-nl-tides). The prior distribution plots, Bayes factor calculations, and posterior distribution plots can be generated from a branch of this nl-tides called [log_scattergrams](https://github.com/sugwg/pycbc-nl-tides/tree/log_scattergrams).

## Acknowledgements
We thank Soumi De and Daniel Finstad for helpful discussions. We thank Alex Nitz for writing the initial version of
the code for non-linear tides in PyCBC.

## Funding
The authors were supported by the National Science Foundation grant PHY1707954.
Computational work was supported by Syracuse University and National Science Foundation grant OAC1541396.
This research has made use of data obtained from the LIGO Open Science Center (http://www.losc.org).
