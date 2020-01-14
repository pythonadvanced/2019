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
                        notebooks=notebooks_by_pattern(coursedir,"cours1.ipynb")),
                Section(name="cours 2/9",
                        coursedir=coursedir,
                        notebooks=notebooks_by_pattern(coursedir,"cours2.ipynb")),
                Section(name="cours 3/9",
                        coursedir=coursedir,
                        notebooks=notebooks_by_pattern(coursedir,"cours3.ipynb")),
                Section(name="cours 4/9",
                        coursedir=coursedir,
                        notebooks=notebooks_by_pattern(coursedir,"cours4.ipynb")),
                Section(name="cours 5/9",
                        coursedir=coursedir,
                        notebooks=notebooks_by_pattern(coursedir,"cours5.ipynb")),
                Section(name="cours 6/9",
                        coursedir=coursedir,
                        notebooks=notebooks_by_pattern(coursedir,"cours6.ipynb")),
                Section(name="cours 7/9",
                        coursedir=coursedir,
                        notebooks=notebooks_by_pattern(coursedir,"cours7.ipynb")),
                Section(name="cours 8/9",
                        coursedir=coursedir,
                        notebooks=notebooks_by_pattern(coursedir,"cours8.py") 
                                  + notebooks_by_pattern(coursedir,"sujet-evaluation.md")),
                Section(name="cours 9/9",
                        coursedir=coursedir,
                        notebooks=notebooks_by_pattern(coursedir,"cours9.py") 
                                  + notebooks_by_pattern(coursedir,"sujet-evaluation.md")),
                ],
              description="le cours de Python avancé"),
        ]
