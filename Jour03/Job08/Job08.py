def fonction(Type,Saison):
    if Type == "fruits" and Saison == "hiver":
        print("orange,mandarine,kiwi")
    
    elif Type == "fruits" and Saison == "ete":
        print("pomme,fraise,cassis")
    
    elif Type == "legume" and Saison == "hiver":
        print("carotte,topinambour,endive")
    
    elif Type == "legume" and Saison == "ete":
        print("artichaud,aubergine,navet")
    
print(fonction("legume","hiver"))