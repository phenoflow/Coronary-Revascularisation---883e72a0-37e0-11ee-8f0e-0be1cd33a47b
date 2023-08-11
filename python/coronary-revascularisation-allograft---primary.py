# Nathaniel M Hawkins, Shaun Scholes, Madhavi Bajekal, Hande Love, Martin O'Flaherty, Rosalind Raine, Simon Capewell, 2023.

import sys, csv, re

codes = [{"code":"792..11","system":"readv2"},{"code":"7920y00","system":"readv2"},{"code":"7920z00","system":"readv2"},{"code":"7922y00","system":"readv2"},{"code":"7922z00","system":"readv2"},{"code":"K3043","system":"readv2"},{"code":"K3043T","system":"readv2"},{"code":"ZV45700","system":"readv2"},{"code":"ZV45K00","system":"readv2"},{"code":"ZV45K11","system":"readv2"},{"code":"792..11","system":"oxmis"},{"code":"7920","system":"oxmis"},{"code":"7920.11","system":"oxmis"},{"code":"7920000","system":"oxmis"},{"code":"7920100","system":"oxmis"},{"code":"7920300","system":"oxmis"},{"code":"7920y00","system":"oxmis"},{"code":"7922","system":"oxmis"},{"code":"7922.11","system":"oxmis"},{"code":"7922000","system":"oxmis"},{"code":"7922100","system":"oxmis"},{"code":"7922300","system":"oxmis"},{"code":"K3043","system":"oxmis"},{"code":"K3043T","system":"oxmis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('coronary-revascularisation-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["coronary-revascularisation-allograft---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["coronary-revascularisation-allograft---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["coronary-revascularisation-allograft---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
