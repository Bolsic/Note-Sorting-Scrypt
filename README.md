# Obsidian Note Sorting script

This script is made for the purpose of sorting markdown files generated in Obsidian while writing. It is specificaly made for sorting DnD notes, where a note has a tag at the beggining, indicated by a "#". 

The script reads the first few lines of a file and detects words that start with "#". Then it reads trough a map file that links tags and folders and checks if there are any matches. The first match found is used as a file destination and the file is moved there. 

When a note is moved a message is written in the system logs (journalctl). The script is called using a fich script and that script is called trough cronjob.
