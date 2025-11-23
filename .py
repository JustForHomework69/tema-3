def suma_cifrelor(n: int):
    s = sum(int(c) for c in str(abs(n)))
    return f"Suma cifrelor lui {n} este {s}."


def cmmdc(a: int, b: int):
    if a == 0 and b == 0:
        return "Eroare: CMMDC nu este definit pentru 0 și 0."
    x, y = abs(a), abs(b)
    while y != 0:
        x, y = y, x % y
    rezultat = x
    return f"CMMDC({a}, {b}) = {rezultat}."


def cmmmc(a: int, b: int):
    if a == 0 or b == 0:
        return "Eroare: CMMMC nu este definit pentru 0."
    x, y = abs(a), abs(b)
    cmmdc_val = x
    while y != 0:
        cmmdc_val, y = y, cmmdc_val % y
    rezultat = abs(a * b) // cmmdc_val
    return f"CMMMC({a}, {b}) = {rezultat}."


def numar_divizori(n: int):
    if n <= 0:
        return "Eroare: n trebuie să fie un număr pozitiv."
    nr = 0
    for i in range(1, n + 1):
        if n % i == 0:
            nr += 1
    return f"Numărul de divizori ai lui {n} este {nr}."


def lista_prime_pana_la(n: int):
    if n < 2:
        return f"Nu există numere prime până la {n}."
    prime = []
    for num in range(2, n + 1):
        ok = True
        for d in range(2, int(num**0.5) + 1):
            if num % d == 0:
                ok = False
                break
        if ok:
            prime.append(str(num))
    return f"Numere prime până la {n}: {', '.join(prime)}"


def filtreaza_pare(lista: list[int]):
    pare = [str(x) for x in lista if x % 2 == 0]
    if not pare:
        return "Nu există numere pare în listă."
    return f"Numere pare: {', '.join(pare)}"


def produs_scalar(v1: list[float], v2: list[float]):
    if len(v1) != len(v2):
        return "Eroare: vectorii trebuie să aibă aceeași lungime."
    produs = sum(v1[i] * v2[i] for i in range(len(v1)))
    return f"Produsul scalar este {produs}."


def medie_ponderata(valori: list[float], ponderi: list[float]):
    if len(valori) != len(ponderi) or len(valori) == 0:
        return "Eroare: listele trebuie să aibă aceeași lungime și să nu fie goale."
    s_pond = sum(ponderi)
    if s_pond <= 0:
        return "Eroare: suma ponderilor trebuie să fie mai mare decât 0."
    suma = sum(valori[i] * ponderi[i] for i in range(len(valori)))
    medie = suma / s_pond
    return f"Media ponderată este {medie}."


def rotire_dreapta(lista: list[int], k: int):
    if not lista:
        return "Lista este goală."
    k = k % len(lista)
    rezultat = lista[-k:] + lista[:-k]
    return f"Lista rotită: {', '.join(str(x) for x in rezultat)}"


def interclaseaza(l1: list[int], l2: list[int]):
    i = j = 0
    rezultat = []
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            rezultat.append(l1[i])
            i += 1
        else:
            rezultat.append(l2[j])
            j += 1
    rezultat.extend(l1[i:])
    rezultat.extend(l2[j:])
    return f"Interclasare: {', '.join(str(x) for x in rezultat)}"


def elimina_duplicate(lista: list[int]):
    vazute = set()
    rezultat = []
    for x in lista:
        if x not in vazute:
            vazute.add(x)
            rezultat.append(x)
    return f"Fără duplicate: {', '.join(str(x) for x in rezultat)}"


def frecventa_litere(text: str):
    frec = {}
    for c in text.replace(" ", ""):
        frec[c] = frec.get(c, 0) + 1
    if not frec:
        return "Nu există caractere."
    sir = ", ".join(f"'{k}': {v}" for k, v in frec.items())
    return sir


def cel_mai_frecvent_cuvant(text: str):
    cuvinte = text.split()
    if not cuvinte:
        return "Nu există cuvinte."
    frec = {}
    for c in cuvinte:
        frec[c] = frec.get(c, 0) + 1
    cuv_max = max(frec, key=frec.get)
    return f"Cel mai frecvent cuvânt este '{cuv_max}' (apariții: {frec[cuv_max]})."


def este_isograma(text: str):
    t = text.replace(" ", "").lower()
    vazute = set()
    for c in t:
        if c in vazute:
            return f"'{text}' NU este isogramă."
        vazute.add(c)
    return f"'{text}' este isogramă."


def numere_distincte(lista: list[int]):
    if not lista:
        return "Lista este goală."
    if len(lista) == len(set(lista)):
        return "Toate numerele din listă sunt distincte."
    return "Lista conține elemente care se repetă."


def timp_in_format(secunde: int):
    if secunde < 0:
        return "Eroare: numărul de secunde trebuie să fie nenegativ."
    h = secunde // 3600
    m = (secunde % 3600) // 60
    s = secunde % 60
    return f"{secunde} secunde înseamnă {h:02d}:{m:02d}:{s:02d}."


def parola_valida(parola: str):
    if len(parola) < 8:
        return "Parola este invalidă: prea scurtă."
    if not any(c.isalpha() for c in parola):
        return "Parola este invalidă: nu conține litere."
    if not any(c.isdigit() for c in parola):
        return "Parola este invalidă: nu conține cifre."
    return "Parola este validă."


def in_binar(n: int):
    if n < 0:
        return "Eroare: numărul trebuie să fie nenegativ."
    return f"Reprezentarea în baza 2 a lui {n} este {bin(n)[2:]}."


def numar_unic(lista: list[int]):
    frec = {}
    for x in lista:
        frec[x] = frec.get(x, 0) + 1
    unice = [x for x in frec if frec[x] == 1]
    if len(unice) != 1:
        return "Eroare: lista nu conține un singur număr unic."
    return f"Numărul unic este {unice[0]}."


def sunt_anagrame(a: str, b: str):
    x = a.replace(" ", "").lower()
    y = b.replace(" ", "").lower()
    if sorted(x) == sorted(y):
        return f"'{a}' și '{b}' sunt anagrame."
    return f"'{a}' și '{b}' nu sunt anagrame."
