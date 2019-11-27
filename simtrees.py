import msprime
import numpy as np

ts = msprime.simulate(5, random_seed=666)
t = next(ts.trees())
nl = {i: "{:0.2f}".format(ts.tables.nodes.time[i])
      for i in range(len(ts.tables.nodes))}
for key, value in nl.items():
    if key < 5:
        nl[key] = '0'
tree1_svg = t.draw(path="tree1.svg", format='svg',
                   # height=100,width=100,
                   node_labels=nl)
ts = msprime.simulate(population_configurations=[msprime.PopulationConfiguration(sample_size=5, growth_rate=10)],
                      random_seed=42*666)
# Cheat here even more: divide times by 50 to look more realistic
nl = {i: "{:0.3f}".format(
    ts.tables.nodes.time[i]/50.) for i in range(len(ts.tables.nodes))}
for key, value in nl.items():
    if key < 5:
        nl[key] = '0'
t = next(ts.trees())
tree2_svg = t.draw(path="tree2.svg",
                   # height=100,width=100,
                   format='svg', node_labels=nl)
