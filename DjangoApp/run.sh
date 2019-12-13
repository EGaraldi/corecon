#!/bin/bash
python3 manage.py runserver & xdg-open http://localhost:8000/admin/ & xdg-open http://localhost:8000/constraints/ion_frac  & xdg-open http://localhost:8000/search/ion_frac


