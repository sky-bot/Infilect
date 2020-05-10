pattern = '{}'


def _make_key(*args, **kwargs):
    separator = kwargs.get('separator', '_')
    return separator.join(args)


def make_key(*args, **kwargs):
    un_formatted = _make_key(*([pattern]*len(args)), **kwargs)  # to avoid NoneType exception
    return un_formatted.format(*args)