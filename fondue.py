base=4
fromage=800.0
eau=2
ail=2
pain=400
nbConvives=int(input("nombre de personne :"))
qtfromage=str(fromage*nbConvives/base)
qteau=str(eau*nbConvives/base)
qtail=str(ail*nbConvives/base)
qtpain=str(pain*nbConvives/base)
Convive=str(nbConvives)
print("pour faire une fondue fribourgeoise pour "+Convive+" personnes, il vous faut :\n - "+qtfromage+ "gr de fromage\n - "+qteau+ "dl d'eau\n - "+qtail+ "gousse(s) d'ail\n - "+qtpain+"gr de pain")