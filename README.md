# MiddleEarthDays
Second bot I made.  Collaborated with a friend.  It manages a twitter bot that posts a daily update if a relevant LOTR event happened on that date and also monitors the mentions timeline to respond to user queries against dates.  In the future it would be cool to expand the calendar json.

Also have a branch to do handle user queries for a separate bot that provides LA City ordinance information.

Used the following grep to generate sections files

grep -E "SEC. x" ChapterX.txt > ChapterX_Sections.txt

Where X is an int between 1 and 19.  Only works when the source ChapterX.txt is in the same directory.

Used the following terminal command to coalesce the sections into one file.

cat Chapter1_Sections.txt Chapter2_Sections.txt Chapter3_Sections.txt Chapter4_Sections.txt Chapter5_Sections.txt Chapter6_Sections.txt Chapter7_Sections.txt Chapter8_Sections.txt Chapter9_Sections.txt Chapter10_Sections.txt Chapter11_Sections.txt Chapter12_Sections.txt Chapter13_Sections.txt Chapter15_Sections.txt Chapter16_Sections.txt Chapter17_Sections.txt Chapter18_Sections.txt Chapter19_Sections.txt > LAMC_Sections.txt
