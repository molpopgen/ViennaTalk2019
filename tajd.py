# Get distributions of D for neutral and for growth,
# which we're using to fake what hard sweeps look like
import libsequence.variant_matrix as vm
import libsequence.summstats as sstats
import matplotlib.pyplot as plt
import seaborn as sns
import msprime

PC = msprime.PopulationConfiguration

Dneutral = []
for ts in msprime.simulate(50, mutation_rate=100.,
                           num_replicates=1000, random_seed=666):
    m = vm.VariantMatrix.from_TreeSequence(ts)
    ac = m.count_alleles()
    Dneutral.append(sstats.tajd(ac))
Dgrowth = []
for ts in msprime.simulate(population_configurations=[PC(sample_size=50, growth_rate=5)],
                           mutation_rate=100.,
                           num_replicates=1000, random_seed=351212):
    m = vm.VariantMatrix.from_TreeSequence(ts)
    ac = m.count_alleles()
    Dgrowth.append(sstats.tajd(ac))

f, ax = plt.subplots(1, 2,
                     figsize=(6, 4),
                     sharey=True, sharex=True)
sns.distplot(Dneutral, ax=ax[0], norm_hist=False, kde=False)
sns.distplot(Dgrowth, ax=ax[1], norm_hist=False, kde=False)
ax[0].set_ylabel("Count")
ax[0].set_xlabel("Tajima's D")
ax[1].set_xlabel("Tajima's D")
ax[0].set_title("Neutral")
ax[1].set_title("Recent hard sweep")
plt.savefig("tajd.png", dpi=300)
