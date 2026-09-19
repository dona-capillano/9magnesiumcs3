# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class
Class: Songs
Description: Songs I like the most 

## New Related Class
Class: Liked Songs Folder
Description: Songs in my Liked Songs folder

## Association
Relationship: Liked Songs Folder HAS Songs
Explanation: The 'Liked Songs Folder' contains 'Songs'.
| UML | Meaning |
|---|---|
| 1 | Exactly one |
| 0..* | Zero or more |

# Multiplicity:
Multiplicity: '1' to '0..*'
Explanation: Exactly one 'Liked Songs Folder' can contain zero or more 'Songs'

## UML Class Relationship Diagram



