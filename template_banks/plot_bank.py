import h5py
import matplotlib.pyplot as plt

f = h5py.File("uniform_m_1p0_2p0_non_spin_99p9mm_loose_chirp_cut_v2.hdf", "r")

m1 = f["mass1"][:]
m2 = f["mass2"][:]

plt.scatter(m1, m2, s=1, color="k", alpha=0.6)

plt.xlabel("Mass 1")
plt.ylabel("Mass 2")

plt.minorticks_on()
plt.grid(True, which='minor', axis='y', ls="--", alpha=0.1, color="k")
plt.grid(True, which='major', axis='y', ls="-", alpha=0.2, color="k")
plt.grid(True, which='major', axis='x', ls="-", alpha=0.2, color="k")
plt.grid(True, which="minor", axis='x', ls="--", alpha=0.1, color="k")

plt.savefig("template_bank.png", dpi=200)
