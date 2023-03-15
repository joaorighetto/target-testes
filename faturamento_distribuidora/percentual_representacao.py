SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OUTROS = 19849.53
TOTAL = SP + RJ + MG + ES + OUTROS

perc_sp = round(SP / TOTAL * 100, 2)
perc_rj = round(RJ / TOTAL * 100, 2)
perc_mg = round(MG / TOTAL * 100, 2)
perc_es = round(ES / TOTAL * 100, 2)
perc_outros = round(OUTROS / TOTAL * 100, 2)

print("Percentual SP: ", perc_sp, "%")
print("Percentual RJ: ", perc_rj, "%")
print("Percentual MG: ", perc_mg, "%")
print("Percentual ES: ", perc_es, "%")
print("Percentual Outros: ", perc_outros, "%")