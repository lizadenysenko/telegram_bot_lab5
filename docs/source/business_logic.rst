Business Logic
==============

Main goal — allow users to find movie information using simple commands.

Use case scenarios:

- `/find Title` — search for a movie by exact title.
- `/genre Genre` — filter results by genre.
- `/search Keyword` — search movies using keywords.
- Language toggle between Ukrainian and English.

The bot sends HTTP requests to the OMDb API, receives JSON, parses it, and displays user-friendly output.
