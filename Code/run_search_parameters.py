import model_alphabeta as m
import data
import numpy as np
import scipy.optimize

pcorr_1s=0.46
pcorr_2s=0.78
pcorr_1d=0.44
pcorr_2d=0.5

manual=True
auto=False

def run_model():
	print 'running with alpha={0}, beta={1}, gamma={2}, epsilon={3}'.format(m.alpha,m.beta,m.gamma,m.epsilon)
	m.initialize()

	upsamesame=m.p_singledata_data(data.tests, data.data_same)
	updiffsame=m.p_singledata_data(data.testd, data.data_same)
	normsamesame=m.p_singledata_data(data.testsnorm, data.data_same)
	normdiffsame=m.p_singledata_data(data.testdnorm, data.data_same)
	psamesame=upsamesame/(upsamesame+normsamesame)
	pdiffsame=updiffsame/(updiffsame+normdiffsame)
	upsamediff=m.p_singledata_data(data.tests, data.data_diff)
	updiffdiff=m.p_singledata_data(data.testd, data.data_diff)
	normsamediff=m.p_singledata_data(data.testsnorm, data.data_diff)
	normdiffdiff=m.p_singledata_data(data.testdnorm, data.data_diff)
	psamediff=upsamediff/(upsamediff+normsamediff)
	pdiffdiff=updiffdiff/(updiffdiff+normdiffdiff)
	psameplussame=m.p_singledata_data_binormalized(data.tests,data.data_same_plus)
	pdiffplussame=m.p_singledata_data_binormalized(data.testd,data.data_same_plus)
	psameplusdiff=m.p_singledata_data_binormalized(data.tests,data.data_diff_plus)
	pdiffplusdiff=m.p_singledata_data_binormalized(data.testd,data.data_diff_plus)

	return m.choose(psamesame,pdiffsame), m.choose(pdiffdiff,psamediff),\
		m.choose(psameplussame,pdiffplussame), m.choose(pdiffplusdiff,psameplusdiff)


#manual minimization
if manual:
	# epsilons=[0.001, 0.01, 0.05, 0.1, 0.25]
	# alphas=[0.01, 0.05, 0.2, 0.33, 0.5, 0.9]
	# betas=[0.01, 0.05, 0.2, 0.33, 0.5, 0.9]
	# gammas=[0.01, 0.1, 0.5, 0.9, 0.99]
	epsilons=[0.01,0.05,0.1]
	alphas=[0.1,0.25,0.33]
	betas=[0.1,0.25,0.33]
	gammas=[0.1,0.5,0.9]

	mindist=100
	stars=(0,0,0)
	pstars=(0,0,0,0)
	for epsilon in epsilons:
		m.epsilon=epsilon
		for alpha in alphas:
			m.alpha=alpha
			for beta in betas:
				m.beta=beta
				if alpha+beta>1:
					continue
				for gamma in gammas:
					m.gamma=gamma
					pc1s,pc1d,pc2s,pc2d =run_model()
					dist=(pc1s-pcorr_1s)**2+(pc1d-pcorr_1d)**2+(pc2s-pcorr_2s)**2+(pc2d-pcorr_2d)**2
					if dist<mindist:
						stars=(epsilon,alpha,beta,gamma)
						pstars=pc1s,pc1d,pc2s,pc2d
						mindist=dist

	print stars
	print pstars
	print mindist
#
# def model_dist((alpha)):#((gain,gamma,alpha,epsilon)):
# 	m.gain=1#gain
# 	m.gamma=0.9#gamma
# 	m.alpha=alpha
# 	m.beta=alpha
# 	m.epsilon=0.01#epsilon
# 	#m.initialize()
# 	pc1s,pc1d,pc2s,pc2d =run_model()
# 	dist=(pc1s-pcorr_1s)**2+(pc1d-pcorr_1d)**2+(pc2s-pcorr_2s)**2+(pc2d-pcorr_2d)**2
# 	return dist

# if auto:
# 	import scipy
# 	x0=np.array([1,0.9,0.3,0.01])
# 	x0=np.array([0.3])
#
# 	res=scipy.optimize.minimize(model_dist,x0)
#
# 	print res
