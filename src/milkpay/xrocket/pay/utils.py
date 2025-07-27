"""Utility functions for Pay XRocket API."""

from typing import Dict, Optional


CURRENCY_ALIASES: Dict[str, str] = {
    "TON": "TONCOIN",
}


def normalize_currency(
    currency: str, 
    custom_aliases: Optional[Dict[str, str]] = None
) -> str:
    """
    Normalize currency code to the format expected by the API.
    
    Args:
        currency: The currency code to normalize
        custom_aliases: Optional custom currency aliases to use in addition to defaults
        
    Returns:
        The normalized currency code
        
    Examples:
        >>> normalize_currency("TON")
        'TONCOIN'
        >>> normalize_currency("USDT")
        'USDT'
        >>> normalize_currency("TON", {"TON": "CUSTOM_TON"})
        'CUSTOM_TON'
    """
    # Merge default aliases with custom ones (custom takes precedence)
    aliases = CURRENCY_ALIASES.copy()
    if custom_aliases:
        aliases.update(custom_aliases)
    
    return aliases.get(currency.upper(), currency.upper())
