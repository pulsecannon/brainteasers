pivotview
=========

We are attempting to visualize sample in Pivot with different dynamic groups

Sample Input file (data.txt)

| name   | Gender | Age | Location |
| ------ |:------:| --- | -------  |
| User1  | M      | 20  | Location1|
| User2  | M      | 18  | Location3|
| User3  | F      | 45  | Location2|
| User4  | F      | 25  | Location2|
| User4  | F      | 7   | Location2|
 
Design sample program "pivot" using python or golang

Group data based on Age

```
$ cat data.txt|piviot -by Age
```

| Gender | Count |
| ------ | ----- |
| M      |  2    |
| F      |  3    |


Group data based on Age,Location

```
$ cat data.txt|piviot -by Gender -by Location
```

| Gender |Location   | Count |
| ------ |---------- | ----- |
| M      | Location1 |  1    |     
| F      | Location2 |  3    |     
| M      | Location3 |  1    |     

Support Output format csv,html

```