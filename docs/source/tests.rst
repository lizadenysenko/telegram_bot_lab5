Test-Driven Documentation
==========================

Example of how to manually test the `/find` command:

::

    1. Type in chat: /find Titanic
    2. Expected output includes:
       - Movie title: Titanic
       - Year: 1997
       - Poster image
       - YouTube trailer link
       - Genre: Drama, Romance

    3. If the movie is not found:
       - An appropriate message is returned in the selected language.

These steps could also be turned into automated tests using `pytest` and mocking API responses.
