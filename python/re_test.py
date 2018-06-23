import re
SECTCRE = re.compile(
        # r'\['                                 # [
        r'(?P<hearder>[^]]+)'                  # very permissive!
        # r'\]'                                 # ]
        )

m = re.match(SECTCRE, r"[^]]]]")

print m.group()

