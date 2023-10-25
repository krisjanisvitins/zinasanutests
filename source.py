import PyPDF2
import pathlib
import csv
import datetime

adrese = pathlib.Path("invoices")
visi_faili=list(adrese.glob("*.pdf"))

for f in range(len(visi_faili)):
    row=[]
    pdf_file=PyPDF2.PdfReader(open(visi_faili[f],"rb"))
    number_of_pages=len(pdf_file.pages)
    page1=pdf_file.pages[0]
    page2=pdf_file.pages[1]

    text1=page1.extract_text()
    text2=page2.extract_text()

    pos1 = text1.find("Elektroenerģija")
    pos2 = text1.find("Elektroenerģijas papildpakalpojumi")

    kop_maksa_text = (text1[pos1+len("Elektroenerģija"):pos2-2]).rstrip()
    kop_maksa = float(kop_maksa_text.replace(",", "."))
    #print(kop_maksa)

    pos3 = text1.find("Elektroenerģijas patēriņš kopā: ")
    pos4 = text1.find("Veicot rēķina apmaksu, lūdzu, norādiet Klienta Nr")

    elek_daudzums_text = (text1[pos3+len("Elektroenerģijas patēriņš kopā: "):pos4-5]).rstrip()
    #print(elek_daudzums_text)
    elek_daudzums = float(elek_daudzums_text.replace(" ", "").replace(",", "."))
    #print(elek_daudzums)

    #pos5 = text2.find("kWh")
    cena_par_kwh = 0.1157

    #print(cena_par_kwh)

    pos5 = text1.find("Rēķina Nr.")
    pos6 = text1.find("RĒĶINA KOPSAVILKUMS")

    invoice_datums = (text1[pos5+21:pos6-9]).rstrip()
    #print(periods)

    with open("data.csv", r) as f:
        next(f)
        for line in f:
            




    #invoice_datums = datetime.datetime.strptime(invoice_datums, "%d.%m.%Y")

    #periods_start = invoice_datums.replace(day=1)
    #periods_end = (periods_start + datetime.timedelta(days=32)).replace(day=1) - datetime.timedelta(days=1)

    #periods_start = datetime.datetime.strptime(periods.split(' - ')[0], "%d.%m.%Y")
    #periods_end = datetime.datetime.strptime(periods.split(' - ')[1], "%d.%m.%Y")

#nordpool_data=[]
#with open("nordpool.csv", "r") as f:
#    reader = csv.reader(f)
#    next(reader)
#    for row in reader:
#        ts_start = datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
#       ts_end = datetime.datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")
#       price = float(row[2])
#       nordpool_data.append((ts_start, ts_end, price))

#nordpool_tarifs=0.0
#for entry in nordpool_data:
#    if periods_start <= entry[0] and periods_end >= entry[1]:
#        nordpool_tarifs = entry[2]
#        break

#iesp_ietaup = (elek_daudzums * (nordpool_tarifs - cena_par_kwh)) if elek_daudzums > 0 else 0.00

#print(iesp_ietaup)




#    next(reader)

 #   for row in reader:
  #      date = row[0]
   #     price = float(row[3])
    #    year, month = date.split()[0].split("-")[:2]
     #   date_parts=date.split(" ")
      #  find1= date_parts[0]
#
 #       if find1 == periods:



