provincias={"misiones":"posadas","Buenos Aires":"La Plata","Rio Negro":"Viedma","Corrientes":"Ciudad de Corrientes","Entre Rios":"Parana","Tierra Del Fuego":"Ushuaia","Chubut":"Rawson","Chaco":"Resistencia","La Pampa":"Ciudad de santa rosa","Formosa":"Formosa","Santa Cruz":"Rio Gallegos","Santa Fe":"Ciudad de Santa Fe","Salta":"Salta","Tucuman":"San Miguel De Tucuman","Mendoza":"Mendoza","Cordoba":"Ciudad de Cordoba","Jujuy":"San Salvador de Jujuy","Santiago del Estero":"ciudad de Santiago del Estero","San Luis":"Ciudad de San Luis","La Rioja":"La rioja","San Juan":"San Juan","Catamarca":"San Fernando Del Valle Catamarca"} 
print (provincias)
for t, v in provincias.items(): 
 print (t,":",v) 
 print (f"(c):(v)")
if "Mendoza" in v:
         print ("la provincia mendoza existe y tiene clave:",t)
