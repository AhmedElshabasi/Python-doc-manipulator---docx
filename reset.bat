@echo off

REM Clear input.txt
type nul > input.txt

REM Delete Updated_CoverLetter.docx if it exists
if exist Updated_CoverLetter.docx del Updated_CoverLetter.docx

echo Reset complete.
