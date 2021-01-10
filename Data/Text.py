
Ano_score = []
windo =[]
step = []
class Data_gather(object):
	def __init__(self, arg, value):
		super(Data_gather, self)
		Ano_score.append(value)
		print( "Anovva = ", Ano_score)

	def window(val):
		windo.append(val)
		print("\n Win = ",Win)

	def Step_Size(val1):
		step.append(val1)
		print("\n Step = ",step)

	def Two_factor_anova():
		df = pd.Dataframe({'window':windo,'step':step,"Ano_score":Ano_score})
		win_m =df.window.mean()
		step_m = df.step.mean()
		Ano_m = df.Ano_score.mean()
		print("Mean of window : ",win_m)
		print("Mean of step : ", step_m)
		print("Mean of Ano_m : ", Ano_m)
		overall = (win_m + step_m+ Ano_m)/3
		# SST
		lis = ['window', 'step', 'Ano_score']
		sst = ((overall-df[lis])**2).sum()
		print("SST value= ",sst)

		#SSC
		ssc_list = [Apple_m, Amzn_m, Crm_m]
		for i in ssc_list:
		  ssc0 = ssc0+(overall-i)**2
		print("SSC value = ",ssc0)

		# SSB
		ssb0 = ((AK_df.R_mean - overall)**2).sum()
		print("SSB value = ",ssb0)

		print(sst,"\n", ssc0,"\n \t", ssb)
		err = sst - ssc0 -ssb
		print("Error = ",err)

