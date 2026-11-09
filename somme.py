def somme_iterative(n: int) -> int:
    """Calcule la somme des n premiers entiers par itération.

    Parameters
    ----------
    n : int
        Nombre d'entiers à additionner. Doit être positif
        ou nul.

    Returns
    -------
    int
        Somme des entiers de 1 à n.

    Raises
    ------
    ValueError
        Si n est négatif.

    Notes
    -----
    La méthode additionne successivement les entiers
    de 1 à n. Sa complexité temporelle est O(n).

    """
    if n < 0:
        raise ValueError("n doit être positif ou nul")

    total = 0
    for i in range(1, n):
        total += i

    return total