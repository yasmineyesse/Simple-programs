""" Write in multiple files """
# Created by Yenami
# Date : May 31, 2017

for i in range(0,10000,1000):
    myfile = "mon_fichier_%d_%d.txt" % (i,i+1000)
    with open(myfile, "w") as f:
        f.write(str(myfile))
    print(str(myfile))

"""
mon_fichier_0_1000.txt
mon_fichier_1000_2000.txt
mon_fichier_2000_3000.txt
mon_fichier_3000_4000.txt
mon_fichier_4000_5000.txt
mon_fichier_5000_6000.txt
mon_fichier_6000_7000.txt
mon_fichier_7000_8000.txt
mon_fichier_8000_9000.txt
mon_fichier_9000_10000.txt
"""