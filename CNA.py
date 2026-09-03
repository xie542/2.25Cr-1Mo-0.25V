from ovito.io import import_file
from ovito.modifiers import CommonNeighborAnalysisModifier

#定义变量
steps =[]

counts_fcc = []
counts_bcc = []
counts_hcp = []
counts_ico = []
counts_other = []
#导入轨迹文件、添加CNA
pipeline = import_file('tensile.xyz')
modifiers = CommonNeighborAnalysisModifier()
pipeline.modifiers.append(modifiers)
#循环计算并保存每一帧的CNA分析结果
for frame in range(pipeline.source.num_frames):
    data = pipeline.compute(frame)
    step = str(frame * 100)
    count_fcc = str(data.attributes['CommonNeighborAnalysis.counts.FCC'] * 100 / data.particles.count)
    count_bcc = str(data.attributes['CommonNeighborAnalysis.counts.BCC'] * 100 / data.particles.count)
    count_hcp = str(data.attributes['CommonNeighborAnalysis.counts.HCP'] * 100 / data.particles.count)
    count_ico = str(data.attributes['CommonNeighborAnalysis.counts.ICO'] * 100 / data.particles.count)
    count_other = str(data.attributes['CommonNeighborAnalysis.counts.OTHER'] * 100 / data.particles.count)
    #single_line_length = data.attributes['DislocationAnalysis.length.1/6<112>']
    #保存数据到变量
    steps.append(step)
    counts_fcc.append(count_fcc)
    counts_bcc.append(count_bcc)
    counts_hcp.append(count_hcp)
    counts_ico.append(count_ico)
    counts_other.append(count_other)

file = open("result.txt", 'w')
for i in range(len(steps)):
    file.write(str(steps[i])+' '+counts_fcc[i]+' '+counts_bcc[i]+' '+counts_hcp[i]+' '+counts_ico[i]+' '+counts_other[i])
    file.write('\n')
file.close()
