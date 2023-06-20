# Welcome to autounicycler
autounicycler is a python script to run unicycler to all files in a folder.

Simple run in your terminal: <code>python path/to/script.py</code>     with the options and go grab a coffe <p>
  
options:<p>
  -h, --help       show this help message and exit<p>
  -i , --input     path to the fastq files i.e: <code>home/usr/Desktop/folder_with_your_files or ~/Desktop/folder_with_your_files</code><p>
  -t , --threads       CPU thread usage (OPTIONAL)<p>
 
 
Exemple of running it: <code>python ~/Desktop/scripts/autounicycler.py -i ~/Desktop/myfiles</code>

    
#
* Must run it in terminal/enviroment with unicycler installed
* In order to facilitate the execution of a script designed to process multiple sequencing files, it is essential that the naming convention of the files follows a standardized format. Specifically, the file names should be structured in a manner that enables the script to sequentially process the paired-end reads. For instance, a common convention involves the inclusion of a consistent base file name followed by a specific identifier for each read direction, such as "file1.fastq" and "file2.fastq", or alternatively, "1.fastq" and "2.fastq". This naming convention enables the script to correctly identify and process each paired-end read, ensuring accurate and comprehensive analysis of the sequencing data.
