# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2024.

import sys, csv, re

codes = [{"code":"25238","system":"gprdproduct"},{"code":"3705","system":"gprdproduct"},{"code":"94","system":"gprdproduct"},{"code":"3286","system":"gprdproduct"},{"code":"34024","system":"gprdproduct"},{"code":"3181","system":"gprdproduct"},{"code":"33274","system":"gprdproduct"},{"code":"34328","system":"gprdproduct"},{"code":"42990","system":"gprdproduct"},{"code":"40245","system":"gprdproduct"},{"code":"20844","system":"gprdproduct"},{"code":"33612","system":"gprdproduct"},{"code":"48587","system":"gprdproduct"},{"code":"43577","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('digoxin-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["digoxin-p9-500microgram---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["digoxin-p9-500microgram---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["digoxin-p9-500microgram---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
