from ovito.io import import_file
from ovito.modifiers import DislocationAnalysisModifier

lines = []

pipeline = import_file('tensile.xyz')
modifiers = DislocationAnalysisModifier()
modifiers.input_crystal_structure = DislocationAnalysisModifier.Lattice.BCC
pipeline.modifiers.append(modifiers)

for frame in range(pipeline.source.num_frames):
    data = pipeline.compute(frame)
    step = frame * 100
    total_line_length = data.attributes['DislocationAnalysis.total_line_length']
    #single_line_length = data.attributes['DislocationAnalysis.length.1/6<112>']
    #single_line_length = data.attributes['DislocationAnalysis.length.other']
    #盒子体积
    cell_volume = data.attributes['DislocationAnalysis.cell_volume']
    #位错密度计算
    dislocation_density=total_line_length / cell_volume


    tmp = str(step) + " "+str(total_line_length)+" "+str(dislocation_density)+ "\n"
    lines.append(tmp)

save_data = open('dislocation.txt',"w")
save_data.write("step dislocation_length dislociation_density\n")
save_data.writelines(lines)
save_data.close()

