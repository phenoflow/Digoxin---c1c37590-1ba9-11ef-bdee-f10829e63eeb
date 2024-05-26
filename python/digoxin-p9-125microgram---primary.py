# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2024.

import sys, csv, re

codes = [{"code":"42989","system":"gprdproduct"},{"code":"47813","system":"gprdproduct"},{"code":"2511","system":"gprdproduct"},{"code":"33080","system":"gprdproduct"},{"code":"20944","system":"gprdproduct"},{"code":"2302","system":"gprdproduct"},{"code":"34017","system":"gprdproduct"},{"code":"33675","system":"gprdproduct"},{"code":"792","system":"gprdproduct"},{"code":"34327","system":"gprdproduct"},{"code":"3308","system":"gprdproduct"},{"code":"34023","system":"gprdproduct"},{"code":"36","system":"gprdproduct"},{"code":"34519","system":"gprdproduct"},{"code":"54117","system":"gprdproduct"},{"code":"34948","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('digoxin-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["digoxin-p9-125microgram---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["digoxin-p9-125microgram---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["digoxin-p9-125microgram---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
