from ovito.io import import_file, export_file
from ovito.modifiers import CoordinationAnalysisModifier,TimeAveragingModifier

pipeline = import_file('tensile.xyz')

modifier = CoordinationAnalysisModifier(cutoff=5,number_of_bins=200,partial=True)
pipeline.modifiers.append(modifier)

pipeline.modifiers.append(TimeAveragingModifier(operate_on='table:coordination-rdf'))


export_file(pipeline,"rdf2.txt","txt/table",key="coordination-rdf[average]")
