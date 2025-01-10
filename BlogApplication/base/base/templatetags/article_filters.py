from django import template

register = template.Library()

@register.filter
def make_chunks(value, chunk_size):
    """
    Divise une liste en sous-listes de taille égale à chunk_size.
    :param value: La liste ou itérable à diviser.
    :param chunk_size: La taille de chaque sous-liste.
    :return: Une liste de sous-listes.
    """
    if not value:
        return []
    try:
        chunk_size = int(chunk_size)
        return [value[i:i + chunk_size] for i in range(0, len(value), chunk_size)]
    except (ValueError, TypeError):
        return []

@register.filter
def get_dict_value(dictionary, key):
    """
    Retourne la valeur associée à une clé dans un dictionnaire.
    :param dictionary: Le dictionnaire.
    :param key: La clé pour laquelle récupérer la valeur.
    :return: La valeur associée à la clé ou 0 si la clé n'existe pas.
    """
    if not isinstance(dictionary, dict):
        return 0
    return dictionary.get(key, 0)
