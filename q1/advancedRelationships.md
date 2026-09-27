# Advanced class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)

[classRel](classRelationships.md)
## Existing System Description:

## Inheritance Relationship

Parent: 'Songs'

Child: 'LiveSongs'
Explanation: it inherits basic properties and adds 'venue'. 

## Inheritance UML
[Inheritance](q1/imagesinheritanceDiagram.png)
## Composition/Aggregation

Relationship: Aggregation (Weak HAS-A)

Explanation: 'LikedSongsFolder' holds reference to 'Songs' and 'LiveSong' ojects in a list.

## Advanced UML Diagram
[Advanced UML](q1/imagesadvancedClassDiagram.png)
## Python Implementation 
[Source Code](advanceRelationships.py)
## Test Run
[Test](images/advancedTestRun.png)
## Object Diagram
[Objects](q1/imagesadvancedObjectDiagram.png)

## Reflection 
1. Why did you choose your inheritance relationship?
   - I chose Livesong as a live recording of a song IS-A song.
2. How did inheritance reduce duplicate code?
   - Inheritance allowed LiveSong to automatically reuse title, artist, genre, and album from Songs.
3. Why is your HAS-A relationship Composition or Aggregation?
   - It is Aggregation as the lifecycle of a Songs or LiveSong is independent of the LikedSongsFolder.
4. What is the difference between Association from Part III and the advanced relationship implemented?
   - Association in Part III only showed how 2 classes interact. aggregation adds clear ownership, showing that LikedSongsFolder acts a container for songs without putting them at risk if ever the folder is deleted.
5. How does your design follow the DRY principle?
   - It follows the DRY by keeping common attributes inside Songs. LiveSong inherits them automatically, so we won't be needing to rewrite the same code.
