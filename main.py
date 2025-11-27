"""Syracuse"""
# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """Syracuse"""
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """

    l = [n]

    while n != 1:# tant que la suite n'est pas terminée :
        if n%2 == 0:
            n = n//2
        else:
            n = n*3+1
        l.append(n)# ajout d'élément de liste l

    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    n=0
    n = len(l)-1
    return n

def temps_de_vol_en_altitude(l): # plus petit indice k tel que Uk+1 < U0
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    tva = 0 # temps de vol en altitude
    trouve = False

    # for i in l[1:]:
    #     if trouve:
    #         break
    #     if i >l[0]:
    #         tva += 1
    #     else:
    #         trouve = True

    for i in range(1, len(l)):
        if trouve:
            break
        if l[i] >l[0]:
            tva += 1
        else:
            trouve = True

    return tva

def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """

    am = 0 #altitude maximale
    am = max(l)

    return am

#### Fonction principale

def main():
    """
    Returns:
        int: l'altitude maximale
        int: temps de vol en altitude
        int: temps de vol
    """

    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))

if __name__ == "__main__":
    main()
