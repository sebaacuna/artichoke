def read(msg, default=None, options=None):
    if options is not None:
        msg = "%s [%s]" % (msg, ', '.join(options))
    if default is None:
        msg = "%s: " % msg
    else:
        msg = "%s (%s): " % (msg, default)

    user_input = raw_input(msg)
    if user_input == "" and default is not None:
        user_input = default

    if options is not None and user_input not in options:
        return read(msg, default=default, options=options)
    return user_input
