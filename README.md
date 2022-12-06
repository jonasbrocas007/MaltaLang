# MaltaLang  
## Philosofy:  

### The Philosofy of MaltaLang announces some rules to follow while coding:  
  
1 - Everything should be simple as possible, unless it's more work for the creator to do (me).  
2 - Backwards compatibility is very very cringe and we don't care about it.  
3 - For loops have no reason to exist, that's why they don't.  
4 - Functions and it's consequences have been a disaster for the human race.  
5 - You should be aware of what you write, if you try to write complex code like a dumbass
things might not go your away and don't work, there are thing that work and things that should but
don't work.  

## Chapter 1 - Introduction:  
MaltaLang is a interpreted Language so, to program in maltalang you need to download the interpreter from 
this page, this document focus on MaltaLang 2.5  

### Numbers in Maltalang:  
We are going to start the documentation with numbers, numbers are the basics of computing, and number 
operation are one of the first things i did in MaltaLang.  

#### Calculating two numbers:  
In MaltaLang to calculate two numbers that are not stored in variables you need to use the op keyword 
it's syntax is op (the operator), the first number, the signal (+ - / *), the second number and finnaly 
the type of output (integer (i) or float (f))  
An example of that would be: op 1 + 1 i, calculates 1 + 1 and shows the final output as a integer.  

#### Calculating two numbers from two variables:
To calculate numbers from variables you need to use a different keyword, (ov) which means (operation with variables).  
it's syntax is ov (the operator), the first variable, the signal (+ - / *), the second number, the output separeted with >> and finnaly
the type of the output (integer (i) or float (f)).
The output will not be shown but you can print it with >> or >.  
An example of that would be:  
ov x + y >> result i  
*>>result  

Note: The type should be the final character of the line!  

#### An example of basic MaltaLang:  
---  
START  
<a = 0 i  
<b = 1 i  
<result = 0 i  
<check = 1000 i  

while a < check: goto start, else end  
:start  

>>a  
ov a + b >> result i  
@b,a  
@result, b  

:end  

END  
---
