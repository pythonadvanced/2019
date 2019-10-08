"""
This module is for nbhosting
"""

from nbhosting.courses import (
    Track, Section, Notebook,
    notebooks_by_pattern, track_by_directory)

def tracks(coursedir):
    return [
        Track(coursedir,
              name="python avancé",
              sections=[
                Section(name="cours 1",
                        coursedir=coursedir,
                        notebooks=notebooks_by_pattern(coursedir,"cours1*")),
                Section(name="cours 2",
                        coursedir=coursedir,
                        notebooks=notebooks_by_pattern(coursedir,"cours2*")),
                ],
              description="le serpent en pygame"),
        ]
