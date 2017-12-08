import pandas as pd
import glob
import matplotlib.pyplot as plt

all_files = glob.glob("*.bal")
# remove the file summary.bal
all_files = all_files[:-1] 
# read all files into one dataframe by skiping the first three columns of each file and the header
df = pd.concat((pd.read_csv(f,delim_whitespace=True,header=1,usecols=list(range(3,10))) for f in all_files),axis=1)
df = df.apply(pd.to_numeric)
Qstore = df['[kJ/hr].1']
Qstore.columns = ['Qs_W01','Qs_W02','Qs_W03','Qs_W04','Qs_W05','Qs_W06','Qs_W07','Qs_W08','Qs_W09','Qs_W10','Qs_W11','Qs_W12','Qs_W13']
Qstore['Qs_tot'] = Qstore.sum(axis=1)/3600

# Read ambient temp, total horizontal radiation and zone temperatures
R = pd.read_csv('ConstantSpRef_v2.out',delim_whitespace=True)
R['Qsolar'] = R['Qsolar']/100 # unit=kJ/h.m2, scale down 100 times

# Read energy flexibility per hour
flex_pos = pd.read_csv('ConstantAdr_pos.txt',header=None)
flex_neg = pd.read_csv('ConstantAdr_neg.txt',header=None,usecols=list([1,2]))
flex = pd.concat([flex_pos,flex_neg],axis=1)
flex.columns = ['Time','Adr_pos','eta_pos','Adr_neg','eta_neg']

fig = plt.figure()
ax1 = fig.add_subplot(111)
line1 = ax1.plot(R['TIME'],Qstore['Qs_tot'],'r',label='Qstore')
line2 = ax1.plot(R['TIME'],R['Qsolar'],'g--',label='Qsolar')
line3 = ax1.plot(R['TIME'],R['QHeatTotal'],'b-',label='QHeatTotal')

ax2 = ax1.twinx() 
line4 = ax2.plot(R['TIME'],R['Tamb'],'m--',label='Tamb')

line = line1+line2+line3+line4
labs = [l.get_label() for l in line]
ax1.set_xlabel('Time(h)')
ax1.set_ylabel('Heating rate [kW]')
ax2.set_ylabel('Temperature [C]')
ax1.legend(line,labs,loc=0)
ax1.grid()
plt.show()

plt.figure(2)
x = flex['Time']
plt.plot(x,flex[['Adr_pos','Adr_neg']])
plt.plot(x,Qstore['Qs_tot'].iloc[167:167+168])
plt.legend(['Adr_pos','Adr_neg','Qs_tot'])
plt.grid(True)
plt.show()