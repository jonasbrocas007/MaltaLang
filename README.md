# MaltaLang
The MaltaLang proper language.  
contains:  
print         | yes  
operations    | yes  
variables     | yes  
conditions    | yes  
loops         | yes  
input         | yes   
error messages| kinda   

### Hello World  
>.Hello World  
>END 

### Getting Started  
you can download the interpreter from this page, malta 1 for the first version of the language and malta 2 for the second version.  
Or you can download Malta on Train.  

## with the interpreter:  
>python malta2.py code.mlt  
## with Malta on train  
>first create a file > python train.py createmalta2  
>now you can run the file with > python train.py run  

### Why you SHOULD use Malta on train?  
Now, Malta on Train is not that useful but in the feature it is going to have lots of more features, so you should get used to it now.  
Also, it's cool.  

## Documentation:  
### What you need for a program:  
Programs are very basic, the only thing is that you need to use the END command to end a program, you cannot program after using END.  
**Note:** you can't use identation, maybe in the feature this will change.  

### Print:
to print you should use the **.** command.  
>.Hello World  

to print variables use the '>' command.  
> '>'var

### variables:  
to create a variable use the '<' command:  
> <var = 0  

to input into a variable use the '$' command:  
> $var  

you can also increment into the variable with '++'  
>var++  

and pipe a result into a variable with '>>'  
>ov a + b >> var  

### loops:  
In MaltaLang v1 you can use the loop command:  
>lp .Hello 10  
this command loops Hello 10 times.  

But in MaltaLang the loop command was discontinued, now you are force to used the holy grail of commands, **goto**  
with goto you can go to  stamps:  
> :start  
> goto start  

and go to lines:
>goto 50  

 

### conditions (if):  
with if you only can program one line, for example you cannot condition multiple commands, only one.  
the if has multiple parts: if, the condition and the command to do after.  
>if a = 1: >a  

### Memory  
MaltaLang has a garbage collector but you need to call it with c   
>c  

if you want a variable to get deleted but it is not elegible for the garbage collector you can use the del  
 keyword  
>del var





