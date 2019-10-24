# Chirp mass constraints plus fudge factor
# 1.1876 - 0.005 = 1.1826
# 1.2076 + 0.015 = 1.2226

pycbc_geom_nonspinbank --pn-order threePointFivePN --f0 20 --f-low 20 --f-upper 2048 --delta-f 0.004 --min-match 0.999 --min-mass1 1.0 --min-mass2 1.0 --max-mass1 2. --max-mass2 2. --min-chirp-mass 1.1826 --max-chirp-mass 1.2226 --verbose --output-file uniform_m_1p0_2p0_non_spin_99p9mm_loose_chirp_cut_v2.xml --filter-cutoff SchwarzISCO --psd-file L1_PSD.txt --f-low-column "alpha6"
