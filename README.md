# Cesium Radioactivity Perfect Secrecy Protocol #
## Protocol ##
1.  Acquire API
2.  Acquire Cesium data
3.  Create encryption software
4.  Host software on offline RB Pi
5.  Plug USB Drive containing key (1) in RB Pi
6.  Run encryption on message
7.  Store encrypted message on Transfer USB Drive (2)
8.  Send via an online computer the encrypted message

## Encryption Structure ##
1.  Subject (Unencrypted)
2.  Data Encryption Archictecture Index (0-9)
 (Unencrypted)
    -   Critical - 1 (A-Z, ".")
    -   Normal - 2 (A-Z, a-z, ",", ".", "!", "?", "()", ", ', "RETURN", "-", "#")
    -   Casual - 3 (ASCII - 0-255)
3.  ID (Unencrypted)
4.  Message (Encrypted)
-   Ideas
    -   xml format
    -   store original cesium len for ID reference

### Ideas ###
-   Log file at root database directory
-   100/100/100.CRPSP FILE STRUCTURE SETUP
-   Breadcrumbs protocol
