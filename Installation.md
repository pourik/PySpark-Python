# Installing Apache Spark and Python

## Windows

1. Install a JDK (Java Development Kit) from http://www.oracle.com/technetwork/java/javase/downloads/index.html [.](http://www.oracle.com/technetwork/java/javase/downloads/index.html) **SPARK 4 IS ONLY COMPATIBLE WITH JAVA 17 or 21 at this time.**
2. Download a **pre-built** version of **Apache Spark 4** from https://spark.apache.org/downloads.html
3. If necessary, download and install WinRAR so you can extract the .tgz file you downloaded. http://www.rarlab.com/download.htm
4. Extract the Spark archive, and copy its **contents** into **C:\spark** after creating that directory. You should end up with directories like c:\spark\bin, c:\spark\conf, etc.
5. Open the the **c:\spark\conf** folder, and make sure “File Name Extensions” is checked in the “view” tab of Windows Explorer. Rename the log4j2.properties.template file to log4j2.properties. Edit this file (using Wordpad or something similar) and change the error level from “info” to “error” for log4j.rootCategory
6. Download hadoop.zip from https://s3.amazonaws.com/media.sundog-soft.com/Udemy/hadoop.zip and unzip it to **c:\hadoop** (you should end up with **c:\hadoop\bin** directory containing winutils.exe and hadoop.dll)
7. Right-click your Windows menu, select Control Panel, System and Security, and then System. Click on “Advanced System Settings” and then the “Environment Variables” button.
8. Add the following new USER variables:
    1. **SPARK_HOME c:\spark**
    2. **PYSPARK_PYTHON python**
    3. **HADOOP_HOME c:\hadoop**
9. Add the following path to your PATH user variable: **%SPARK_HOME%\bin**

1. Close the environment variable screen and the control panels.
2. Install the latest **Anaconda for Python 3** from [anaconda.com](https://anaconda.com/). If you already use some other Python environment, that’s OK – you can use it instead, as long as it is a Python 3 environment.
3. Test it out!
    1. Open up your Start menu and select “Anaconda Prompt” from the Anaconda3 menu.
    2. Currently, **Spark is NOT compatible with Python 3.12** or newer! Create a Python 3.10 environment for use with this course:
        1. **conda create -n py310 python=3.10**
        2. **conda activate py310**
        3. **pip install py4j**
        4. **conda install pandas**
        5. **conda install pyarrow**
        6. Remember to run “**conda activate py310**” whenever working with this course.
    3. Enter **cd c:\spark** and then **dir** to get a directory listing.
    4. Look for a text file we can play with, like README.md or CHANGES.txt
    5. Enter **pyspark**
    6. At this point you should have a >>> prompt. If not, double check the steps above.
    7. Enter **rdd = sc.textFile(“README.md”)** (or whatever text file you’ve found) Enter **rdd.count()**
    8. You should get a count of the number of lines in that file! Congratulations, you just ran your first Spark program!
    9. Enter **quit()** to exit the spark shell, and close the console window
    10. You’ve got everything set up! Hooray!
