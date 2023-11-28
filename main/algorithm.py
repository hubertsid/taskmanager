def algorithm(estimation, completed, assignments):
    #Algorytm liczy punkty i przyznaje je deweloperom
    #Według algorytmu, deweloper o najmniejszej ilości punktów, dostaje pracę
    points = 0

    #score 1
    #Porównanie estymacji taska z wykonanymi przez dewelopera do tej pory taskami
    #szukamy liczby która jest najbliżej
    closest = 100_000_000
    for i in completed:
        dist = abs(estimation-i.estimation)
        if dist < closest:
            closest = dist 
    points += closest

    #score 2
    #sprawdzamy czy deweloper pracuje już nad taskami
    #przyznawane jest 10 punktów za każdy wykonywany task
    points += assignments*10

    return points