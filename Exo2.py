# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:36:14 2020
TP1
@author: gtchi
"""
def mesImpots(revenu):
    """montant des impots d'une personne"""
    try:
        revenu=int(revenu)
        taxes={9964:0, 17555:14, 46260:30, 82565:41, -1:45}
        tot=0
        for tranche in taxes:
            if revenu-tranche>0 and revenu>revenu-tranche:
                revenu-=tranche
                tot+=tranche*(taxes[tranche]/100)
            else:
                tot+=revenu*(taxes[tranche]/100)
                return round(tot,2)
        
    except Exception as error:
        print(error)
        return 'NaN'
 
    
revenu = input('Quels sont vaut revenu ? :')
print('Vous payerez %s € d\'impot cette annee' %(mesImpots(revenu)))
