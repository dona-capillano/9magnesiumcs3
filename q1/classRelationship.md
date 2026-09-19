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
[Class Relationship Diagram](q1/imagesclassRelationshipDiagram.png)

## Python Implementation 
[View Python Source](q1/classRelationships.py)

## Test Run 
[Relationship Test Run](q1/imageRelationshipTestRun.png)

## Object Relationship Diagram 
[Object Relationship Diagram](q1/imagesobjectRelationshipDiagram.png)

## Analysis
### What is the association between your two classes?
The association is "contains" HAS-A relationship where LikedSongsFolder acts as a container for Songs. This folder allows to manage individual song tracks and access their properties directly through object interaction.
### What multiplicity did you choose and why?
I chose a 1 to 0..* multiplicity as one folder can hold 0 or many songs. A folder can exist while empty and have song preferences added to it over time.
### How did you implement the relationship in Python?
It is implemented by giving LikedSongsFolder an empty list attribute. 
### Why did you store an object reference instead of copying its data?
Storing references prevents data duplication and keeps objects synchronized.
### If your relationship uses many, why is a list appropriate?
A list is ideal as it resizes as songs are added or removed. It helps preserve the order of song preferences, allowing the folder to easily loops each track.
