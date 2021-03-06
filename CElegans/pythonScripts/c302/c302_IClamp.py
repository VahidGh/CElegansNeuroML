from c302 import generate
import sys


if __name__ == '__main__':
    
    parameter_set = sys.argv[1] if len(sys.argv)==2 else 'A'
    
    exec('from parameters_%s import ParameterisedModel'%parameter_set)
    params = ParameterisedModel()
    
    params.set_bioparameter("unphysiological_offset_current", "0.21nA", "Testing IClamp", "0")
    params.set_bioparameter("unphysiological_offset_current_del", "100 ms", "Testing IClamp", "0")
    params.set_bioparameter("unphysiological_offset_current_dur", "200 ms", "Testing IClamp", "0")
    
    
    my_cell = "ADAL"
    
    cells               = [my_cell]
    cells_to_stimulate  = [my_cell]
    
    reference = "c302_%s_IClamp"%parameter_set
    
    
    generate(reference, 
             params, 
             cells=cells, 
             cells_to_stimulate=cells_to_stimulate, 
             duration=500, 
             dt=0.1, 
             vmin=-72 if parameter_set=='A' else -52, 
             vmax=-48 if parameter_set=='A' else -28,
             validate=(parameter_set!='B'))