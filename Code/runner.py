
#import model_delta as m
import data

#def select_model(model):


def run(model, alpha=None, beta=None, delta=None):
	m=__import__(model)
	m.alpha=alpha
	if beta is not None:
		m.beta=beta
	if delta is not None:
		m.delta=delta
	print 'running with alpha={0}, beta={1}, delta={2}'.format(alpha,beta,delta)
	m.initialize()

	upsamesame=m.p_data_data([data.tests], data.data_same)
	updiffsame=m.p_data_data([data.testd], data.data_same)
	normsamesame=m.p_data_data([data.testsnorm], data.data_same)
	normdiffsame=m.p_data_data([data.testdnorm], data.data_same)
	psamesame=upsamesame/(upsamesame+normsamesame)
	pdiffsame=updiffsame/(updiffsame+normdiffsame)
	upsamediff=m.p_data_data([data.tests], data.data_diff)
	updiffdiff=m.p_data_data([data.testd], data.data_diff)
	normsamediff=m.p_data_data([data.testsnorm], data.data_diff)
	normdiffdiff=m.p_data_data([data.testdnorm], data.data_diff)
	psamediff=upsamediff/(upsamediff+normsamediff)
	pdiffdiff=updiffdiff/(updiffdiff+normdiffdiff)
	psameplussame=m.p_data_data_binormalized([data.tests],data.data_same_plus)
	pdiffplussame=m.p_data_data_binormalized([data.testd],data.data_same_plus)
	psameplusdiff=m.p_data_data_binormalized([data.tests],data.data_diff_plus)
	pdiffplusdiff=m.p_data_data_binormalized([data.testd],data.data_diff_plus)

	return (m.choose(psamesame,pdiffsame), m.choose(pdiffdiff,psamediff),\
		m.choose(psameplussame,pdiffplussame), m.choose(pdiffplusdiff,psameplusdiff))



def compare(p_model):
	pc1s,pc1d,pc2s,pc2d=p_model
	distance=(pc1s-data.pe_1s)**2+(pc1d-data.pe_1d)**2+(pc2s-data.pe_2s)**2+(pc2d-data.pe_2d)**2
	return distance
