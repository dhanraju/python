# 1. PYTHON PRIMER


## 1.1 Python Overview:
### 1.1.1 Python Interpreter:
Python is formally an integrated language.
Using "-i" flag we can execute a script and then enter interactive mode (e.g., python -i demo.py)

### 1.1.2 Preview of a Python Program
Python's syntax relies heavily on the use of whitespace.
Individual statements are typically concluded with a newline character, although a command can extend to another line, either with a concluding backslash character (\).

## 1.2 Objects in Python
Python is an object-oriented language and classes form the basis for all data types.

### 1.2.1 Identifiers, Objects, and the Assignment Statement
Identifiers (Reseved Words):

False       as      continue     else    from    in       not     return  yield

None        assert  def          except  global  is       or      try

Ture        break   del          finally if      lambda   pass    while

and         classes elif         for     import  nonlocal raise   with

### 1.2.2 Creating and Using Objects

### 1.2.3 Built-In Classes
A class is immutable if each object of that class has a fixed value upon instantiation that cannot subsequently be changed.

<table>
  <tr>
    <th>Class</th>
    <th>Description</th>
    <th>Immutable?</th>
  </tr>

  <tr>
    <td>bool</td>
    <td>Boolean value</td>
    <td>&#x2611;</td>
  </tr>

  <tr>
    <td>int</td>
    <td>integer</td>
    <td>&#9745;</td>
  </tr>

  <tr>
    <td>float</td>
    <td>floating point number</td>
    <td>&#9745;</td>
  </tr>

  <tr>
    <td>list</td>
    <td>mutable sequence of objects</td>
    <td>&#9745;</td>
  </tr>

  <tr>
    <td>tuple</td>
    <td>immutable sequence of objects</td>
    <td>&#9745;</td>
  </tr>

  <tr>
    <td>str</td>
    <td>character string</td>
    <td>&#9745;</td>
  </tr>

  <tr>
    <td>set</td>
    <td>unordered set of distinct objects</td>
    <td>&#x2612;</td>
  </tr>

  <tr>
    <td>frozen set</td>
    <td>immutable form of set class</td>
    <td>&#9745;</td>
  </tr>

  <tr>
    <td>dict</td>
    <td>associative mapping</td>
    <td>&#9746;</td>
  </tr>
</table>

**set and frozenset classes:**

set class represents the mathemtical notion of a set, namely a collection of elements, without duplicates and without an inherent order to those elsements.

Advantage - As opposed to a list, is that it has a hightly optimized method for checking whether a specific element is contained in the set. This is based on a data structure known as a hash table.

eg: set - {'red', 'green', 'blue'}

Restrictions -
(1) The set doesn't maintain the elements in any particular order.
(2) Only instances, floating-point numbers, and character strings are eligble to be elements of a set.
It is possible to maintain a set of tuples, but not a set of lists or a set of sets, as lists and sets are mutable.

frozen set class is an immutable form of the set type, so it is legal to have a set of frozensets.


## 1.3 Expressions, Operators, and Precedence

<table>
  <tr>
    <tr><th>Logical Operators</th></tr>
    <tr><td>not</td></tr>
    <tr><td>and</td></tr>
    <tr><td>or</td></tr>
  </tr>
</table>

<table>
  <tr>
    <tr><th>Equlity Operators</th></tr>
    <tr><td>is</td></tr>
    <tr><td>is not</td></tr>
    <tr><td>==</td></tr>
    <tr><td>!=</td></tr>
  </tr>
</table>

<table>
  <tr>
    <tr><th>Comparison Operators</th></tr>
    <tr><td><</td></tr>
    <tr><td><=</td></tr>
    <tr><td>></td></tr>
    <tr><td>>=</td></tr>
  </tr>
</table>

<table>
  <tr>
    <tr><th>Arithmetic Operators</th></tr>
    <tr><td>+</td></tr>
    <tr><td>-</td></tr>
    <tr><td>*</td></tr>
    <tr><td>/</td></tr>
    <tr><td>//</td></tr>
    <tr><td>%</td></tr>
  </tr>
</table>

<table>
  <tr>
    <tr><th>Bitwise Operators</th></tr>
    <tr><td>~</td></tr>
    <tr><td>&</td></tr>
    <tr><td>|</td></tr>
    <tr><td>^</td></tr>
    <tr><td><<</td></tr>
    <tr><td>>></td></tr>
  </tr>
</table>

<table>
  <tr>
    <tr><th>Sequence Operators</th></tr>
    <tr><td>s[j]</td></tr>
    <tr><td>s[start:stop]</td></tr>
    <tr><td>s[start:stop:step]</td></tr>
    <tr><td>s + t</td></tr>
    <tr><td>k * s</td></tr>
    <tr><td>val in s</td></tr>
    <tr><td>val not in s</td></tr>
  </tr>
</table>

<table>
  <tr>
    <tr><th>Sets and Frozensets operators</th></tr>
    <tr><td>key in s</td></tr>
    <tr><td>key not in s</td></tr>
    <tr><td>s1 == s2</td></tr>
    <tr><td>s1 <= s2</td></tr>
    <tr><td>s1 < s2</td></tr>
    <tr><td>s1 >= s2</td></tr>
    <tr><td>s1 > s2</td></tr>
    <tr><td>s1 | s2</td></tr>
    <tr><td>s1 & s2</td></tr>
    <tr><td>s1 - s2</td></tr>
    <tr><td>s1 ^ s2</td></tr>
  </tr>
</table>

<table>
  <tr>
    <tr><th>Dictionairies operators</th></tr>
    <tr><td>d[key]</td></tr>
    <tr><td>d[key] = value</td></tr>
    <tr><td>del d[key]</td></tr>
    <tr><td>key in d</td></tr>
    <tr><td>key not in d</td></tr>
    <tr><td>d1 == d2</td></tr>
    <tr><td>d1 != d2</td></tr>
  </tr>
</table>

<table>
  <tr>
    <tr><th>Extended Assignment operators</th></tr>
    <tr><td>alpha = [1, 2, 3]</td></tr>
    <tr><td>beta = alpha</td></tr>
    <tr><td>beta += [4, 5]</td></tr>
    <tr><td>beta = beta + [6, 7]</td></tr>
    <tr><td>print(alpha)</td></tr>
  </tr>
</table>


### 1.3.1 Compount Expressions and Operator Precedence

## 1.4 Control Flow
### 1.4.1 Conditionals - if, elif
### 1.4.2 Loops - while, for
Special statements - Break, Continue

Break - It immediately terminate a while or for loop when executed within its body. More formally, if applied within nested control structures, it causes the termination of the most immediately enclosing loop.

Continue - It causes the current iteration of a loop body to stop, but with subsequent passes of the loop proceeding as expected.

## 1.5 Functions
### 1.5.1 Information Passing
### 1.5.2 Built in functions

