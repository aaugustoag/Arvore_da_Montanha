arvore_da_montanha = ["arvore","galho","broto","folha","ninho","ovo","ave","pluma","indio","arco","flecha"]

for j in range(len(arvore_da_montanha)-1):
    print(("\nA árvore da montanha\nOle-li aio") * 2)
    print("Esta " + arvore_da_montanha[j] + " tinha um " + arvore_da_montanha[j+1]+"\nO que " + arvore_da_montanha[j+1]+", belo " + arvore_da_montanha[j+1] + "\nAi, ai, ai que amor de " + arvore_da_montanha[j+1])
    for i in range(j+1,0,-1):
        print("E o "+arvore_da_montanha[i]+" do "+arvore_da_montanha[i-1])