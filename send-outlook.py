
import win32com.client
import pandas

def send_mail(to,attachments,name):

    ol = win32com.client.Dispatch('Outlook.Application')
    olmailitem = 0x0
    newmail = ol.CreateItem(olmailitem)
    """
    for oacc in ol.Session.Accounts:
        if oacc.SmtpAddress == "munkaugy@porscheinterauto.hu":
            newmail.SendUsingAccount = oacc
            newmail._oleobj_.Invoke(*(64209, 0, 8, 0, oacc))
            break
    """
    
    newmail.Subject = 'Fotózás képek'
    newmail.To = to
    
    
    newmail.Body= f'''Kedves {name}!
 
Csatolva küldöm a fotózáson készült képeidet.
Kérjük állítsd be profilképként a Microsoft fiókodban (Teams, Outlook). 

Az alábbi linken találsz segítséget hozzá:
https://support.microsoft.com/hu-hu/account-billing/a-microsoft-fi%C3%B3k-k%C3%A9p%C3%A9nek-m%C3%B3dos%C3%ADt%C3%A1sa-57db783b-0646-f624-ebb9-52ad4f1ce0ee

Kérdéseiddel kapcsolatban fordulj a HR (4515-250) vagy az IT (4515-323) osztályhoz.

Üdvözlettel:

HR
    '''
    
    
    for attachment in attachments:
        newmail.Attachments.Add(attachment)
    
    newmail.Send()
    
# Read excel table to dataframe
base_excel_file = 'C:\\fotok\\list.xlsx'
basetable = pandas.read_excel(base_excel_file)

print(basetable)

logfile = open('c:\\temp\\sendlog.txt', 'w+')
nev = email = ''
files = []

for i in basetable.index:
    if basetable['email'][i] == email:
        files.append(basetable['url'][i])
    else:
        if email != '':
            try:
                send_mail(email, files, nev)
                logfile.write(nev+';'+email+';OK\n')
            except BaseException as e:
                logfile.write(nev+';'+email+';'+str(e)+'\n')
        files = []
        nev = basetable['nev'][i]
        email = basetable['email'][i]
        files.append(basetable['url'][i])
    if i == len(basetable)-1:
        try:
            send_mail(email, files, nev)
            logfile.write(nev+';'+email+';OK\n')
        except BaseException as e:
            logfile.write(nev+';'+email+';'+str(e)+'\n')

logfile.close()
