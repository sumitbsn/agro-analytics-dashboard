import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def kharif(rf):
	khar=rf['June']+rf['July']+rf['August']+rf['September']+rf['October']
	return khar
def wholeyear(rf):
	wy=rf.sum(axis=1)
	return wy
def tkharif(t):
	tk=(t['June']+t['July']+t['August']+t['September']+t['October'])/5
	return tk

# cropdata = pd.read_excel(io='/home/sumit/finalyearproject/data/CropProject.xlsx', sheetname='crop_data')

# cropdata = pd.ExcelFile("/home/sumit/finalyearproject/data/CropProject.csv")

tempdata = pd.ExcelFile("/home/sumit/finalyearproject/data/temperature.xlsx")
tempnagapattinam=pd.read_excel(io='/home/sumit/finalyearproject/data/temperature.xlsx',sheetname='nagapattinam')
temppudukkottai=pd.read_excel(io='/home/sumit/finalyearproject/data/temperature.xlsx',sheetname='pudukkottai')
tempramanathapuram=pd.read_excel(io='/home/sumit/finalyearproject/data/temperature.xlsx',sheetname='ramanathapuram')
tempsivaganga=pd.read_excel(io='/home/sumit/finalyearproject/data/temperature.xlsx',sheetname='sivaganga')
tempthanjavur=pd.read_excel(io='/home/sumit/finalyearproject/data/temperature.xlsx',sheetname='thanjavur')
temptiruvallur=pd.read_excel(io='/home/sumit/finalyearproject/data/temperature.xlsx',sheetname='tiruvallur')
temptiruvarur=pd.read_excel(io='/home/sumit/finalyearproject/data/temperature.xlsx',sheetname='tiruvarur')


pressnagapattinam=pd.read_excel(io='/home/sumit/finalyearproject/data/pressure.xlsx',sheetname='nagapattinam')
presspudukkottai=pd.read_excel(io='/home/sumit/finalyearproject/data/pressure.xlsx',sheetname='pudukkottai')
pressramanathapuram=pd.read_excel(io='/home/sumit/finalyearproject/data/pressure.xlsx',sheetname='ramanathapuram')
presssivaganga=pd.read_excel(io='/home/sumit/finalyearproject/data/pressure.xlsx',sheetname='sivaganga')
pressthanjavur=pd.read_excel(io='/home/sumit/finalyearproject/data/pressure.xlsx',sheetname='thanjavur')
presstiruvallur=pd.read_excel(io='/home/sumit/finalyearproject/data/pressure.xlsx',sheetname='tiruvallur')
presstiruvarur=pd.read_excel(io='/home/sumit/finalyearproject/data/pressure.xlsx',sheetname='tiruvarur')

rfnagapattinam=pd.read_excel(io='/home/sumit/finalyearproject/data/rainfall.xlsx',sheetname='nagapattinam')
rfpudukkottai=pd.read_excel(io='/home/sumit/finalyearproject/data/rainfall.xlsx',sheetname='pudukkottai')
rframanathapuram=pd.read_excel(io='/home/sumit/finalyearproject/data/rainfall.xlsx',sheetname='ramanathapuram')
rfsivaganga=pd.read_excel(io='/home/sumit/finalyearproject/data/rainfall.xlsx',sheetname='sivaganga')
rfthanjavur=pd.read_excel(io='/home/sumit/finalyearproject/data/rainfall.xlsx',sheetname='thanjavur')
rftiruvallur=pd.read_excel(io='/home/sumit/finalyearproject/data/rainfall.xlsx',sheetname='tiruvallur')
rftiruvarur=pd.read_excel(io='/home/sumit/finalyearproject/data/rainfall.xlsx',sheetname='tiruvarur')

kharnagapattinam=kharif(rfnagapattinam)
kharpudukkottai=kharif(rfpudukkottai)
kharramanathapuram=kharif(rframanathapuram)
kharsivaganga=kharif(rfsivaganga)
kharthanjavur=kharif(rfthanjavur)
khartiruvallur=kharif(rftiruvallur)
khartiruvarur=kharif(rftiruvarur)

wynagapattinam=wholeyear(rfnagapattinam)
wypudukkottai=wholeyear(rfpudukkottai)
wyramanathapuram=wholeyear(rframanathapuram)
wysivaganga=wholeyear(rfsivaganga)
wythanjavur=wholeyear(rfthanjavur)
wytiruvallur=wholeyear(rftiruvallur)
wytiruvarur=wholeyear(rftiruvarur)

tknagapattinam=tkharif(tempnagapattinam)
tkpudukkottai=tkharif(temppudukkottai)
tkramanathapuram=tkharif(tempramanathapuram)
tksivaganga=tkharif(tempsivaganga)
tkthanjavur=tkharif(tempthanjavur)
tktiruvallur=tkharif(temptiruvallur)
tktiruvarur=tkharif(temptiruvarur)
