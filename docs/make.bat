@echo off

rem Command file for Sphinx documentation
set SPHINXBUILD=sphinx-build
set SOURCEDIR=source
set BUILDDIR=build

%SPHINXBUILD% -M html %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%

