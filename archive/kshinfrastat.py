"""
2010 - Kiszállítás
Created on Wed Oct 18 09:45:28 2023
@author: rkoczur
"""

# Import packages
import pandas
import math
import datetime

# Declare constant variables
last_day = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
month = last_day.month
year = last_day.year


ev = str(last_day.year)[2:4]
honap = str(last_day.month)
base_excel_file = 'C:\\temp\\ksh11.xlsx'
final_csv_file = 'C:\\temp\\osap-2010-'+ev+'-'+honap+'.csv'

final_datas = list()
sorszam = 1



print(ev, honap)

# Read excel table to dataframe
basetable = pandas.read_excel(base_excel_file)

for row in basetable.index:
    termekkod = basetable['Termék kódja'][row]
    rend_orszag = basetable['Rendeltetési tagállam'][row]
    szarm_orszag = basetable['Származási ország'][row]
    tomeg = float(str(basetable['Nettó tömeg egyenként'][row]).replace(',','.'))
    mennyiseg = int(basetable['Mennyiség'][row])
    egysegar = int(basetable['Számlázott összeg'][row])
    adoszam = str(basetable['Partner adószáma'][row])

    osszeg = egysegar*mennyiseg
    ossztomeg = tomeg*mennyiseg
    ukod = '12' if len(str(adoszam)) < 4 else '11'

    if len(final_datas) == 0:
        akt_sorszam = '0'*(5-len(str(sorszam)))+str(sorszam)

        final_datas.append([akt_sorszam,
                            termekkod,
                            ukod,
                            rend_orszag,
                            szarm_orszag,
                            ossztomeg,
                            mennyiseg,
                            osszeg,
                            osszeg,
                            adoszam])

    else:
        current_line = len(final_datas)
        found = False
        for line in range(len(final_datas)):
            if (final_datas[line][1] == termekkod and
                final_datas[line][3] == rend_orszag and
                final_datas[line][4] == szarm_orszag and
                final_datas[line][9] == adoszam): #or (len(str(final_datas[line][9])) < 4 and len(str(adoszam)) < 4))):
                    final_datas[line][5] = ossztomeg + final_datas[line][5]
                    final_datas[line][6] = mennyiseg + final_datas[line][6]
                    final_datas[line][7] = osszeg + final_datas[line][7]
                    found = True
                    break
        if not found:
            sorszam += 1
            akt_sorszam = '0'*(5-len(str(sorszam)))+str(sorszam)

            final_datas.append([akt_sorszam,
                                termekkod,
                                ukod,
                                rend_orszag,
                                szarm_orszag,
                                ossztomeg,
                                mennyiseg,
                                osszeg,
                                osszeg,
                                adoszam])

# Convert datas to strings in the array
for i in range(len(final_datas)):
    for j in range(len(final_datas[i])):
        final_datas[i][j] = str(final_datas[i][j])
        if final_datas[i][j] == 'nan':
            final_datas[i][j] = ''

for i in range(len(final_datas)):
    final_datas[i][5] = str(final_datas[i][5]).replace('.',',')

# Write datas to csv
final_file = open(final_csv_file, 'w+')
fejezet_counter = 1
sor_counter = 1


final_file.write('{fejezet;sorrend};;;;;;;;;;;;;\n')
final_file.write('0;1;;;;;;;;;;;;;\n;;;;;;;;;;;;;;\n')
final_file.write('{MC01;M003_G;M003;MEV;MHO;JHNEV;JBEOSZTAS;JTELEFON;JEMAIL;KNEV;KBEOSZTAS;KTELEFON;KEMAIL;MEGJEGYZES;VGEA002}\n')
final_file.write('2010;14515239;14515239;'+ev+';'+honap+';Tótvári Tamás;Pénzügyi vezető;1/4515232;tamas.totvari@porscheinterauto.hu;Borók Judit;könyvelő;1/4515240;judit.borok@porscheinterauto.hu;;\n')
final_file.write(';;;;;;;;;;;;;;\n{fejezet;sorrend};;;;;;;;;;;;;\n1;1;;;;;;;;;;;;;\n;;;;;;;;;;;;;;\n')
final_file.write('{T_SORSZ;TEKOD;UKOD;RTA;SZAORSZ;KGM;KIEGME;SZAOSSZ;STAERT;PADO};;;;;\n')
for line in final_datas:
    if math.ceil(sor_counter/25) > fejezet_counter:
        fejezet_counter += 1
        final_file.write(';;;;;;;;;;;;;;\n{fejezet;sorrend};;;;;;;;;;;;;\n1;'+str(fejezet_counter)+';;;;;;;;;;;;;\n;;;;;;;;;;;;;;\n')
        final_file.write('{T_SORSZ;TEKOD;UKOD;RTA;SZAORSZ;KGM;KIEGME;SZAOSSZ;STAERT;PADO};;;;;\n')
    final_file.write(';'.join(line)+"\n")
    sor_counter += 1

final_file.close()
