import pandas as pd

cartoonmovies= {
    "name":["snowwhite","wishes","beautythebeast","brave","slayofgod","ben10","rupenzal","kung fu panda","the looney tones show","frozen","mr.bean","dragon","loadofgod","tee tinas","Oggy and the Cockroaches"],
    "year":[2010,2013,2012,2006,2008,2009,1990,2020,2019,2022,2003,2001,2003,2000,1998],
    "reviwe":["good","excellent","good","fair","awsome","very nice","awsome","good","excellent","nice","fair","good","very good","good","notbad"],
    "vote":[9,10,10,7,8,5,4,11,10,8,9,2,6,5,8]
}

df=pd.DataFrame(cartoonmovies)
print(df)


import pandas as pd

hospital={
    "Name":["asma","sara","ali","dua","zara","arsalan","bushra","maria","zeeshan","wasi","ahmed","mazz","areeb","jawed","sania"],
    "Number":[20,60,50,80,30,10,55,88,100,33,22,12,11,45,75],
    "Room Number":[2,6,9,4,10,12,19,5,15,7,8,1,3,20,14],
    "ID Number":[101,102,103,104,105,106,107,108,109,1010,1011,1012,1013,1014,1015],
    "Adress":[2818,1930,2043,2960,2740,2320,2890,1950,1830,2732,2942,2853,2945,1632,2512]
}
df=pd.DataFrame(hospital)
print(df)

import pandas as pd

students={
    "name":["asma","sara","fiza","zainab","mahreen","saeeda","sajida","iqra","aliza","javeria","sana","mahreen","ayesha","ruquiya","hadia","nawal","maha","neha","samia","nehal"],
    "marks":[80,70,66,55,40,35,25,90,65,87,94,68,49,58,44,92,29,46,62,73],
    "class":[10,11,8,6,8,9,12,7,6,5,12,11,10,9,8,6,7,4,3,2],
    "student ID":[201,202,203,204,205,206,207,208,209,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
}
df=pd.DataFrame(students)
print(df)



