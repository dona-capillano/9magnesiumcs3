# Class Attributes and Methods
## Previous Design 
Link to my previous activity:
[classObjectUML.md](q1/classObjectUML.md)

## No major changes were needed from my original design.
### Visibility Decisions
|Attribute | Data Type | Visibility | Why Public/Private? |
|---|---|---|---|
| Title | String | Public | The title of the song should always be visible so it ca be easily accessed and displayed. |
| Genre | String | Public | The genre of the song should be always be visible so people can see if they like the specific type of music. |
| Artist | String | Private | The artist of the song should be in private as a person dont have to know who the artist is to enjoy the song. |
| Album | String | Public | The album should be public as it is important to know what album the song is from. |

## Updated UML Class Diagram 
<img width="736" height="1053" alt="Songs (1)" src="https://github.com/user-attachments/assets/368621e8-cc81-43e7-90d4-c7b535eea02e" />
## Python Implementation
[Python Source](q1/classImplementation.py)

## Test Run
<img width="1430" height="872" alt="imagesclassTestRun" src="https://github.com/user-attachments/assets/4f0f50d5-9a71-4576-a366-73f8c765ea72" />
## Object Diagram
<img width="401" height="542" alt="image" src="https://github.com/user-attachments/assets/c4f702ca-1799-47b6-b488-960f3eca8589" />

## Analysis
### Why did you make your chosen attribute private?
- I believe that a person shouldn't listen to a song they don't like just because they like the artist.
### Which method changes the state of your object?
- The set_artist() method changes the object's state by updating the private __private_artist attribute. 
### How did your two objects demonstrate that instances are independent?
- When set_artist() was executed on song1, its artist value was successfully updated in memory. However, song2 retained its original artist ("88rising and NIKI") in the --- AFTER --- test output. This proves that each object maintains its own independent state.
### What is the difference between your class diagram and your object diagram?
- The class diagram is a blueprint defining the attributes, data types, and methods of the Songs class, the object diagrams is a dynamic snapshot showing specific instances and their actual values at a specific point during program execution.
