def A60script(base_excel_file):
    try:

        import pandas
        import math
        import datetime
        import copy

        #Class definition for easier data handling
        class Data_Unit:

            def __init__(self,full_vat,cust_field):
                self.country_code = full_vat[:2]
                self.vat = full_vat[2:]
                self.cust_field = cust_field
                self.amount = 0
            
            def add_amount(self, n):
                self.amount += n

        # Function declarations
        def check_existing(current_unit, current_list):
            found = None
            country_code = current_unit.country_code
            cust_field = current_unit.cust_field
            vat = current_unit.vat
            for i,unit in enumerate(current_list):
                if unit.vat == vat and unit.country_code == country_code and unit.cust_field == cust_field:
                    found = i
                    break
            return found


        def process_unit(current_unit, current_list):
            search_result = check_existing(current_unit, current_list)
            if search_result == None:
                current_list.append(current_unit)
            else:
                current_list[search_result].add_amount(current_unit.amount)
            return current_list

        # Declare constant variables
        last_day = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
        month = last_day.month
        year = last_day.year

        from_date = str(year)+str('{:02d}'.format(month))+'01'
        to_date = str(year)+str('{:02d}'.format(month))+str('{:02d}'.format(last_day.day))
        print (to_date)
        # final_imp_file = 'c:\\temp\\teszt.imp'
        final_imp_file = '\\\\as1pia.piahu.hu\\rpa-share\\4-Adatok\\24-Bevallas-22A60\\a60-'+from_date+'-'+to_date+'.imp'
        reference_file = 'C:\\temp\\a60sap.csv'


        # Read excel table to dataframe
        basetable = pandas.read_excel(base_excel_file)

        # List for storing final data

        page_01 = list()
        page_02 = list()
        page_03 = list()
        page_04 = list()

        # Summarize datas into lists
        for index,row in basetable.iterrows():
            
            tax_code = row['Ad']
            full_vat = row['Forgalmi adó-Id szám']
            amount = row['SP-összeg']/1000
            cust_field = str()
            
            if tax_code == 'D2':
                cust_field = 'C'
            else:
                cust_field = None

            current_unit = Data_Unit(full_vat, cust_field)
            current_unit.add_amount(amount)

            if len(full_vat)<7:
                continue

            if tax_code in ['G4','I1']:
                print(tax_code)
                current_unit.amount = -1*current_unit.amount
                page_01 = process_unit(current_unit,page_01)
            elif tax_code in ['E0','EG','EH','EM','EJ','D2']:
                page_02 = process_unit(current_unit,page_02)
            elif tax_code == 'I8':
                current_unit.amount = -current_unit.amount
                page_03 = process_unit(current_unit,page_03)
            elif tax_code in ['EN','EP']:
                page_04 = process_unit(current_unit,page_04)
            else:
                continue
            
        # Define descriptive data
        number_of_pages = 4

        n=len(page_01) 
        no_pages_01 = math.floor(n/24)+1
        d_lap1 = '01,'+str(no_pages_01)

        n=len(page_02) 
        no_pages_02 = math.floor(n/24)+1
        d_lap2 = '02,'+str(no_pages_02)

        n=len(page_03)
        no_pages_03 = math.floor(n/24)+1
        d_lap3 = '03,'+str(no_pages_03)

        n=len(page_04)>0
        no_pages_04 = math.floor(n/24)+1
        d_lap4 = '04,'+str(no_pages_04)

        number_of_lines = (len(page_01)+len(page_02)+len(page_03)+len(page_04))*3+11+number_of_pages

        #Reference file
        reference = open(reference_file, 'w+')
        for item in page_01:
            reference.write(str(item.country_code)+';'+str(item.vat)+';'+str(int(item.amount))+'\n')
        reference.close

        #Write IMP file
        final_file = open(final_imp_file, 'w+')
        final_file.write('$ny_azon=25A60\n')
        final_file.write('$sorok_száma='+str(number_of_lines)+'\n')
        final_file.write('$d_lapok_száma='+str(number_of_pages)+'\n')
        final_file.write('$d_lap1='+d_lap4+'\n')
        final_file.write('$d_lap2='+d_lap3+'\n')
        final_file.write('$d_lap3='+d_lap2+'\n')
        final_file.write('$d_lap4='+d_lap1+'\n')
        final_file.write('$info=\n')
        final_file.write('23335='+from_date+'\n')
        final_file.write('23336='+to_date+'\n')
        final_file.write('23339=H\n')
        final_file.write('23805=14515239\n')
        final_file.write('23815=Porsche Inter Auto Hungaria Kft.\n')
        final_file.write('23838=Borók Judit\n')
        final_file.write('23839=06-1-4515-240\n')

        buffer = list()

        for row in page_01:
            if row.amount == 0:
                continue
            buffer.append(row)
        page_01 = copy.deepcopy(buffer)
        buffer.clear()

        for row in page_02:
            if row.amount == 0:
                continue
            buffer.append(row)
        page_02 = copy.deepcopy(buffer)
        buffer.clear()

        for row in page_03:
            if row.amount == 0:
                continue
            buffer.append(row)
        page_03 = copy.deepcopy(buffer)
        buffer.clear()

        for row in page_04:
            if row.amount == 0:
                continue
            buffer.append(row)
        page_04 = copy.deepcopy(buffer)
        buffer.clear()

        #Page 01
        line_identifier = 1713
        page_number = 1
        for index,row in enumerate(page_01):
            prev_page_number = page_number
            page_number = math.floor((index)/24)+1
            if prev_page_number<page_number: 
                line_identifier = 1713
            final_file.write(str(line_identifier)+"["+str(page_number)+"]="+str(row.country_code)+'\n')
            final_file.write(str(line_identifier+1)+"["+str(page_number)+"]="+str(row.vat)+'\n')
            final_file.write(str(line_identifier+2)+"["+str(page_number)+"]="+str("%.f" % row.amount)+'\n')
            line_identifier+=12


        #Page 02
        line_identifier = 2059
        page_number = 1
        for index,row in enumerate(page_02):
            prev_page_number = page_number
            page_number = math.floor((index/24))+1
            if prev_page_number<page_number: 
                line_identifier = 2059
            final_file.write(str(line_identifier)+"["+str(page_number)+"]="+str(row.country_code)+'\n')
            final_file.write(str(line_identifier+1)+"["+str(page_number)+"]="+str(row.vat)+'\n')
            final_file.write(str(line_identifier+2)+"["+str(page_number)+"]="+str("%.f" % row.amount)+'\n')
            if row.cust_field == 'C':
                final_file.write(str(line_identifier+3)+"["+str(page_number)+"]=C\n")
            line_identifier+=12

        #Page 03
        line_identifier = 2380
        page_number = 1
        for index,row in enumerate(page_03):
            prev_page_number = page_number
            page_number = math.floor((index)/24)+1
            if prev_page_number<page_number: 
                line_identifier = 2380
            final_file.write(str(line_identifier)+"["+str(page_number)+"]="+str(row.country_code)+'\n')
            final_file.write(str(line_identifier+1)+"["+str(page_number)+"]="+str(row.vat)+'\n')
            final_file.write(str(line_identifier+2)+"["+str(page_number)+"]="+str("%.f" % row.amount)+'\n')
            line_identifier+=9

        #Page 04
        line_identifier = 2629
        page_number = 1
        for index,row in enumerate(page_04):
            prev_page_number = page_number
            page_number = math.floor((index)/24)+1
            if prev_page_number<page_number: 
                line_identifier = 2629
            final_file.write(str(line_identifier)+"["+str(page_number)+"]="+str(row.country_code)+'\n')
            final_file.write(str(line_identifier+1)+"["+str(page_number)+"]="+str(row.vat)+'\n')
            final_file.write(str(line_identifier+2)+"["+str(page_number)+"]="+str("%.f" % row.amount)+'\n')
            line_identifier+=9
        
        return final_imp_file
            
    except BaseException as e:
        return (str(e))

print(A60script("C:\\temp\\SAP-A60-2025-01.xlsx"))