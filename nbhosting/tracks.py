"""
This module is for nbhosting
"""

from nbhosting.courses import (
    Track, Section, Notebook,
    notebooks_by_pattern, track_by_directory)

def tracks(coursedir):
    return [
        Track(coursedir,
              name="advanced",
              sections=[
                Section(name="cours 1/9",
                        coursedir=coursedir,
                        notebooks=notebooks_by_pattern(coursedir,"cours1*.ipynb")),
                Section(name="cours 2/9",
                        coursedir=coursedir,
                        notebooks=notebooks_by_pattern(coursedir,"cours2*.ipynb")),
                Section(name="cours 3/9",
                        coursedir=coursedir,
                        notebooks=notebooks_by_pattern(coursedir,"cours3*.ipynb")),
                ],
              description="le cours de Python avancé"),
        ]
