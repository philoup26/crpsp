# Parts to the Software Architecture
- [x]   Data Acquisition (Java)
- [x]   File indexation/storage
- [x]   UI (Message redacting environment + file format prompt)
- [x]   Key usage protocol (using the actual key with the XOR function)
- [ ]   Key deletion protocol
- [ ]   Breadcrumbs protocol

## DATA ACQUISITION PROTOCOL ##
- [x]   VPN wall
    - [ ]   Correctly receive expressvpn response
- [x]   Java initiates
- [x]   Java launches the python script that handles the indexation

## FILE INDEXATION PROTOCOL ##
- [x]   For best speeds -> 100 folder (00-99) contain 100 folders each (00-99)
        which contain a 100 .xml files for a
        total of 1 000 000 files each containing 2048 bits (2.048 GB).
- [x]   The file name is a 6 digit ID (folder1-folder2-rank ex:12-74-27.xml).
- [ ]   The entire file structure is written on 4 drives (2 per person to prevent
        drive corruption issues).
- [x]   A log of each append is kept on all drives in case of an error.
    - [ ]   Breadrcumbs append to the log

## USER INTERFACING (+ BACKGROUND PROCESSES) ##
- [ ]   XML takes an ID from key database (and notes it in the XML)
- [ ]   Prompt for message subject + Append to XML
- [ ]   Prompt for Preface (unencrypted intro) + Append to XML
- [ ]   Prompt for Body (encrypted message) + Store in txt file
        until encryption
- [ ]   Prompt for Postface (unencrypted message post Body) + Append to XML
- [ ]   Append breadcrumbs instructions if necessary (and if master) to XML
- [ ]   Encrypt message (Refer to ENCRYPTION PROTOCOL) + Append to XML
- [ ]   Store key ID, message length, in a termination-schedule.txt + Append
        to XML (so that Bob can delete the correct information also)
- [ ]   Store completed XML on the drive (for sending) and prepare
        it for ejection.
- [ ]   Launch KEY SUPPRESSION PROTOCOL

## ENCRYPTION PROTOCOL ##


## KEY SUPPRESSION PROTOCOL ##
- [ ]   Retrieve ID and message length from termination-schedule.txt
- [ ]   If the mentioned ID is smaller than 2048 -> Delete from the end (correct
        length) + Move to breadcrumbs folder.
- [ ]   If not, delete from the start and keep in current directory.

## BREADCRUMBS PROTOCOL ##
1-   A master device is set.
2-   Breadcrumbs are never assembled until master sends instructions. He will
     add the instructions to an XML message in a specified insructions section.
3-   When the is enough data to generate a new key from breadcrumbs, master
     creates an instructions file detailing which ID's are appended where.
4-   Breadcrumbs are appended one after the other until the reach of 2048 bits.
5-   The created file is added to the index.
6-   The file with remaining data after the BREADCRUMBS PROTOCOL remains in the
     breadcrumbs folder for further use.
7-   Repeat as needed


