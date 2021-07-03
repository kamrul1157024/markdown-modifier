# Markdown Modifier 
This code can parse markdown and sort it by header.

Expected Maarkdown format,

```
# header
content 
## sub-header
content
### sub-sub-header
content
## sub-sub-header
# another first level header
content
# another first level header
content
```
# Input 


# Header 2
content from header 2
## sub-header 2
content from sub-header 2
## sub-header 1
content from sub-header 1
### sub-sub-header 2
content from sub-sub-header 2 
### sub-sub-header 1
content from sub-sub-header 1
#### sub-sub-sub-header 2
content from sub-sub-sub-header2
#### sub-sub-sub-header 1
content from sub-sub-sub-header 1
### sub-sub-header 3
content from sub-sub-header 3
## sub-header 2
content from sub-header 2
# Header 1
content of header 1
 

# Result 


# Header 1
content of header 1
 # Header 2
content from header 2
## sub-header 1
content from sub-header 1
### sub-sub-header 1
content from sub-sub-header 1
#### sub-sub-sub-header 1
content from sub-sub-sub-header 1
#### sub-sub-sub-header 2
content from sub-sub-sub-header2
### sub-sub-header 2
content from sub-sub-header 2 
### sub-sub-header 3
content from sub-sub-header 3
## sub-header 2
content from sub-header 2
## sub-header 2
content from sub-header 2
