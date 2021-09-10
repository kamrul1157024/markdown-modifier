# Markdown Modifier 
This code can parse markdown and sort it by header.

## Algorithm
- recursively iterate each line of markdown file to create markdown tree.
- sort child nodes of a parent node from left to right by lexicographical order
- preorderly traverse the markdown tree convert the tree back to markdown file

## What can you do
You can use is as markdown serilizer to convert markdown file to markdown tree do all kind of operation
on the markdown file.

#### Example:
- Dynamically generate markdown file inserting node to the markdown tree.
- Merge markdown files

## Expected Maarkdown format

```markdown
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
### Input 

```markdown
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
```

### Result (after sorting)

```markdown
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
```
