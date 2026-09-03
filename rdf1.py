#导入函数
from ovito.io import import_file, export_file
from ovito.modifiers import CoordinationAnalysisModifier,TimeAveragingModifier
#加载dump文件
pipeline = import_file('tensile.xyz')
#添加rdf计算
modifier = CoordinationAnalysisModifier(cutoff=5,number_of_bins=200)
pipeline.modifiers.append(modifier)
#平均值计算
pipeline.modifiers.append(TimeAveragingModifier(operate_on='table:coordination-rdf'))
#输出结果
export_file(pipeline,"rdf1.txt","txt/table",key="coordination-rdf[average]")
