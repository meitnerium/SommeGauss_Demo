"""Tests de verification pour les deux methodes."""

import pytest

from somme import somme_gauss, somme_iterative


@pytest.mark.parametrize(
    "n",
    [0, 1, 10, 55]
)
def test_somme(n):
    assert somme_iterative(n) == somme_gauss(n)

@pytest.mark.parametrize("fonction", [somme_iterative, somme_gauss])
def test_n_negatif_refuse(fonction) -> None:
    """Negative values are invalid input."""
    with pytest.raises(ValueError):
        fonction(-1)
