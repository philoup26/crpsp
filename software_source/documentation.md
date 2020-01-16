# Documentation #


## Log file ##
To prevent our software to search (and use loads of CPU)  for the latest xml
index file to use when encrypting, we give it a log file that lists all the
operations made in the index. Here is the used format:

`O : XX-XX-XX.xml`

-   __O__: Operation
-   __XX-XX-XX.xml__: File on which the operation was executed

### List of operations ###

-   __x__: Wrote a new file from Hotbits Server data.
-   __D__: Deleted a file.
-   __S__: Sent a used file to the breadrumbs protocol.
-   __C__: Compiled mentionned files into a new file from breadcrumb.
-   __L__: Leftovers post Breadcrumbs protocol. \*
-   __N__: New file officially added to index after Breadcrumbs compilation.
\*: Lines marked with an L will only display how many bits remain in the file
after the breadcrumbs protocol. It depends on the line above (tagged C) to point
to which file is the one with remaining bits. For the sake of consistency, it
will consist of 8 digits (ex: `00000024`).
