# --------
# using scipy, it's kinda big but that should not be a problem
# base-notebook lacks at least numpy, widgets, so...
FROM nbhosting/minimal-notebook

# nbautoeval is in the core images but we often need 
# the very latest version, that core images cannot
# always afford to follow very closely
# RUN pip install --upgrade nbautoeval --pre
RUN pip install --upgrade nbautoeval

