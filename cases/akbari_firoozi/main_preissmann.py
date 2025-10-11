from hydromodel.channel import Channel
from hydromodel.boundary import Boundary
from hydromodel.preissmann import PreissmannSolver
from hydromodel.utility import Hydrograph
from cases.akbari_firoozi.settings import *

hyd = Hydrograph(hydrograph)

us = Boundary(condition='flow_hydrograph',
              bed_level=S_0*length,
              chainage=0,
              hydrograph=hyd)

ds = Boundary(condition='normal_depth',
              bed_level=0,
              chainage=length)

example_channel = Channel(width=width,
                        initial_flow=initial_flow,
                        roughness=roughness,
                        upstream_boundary=us,
                        downstream_boundary=ds,
                        interpolation_method='steady-state')

solver = PreissmannSolver(channel=example_channel,
                          theta=theta,
                          time_step=preissmann_dt,
                          spatial_step=spatial_step,
                          simulation_time=duration,
                          regularization=False)

solver.run(verbose=0, tolerance=tolerance)
solver.save_results(folder_path='cases\\akbari_firoozi\\results\\preissmann')
print('Simulation finished successfuly.')
